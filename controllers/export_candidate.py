import flask as fk
import http
import helper.exceptions as  exceptions
import controllers.writer as writer
import controllers.candidate_info as cd


class ExportCandidateController:

    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _CreateExtensionValidator()
    
    def handler(self, extension_creator_test=None):
        return extension_creator_test or _ExtensionCreator()
    
    def serializer(self, serializer_test=None):
        return serializer_test or _ExportCandidateSerializer()
    
    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def export_candidate(self,validator_test=None, handler_test=None, serializer_test=None,status_test=None):
        self.validator(validator_test).validate(self.body_request)
        self.response = self.handler(handler_test).export_candidate()
        return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK

class ExportAllCandidateController:

    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _CreateExtensionValidator()
    
    def handler(self, extension_creator_test=None):
        return extension_creator_test or _ExtensionCreator()
    
    def serializer(self, serializer_test=None):
        return serializer_test or _ExportCandidateSerializer()
    
    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def export_all_candidate(self,validator_test=None, handler_test=None, serializer_test=None,status_test=None):
        self.validator(validator_test).validate(self.body_request)
        self.response = self.handler(handler_test).export_all_candidate()
        return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK


class _CreateExtensionBuilder:
    def __init__(self,writer_test=None):
        self.write = writer_test or writer
        self.candidate = None
        self.row_data = None
        self.extension_file = None
    
    def handler(self, business_handler_test=None):
        return business_handler_test or cd._CandidateBusinessHandler()
    
    def request_body(self, request_test=None):
        return request_test or fk.request.get_json()

    def data_serializer(self, serializer_test=None):
        return serializer_test or _DataSerializer()

    def prepare_candidate_data(self,candidate_id_test=None,handler_test=None):
        candidate_id = self.request_body(candidate_id_test).get("candidate_id")
        self.candidate = self.handler(handler_test).get(candidate_id)
        serializer = self.data_serializer().All_serialize(self.candidate)
        self.row_data = self.write.RowExcelData(serializer)

    def prepare_all_candidate_data(self,handler_test=None):
        self.candidate = self.handler(handler_test).get_all()
        serializer = self.data_serializer().All_serialize(self.candidate)
        self.row_data = self.write.RowExcelData(serializer)

    def create_file(self,extension):
        self.extension_file = extension

    def save_file(self,request_test=None):
        filename = self.request_body(request_test).get("filename")
        manger = self.write.DataManger(self.extension_file)
        manger.save(self.row_data, filename)
        return self.candidate
    

# builder Director
ExtensionCreator = {
    "pdf": writer.PDFCreator(),
    "csv": writer.CSVCreator(),
    "xlsx": writer.ExcelCreator(),
}

class _ExtensionCreator:
    
    def __init__(self,request_test=None,operation_test=None,builder_test=None,Excel_test=None):
        self.request = request_test or fk.request.args
        self.extension_creator = operation_test or ExtensionCreator
        self.create = builder_test or _CreateExtensionBuilder()
        self.excel_creator = Excel_test or writer.ExcelCreator()


    def export_candidate(self):
        operation = self.request.get("operation")
        extension = self.extension_creator.get(operation)
        self.create.prepare_candidate_data()
        if operation == "xlsx":
            self.create.create_file(self.excel_creator)
        else:
            self.create.create_file(extension)
        return self.create.save_file()
    
    def export_all_candidate(self):
        operation = self.request.get("operation")
        extension = self.extension_creator.get(operation)
        self.create.prepare_all_candidate_data()
        if operation == "xlsx":
            self.create.create_file(self.excel_creator)
        else:
            self.create.create_file(extension)
        return self.create.save_file()


# Validation
class _CreateExtensionValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self, body):
        self.is_valid_token(self.token)
        self.is_valid_fileName(body.get("filename"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")
        
    def is_valid_fileName(self, fileName):
        if not fileName:
            raise exceptions._RequiredInputError("filename is required")
        self._is_valid_fileName(fileName)

    def _is_valid_fileName(self, fileName):
        if not isinstance(fileName, str):
            raise exceptions._InvalidInputError("filename is not valid string")

# Serialization
class _DataSerializer:
    
    def All_serialize(self,candidate):
        if isinstance(candidate, list):
            return [self.serialize(user) for user in candidate]
        return [self.serialize(candidate)]

    def serialize(self, candidate):
        return {
            "name": candidate.name,
            "age": candidate.age,
            "email": candidate.email,
            "phone": candidate.phone,
            "skills": ", ".join(skill.name for skill in candidate.skills),
            "degree": ", ".join(education.degree for education in candidate.education),
            "graduation_year": ", ".join(str(education.graduation_year) for education in candidate.education),
            "institution": ", ".join(education.institution for education in candidate.education),
            "company": ", ".join(experience.company for experience in candidate.experience),
            "position": ", ".join(experience.position for experience in candidate.experience),
            "start_date": ", ".join(experience.start_date for experience in candidate.experience),
            "end_date": ", ".join(experience.end_date for experience in candidate.experience),
            "date": ", ".join(applications.date for applications in candidate.applications), 
            }

class _ExportCandidateSerializer:
    
    def All_serialize(self,candidate):
        if isinstance(candidate, list):
            return [self.serialize(user) for user in candidate]
        return self.serialize(candidate)

    def serialize(self, candidate):
        return {
            "id": candidate.id,
            "name": candidate.name,
            "age": candidate.age,
            "email": candidate.email,
            "phone": candidate.phone,
            "skills": ", ".join(skill.name for skill in candidate.skills),
            "degree": ", ".join(education.degree for education in candidate.education),
            "graduation_year": ", ".join(str(education.graduation_year) for education in candidate.education),
            "institution": ", ".join(education.institution for education in candidate.education),
            "company": ", ".join(experience.company for experience in candidate.experience),
            "position": ", ".join(experience.position for experience in candidate.experience),
            "start_date": ", ".join(experience.start_date for experience in candidate.experience),
            "end_date": ", ".join(experience.end_date for experience in candidate.experience),
            "date": ", ".join(applications.date for applications in candidate.applications), 
            }


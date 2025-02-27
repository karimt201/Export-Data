import flask as fk
import http
import helpers.exceptions as  exceptions
import controllers.writer as writer
import controllers.candidate_info as cd


class ExportCandidateController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')
        self.operation = self.request.args.get("operation")

    
    @property
    def validator(self):
        return _CreateExtensionValidator()
    
    @property
    def handler(self):
        return _ExtensionCreator()
    
    @property
    def serializer(self):
        return _ExportCandidateSerializer()
    
    def export_record(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.export_candidate(self.operation)
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ExportAllCandidateController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')
        self.operation = self.request.args.get("operation")

        
    @property
    def validator(self):
        return _CreateExtensionValidator()
    
    @property
    def handler(self):
        return _ExtensionCreator()
    
    @property
    def serializer(self):
        return _ExportCandidateSerializer()

    def export_all_records(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.export_all_candidate(self.operation)
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class _CreateExtensionBuilder:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.candidate = None
        self.row_data = None
        self.extension_file = None
    
    @property
    def writer(self):
        return writer
    
    @property
    def handler(self):
        return cd._CandidateBusinessHandler()
    
    @property
    def serializer(self):
        return _DataSerializer()

    def prepare_candidate_data(self):
        candidate_id = self.body_request.get("candidate_id")
        self.candidate = self.handler.get(candidate_id)
        serializer = self.serializer.All_serialize(self.candidate)
        self.row_data = self.writer.RowExcelData(serializer)

    def prepare_all_candidate_data(self):
        self.candidate = self.handler.get_all()
        serializer = self.data_serializer.All_serialize(self.candidate)
        self.row_data = self.writer.RowExcelData(serializer)

    def create_file(self,extension):
        self.manger = self.writer.DataManger(extension)

    def save_file(self):
        filename = self.body_request.get("filename")
        self.manger.save(self.row_data, filename)
        return self.candidate
    

# builder Director
ExtensionCreator = {
    "pdf": writer.PDFCreator(),
    "csv": writer.CSVCreator(),
    "xlsx": writer.ExcelCreator(),
}

class _ExtensionCreator:
    
    @property
    def create(self):
        return _CreateExtensionBuilder()
    
    @property
    def excel_creator(self):
        return writer.ExcelCreator()
    
    @property
    def extension_creator(self):
        return ExtensionCreator

    def export_candidate(self,operation):
        extension = self.extension_creator.get(operation)
        self.create.prepare_candidate_data()
        if operation == "xlsx":
            self.create.create_file(self.excel_creator)
        else:
            self.create.create_file(extension)
        return self.create.save_file()

    def export_all_candidate(self,operation):
        extension = self.extension_creator.get(operation)
        self.create.prepare_all_candidate_data()
        if operation == "xlsx":
            self.create.create_file(self.excel_creator)
        else:
            self.create.create_file(extension)
        return self.create.save_file()


# Validation
class _CreateExtensionValidator:
    
    def validate(self,token, body):
        self.is_valid_token(token)
        self.is_valid_fileName(body.get("filename"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")
        
    def is_valid_fileName(self, fileName):
        if not fileName:
            raise exceptions.RequiredInputError("filename is required")
        self._is_valid_fileName(fileName)

    def _is_valid_fileName(self, fileName):
        if not isinstance(fileName, str):
            raise exceptions.InvalidInputError("filename is not valid string")

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


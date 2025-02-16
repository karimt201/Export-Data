import flask as fk
import http
import exceptions
import data_handler as dh
import models as md
import re
import controllers.writer as writer
import controllers.candidate_info as ci


# Builder interface
class CreateExtension:

    def prepare_data(self):
        raise exceptions._NotImplementError("children must implement this method")

    def create_file(self, extension):
        raise exceptions._NotImplementError("children must implement this method")

    def save_file(self, filename):
        raise exceptions._NotImplementError("children must implement this method")



class _CreateExtensionController(CreateExtension):
    def __init__(self):
        self.candidate = None
        self.row_data = None
        self.extension_file = None

    
    def handler(self, business_handler_test=None):
        return business_handler_test or _CandidateBusinessHandler()

    
    def request(self, request_test=None):
        return request_test or fk.request.args

    
    def request_body(self, request_test=None):
        return request_test or fk.request.get_json()
    
    @property
    def data_serializer(self, serializer_test=None):
        return serializer_test or _DataSerializer

    
    def row_excel_data(self, row_excel_data_test=None):
        return row_excel_data_test or writer

    def prepare_data(self,page_test=None,per_page_test=None,candidate_id_test=None,handler_test=None):
        page = self.request(page_test).get("page", type=int)
        per_page = self.request(per_page_test).get("per_page", 3, type=int)
        candidate_id = self.request_body(candidate_id_test).get("candidate_id")
        if candidate_id:
            self.candidate = self.handler(handler_test).get(candidate_id)
        elif page:
            self.candidate = self.handler(handler_test).get_paginated(page, per_page)
        else:
            self.candidate = self.handler(handler_test).get_all()
        serializer = self.data_serializer(self.candidate).data_serialize()
        self.row_data = self.row_excel_data(page_test).RowExcelData(serializer)

    def create_file(self, extension):
        self.extension_file = extension

    def data_manger(self,data_manger_test=None):
        return data_manger_test or  writer

    def save_file(self, filename,data_manger_test=None):
        manger = self.data_manger(data_manger_test).DataManger(self.extension_file)
        manger.save(self.row_data, filename)
        return self.candidate


# Main
class _CandidateController:

    def __init__(self, candidate_test=None):
        self.request_body = candidate_test or fk.request.get_json()

    
    def handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    
    def request(self, request_test=None):
        return request_test or fk.request.args

    @property
    def extension_creator(self, extension_creator_test=None):
        return extension_creator_test or _ExtensionCreator
    
    @property
    def candidate_info(self, candidate_info_test=None,request_body=None):
        return candidate_info_test or ci._Candidateinfo

    def create(self,operation_test=None,info_test=None,add_test=None):
        try:
            operation = self.request(operation_test).get("operation")
            info = self.request(info_test).get("info")
            file_name = self.request_body.get("fileName")
            if operation:
                _CreateExtensionValidator(self.request_body).All_validate()
                record = self.extension_creator(operation).export(file_name)
                return _Serializer(record, file_name).All_serialize(),http.HTTPStatus.CREATED,
            elif info:
                return self.candidate_info(info,self.request_body).post()
            else:
                _AddCandidateValidator(self.request_body).All_validate()
                record = self.handler(add_test).post(self.request_body)
                return _Serializer(record, file_name).All_serialize(),http.HTTPStatus.CREATED,
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


# builder Director
ExtensionCreator = {
    "pdf": writer.PDFCreator(),
    "csv": writer.CSVCreator(),
    "xlsx": writer.ExcelCreator(),
}


class _ExtensionCreator:
    def __init__(self, operation,extension_test=None):
        self.operation = operation
        self._create_controller = extension_test or _CreateExtensionController()
        self._extension = None

    @property
    def create(self):
        return self._create_controller

    def extension_creator(self,extension_creator_test=None):
        return extension_creator_test or ExtensionCreator
    
    def extension(self,operation_test=None):
        self._extension = self.extension_creator(operation_test).get(self.operation)
        return self._extension

    def export(self, filename,operation_test=None):
        self.create.prepare_data()
        if self.operation == "xlsx":
            self.create.create_file(writer.ExcelCreator())
        else:
            self.create.create_file(self.extension(operation_test))
        return self.create.save_file(filename)


# BusinessHandler
class _CandidateBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.CandidateModel)

    def post(self, request_body):
        record = self.data.create(request_body)
        return record

    def get_all(self):
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records

    def get(self, _id):
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record

    def get_paginated(self, page, per_page):
        pagination = self.data.get_paginated(page, per_page)
        if not pagination.items:
            raise exceptions._NotFoundError("No Records in this Page")
        return pagination.items


# Validation
class _CreateExtensionValidator:
    def __init__(self, json_body=None):
        self.json_body = json_body

    def All_validate(self):
        self.validate(self.json_body)

    def validate(self, body):
        self.is_valid_fileName(body.get("filename"))

    def is_valid_fileName(self, fileName):
        if not fileName:
            raise exceptions._RequiredInputError("filename is required")
        self._is_valid_fileName(fileName)

    def _is_valid_fileName(self, fileName):
        if not isinstance(fileName, str):
            raise exceptions._InvalidInputError("filename is not valid string")

class _AddCandidateValidator:
    def __init__(self, json_body=None):
        self.json_body = json_body

    def All_validate(self):
        if isinstance(self.json_body, list):
            for body in self.json_body:
                self.validate(body)
        else:
            self.validate(self.json_body)

    def validate(self, body):
        self.is_valid_name(body.get("name"))
        self.is_valid_age(body.get("age"))
        self.is_valid_email(body.get("email"))
        self.is_valid_phone(body.get("phone"))

    def is_valid_name(self, name):
        if not name:
            raise exceptions._RequiredInputError("name is required")
        self._is_valid_name(name)

    def _is_valid_name(self, name):
        if not isinstance(name, str):
            raise exceptions._InvalidInputError("name is not valid string")

    def is_valid_age(self, age):
        if not age:
            raise exceptions._RequiredInputError("age is required")
        self._is_valid_age(age)

    def _is_valid_age(self, age):
        if not isinstance(age, int):
            raise exceptions._InvalidInputError("age is not valid int")

    def is_valid_email(self, email):
        if not email:
            raise exceptions._RequiredInputError("Email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise exceptions._InvalidInputError("Email is not valid")

    def is_valid_phone(self, phone):
        if not phone:
            raise exceptions._RequiredInputError("phone is required")
        self._is_valid_phone(phone)
        
    def _is_valid_phone(self, phone):
        if not isinstance(phone, str):
            raise exceptions._InvalidInputError("phone must be a number")


# Serialization
class _DataSerializer:
    def __init__(self, user=None, filename=None):
        self.user = user
        self.filename = filename

    def data_serialize(self):
        if isinstance(self.user, list):
            return [self.serialize(user) for user in self.user]
        return [self.serialize(self.user)]

    def serialize(self, user=None):
        user = user or self.user
        return {
            "name": user.name,
            "age": user.age,
            "email": user.email,
            "phone": user.phone,
            "skills": ", ".join(skill.name for skill in user.skills),
            "degree": ", ".join(education.degree for education in user.education),
            "graduation_year": ", ".join(str(education.graduation_year) for education in user.education),
            "institution": ", ".join(education.institution for education in user.education),
            "company": ", ".join(experience.company for experience in user.experience),
            "position": ", ".join(experience.position for experience in user.experience),
            "start_date": ", ".join(experience.start_date for experience in user.experience),
            "end_date": ", ".join(experience.end_date for experience in user.experience),
            "date": ", ".join(applications.date for applications in user.applications),
        }


class _Serializer:
    def __init__(self, user=None, filename=None):
        self.user = user
        self.filename = filename

    def All_serialize(self):
        if isinstance(self.user, list):
            return [self.all_serialize(user) for user in self.user]
        return self.all_serialize(self.user)

    def all_serialize(self, user=None):
        user = user or self.user
        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "email": user.email,
            "phone": user.phone,
            "skills": ", ".join(skill.name for skill in user.skills) if user.skills else None,
            "degree": ", ".join(education.degree for education in user.education),
            "graduation_year": ", ".join(str(education.graduation_year) for education in user.education),
            "institution": ", ".join(education.institution for education in user.education),
            "company": ", ".join(experience.company for experience in user.experience),
            "position": ", ".join(experience.position for experience in user.experience),
            "start_date": ", ".join(experience.start_date for experience in user.experience),
            "end_date": ", ".join(experience.end_date for experience in user.experience),
            "date": ", ".join(applications.date for applications in user.applications), 
            }

# ErrorSerialize
class _ErrorSerialize:
    def core_error_serialize(self, error, status):
        return {
            "status": status,
            "description": status.phrase,
            "message": error.message,
        }

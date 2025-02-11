import flask as fk
import http
import exceptions
import controllers.csv as csv
import controllers.pdf as pdf
import controllers.excel as xlsx
import data_handler as dh
import models as md
import re
import controllers.writer as writer


# Builder interface
class BuilderInterface:
    
    def prepare_data(self):
        raise exceptions._NotImplementError("children must implement this method")
    
    def create_file(self):
        raise exceptions._NotImplementError("children must implement this method")
    
    def save_file(self):
        raise exceptions._NotImplementError("children must implement this method")

# Builder
class _CandidateController(BuilderInterface):
    def __init__(self):
        self.candidate = None
        self.row_data = None
        self.csv_file = None
        
    @property
    def handler(self,business_handler_test=None):
        return business_handler_test or _CandidateBusinessHandler()
    
    @property
    def request(self,request_test=None):
        return request_test or fk.request.args.get
    
    @property
    def data_serializer(self,serializer_test=None):
        return serializer_test or _DataSerializer
    
    @property
    def row_excel_data(self,row_excel_data_test=None):
        return row_excel_data_test or writer.RowExcelData
    
    def prepare_data(self):
        page = self.request("page", type=int)
        per_page = self.request("per_page", 3 , type=int)
        candidate_id = self.request("candidateId")
        if candidate_id :
            self.candidate = self.handler.get(candidate_id)
        elif page:
            self.candidate = self.handler.get_paginated(page,per_page)
        else:
            self.candidate = self.handler.get_all()
        serializer = self.data_serializer(self.candidate)._data_serialize()
        self.row_data = self.row_excel_data(serializer)
    
    def create_file(self,exten):
        self.csv_file = exten
    
    @property
    def data_manger(self,data_manger_test=None):
        return data_manger_test or writer.DataManger
    
    def save_file(self,filename):
        manger = self.data_manger(self.csv_file)
        manger.save(self.row_data, filename)
        return self.candidate

# Main
class _CreateAllCandidateController:
    
    def __init__(self, candidate_test=None):
        self._request_body = candidate_test or fk.request.get_json()

    @property
    def handler(self,handler_test):
        return handler_test or _CandidateBusinessHandler()
    
    @property
    def request(self,request_test=None):
        return request_test or fk.request.args.get
    
    @property
    def _extension_creator(self,extension_creator_test=None):
        return extension_creator_test or _ExtensionCreator
    
    def create(self):
        try:
            operation = self.request("operation")
            file_name = self._request_body.get("fileName")
            if operation:
                _AllCandidateValidator(self._request_body)._All_validate()
                record = self._extension_creator(operation).export(file_name)
            else:
                _AddCandidateValidator(self._request_body)._All_validate()
                record = self.handler.post(self._request_body)
            return _Serializer(record,file_name)._All_serialize(), http.HTTPStatus.CREATED
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


# builder Director
ExtensionCreator = {"pdf": writer.PDFCreator(), "csv": writer.CSVCreator(), "xlsx": writer.ExcelCreator()}

class _ExtensionCreator:
    def __init__(self,operation):
        self.operation = operation

    @property
    def create(self):
        return _CandidateController()
    
    @property
    def extension(self):
        return ExtensionCreator.get(self.operation)
    
    def export(self,filename):
        self.create.prepare_data()
        if self.operation == "xlsx":
            self.create.create_file(writer.ExcelCreator())
        else:
            self.create.create_file(self.extension)
        return self.create.save_file(filename)

# BusinessHandler
class _CandidateBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.CandidateModel)
        
    def post(self, request_body):
        if request_body.get("age") < 30:
            raise exceptions._InvalidInputError("Age must be greater than 30")
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
class _AllCandidateValidator:
    def __init__(self, json_body=None):
        self.json_body = json_body

    def _All_validate(self):
        self.validate(self.json_body)

    def validate(self, body):
        self.is_valid_fileName(body.get("fileName"))
        
    def is_valid_fileName(self, fileName):
        if not fileName:
            raise exceptions._RequiredInputError("fileName is required")
        self._is_valid_fileName(fileName)

    def _is_valid_fileName(self, fileName):
        if not isinstance(fileName, str):
            raise exceptions._InvalidInputError("fileName is not valid string")


class _AddCandidateValidator:
    def __init__(self, json_body=None):
        self.json_body = json_body

    def _All_validate(self):
        if isinstance(self.json_body, list):
            for body in self.json_body:
                self.validate(body)
        else:
            self.validate(self.json_body)

    def validate(self, body):
        self.is_valid_name(body.get("name"))
        self.is_valid_age(body.get("age"))
        self.is_valid_email(body.get("email"))
        self.is_valid_compatibility(body.get("compatibility"))
        self.is_valid_sourcing(body.get("sourcing"))
        self.is_valid_status(body.get("status"))

    def is_valid_name(self, name):
        if not name:
            raise exceptions._RequiredInputError("Name is required")
        self._is_valid_name(name)

    def _is_valid_name(self, name):
        if not isinstance(name, str):
            raise exceptions._InvalidInputError("Name is not valid string")
        
    def is_valid_age(self, age):
        if not age:
            raise exceptions._RequiredInputError("Age is required")
        self._is_valid_age(age)

    def _is_valid_age(self, age):
        if not isinstance(age, int):
            raise exceptions._InvalidInputError("Age is not valid int")

    def is_valid_email(self, email):
        if not email:
            raise exceptions._RequiredInputError("Email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise exceptions._InvalidInputError("Email is not valid")

    def is_valid_compatibility(self, compatibility):
        if compatibility is not None:
            if not compatibility:
                raise exceptions._RequiredInputError("Compatibility is required")
            self._is_valid_compatibility(compatibility)
        else:
            return compatibility

    def _is_valid_compatibility(self, compatibility):
        if not isinstance(compatibility, (int)):
            raise exceptions._InvalidInputError("Compatibility must be a number")

    def is_valid_sourcing(self, sourcing):
        if not sourcing:
            raise exceptions._RequiredInputError("Sourcing is required")
        self._is_valid_sourcing(sourcing)

    def _is_valid_sourcing(self, sourcing):
        if not isinstance(sourcing, str):
            raise exceptions._InvalidInputError("Sourcing is not valid string")

    def is_valid_status(self, status):
        if not status:
            raise exceptions._RequiredInputError("Status is required")
        self._is_valid_status(status)

    def _is_valid_status(self, status):
        if not isinstance(status, str):
            raise exceptions._InvalidInputError("Status is not valid string")

# Serialization
class _DataSerializer:
    def __init__(self, user=None, filename=None):
        self.user = user
        self.filename = filename

    def _data_serialize(self):
        if isinstance(self.user, list):
            return [self.serialize(user) for user in self.user]
        return [self.serialize(self.user)]

    def serialize(self, user=None):
        user = user or self.user
        return {
            "name": user.name,
            "age": user.age,
            "email": user.email,
            "compatibility": user.compatibility,
            "sourcing": user.sourcing,
            "status": user.status,
        }


class _Serializer:
    def __init__(self, user=None, filename=None):
        self.user = user
        self.filename = filename

    def _All_serialize(self):
        if isinstance(self.user, list):
            return [self.all_serialize(user) for user in self.user]
        return self.all_serialize(self.user)
    
    def all_serialize(self,user=None):
        user = user or self.user
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "compatibility": user.compatibility,
            "sourcing": user.sourcing,
            "status": user.status,
            "filename": self.filename,
        }

class _ErrorSerialize:
    def _core_error_serialize(self, error, status):
        return {
            "status": status,
            "description": status.phrase,
            "message": error.message,
        }


import unittest
import http
from assertpy import assert_that
import helpers.exceptions as exceptions
import controllers.export_candidate as export


class TestExportCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ExportCandidateControllerSpy(self.test_request)

    def test_has_expected_properties(self):
        controller = export.ExportCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(export._CreateExtensionValidator)
        assert_that(controller.handler).is_instance_of(export._ExtensionCreator)
        assert_that(controller.serializer).is_instance_of(export._ExportCandidateSerializer)

    def test_register_returns_okay(self):
        response, status_code = self.controller.export_record()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_export_candidate_called_with("operation")
        self.controller.serializer.assert_that_all_serialize_called_with("user object")

    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.export_record()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)

    def test_register_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")

    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.export_record()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class ExportCandidateControllerSpy(export.ExportCandidateController):
    def __init__(self, request):
        super().__init__(request)
        self._validator = ValidatorDouble()
        self._handler = BusinessHandlerDouble()
        self._serializer = SerializerDouble()

    @property
    def validator(self):
        return self._validator

    @property
    def handler(self):
        return self._handler

    @property
    def serializer(self):
        return self._serializer

class TestExportAllCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ExportAllCandidateControllerSpy(self.test_request)

    def test_has_expected_properties(self):
        controller = export.ExportAllCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(export._CreateExtensionValidator)
        assert_that(controller.handler).is_instance_of(export._ExtensionCreator)
        assert_that(controller.serializer).is_instance_of(export._ExportCandidateSerializer)

    def test_register_returns_okay(self):
        response, status_code = self.controller.export_all_records()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_export_candidate_called_with("operation")
        self.controller.handler.assert_that_body_called_with({'test': 'json'})
        self.controller.serializer.assert_that_all_serialize_called_with("user object")

    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.export_all_records()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)

    def test_register_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")

    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.export_all_records()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class ExportAllCandidateControllerSpy(export.ExportAllCandidateController):
    def __init__(self, request):
        super().__init__(request)
        self._validator = ValidatorDouble()
        self._handler = BusinessHandlerDouble()
        self._serializer = SerializerDouble()

    @property
    def validator(self):
        return self._validator

    @property
    def handler(self):
        return self._handler

    @property
    def serializer(self):
        return self._serializer


# class TestCreateExtensionBuilder(unittest.TestCase):
#     def setUp(self):
#         self.test_request = RequestDouble()
#         self.controller = _CreateExtensionBuilderSpy(self.test_request)

#     def test_has_expected_properties(self):
#         controller = export._CreateExtensionBuilder(self.test_request)
#         assert_that(controller.handler).is_instance_of(cd._CandidateBusinessHandler)
#         assert_that(controller.row_excel_data).is_instance_of(writer.RowExcelData)
#         assert_that(controller.date_manger).is_instance_of(writer.DataManger)
#         assert_that(controller.data_serializer).is_instance_of(export._DataSerializer)

#     def test_register_returns_okay(self):
#         response, status_code = self.controller.prepare_candidate_data()
#         assert_that(response.get("status")).is_equal_to("test status")
#         assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
#         self.controller.writer.assert_that_RowExcelData_called_with('Authorization')
#         self.controller.writer.assert_that_DataManger_called_with({'test': 'json'})
#         self.controller.handler.assert_that_export_candidate_called_with("operation")
#         self.controller.serializer.assert_that_all_serialize_called_with("user object")


# class _CreateExtensionBuilderSpy(export._CreateExtensionBuilder):
#     def __init__(self, request):
#         super().__init__(request)
#         self._writer = writerDouble()
#         self._handler = BusinessHandlerDouble()
#         self._serializer = SerializerDouble()

#     @property
#     def writer(self):
#         return self._writer

#     @property
#     def handler(self):
#         return self._handler

#     @property
#     def serializer(self):
#         return self._serializer


class RequestDouble:
    def __init__(self):
        self.headers = self
        self.args = self
        self.given_header = None
    
    def get_json(self):
        return {"test": "json"}
    
    def get(self,header):
        self.given_header = header
        return self.given_header


class ValidatorDouble:
    def __init__(self):
        self.validate_raised_exception = None
        self.validated_called_with = None

    def validate(self,token, body=None):
        self.validated_called_with = token,body
        if self.validate_raised_exception:
            raise self.validate_raised_exception

    def assert_that_validate_token_called_with(self,token):
        assert_that(self.validated_called_with[0]).is_equal_to(token)

    def assert_that_validate_body_called_with(self, body):
        assert_that(self.validated_called_with[1]).is_equal_to(body)


class BusinessHandlerDouble:
    def __init__(self):
        self.given_operation = None
        self.given_body = None
        self.given_candidate_id = None

    def export_candidate(self, operation,body):
        self.given_operation = operation
        self.given_body = body
        return "user object"
    
    def export_all_candidate(self, operation,body):
        self.given_operation = operation
        self.given_body = body
        return "user object"
    
    def get(self,candidate_id):
        self.given_candidate_id = candidate_id
        return "user object"
    
    def assert_that_export_candidate_called_with(self, operation):
        assert_that(self.given_operation).is_equal_to(operation)
        
    def assert_that_export_all_candidate_called_with(self, operation):
        assert_that(self.given_operation).is_equal_to(operation)
        
    def assert_that_get_called_with(self, candidate_id):
        assert_that(self.given_candidate_id).is_equal_to(candidate_id)
        
    def assert_that_export_all_candidate_called_with(self, operation):
        assert_that(self.given_operation).is_equal_to(operation)
        
    def assert_that_body_called_with(self, body):
        assert_that(self.given_body).is_equal_to(body)
            
class SerializerDouble:
    def __init__(self):
        self.serialize_called_with = None
        self.all_serialize_called_with = None

    def serialize(self, user):
        self.serialize_called_with = user
        return {"status": "test status"}
    
    def All_serialize(self, user):
        self.all_serialize_called_with = user
        return {"status": "test status"}

    def assert_that_serialize_called_with(self, user):
        assert_that(self.serialize_called_with).is_equal_to(user)
        
    def assert_that_all_serialize_called_with(self, user):
        assert_that(self.all_serialize_called_with).is_equal_to(user)

# class writerDouble:
#     def __init__(self):
#         self.given_serializer = None
#         self.given_extension = None
    
#     def RowExcelData(self,serializer):
#         self.given_serializer = serializer
#         return "user object"
        
#     def DataManger(self,extension):
#         self.given_extension = extension
#         return "user object"
        
#     def assert_that_RowExcelData_called_with(self, serializer):
#         assert_that(self.given_serializer).is_equal_to(serializer)
        
#     def assert_that_DataManger_called_with(self, extension):
#         assert_that(self.given_extension).is_equal_to(extension)
        

class TestCreateExtensionValidator(unittest.TestCase):
    def setUp(self):
        self.create_extension_validator = export._CreateExtensionValidator()
        
    def test_create_extension_validator(self):
        token_false = False
        token_true = True
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.create_extension_validator.validate(token_false,{})
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.create_extension_validator.validate(token_true,{})
        assert_that(str(exc.exception)).is_equal_to(
            "filename is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.create_extension_validator.validate(token_true,{"filename":1})
        assert_that(str(exc.exception)).is_equal_to(
            "filename is not valid string"
        )


class TestDataSerializer(unittest.TestCase):
    def setUp(self):
        self.data_serializer = export._DataSerializer()
        self.data_serializer_double = DataSerializerDouble()
        
    def test_data_serializer(self):
        data_serializer = self.data_serializer.All_serialize(self.data_serializer_double)
        assert_that(data_serializer[0].get('institution')).is_equal_to("cairo unverisity")


class DataSerializerDouble:
    def __init__(self):
        self.id = 1
        self.name = "karim"
        self.age = 25
        self.email = "karim@gmail.com"
        self.phone = "01016767542"
        self.skills = [self]
        self.education = [self]
        self.experience = [self]
        self.applications = [self]
        self.degree = "high school"
        self.graduation_year = 2025
        self.institution = "cairo unverisity"
        self.company = "arete"
        self.position = "fullstack"
        self.start_date = "2025-2-1"
        self.end_date = "2025-2-10"
        self.date = "2024-2-10"

class TestExportCandidateSerializer(unittest.TestCase):
    def setUp(self):
        self.export_candidate_serializer = export._ExportCandidateSerializer()
        self.export_candidate_serializer_double = ExportCandidateSerializerDouble()
        
    def test_data_serializer(self):
        data_serializer = self.export_candidate_serializer.All_serialize(self.export_candidate_serializer_double)
        assert_that(data_serializer.get('institution')).is_equal_to("cairo unverisity")


class ExportCandidateSerializerDouble:
    def __init__(self):
        self.id = 1
        self.name = "karim"
        self.age = 25
        self.email = "karim@gmail.com"
        self.phone = "01016767542"
        self.skills = [self]
        self.education = [self]
        self.experience = [self]
        self.applications = [self]
        self.degree = "high school"
        self.graduation_year = 2025
        self.institution = "cairo unverisity"
        self.company = "arete"
        self.position = "fullstack"
        self.start_date = "2025-2-1"
        self.end_date = "2025-2-10"
        self.date = "2024-2-10"

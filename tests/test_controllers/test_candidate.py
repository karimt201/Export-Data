import hashlib
import unittest
import http
from assertpy import assert_that
import helpers.exceptions as exceptions
import controllers.candidate_info as candidate
import services.data_handler as dh


class TestAddCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = AddCandidateControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.AddCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._AddCandidateValidator)
        assert_that(controller.handler).is_instance_of(candidate._CandidateBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._CandidateSerializer)
        
    
    def test_register_returns_okay(self):
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.create()
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
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class AddCandidateControllerSpy(candidate.AddCandidateController):
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


class TestUpdateCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = UpdateCandidateControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.UpdateCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._CandidateBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._CandidateSerializer)
        
    def test_update_returns_okay(self):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_update_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)
        
    def test_update_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_update_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class UpdateCandidateControllerSpy(candidate.UpdateCandidateController):
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


class TestReadAllCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadAllCandidateControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadAllCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._CandidateBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._CandidateSerializer)
        
    def test_get_all_returns_okay(self):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_all_serialize_called_with("user object")
    
    def test_get_all_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_all_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadAllCandidateControllerSpy(candidate.ReadAllCandidateController):
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
    
    
class TestReadCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadCandidateControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._CandidateBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._CandidateSerializer)
        
    def test_get_returns_okay(self):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)

    
    def test_get_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadCandidateControllerSpy(candidate.ReadCandidateController):
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


class TestDeleteCandidateController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = DeleteCandidateControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.DeleteCandidateController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._CandidateBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._DeleteSerializer)
        
    def test_delete_returns_okay(self):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_id_is(1)
        self.controller.serializer.assert_that_serialize_called_with(1)
        
    def test_delete_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_delete_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class DeleteCandidateControllerSpy(candidate.DeleteCandidateController):
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


class TestAddCandidateSkillsController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = AddCandidateSkillsControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.AddCandidateSkillsController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._AddSkillsValidator)
        assert_that(controller.handler).is_instance_of(candidate._SkillsBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._SkillsSerializer)
        
    
    def test_register_returns_okay(self):
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.create()
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
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class AddCandidateSkillsControllerSpy(candidate.AddCandidateSkillsController):
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


class TestUpdateCandidateSkillsController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = UpdateCandidateSkillsControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.UpdateCandidateSkillsController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._SkillsBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._SkillsSerializer)
        
    def test_update_returns_okay(self):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_update_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)
        
    def test_update_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_update_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class UpdateCandidateSkillsControllerSpy(candidate.UpdateCandidateSkillsController):
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


class TestReadAllCandidateSkillsController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadAllCandidateSkillsControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadAllCandidateSkillsController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._SkillsBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._SkillsSerializer)
        
    def test_get_all_returns_okay(self):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_all_serialize_called_with("user object")
    
    def test_get_all_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_all_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadAllCandidateSkillsControllerSpy(candidate.ReadAllCandidateSkillsController):
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
    
    
class TestReadCandidateSkillsController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadCandidateSkillsControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadCandidateSkillsController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._SkillsBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._SkillsSerializer)
        
    def test_get_returns_okay(self):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)

    
    def test_get_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadCandidateSkillsControllerSpy(candidate.ReadCandidateSkillsController):
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


class TestDeleteCandidateSkillsController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = DeleteCandidateSkillsControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.DeleteCandidateSkillsController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._SkillsBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._DeleteSerializer)
        
    def test_delete_returns_okay(self):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_id_is(1)
        self.controller.serializer.assert_that_serialize_called_with(1)
        
    def test_delete_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_delete_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class DeleteCandidateSkillsControllerSpy(candidate.DeleteCandidateSkillsController):
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


class TestAddCandidateApplicationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = AddCandidateApplicationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.AddCandidateApplicationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._AddApplicationValidator)
        assert_that(controller.handler).is_instance_of(candidate._ApplicationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ApplicationSerializer)
        
    
    def test_register_returns_okay(self):
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.create()
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
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class AddCandidateApplicationControllerSpy(candidate.AddCandidateApplicationController):
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


class TestUpdateCandidateApplicationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = UpdateCandidateApplicationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.UpdateCandidateApplicationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ApplicationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ApplicationSerializer)
        
    def test_update_returns_okay(self):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_update_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)
        
    def test_update_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_update_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class UpdateCandidateApplicationControllerSpy(candidate.UpdateCandidateApplicationController):
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


class TestReadAllCandidateApplicationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadAllCandidateApplicationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadAllCandidateApplicationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ApplicationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ApplicationSerializer)
        
    def test_get_all_returns_okay(self):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_all_serialize_called_with("user object")
    
    def test_get_all_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_all_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadAllCandidateApplicationControllerSpy(candidate.ReadAllCandidateApplicationController):
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
    
    
class TestReadCandidateApplicationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadCandidateApplicationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadCandidateApplicationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ApplicationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ApplicationSerializer)
        
    def test_get_returns_okay(self):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)

    
    def test_get_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadCandidateApplicationControllerSpy(candidate.ReadCandidateApplicationController):
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


class TestDeleteCandidateApplicationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = DeleteCandidateApplicationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.DeleteCandidateApplicationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ApplicationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._DeleteSerializer)
        
    def test_delete_returns_okay(self):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_id_is(1)
        self.controller.serializer.assert_that_serialize_called_with(1)
        
    def test_delete_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_delete_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class DeleteCandidateApplicationControllerSpy(candidate.DeleteCandidateApplicationController):
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


class TestAddCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = AddCandidateExperienceControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.AddCandidateExperienceController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._AddExperienceValidator)
        assert_that(controller.handler).is_instance_of(candidate._ExperienceBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ExperienceSerializer)
        
    
    def test_register_returns_okay(self):
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.create()
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
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class AddCandidateExperienceControllerSpy(candidate.AddCandidateExperienceController):
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


class TestUpdateCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = UpdateCandidateExperienceControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.UpdateCandidateExperienceController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ExperienceBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ExperienceSerializer)
        
    def test_update_returns_okay(self):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_update_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)
        
    def test_update_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_update_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class UpdateCandidateExperienceControllerSpy(candidate.UpdateCandidateExperienceController):
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


class TestReadAllCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadAllCandidateExperienceControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadAllCandidateExperienceController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ExperienceBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ExperienceSerializer)
        
    def test_get_all_returns_okay(self):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_all_serialize_called_with("user object")
    
    def test_get_all_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_all_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadAllCandidateExperienceControllerSpy(candidate.ReadAllCandidateExperienceController):
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
    
    
class TestReadCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadCandidateExperienceControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadCandidateExperienceController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ExperienceBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._ExperienceSerializer)
        
    def test_get_returns_okay(self):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)

    
    def test_get_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadCandidateExperienceControllerSpy(candidate.ReadCandidateExperienceController):
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


class TestDeleteCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = DeleteCandidateExperienceControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.DeleteCandidateExperienceController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._ExperienceBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._DeleteSerializer)
        
    def test_delete_returns_okay(self):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_id_is(1)
        self.controller.serializer.assert_that_serialize_called_with(1)
        
    def test_delete_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_delete_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class DeleteCandidateExperienceControllerSpy(candidate.DeleteCandidateExperienceController):
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

class TestAddCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = AddCandidateEducationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.AddCandidateEducationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._AddEducationValidator)
        assert_that(controller.handler).is_instance_of(candidate._EducationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._EducationSerializer)
        
    
    def test_register_returns_okay(self):
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.validator.assert_that_validate_body_called_with({'test': 'json'})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.create()
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
        response, status_code = self.controller.create()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class AddCandidateEducationControllerSpy(candidate.AddCandidateEducationController):
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


class TestUpdateCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = UpdateCandidateEducationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.UpdateCandidateEducationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._EducationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._EducationSerializer)
        
    def test_update_returns_okay(self):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_update_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)
        
    def test_update_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_update_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class UpdateCandidateEducationControllerSpy(candidate.UpdateCandidateEducationController):
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


class TestReadAllCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadAllCandidateEducationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadAllCandidateEducationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._EducationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._EducationSerializer)
        
    def test_get_all_returns_okay(self):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_all_serialize_called_with("user object")
    
    def test_get_all_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_all_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadAllCandidateEducationControllerSpy(candidate.ReadAllCandidateEducationController):
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
    
    
class TestReadCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadCandidateEducationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.ReadCandidateEducationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._EducationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._EducationSerializer)
        
    def test_get_returns_okay(self):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.serializer.assert_that_serialize_called_with("user object")
        self.controller.handler.assert_that_id_is(1)

    
    def test_get_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class ReadCandidateEducationControllerSpy(candidate.ReadCandidateEducationController):
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


class TestDeleteCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = DeleteCandidateEducationControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = candidate.DeleteCandidateEducationController(self.test_request)
        assert_that(controller.validator).is_instance_of(candidate._TokenValidator)
        assert_that(controller.handler).is_instance_of(candidate._EducationBusinessHandler)
        assert_that(controller.serializer).is_instance_of(candidate._DeleteSerializer)
        
    def test_delete_returns_okay(self):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_token_called_with('Authorization')
        self.controller.handler.assert_that_id_is(1)
        self.controller.serializer.assert_that_serialize_called_with(1)
        
    def test_delete_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_delete_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("name is required")
        self.expect_bad_request_with_message("name is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("name must be string")
        self.expect_bad_request_with_message("name must be string")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class DeleteCandidateEducationControllerSpy(candidate.DeleteCandidateEducationController):
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


class RequestDouble:
    def __init__(self):
        self.headers = self
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
        self.post_called_with = None
        self.update_called_with = None
        self.given_id = None

    def post(self, request_body):
        self.post_called_with = request_body
        return "user object"

    def get_all(self):
        return "user object"
    
    def update(self,id, request_body):
        self.given_id = id
        self.update_called_with = request_body
        return "user object"
    
    def get(self,id):
        self.given_id = id
        return "user object"
    
    def delete(self,id):
        self.given_id = id
        
    def assert_that_post_called_with(self, request_body):
        assert_that(self.post_called_with).is_equal_to(request_body)
    
    def assert_that_update_called_with(self, request_body):
        assert_that(self.update_called_with).is_equal_to(request_body)

    def assert_that_id_is(self, id):
        assert_that(self.given_id).is_equal_to(id)


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


class TestCandidateBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.operator = OperatorDouble()
        self.token = TokenDouble()
        self.handler = candidate._CandidateBusinessHandler(self.operator, self.token)
        self.request_body = {"email": "new@test.com", "password": "test"}

    def test_post_returns_user_object(self):
        response = self.handler.post(self.request_body)
        self.operator.assert_that_create_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
    
    def test_get_all_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get_all()
        assert_that(str(exc.exception)).is_equal_to("Records does not exist")
        
    def test_get_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get(1)
        assert_that(str(exc.exception)).is_equal_to("Record does not exist")

    def test_update_returns_user_object(self):
        response = self.handler.update(1, self.request_body)
        self.operator.assert_that_update_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
        
    def test_update_returns_user_object(self):
        self.handler.delete(1)
        self.operator.assert_that_get_one_called_with(1)
        self.operator.assert_that_delete_called_with(1)
    

class TestApplicationBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.operator = OperatorDouble()
        self.token = TokenDouble()
        self.handler = candidate._ApplicationBusinessHandler(self.operator, self.token)
        self.request_body = {"email": "new@test.com", "password": "test"}

    def test_post_returns_user_object(self):
        response = self.handler.post(self.request_body)
        self.operator.assert_that_create_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
    
    def test_get_all_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get_all()
        assert_that(str(exc.exception)).is_equal_to("Records does not exist")
        
    def test_get_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get(1)
        assert_that(str(exc.exception)).is_equal_to("Record does not exist")

    def test_update_returns_user_object(self):
        response = self.handler.update(1, self.request_body)
        self.operator.assert_that_update_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
        
    def test_update_returns_user_object(self):
        self.handler.delete(1)
        self.operator.assert_that_get_one_called_with(1)
        self.operator.assert_that_delete_called_with(1)
        

class TestExperienceBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.operator = OperatorDouble()
        self.token = TokenDouble()
        self.handler = candidate._ExperienceBusinessHandler(self.operator, self.token)
        self.request_body = {"email": "new@test.com", "password": "test"}

    def test_post_returns_user_object(self):
        response = self.handler.post(self.request_body)
        self.operator.assert_that_create_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
    
    def test_get_all_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get_all()
        assert_that(str(exc.exception)).is_equal_to("Records does not exist")
        
    def test_get_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get(1)
        assert_that(str(exc.exception)).is_equal_to("Record does not exist")

    def test_update_returns_user_object(self):
        response = self.handler.update(1, self.request_body)
        self.operator.assert_that_update_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
        
    def test_update_returns_user_object(self):
        self.handler.delete(1)
        self.operator.assert_that_get_one_called_with(1)
        self.operator.assert_that_delete_called_with(1)


class TestEducationBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.operator = OperatorDouble()
        self.token = TokenDouble()
        self.handler = candidate._EducationBusinessHandler(self.operator, self.token)
        self.request_body = {"email": "new@test.com", "password": "test"}

    def test_post_returns_user_object(self):
        response = self.handler.post(self.request_body)
        self.operator.assert_that_create_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
    
    def test_get_all_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get_all()
        assert_that(str(exc.exception)).is_equal_to("Records does not exist")
        
    def test_get_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get(1)
        assert_that(str(exc.exception)).is_equal_to("Record does not exist")

    def test_update_returns_user_object(self):
        response = self.handler.update(1, self.request_body)
        self.operator.assert_that_update_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
        
    def test_update_returns_user_object(self):
        self.handler.delete(1)
        self.operator.assert_that_get_one_called_with(1)
        self.operator.assert_that_delete_called_with(1)

        
class TestSkillsBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.operator = OperatorDouble()
        self.token = TokenDouble()
        self.handler = candidate._SkillsBusinessHandler(self.operator, self.token)
        self.request_body = {"email": "new@test.com", "password": "test"}

    def test_post_returns_user_object(self):
        response = self.handler.post(self.request_body)
        self.operator.assert_that_create_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
    
    def test_get_all_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get_all()
        assert_that(str(exc.exception)).is_equal_to("Records does not exist")
        
    def test_get_raise_not_found_error_if_not_return_record(self):
        with self.assertRaises(exceptions.NotFoundError) as exc:
            self.handler.get(1)
        assert_that(str(exc.exception)).is_equal_to("Record does not exist")

    def test_update_returns_user_object(self):
        response = self.handler.update(1, self.request_body)
        self.operator.assert_that_update_called_with(self.request_body)
        assert_that(response).is_equal_to("user object")
        self.operator.assert_that_get_one_called_with(1)
        
    def test_update_returns_user_object(self):
        self.handler.delete(1)
        self.operator.assert_that_get_one_called_with(1)
        self.operator.assert_that_delete_called_with(1)
    

class OperatorDouble:
    def __init__(self):
        self.get_one_called_with = None
        self.create_called_with = None
        self.update_called_with = None
        self.given_id = None
    
    def get_one(self,id):
        self.given_id = id
        return None
    
    def create(self,request):
        self.create_called_with = request
        return "user object"
    
    def get_all(self):
        return None
    
    def update(self,id,request):
        self.given_id = id
        self.update_called_with = request
        return "user object"

    def delete(self,id):
        self.given_id = id
        return f"user id {self.given_id}deleted"
    
    def assert_that_create_called_with(self, request):
        assert_that(self.create_called_with).is_equal_to(request)
        
    def assert_that_get_one_called_with(self, id):
        assert_that(self.given_id).is_equal_to(id)  
        
    def assert_that_update_called_with(self, request):
        assert_that(self.update_called_with).is_equal_to(request)   
        
    def assert_that_delete_called_with(self, id):
        assert_that(self.given_id).is_equal_to(id) 

        
class TokenDouble:
    
    def verify_token(self):
        return {"user_id":1}


class TestAddCandidateValidator(unittest.TestCase):
    def setUp(self):
        self.add_candidate_validator = candidate._AddCandidateValidator()
        
    def test_add_application_validator(self):
        token_false = False
        token_true = True
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_candidate_validator.validate(token_false,{})
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_candidate_validator.validate(token_true,{})
        assert_that(str(exc.exception)).is_equal_to(
            "name is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":1})
        assert_that(str(exc.exception)).is_equal_to(
            "name is not valid string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            "age is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":"karim","age":"1"})
        assert_that(str(exc.exception)).is_equal_to(
            "age is not valid int"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":"karim","age":1})
        assert_that(str(exc.exception)).is_equal_to(
            "email is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":"karim","age":1,"email":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            "email is not valid"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":"karim","age":1,"email":"karim@gmail.com"})
        assert_that(str(exc.exception)).is_equal_to(
            "phone is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_candidate_validator.validate(token_true,{"name":"karim","age":1,"email":"karim@gmail.com","phone":1})
        assert_that(str(exc.exception)).is_equal_to(
            "phone must be a string number"
        )
        
        
class TestAddApplicationValidator(unittest.TestCase):
    def setUp(self):
        self.add_application_validator = candidate._AddApplicationValidator()
        
    def test_add_application_validator(self):
        token_false = False
        token_true = True
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_application_validator.validate(token_false,{})
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_application_validator.validate(token_true,{})
        assert_that(str(exc.exception)).is_equal_to(
            "date is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_application_validator.validate(token_true,{"date":1})
        assert_that(str(exc.exception)).is_equal_to(
            "date is not valid string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_application_validator.validate(token_true,{"date":"2010-10-10"})
        assert_that(str(exc.exception)).is_equal_to(
            "candidate_id is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_application_validator.validate(token_true,{"date":"2010-10-10","candidate_id":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            "candidate_id is not valid int"
        )


class TestAddExperienceValidator(unittest.TestCase):
    def setUp(self):
        self.add_experience_validator = candidate._AddExperienceValidator()
        
    def test_add_experience_validator(self):
        token_false = False
        token_true = True
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_experience_validator.validate(token_false,{})
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_experience_validator.validate(token_true,{"name":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            "company is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":1})
        assert_that(str(exc.exception)).is_equal_to(
            "company is not valid string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":"arete"})
        assert_that(str(exc.exception)).is_equal_to(
            "position is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":"arete","position":1})
        assert_that(str(exc.exception)).is_equal_to(
            "position is not valid string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_experience_validator.validate(token_true,{
            "company":"arete",
            "position":"backend"})
        assert_that(str(exc.exception)).is_equal_to(
            "start_date is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":"arete","position":"backend","start_date":1})
        assert_that(str(exc.exception)).is_equal_to(
            "start_date is not valid date string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_experience_validator.validate(token_true,{
            "company":"arete",
            "position":"backend",
            "start_date":"2010-10-10"})
        assert_that(str(exc.exception)).is_equal_to(
            "end_date is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":"arete","position":"backend","start_date":"2010-10-10","end_date":1})
        assert_that(str(exc.exception)).is_equal_to(
            "end_date is not valid date string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":"arete","position":"backend","start_date":"2010-10-10","end_date":"2010-10-20"})
        assert_that(str(exc.exception)).is_equal_to(
            "candidate_id is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_experience_validator.validate(token_true,{"company":"arete","position":"backend","start_date":"2010-10-10","end_date":"2010-10-20","candidate_id":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            "candidate_id is not valid int"
        )


class TestAddEducationValidator(unittest.TestCase):
    def setUp(self):
        self.add_education_validator = candidate._AddEducationValidator()
        
    def test_add_education_validator(self):
        token_false = False
        token_true = True
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_education_validator.validate(token_false,{})
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_education_validator.validate(token_true,{})
        assert_that(str(exc.exception)).is_equal_to(
            "degree is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_education_validator.validate(token_true,{"degree":1})
        assert_that(str(exc.exception)).is_equal_to(
            "degree is not valid string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_education_validator.validate(token_true,{"degree":"high school"})
        assert_that(str(exc.exception)).is_equal_to(
            "graduation_year is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_education_validator.validate(token_true,{"degree":"high school","graduation_year":"2023"})
        assert_that(str(exc.exception)).is_equal_to(
            "graduation_year is not valid int"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_education_validator.validate(token_true,{
            "degree":"high school",
            "graduation_year":2023})
        assert_that(str(exc.exception)).is_equal_to(
            "institution is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_education_validator.validate(token_true,{"degree":"high school","graduation_year":2023,"institution":1})
        assert_that(str(exc.exception)).is_equal_to(
            "institution is not valid string"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_education_validator.validate(token_true,{
            "degree":"high school",
            "graduation_year":2023,"institution":"GUC"})
        assert_that(str(exc.exception)).is_equal_to(
            "candidate_id is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_education_validator.validate(token_true,{"degree":"high school","graduation_year":2023,"institution":"GUC","candidate_id":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            "candidate_id is not valid int"
        )
    

class TestAddSkillsValidator(unittest.TestCase):
    def setUp(self):
        self.add_skills_validator = candidate._AddSkillsValidator()
        
    def test_add_skills_validator(self):
        token_false = False
        token_true = True
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_skills_validator.validate(token_false,{})
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.add_skills_validator.validate(token_true,{})
        assert_that(str(exc.exception)).is_equal_to(
            "name is required"
        )
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.add_skills_validator.validate(token_true,{"name":1})
        assert_that(str(exc.exception)).is_equal_to(
            "name is not valid string"
        )
        
        

class TestTokenValidator(unittest.TestCase):
    def setUp(self):
        self.token_validator = candidate._TokenValidator()
        
    def test_token_validator(self):
        token_false = False
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.token_validator.validate(token_false)
        assert_that(str(exc.exception)).is_equal_to(
            "token is missing"
        )
        
        
class TestCandidateSerializer(unittest.TestCase):
    def setUp(self):
        self.candidate_serializer = candidate._CandidateSerializer()
        self.candidate_serializer_double = CandidateSerializerDouble()

    def test_candidate_serializer(self):
        candidate_serializer = self.candidate_serializer.All_serialize(self.candidate_serializer_double)
        assert_that(candidate_serializer.get('email')).is_equal_to("karim@gmail.com")


class CandidateSerializerDouble:
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
        self.created_at = "2 am"
        self.updated_at = "3 am"


        
class TestApplicationSerializer(unittest.TestCase):
    def setUp(self):
        self.application_serializer = candidate._ApplicationSerializer()
        self.application_serializer_double = ApplicationSerializerDouble()

    def test_application_serializer(self):
        application_serializer = self.application_serializer.All_serialize(self.application_serializer_double)
        assert_that(application_serializer.get('Application_date')).is_equal_to("2010-2-2")


class ApplicationSerializerDouble:
    def __init__(self):
        self.id = 1
        self.date = "2010-2-2"
        self.name = "karim"
        self.created_at = "2 am"
        self.updated_at = "3 am"
        self.candidate = self


class TestExperienceSerializer(unittest.TestCase):
    def setUp(self):
        self.experience_serializer = candidate._ExperienceSerializer()
        self.experience_serializer_double = ExperienceSerializerDouble()

    def test_experience_serializer(self):
        experience_serializer = self.experience_serializer.All_serialize(self.experience_serializer_double)
        assert_that(experience_serializer.get('company')).is_equal_to("arete")


class ExperienceSerializerDouble:
    def __init__(self):
        self.id = 1
        self.company = "arete"
        self.position = "developer"
        self.start_date = "2010-2-2"
        self.end_date = "2010-2-10"
        self.name = "karim"
        self.created_at = "2 am"
        self.updated_at = "3 am"
        self.candidate = self


class TestEducationSerializer(unittest.TestCase):
    def setUp(self):
        self.education_serializer = candidate._EducationSerializer()
        self.education_serializer_double = EducationSerializerDouble()
        
    def test_experience_serializer(self):
        education_serializer = self.education_serializer.All_serialize(self.education_serializer_double)
        assert_that(education_serializer.get('institution')).is_equal_to("GUC")


class EducationSerializerDouble:
    def __init__(self):
        self.id = 1
        self.degree = "commerce"
        self.graduation_year = 2023
        self.institution = "GUC"
        self.name = "karim"
        self.created_at = "2 am"
        self.updated_at = "3 am"
        self.candidate = self


class TestSkillsSerializer(unittest.TestCase):
    def setUp(self):
        self.skills_serializer = candidate._SkillsSerializer()
        self.skills_serializer_double = SkillsSerializerDouble()
        
    def test_skills_serializer(self):
        skills_serializer = self.skills_serializer.All_serialize(self.skills_serializer_double)
        assert_that(skills_serializer.get('skill_name')).is_equal_to("Reading")
        
        
class SkillsSerializerDouble:
    def __init__(self):
        self.id = 1
        self.name = "Reading"
        self.created_at = "2 am"
        self.updated_at = "3 am"
        self.name = "Reading"
        self.candidates = [self]
        
        
class TestDeleteSerializer(unittest.TestCase):
    def setUp(self):
        self.delete_serializer = candidate._DeleteSerializer()
        
    def test_delete_serializer(self):
        delete_serializer = self.delete_serializer.serialize(1)
        assert_that(delete_serializer.get('message')).is_equal_to("record id 1 has been removed successfully")
        

class TestErrorSerializer(unittest.TestCase):
    def setUp(self):
        self.error_serializer = candidate._ErrorSerialize()
        self.error_serializer_double = ErrorDouble()
        self.status_serializer_double = StatusDouble()
        
    def test_error_serializer(self):
        error_serializer = self.error_serializer._get_serialized_response(self.error_serializer_double,self.status_serializer_double)
        assert_that(error_serializer.get('status')).is_equal_to("phrase")
        
        
class ErrorDouble:
    def __init__(self):
        self.message = "message"


class StatusDouble:
    def __init__(self):
        self.phrase = "phrase"
        self.description = "description"
        

class TestCrudOperator(unittest.TestCase):
    def setUp(self):
        self.crud_operator_model_post_double = CrudOperatorPostModelDouble
        self.crud_operator_model_double = CrudOperatorModelDouble()
    
    def test_get_operator(self):
        crud_operator_session_double = CrudOperatorSessionDouble()

        crud_operator = dh.CrudOperator(self.crud_operator_model_double,crud_operator_session_double)
        crud_operator.get_all()
        crud_operator.get_one(1)
        crud_operator.get_paginated(1,3)
        crud_operator_session_double.assert_that_crud_operator_session_get_by_id(1)

        with self.assertRaises(exceptions.InvalidFieldError) as exc:
            crud_operator.create({"name":"karim"})
        assert_that(str(exc.exception)).is_equal_to(
            f"name field is not valid"
        )
        self.crud_operator_model_double.assert_that_crud_operator_model_get_by_page_number(1)
        self.crud_operator_model_double.assert_that_crud_operator_model_get_per_page(3)
        self.crud_operator_model_double.assert_that_crud_operator_model_paginate_error_out(False)
        self.crud_operator_model_double.assert_that_crud_operator_model_filter_by_name("name")
        
    def test_get_operator(self):
        crud_operator_session_double = CrudOperatorSessionDouble()

        crud_operator = dh.CrudOperator(self.crud_operator_model_post_double,crud_operator_session_double)
        crud_operator.create({"id":1,"phone":"01016767542"})

        crud_operator_session_double.assert_that_crud_operator_session_add_new_record_by_phone("01016767542")
        
        
class CrudOperatorPostModelDouble:
    id = 1
    phone = "01016767542"
    
    def __init__(self,**filtered_data):
        self.filtered_data = filtered_data

class CrudOperatorModelDouble:
    
    def __init__(self):
        self.query = self
        self.page = None
        self.per_page = None
        self.error_out = None
        self.name = None
        
    def all(self):
        return "success"
    
    def paginate(self,page,per_page,error_out):
        self.page = page
        self.per_page = per_page
        self.error_out = error_out
        return self.page
    
    def filter_by(self,name):
        self.name = name
        return self
    
    def first(self):
        return "success"

    def assert_that_crud_operator_model_get_by_page_number(self,page):
        assert_that(self.page).is_equal_to(page)
        
    def assert_that_crud_operator_model_get_per_page(self,per_page):
        assert_that(self.per_page).is_equal_to(per_page)
        
    def assert_that_crud_operator_model_paginate_error_out(self,error_out):
        assert_that(self.error_out).is_equal_to(error_out)
        
    def assert_that_crud_operator_model_filter_by_name(self,name):
        assert_that(self.name).is_equal_to(name)
        
        
class CrudOperatorSessionDouble:
    def __init__(self):
        self.model = None
        self.id = None
        self.record = None
        
    def get(self,model,id):
        self.model = model
        self.id = id
        return self.id
    
    def commit(self):
        pass
    
    def add(self,record):
        self.record = record
        return self.record
    
    def assert_that_crud_operator_session_get_by_id(self,id):
        assert_that(self.id).is_equal_to(id)
        
    def assert_that_crud_operator_session_add_new_record_by_phone(self,record):
        assert_that(self.record.phone).is_equal_to(record)

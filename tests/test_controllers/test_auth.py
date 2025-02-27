import hashlib
import unittest
import http
from assertpy import assert_that
import helpers.exceptions as exceptions
import controllers.auth as auth


class TestRegisterController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = RegisterControllerSpy(self.test_request)

    def test_has_expected_properties(self):
        controller = auth.RegisterController(self.test_request)
        assert_that(controller.validator).is_instance_of(auth._UserValidator)
        assert_that(controller.handler).is_instance_of(auth._UserBusinessHandler)
        assert_that(controller.serializer).is_instance_of(auth._RegisterSerializer)

    def test_register_returns_okay(self):
        response, status_code = self.controller.register()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_called_with({"test": "json"})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")

    def test_register_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.register()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)

    def test_register_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("email is required")
        self.expect_bad_request_with_message("email is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("email must have @")
        self.expect_bad_request_with_message("email must have @")

    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.register()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class RegisterControllerSpy(auth.RegisterController):
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


class TestUpdateUserController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = UpdateUserControllerSpy(self.test_request)
    
    def test_has_expected_properties(self):
        controller = auth.UpdateUserController(self.test_request)
        assert_that(controller.validator).is_instance_of(auth._TokenValidator)
        assert_that(controller.handler).is_instance_of(auth._UserBusinessHandler)
        assert_that(controller.serializer).is_instance_of(auth._UserSerializer)
        
    def test_update_returns_okay(self):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_called_with("Authorization")
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
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("email is required")
        self.expect_bad_request_with_message("email is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("email must have @")
        self.expect_bad_request_with_message("email must have @")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.update(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        

class UpdateUserControllerSpy(auth.UpdateUserController):
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


class TestReadAllUserController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadAllUserControllerSpy(self.test_request)

    def test_has_expected_properties(self):
        controller = auth.ReadAllUserController(self.test_request)
        assert_that(controller.validator).is_instance_of(auth._TokenValidator)
        assert_that(controller.handler).is_instance_of(auth._UserBusinessHandler)
        assert_that(controller.serializer).is_instance_of(auth._UserSerializer)
        
    def test_get_all_returns_okay(self):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_called_with("Authorization")
        self.controller.serializer.assert_that_all_serialize_called_with("user object")
        
    def test_get_all_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_all_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("email is required")
        self.expect_bad_request_with_message("email is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("email must have @")
        self.expect_bad_request_with_message("email must have @")

    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get_all()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
            

class ReadAllUserControllerSpy(auth.ReadAllUserController):
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


class TestReadUserController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = ReadUserControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = auth.ReadUserController(self.test_request)
        assert_that(controller.validator).is_instance_of(auth._TokenValidator)
        assert_that(controller.handler).is_instance_of(auth._UserBusinessHandler)
        assert_that(controller.serializer).is_instance_of(auth._UserSerializer)
        
    def test_get_returns_okay(self):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_called_with("Authorization")
        self.controller.handler.assert_that_id_is(1)
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_get_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_get_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("email is required")
        self.expect_bad_request_with_message("email is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("email must have @")
        self.expect_bad_request_with_message("email must have @")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.get(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


class ReadUserControllerSpy(auth.ReadUserController):
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


class TestDeleteUserController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = DeleteUserControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = auth.DeleteUserController(self.test_request)
        assert_that(controller.validator).is_instance_of(auth._TokenValidator)
        assert_that(controller.handler).is_instance_of(auth._UserBusinessHandler)
        assert_that(controller.serializer).is_instance_of(auth._DeleteSerializer)
        
    def test_delete_returns_okay(self):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_called_with("Authorization")
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
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("email is required")
        self.expect_bad_request_with_message("email is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("email must have @")
        self.expect_bad_request_with_message("email must have @")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.delete(1)
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class DeleteUserControllerSpy(auth.DeleteUserController):
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

class TestLoginController(unittest.TestCase):
    def setUp(self):
        self.test_request = RequestDouble()
        self.controller = LoginControllerSpy(self.test_request)
        
    def test_has_expected_properties(self):
        controller = auth.LoginController(self.test_request)
        assert_that(controller.validator).is_instance_of(auth._LoginValidator)
        assert_that(controller.handler).is_instance_of(auth._LoginBusinessHandler)
        assert_that(controller.serializer).is_instance_of(auth._LoginSerializer)
        
    def test_login_returns_okay(self):
        response, status_code = self.controller.login()
        assert_that(response.get("status")).is_equal_to("test status")
        assert_that(status_code).is_equal_to(http.HTTPStatus.OK)
        self.controller.validator.assert_that_validate_called_with({"test": "json"})
        self.controller.handler.assert_that_post_called_with({"test": "json"})
        self.controller.serializer.assert_that_serialize_called_with("user object")
        
    def test_login_returns_not_found(self):
        self.controller.validator.validate_raised_exception = exceptions.NotFoundError("test error")
        response, status_code = self.controller.login()
        assert_that(response.get("status")).is_equal_to("Not Found")
        assert_that(response.get("description")).is_equal_to("Nothing matches the given URI")
        assert_that(response.get("message")).is_equal_to("test error")
        assert_that(status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
        
    def test_login_returns_bad_request(self):
        self.controller.validator.validate_raised_exception = exceptions.RequiredInputError("email is required")
        self.expect_bad_request_with_message("email is required")
        self.controller.validator.validate_raised_exception = exceptions.InvalidInputError("email must have @")
        self.expect_bad_request_with_message("email must have @")
        
    def expect_bad_request_with_message(self, message):
        response, status_code = self.controller.login()
        assert_that(response.get("status")).is_equal_to("Bad Request")
        assert_that(response.get("description")).is_equal_to("Bad request syntax or unsupported method")
        assert_that(response.get("message")).is_equal_to(message)
        assert_that(status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        
        
class LoginControllerSpy(auth.LoginController):
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

    def validate(self, body):
        self.validated_called_with = body
        if self.validate_raised_exception:
            raise self.validate_raised_exception

    def assert_that_validate_called_with(self, body):
        assert_that(self.validated_called_with).is_equal_to(body)


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


class TestUserValidator(unittest.TestCase):
    def setUp(self):
        self.validator = auth._UserValidator()

    def test_validate_raises_required_input_error_if_email_is_not_sent(self):
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.validator.validate({"password": "test"})
        assert_that(str(exc.exception)).is_equal_to("email is required")

    def test_validate_raises_invalid_input_error_if_email_is_invalid(self):
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.validator.validate({"email": "test", "password": "test","role": "test"})
        assert_that(str(exc.exception)).is_equal_to("email is not valid")

    def test_validate_raises_required_input_error_if_password_is_not_sent(self):
        with self.assertRaises(exceptions.RequiredInputError) as exc:
            self.validator.validate({"email": "test@test.com"})
        assert_that(str(exc.exception)).is_equal_to("password is required")


class TestUserBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.operator = OperatorDouble()
        self.token = TokenDouble()
        self.handler = auth._UserBusinessHandler(self.operator, self.token)
        self.request_body = {"email": "new@test.com", "password": "test"}

    def test_post_raise_invalid_input_error_if_email_is_already_registered(self):
        self.operator.first_return_value = "already_existed_user"
        self.request_body["email"] = "already_existed_email"
        with self.assertRaises(exceptions.InvalidInputError) as exc:
            self.handler.post(self.request_body)
        assert_that(str(exc.exception)).is_equal_to("User is already registered!")

    def test_post_returns_the_new_user_with_hashed_password(self):
        new_user = self.handler.post(self.request_body)
        hashed_password = hashlib.sha256(
            self.request_body.get("password").encode()
        ).hexdigest()
        assert_that(new_user.get("email")).is_equal_to(self.request_body.get("email"))
        assert_that(new_user.get("password")).is_not_equal_to(hashed_password)
        self.operator.assert_that_user_filter_data_called_with(
            self.request_body.get("email")
        )
        self.operator.assert_that_first_is_called()
        self.operator.assert_that_create_called_with(self.request_body)


class OperatorDouble:
    def __init__(self):
        self.first_return_value = None
        self.user_filter_data_called_with = None
        self.first_is_called = False
        self.create_called_with = None

    def user_filter_data(self, email):
        self.user_filter_data_called_with = email
        return self

    def first(self):
        self.first_is_called = True
        return self.first_return_value

    def create(self, request_body):
        self.create_called_with = request_body
        return request_body

    def assert_that_user_filter_data_called_with(self, email):
        self.user_filter_data_called_with = email

    def assert_that_first_is_called(self):
        assert_that(self.first_is_called).is_true()

    def assert_that_create_called_with(self, request_body):
        assert_that(self.create_called_with).is_equal_to(request_body)


class TokenDouble:
    pass


class TestRegisterSerializer(unittest.TestCase):

    def test_serialize_returns_the_user_object(self):
        user = UserDouble()
        response = auth._RegisterSerializer().serialize(user)
        assert_that(response.get("user")).is_equal_to("test_id")
        assert_that(response.get("email")).is_equal_to("test@test.com")
        assert_that(response.get("message")).is_equal_to(
            "user id test_id registered successfully!"
        )


class UserDouble:
    def __init__(self):
        self.email = "test@test.com"
        self.id = "test_id"


# class TestGoogleClient(unittest.TestCase):

#     def setUp(self):
#         self.requests = RequestsDouble()
#         self.client = auth.GoogleClient(self.requests)

#     def test_get_data_calls_requests_get_with_correct_url(self):
#         response = self.client.get_data()
#         assert_that(response).is_equal_to("success")
#         self.requests.assert_that_get_callled_with_url("https://www.google.com")
#         self.requests.assert_that_get_callled_with_params({"lang": "python", "num": 10})
#         self.requests.assert_that_get_callled_with_headers(
#             {"Content-Type": "application/json", "token": "bearer test_token"}
#         )

#     def test_post_data_calls_requests_post_with_correct_url(self):
#         response = self.client.post_data()
#         assert_that(response).is_equal_to("success")
#         self.requests.assert_that_post_callled_with_url("https://www.google.com")
#         self.requests.assert_that_post_callled_with_json({"lang": "python", "num": 10})
#         self.requests.assert_that_post_callled_with_headers(
#             {"Content-Type": "application/json", "token": "bearer test_token"}
#         )


# class RequestsDouble:
#     def __init__(self):
#         self.get_called_with = {}
#         self.post_called_with = {}

#     def get(self, url, params, headers):
#         self.get_called_with.update(url=url, params=params, headers=headers)
#         return "success"

#     def post(self, url, json, headers):
#         self.post_called_with.update(url=url, json=json, headers=headers)
#         return "success"

#     def assert_that_get_callled_with_url(self, url):
#         assert_that(self.get_called_with.get("url")).is_equal_to(url)

#     def assert_that_get_callled_with_params(self, params):
#         assert_that(self.get_called_with.get("params")).is_equal_to(params)

#     def assert_that_get_callled_with_headers(self, headers):
#         assert_that(self.get_called_with.get("headers")).is_equal_to(headers)

#     def assert_that_post_callled_with_url(self, url):
#         assert_that(self.post_called_with.get("url")).is_equal_to(url)

#     def assert_that_post_callled_with_json(self, json):
#         assert_that(self.post_called_with.get("json")).is_equal_to(json)

#     def assert_that_post_callled_with_headers(self, headers):
#         assert_that(self.post_called_with.get("headers")).is_equal_to(headers)

    # For your knowledge
    # def request(self, **kwargs):
    #     self.post_called_with.update(kwargs)


if __name__ == "__main__":
    unittest.main()

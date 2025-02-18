import flask as fk
import exceptions
import data_handler as dh
import models as md
import http
import re
import datetime as dt
from passlib.hash import pbkdf2_sha256
import tokens as tk


class Auth:

    def date_validator(self):
        raise exceptions._NotImplementError("children must implement this method")

    def date_handler(self):
        raise exceptions._NotImplementError("children must implement this method")

    def date_serializer(self):
        raise exceptions._NotImplementError("children must implement this method")


class _RegisterBuilder(Auth):
    def __init__(self,body_test=None):
        self.body_request = body_test or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _RegisterValidator()

    def experience_handler(self, handler_test=None):
        return handler_test or _RegisterBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _RegisterSerializer()

    def date_validator(self, validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self, handler_test=None):
        self.response = self.experience_handler(handler_test).post(self.body_request)

    def date_serializer(self, serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response)

class _LoginBuilder(Auth):
    def __init__(self,body_test=None):
        self.body_request = body_test or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _LoginValidator()

    def experience_handler(self, handler_test=None):
        return handler_test or _LoginBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _LoginSerializer()

    def date_validator(self, validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self, handler_test=None):
        self.response = self.experience_handler(handler_test).post(self.body_request)

    def date_serializer(self, serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response)

class _LoginController:
    def __init__(self):
        self.log_in = _LoginBuilder()
        
    def login(self):
        try:
            self.log_in.date_validator()
            self.log_in.date_handler()
            return self.log_in.date_serializer()
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
    
class _RegisterController:

    def __init__(self):
        self.register_builder = _RegisterBuilder()
        
    def register(self):
        try:
            self.register_builder.date_validator()
            self.register_builder.date_handler()
            return self.register_builder.date_serializer()
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,

class _RegisterValidator:

    def validate(self, body):
        self.is_valid_email(body.get("email"))
        self.is_valid_password(body.get("password"))

    def is_valid_email(self, email):
        if not email:
            raise exceptions._RequiredInputError("email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise exceptions._InvalidInputError("email is not valid")
        
    def is_valid_password(self, password):
        if not password:
            raise exceptions._RequiredInputError("password is required")
        
        
class _LoginValidator:

    def validate(self, body):
        self.is_valid_email(body.get("email"))
        self.is_valid_password(body.get("password"))
        self.is_valid_role(body.get("role"))

    def is_valid_email(self, email):
        if not email:
            raise exceptions._RequiredInputError("email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise exceptions._InvalidInputError("email is not valid")
        
    def is_valid_password(self, password):
        if not password:
            raise exceptions._RequiredInputError("password is required")
        
    def is_valid_role(self, role):
        if not role:
            raise exceptions._RequiredInputError("role is required")

class _RegisterBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.UserModel)

    def hash_pass(self,hash_test=None):
        return hash_test or pbkdf2_sha256
    
    def post(self, request_body,hash_test=None):
        get_email = request_body.get("email")
        password = self.hash_pass(hash_test).hash(request_body.get("password"))
        user = self.data.user_filter_data(email=get_email).first()
        if not user:
            new_user = self.data.create_user(request_body,get_email,password)
        if user :
            raise exceptions._InvalidInputError("User is already registered!")
        return new_user


class _LoginBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.UserModel)

    def hash_pass(self,hash_test=None):
        return hash_test or pbkdf2_sha256
    
    def token(self,token_test=None):
        return token_test or tk.Token()
    
    def post(self, request_body,hash_test=None,token_test=None):
        email = request_body.get("email")
        password = request_body.get("password")
        role = request_body.get("role")
        user = self.data.user_filter_data(email=email).first()
        if user :
            payload = {
            'user_id':user.id,
            'role':role,
            'exp': dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=24)
        }
            password = self.hash_pass(hash_test).verify(password,user.password)
            token = self.token(token_test).create_token(payload)
            return token
        elif not user:
            raise exceptions._InvalidInputError("email or password not valid")
        

class _RegisterSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, user,status_test=None):
        return {
            'message': f'{user.email} registered successfully!'
        }, self.http_test(status_test).OK

class _LoginSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, token,status_test=None):
        return {
            'token': token,
            'message': 'Log in successfully!'
        }, self.http_test(status_test).OK

# ErrorSerialize
class _ErrorSerialize:
    def core_error_serialize(self, error, status):
        return {
            "status": status,
            "description": status.phrase,
            "message": error.message,
        }

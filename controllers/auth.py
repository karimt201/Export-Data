import flask as fk
import helper.exceptions as exceptions
import services.data_handler as dh
import models as md
import http
import re
import datetime as dt
from passlib.hash import pbkdf2_sha256
import services.tokens as tk
import controllers.candidate_info as cd

    
class RegisterController:
    def __init__(self,body_test=None):
        self.body_request = body_test or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _UserValidator()

    def handler(self, handler_test=None):
        return handler_test or _UserBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _RegisterSerializer()
    
    def register(self,validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class UpdateUserController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _UserBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _UserSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def update(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).update(id,self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadAllUserController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _UserBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _UserSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def get_all(self,validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get_all()
            return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadUserController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _UserBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _UserSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get(id)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class DeleteUserController:
    def __init__(self):
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _UserBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _DeleteSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def delete(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).delete(id)
            return self.serializer(serializer_test).serialize(id),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class LoginController:
    def __init__(self,body_test=None):
        self.body_request = body_test or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _LoginValidator()

    def handler(self, handler_test=None):
        return handler_test or _LoginBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _LoginSerializer()
    
    def login(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class _UserValidator:

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
        

class _TokenValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self):
        self.is_valid_token(self.token)

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")

        
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

class _UserBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.UserModel)
        self.token = token_test or tk.Token()

    def hash_pass(self,hash_test=None):
        return hash_test or pbkdf2_sha256
    
    def post(self, request_body,hash_test=None):
        user_email = request_body.get("email")
        password = self.hash_pass(hash_test).hash(request_body.get("password"))
        user = self.data.user_filter_data(email=user_email).first()
        if not user:
            request_body['password'] = password
            new_user = self.data.create(request_body)
        if user :
            raise exceptions._InvalidInputError("User is already registered!")
        return new_user
    
    def get_all(self):
        token = self.token.verify_token()
        self.data.get_one(token['user_id'])
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        token = self.token.verify_token()
        self.data.get_one(token['user_id'])
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body,hash_test=None):
        token = self.token.verify_token()
        self.data.get_one(token['user_id'])
        password = request_body.get("password")
        if password :
            hashed_password = self.hash_pass(hash_test).hash(password)
            request_body['password'] = hashed_password
        record = self.data.update(id,request_body)
        return record
    
    def delete(self,id):
        token = self.token.verify_token()
        self.data.get_one(token['user_id'])
        record = self.data.delete(id)
        return record


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
        

class _UserSerializer:

    def All_serialize(self,user):
        if isinstance(user, list):
            return [self.serialize(user) for user in user]
        return self.serialize(user)
    
    def serialize(self, user):
        return {
            "user":user.id,
            "email":user.email,
        }
        
class _RegisterSerializer:

    def serialize(self, user):
        return {
            "user":user.id,
            "email":user.email,
            'message': f'user id {user.id} registered successfully!'
        }

class _LoginSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, token,status_test=None):
        return {
            'token': token,
            'message': 'Log in successfully!'
        }, self.http_test(status_test).OK


class _DeleteSerializer:
    
    def serialize(self, id):
        return {
            "message":f"record id {id} has been removed successfully"
        }

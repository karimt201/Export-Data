import flask as fk
import helpers.exceptions as exceptions
import services.data_handler as dh
import models as md
import http
import re
import datetime as dt
import hashlib
import services.tokens as tk
import controllers.candidate_info as cd

class RegisterController:
    def __init__(self, test_request=None):
        self.request = test_request
        self.body_request = self.request.get_json()

    @property
    def validator(self):
        return _UserValidator()
    
    @property
    def handler(self):
        return _UserBusinessHandler()
    
    @property
    def serializer(self):
        return _RegisterSerializer()
    
    def register(self):
        """
        Validates input and register a new user.
        
        Returns: Repersents the user details and status code
        
        """
        try:
            self.validator.validate(self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response), http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class UpdateUserController:
    def __init__(self, test_request=None):
        self.request = test_request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return  _TokenValidator()

    @property
    def handler(self):
        return _UserBusinessHandler()
    
    @property
    def serializer(self):
        return  _UserSerializer()
    
    def update(self,id):
        """
        Validates input and updates a user.

        :param id: The ID of the user to update.
        
        Returns: Repersents the user details and status code
        
        """
        try:
            self.validator.validate(self.token)
            self.response = self.handler.update(id,self.body_request)
            return self.serializer.serialize(self.response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadAllUserController:
    def __init__(self, test_request=None):
        self.request = test_request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _UserBusinessHandler()

    @property
    def serializer(self):
        return _UserSerializer()

    def get_all(self):
        """
        Validates token and retrieves all users.
        
        Returns: Repersents all users details and status code
        
        """
        try:
            self.validator.validate(self.token)
            response = self.handler.get_all()
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadUserController:
    def __init__(self, test_request=None):
        self.request = test_request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return  _TokenValidator()
    
    @property
    def handler(self):
        return _UserBusinessHandler()

    @property
    def serializer(self):
        return _UserSerializer()

    def get(self,id):
        """
        Validates token and retrieves a user by ID.
        
        :param id: The ID of the user to retrieve.
    
        Returns: Repersents user details and status code
        
        """
        try:
            self.validator.validate(self.token)
            response = self.handler.get(id)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class DeleteUserController:
    def __init__(self, test_request=None):
        self.request = test_request
        self.token = self.request.headers.get('Authorization')
    
    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _UserBusinessHandler()

    @property
    def serializer(self):
        return cd._DeleteSerializer()

    def delete(self,id):
        """
        Validates token and delete a user by ID.
                
        :param id: The ID of the user to delete.
            
        Returns: Repersents Candidate iD user and status code
        
        """
        try:
            self.validator.validate(self.token)
            self.handler.delete(id)
            return self.serializer.serialize(id),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class LoginController:
    def __init__(self,test_request=None):
        self.request = test_request
        self.body_request = self.request.get_json()

    @property
    def validator(self):
        return _LoginValidator()

    @property
    def handler(self):
        return _LoginBusinessHandler()

    @property
    def serializer(self):
        return _LoginSerializer()
    
    def login(self):
        """
        Validates input and login user.
        
        Returns: Repersents the access token and status code
        
        """
        try:
            self.validator.validate(self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return cd._ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class _UserBusinessHandler:
    def __init__(self, operator_test=None,token_test=None):
        self.operator = operator_test or dh.CrudOperator(md.UserModel)
        self.token = token_test or tk.Token()
    
    def post(self, request_body):
        """
        Register user.

        :param request_body: The data for the new user.
        
        :return: The registered user record.
        
        """
        user_email = request_body.get("email")
        user = self.operator.user_filter_data(email=user_email).first()
        if user : raise exceptions.InvalidInputError("User is already registered!")
        decoded_password = request_body.get("password").encode('utf-8')
        request_body['password'] = hashlib.sha256(decoded_password).hexdigest()
        new_user = self.operator.create(request_body)
        return new_user
    
    
    def update(self,id,request_body):
        """
        Updates a user by ID.

        :param id: The ID of the user to update.
        
        :param request_body: The updated data for the user.
        
        :return: The updated user record.
        
        """
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        decoded_password = request_body.get("password")
        if decoded_password :
            hashed_password = hashlib.sha256(decoded_password).hexdigest()
            request_body['password'] = hashed_password
        record = self.operator.update(id,request_body)
        return record
    
    def get_all(self):
        """
        Retrieves all users.

        :return: A list of user records.
        
        """
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        records = self.operator.get_all()
        if not records:
            raise exceptions.NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        """
        Retrieves a user by ID.

        :param _id: The ID of the user to retrieve.
        
        :return: The user record.
        
        """
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.get_one(_id)
        if not record:
            raise exceptions.NotFoundError("Record does not exist")
        return record
    
    def delete(self,id):
        """
        Deletes a candidate by ID.

        :param id: The ID of the candidate to delete.
        
        :return: The deleted candidate record.
        
        """
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.delete(id)
        return record


class _LoginBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.UserModel)
        self.token = token_test or tk.Token()
    
    def post(self, request_body):
        """
        Login user.

        :param request_body: The data for the user.
        
        :return: The user access token.
        
        """
        email = request_body.get("email")
        decoded_password = request_body.get("password").encode('utf-8')
        role = request_body.get("role")
        user = self.data.user_filter_data(email=email).first()
        if not user: raise exceptions.InvalidInputError("email or password not valid")
        hashed_input_password = hashlib.sha256(decoded_password).hexdigest()
        if hashed_input_password != user.password: raise exceptions.InvalidInputError("Email or password is not valid")
        payload = {
            'user_id':user.id,
            'role':role,
            'exp': dt.datetime.now(dt.timezone.utc) + dt.timedelta(hours=24)
        }
        token = self.token.create_token(payload)
        return token
        

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"
class _UserValidator:
    def __init__(self):
        self.required_attr = ["email", "password","role"]

    def validate(self, body):
        """
        Validates user data.
        
        :param body: The user data to validate.
        
        """
        self._check_required(body)
        self._is_valid_email(body.get("email"))

    def _check_required(self, body):
        for attr in self.required_attr:
            if not (body and body.get(attr)):
                raise exceptions.RequiredInputError(f"{attr} is required")

    def _is_valid_email(self, email):
        if not re.match(EMAIL_REGEX, email):
            raise exceptions.InvalidInputError("email is not valid")


class _TokenValidator:

    def validate(self,token):
        self.is_valid_token(token)

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")

    
class _LoginValidator:

    def validate(self, body):
        """
        Validates login user data.
        
        :param body: The login user data to validate.
        
        """
        self.is_valid_email(body.get("email"))
        self.is_valid_password(body.get("password"))

    def is_valid_email(self, email):
        if not email:
            raise exceptions.RequiredInputError("email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(EMAIL_REGEX, email):
            raise exceptions.InvalidInputError("email is not valid")
        
    def is_valid_password(self, password):
        if not password:
            raise exceptions.RequiredInputError("password is required")
        


        
class _UserSerializer:

    def All_serialize(self,user):
        if isinstance(user, list):
            return [self.serialize(user) for user in user]
        return self.serialize(user)
    
    def serialize(self, user):
        """
        Serializes a user.

        :param user : The user to serialize.
        
        :return: Serialized The user data.
        
        """
        return {
            "user":user.id,
            "email":user.email,
            "role":user.role,
            "created_at": user.created_at,
            "updated_at": user.updated_at,

        }
        
class _RegisterSerializer:

    def serialize(self, user):
        """
        Serializes a registered user.

        :param user : The user to serialize.
        
        :return: Serialized The register user data.
        
        """
        return {
            "user":user.id,
            "email":user.email,
            "role":user.role,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
            'message': f'user id {user.id} registered successfully!'
        }

class _LoginSerializer:
    
    def serialize(self, token):
        """
        Serializes a user access token.

        :param token : The user access token serialize.
        
        :return: Serialized The user access token.
        
        """
        return {
            'token': token,
            'message': 'Log in successfully!'
        }



# # Special casses 
# import requests


# class GoogleClient:
#     def __init__(self, test_request=None):
#         self.requests = test_request or requests

#     def get_data(self):
#         params = {
#             "lang": "python",
#             "num": 10
#         }
#         headers = {
#             "Content-Type": "application/json",
#             'token': 'bearer test_token'
#         }
#         return self.requests.get("https://www.google.com", params=params, headers=headers)

#     def post_data(self):
#         body = {
#             "lang": "python",
#             "num": 10
#         }
#         headers = {
#              "Content-Type": "application/json",
#              'token': 'bearer test_token'
#         }
#         return self.requests.post("https://www.google.com", json=body, headers=headers)

        # return self.requests.request("GET", "https://www.google.com", params=params, headers=headers)
        # return self.requests.request("POST", "https://www.google.com", json=body, headers=headers)

#
# code to test the google client
# response = GoogleClient().get_data()
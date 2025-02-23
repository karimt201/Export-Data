import helper.exceptions as exceptions
import http
import services.data_handler as dh
import flask as fk
import models as md
import datetime as dt
import services.tokens as tk
import re


# Controllers
class AddCandidateController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddCandidateValidator()

    def handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _CandidateSerializer()

    def create(self,validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

    
class UpdateCandidateController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _CandidateSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def update(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).update(id,self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadAllCandidateController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _CandidateSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get_all(self,validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get_all()
            return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class ReadCandidateController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _CandidateSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get(id)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class DeleteCandidateController:
    def __init__(self):
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

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
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class AddCandidateSkillsController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddSkillsValidator()

    def handler(self, skills_handler_test=None):
        return skills_handler_test or _SkillsBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _SkillsSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def create(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

        
class UpdateCandidateSkillsController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _SkillsBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _SkillsSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def update(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).update(id,self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadAllCandidateSkillsController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _SkillsBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _SkillsSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def get_all(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get_all()
            return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class ReadCandidateSkillsController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _SkillsBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _SkillsSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get(id)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class DeleteCandidateSkillsController:
    def __init__(self):
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _SkillsBusinessHandler()

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
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

    
class _AddCandidateApplicationController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddApplicationValidator()

    def handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ApplicationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def create(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

    
class UpdateCandidateApplicationController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ApplicationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def update(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).update(id,self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class ReadAllCandidateApplicationController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ApplicationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def get_all(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get_all()
            return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadCandidateApplicationController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ApplicationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get(id)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class DeleteCandidateApplicationController:
    def __init__(self):
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

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
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class AddCandidateExperienceController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddExperienceValidator()

    def handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ExperienceSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def create(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class UpdateCandidateExperienceController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ExperienceSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def update(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).update(id,self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadAllCandidateExperienceController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ExperienceSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def get_all(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get_all()
            return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class ReadCandidateExperienceController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ExperienceSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get(id)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class DeleteCandidateExperienceController:
    def __init__(self):
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

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
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class AddCandidateEducationController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddEducationValidator()

    def handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _EducationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def create(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate(self.body_request)
            self.response = self.handler(handler_test).post(self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class UpdateCandidateEducationController:
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _EducationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def update(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).update(id,self.body_request)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND


class ReadAllCandidateEducationController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _EducationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def get_all(self, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get_all()
            return self.serializer(serializer_test).All_serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class ReadCandidateEducationController:
    def __init__(self):
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()
    
    def handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _EducationSerializer()

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus

    def get(self,id, validator_test=None,handler_test=None,serializer_test=None,status_test=None):
        try:
            self.validator(validator_test).validate()
            self.response = self.handler(handler_test).get(id)
            return self.serializer(serializer_test).serialize(self.response),self.http_test(status_test).OK
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

class DeleteCandidateEducationController:
    def __init__(self):
        self.response = None
        
    def validator(self, validator_test=None):
        return validator_test or _TokenValidator()

    def handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

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
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

    
# BusinessHandler
class _CandidateBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.CandidateModel)
        self.token = token_test or tk.Token().verify_token()

    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record

    def get_all(self):
        self.data.get_one(self.token['user_id'])
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records

    def get_one(self, _id):
        self.data.get_one(self.token['user_id'])
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.update(id,request_body)
        return record
    
    def delete(self,id):
        self.data.get_one(self.token['user_id'])
        record = self.data.delete(id)
        return record


class _ApplicationBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.ApplicationModel)
        self.token = token_test or tk.Token().verify_token()
        
    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record
    
    def get_all(self):
        self.data.get_one(self.token['user_id'])
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        self.data.get_one(self.token['user_id'])
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.update(id,request_body)
        return record
    
    def delete(self,id):
        self.data.get_one(self.token['user_id'])
        record = self.data.delete(id)
        return record


class _ExperienceBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.ExperienceModel)
        self.token = token_test or tk.Token().verify_token()

    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record
    
    def get_all(self):
        self.data.get_one(self.token['user_id'])
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        self.data.get_one(self.token['user_id'])
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.update(id,request_body)
        return record
    
    def delete(self,id):
        self.data.get_one(self.token['user_id'])
        record = self.data.delete(id)
        return record


class _EducationBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.EducationModel)
        self.token = token_test or tk.Token().verify_token()

    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record
    
    def get_all(self):
        self.data.get_one(self.token['user_id'])
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        self.data.get_one(self.token['user_id'])
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.update(id,request_body)
        return record
    
    def delete(self,id):
        self.data.get_one(self.token['user_id'])
        record = self.data.delete(id)
        return record


class _SkillsBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.SkillModel)
        self.token = token_test or tk.Token().verify_token()

    def candidate_handler(self, candidate_handler_test=None):
        return candidate_handler_test or _CandidateBusinessHandler()
    
    def post(self, request_body,candidate_handler_test=None):
        self.data.get_one(self.token['user_id'])
        skill_id = request_body.get("id")
        candidate_id = request_body.get("candidate_id")
        candidate = self.candidate_handler(candidate_handler_test).get(candidate_id)
        skill = self.data.user_filter_data(id=skill_id).first()
        if not skill:
            skill = self.data.create_many(request_body)
        if skill in candidate.skills:
            raise exceptions._InvalidInputError("this candidate has this skill already")
        candidate.skills.append(skill)
        self.data.commit()
        return skill    
    
    def get_all(self):
        self.data.get_one(self.token['user_id'])
        records = self.data.get_all()
        if not records:
            raise exceptions._NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        self.data.get_one(self.token['user_id'])
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.update(id,request_body)
        return record
    
    def delete(self,id):
        self.data.get_one(self.token['user_id'])
        record = self.data.delete(id)
        return record
    

# Validation
class _AddCandidateValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self, body):
        self.is_valid_token(self.token)
        self.is_valid_name(body.get("name"))
        self.is_valid_age(body.get("age"))
        self.is_valid_email(body.get("email"))
        self.is_valid_phone(body.get("phone"))
        
    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")

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
            raise exceptions._RequiredInputError("email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise exceptions._InvalidInputError("email is not valid")

    def is_valid_phone(self, phone):
        if not phone:
            raise exceptions._RequiredInputError("phone is required")
        self._is_valid_phone(phone)
        
    def _is_valid_phone(self, phone):
        if not isinstance(phone, str):
            raise exceptions._InvalidInputError("phone must be a number")


class _AddApplicationValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')
        
    def validate(self, body,body_test=None):
        self.is_valid_token(self.token)
        self.is_valid_date(body.get("date"),body_test)
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")
        
    def is_valid_date(self, date,body_test=None):
        if not date:
            raise exceptions._RequiredInputError("date is required")
        self._is_valid_date(date,body_test)

    def data_time(self,date_time_test=None):
        return date_time_test or dt.datetime
    
    def _is_valid_date(self, date,body_test=None):
        try:
            return self.data_time(body_test).strptime(date, "%Y-%m-%d")
        except ValueError:
            raise exceptions._InvalidInputError(
                f"{date} is not in valid date format (YYYY-MM-DD)"
            )
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions._RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions._InvalidInputError("candidate_id is not valid int")


class _AddExperienceValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self, body,body_test=None):
        self.is_valid_token(self.token)
        self.is_valid_company(body.get("company"))
        self.is_valid_position(body.get("position"))
        self.is_valid_start_date(body.get("start_date"),body_test)
        self.is_valid_end_date(body.get("end_date"),body_test)
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")
        
    def is_valid_company(self, company):
        if not company:
            raise exceptions._RequiredInputError("company is required")
        self._is_valid_company(company)

    def _is_valid_company(self, company):
        if not isinstance(company, str):
            raise exceptions._InvalidInputError("company is not valid string")

    def is_valid_position(self, position):
        if not position:
            raise exceptions._RequiredInputError("position is required")
        self._is_valid_position(position)

    def _is_valid_position(self, position):
        if not isinstance(position, str):
            raise exceptions._InvalidInputError("position is not valid int")

    def is_valid_start_date(self, start_date,body_test=None):
        if not start_date:
            raise exceptions._RequiredInputError("start_date is required")
        self._is_valid_start_date(start_date,body_test)

    def start_date(self,date_time_test=None):
        return date_time_test or dt.datetime
    
    def _is_valid_start_date(self, start_date,body_test=None):
        try:
            self.start_date(body_test).strptime(start_date, "%Y-%m-%d")
            return True
        except ValueError:
            raise exceptions._InvalidInputError(
                f"{start_date} is not in valid date format (YYYY-MM-DD)"
            )

    def is_valid_end_date(self, end_date,body_test=None):
        if not end_date:
            raise exceptions._RequiredInputError("end_date is required")
        self._is_valid_start_date(end_date,body_test)

    def end_date(self,date_time_test=None):
        return date_time_test or dt.datetime
    
    def _is_valid_end_date(self, end_date,body_test=None):
        try:
            self.end_date(body_test).strptime(end_date, "%Y-%m-%d")
            return True
        except ValueError:
            raise exceptions._InvalidInputError(
                f"{end_date} is not in valid date format (YYYY-MM-DD)"
            )
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions._RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions._InvalidInputError("candidate_id is not valid int")


class _TokenValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self):
        self.is_valid_token(self.token)

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")

        
class _AddEducationValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self, body):
        self.is_valid_token(self.token)
        self.is_valid_degree(body.get("degree"))
        self.is_valid_graduation_year(body.get("graduation_year"))
        self.is_valid_institution(body.get("institution"))
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")
        
    def is_valid_degree(self, degree):
        if not degree:
            raise exceptions._RequiredInputError("degree is required")
        self._is_valid_degree(degree)

    def _is_valid_degree(self, degree):
        if not isinstance(degree, str):
            raise exceptions._InvalidInputError("degree is not valid string")

    def is_valid_graduation_year(self, graduation_year):
        if not graduation_year:
            raise exceptions._RequiredInputError("graduation_year is required")
        self._is_valid_graduation_year(graduation_year)

    def _is_valid_graduation_year(self, graduation_year):
        if not isinstance(graduation_year, (int)):
            raise exceptions._InvalidInputError("graduation_year is not valid int")

    def is_valid_institution(self, institution):
        if not institution:
            raise exceptions._RequiredInputError("institution is required")
        self._is_valid_institution(institution)

    def _is_valid_institution(self, institution):
        if not isinstance(institution, str):
            raise exceptions._InvalidInputError("institution is not valid string")
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions._RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions._InvalidInputError("candidate_id is not valid int")


class _AddSkillsValidator:
    def __init__(self,token_test=None):
        self.token = token_test or fk.request.headers.get('Authorization')

    def validate(self, body):
        self.is_valid_token(self.token)
        self.is_valid_name(body.get("name"))
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions._RequiredInputError("token is missing")
        
    def is_valid_name(self, name):
        if not name:
            raise exceptions._RequiredInputError("name is required")
        self._is_valid_name(name)

    def _is_valid_name(self, name):
        if not isinstance(name, str):
            raise exceptions._InvalidInputError("name is not valid string")
        
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions._RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions._InvalidInputError("candidate_id is not valid int")


# Serialization
class _CandidateSerializer:
    
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


class _ApplicationSerializer:

    def All_serialize(self,application):
        if isinstance(application, list):
            return [self.serialize(user) for user in application]
        return self.serialize(application)
    
    def serialize(self, application):
        return {
                "id": application.id,
                "Application_date": application.date,
                "candidate_name": application.candidate.name,
            }


class _ExperienceSerializer:
    
    def All_serialize(self,experience):
        if isinstance(experience, list):
            return [self.serialize(user) for user in experience]
        return self.serialize(experience)
    
    def serialize(self, experience):
        return {
            "id": experience.id,
            "company": experience.company,
            "position": experience.position,
            "start_date": experience.start_date,
            "end_date": experience.end_date,
            "candidate_id": experience.candidate.id,
            "candidate_name": experience.candidate.name,
        }


class _EducationSerializer:

    def All_serialize(self,education):
        if isinstance(education, list):
            return [self.serialize(user) for user in education]
        return self.serialize(education)

    def serialize(self, education):
        return {
            "id": education.id,
            "degree": education.degree,
            "graduation_year": education.graduation_year,
            "institution": education.institution,
            "candidate_name": education.candidate.name,
        }
        
class _DeleteSerializer:

    def serialize(self, id):
        return {
            "message":f"record id {id} has been removed successfully"
        }

class _SkillsSerializer:

    def All_serialize(self,skill):
        if isinstance(skill, list):
            return [self.serialize(user) for user in skill]
        return self.serialize(skill)

    def serialize(self, skill):
        return {
            "skill_id": skill.id,
            "skill_name": skill.name,
            "candidate_id": ", ".join(str(candidate.id) for candidate in skill.candidates),
            "candidate_name": ", ".join(candidate.name for candidate in skill.candidates),
        }

# ErrorSerialize
class _ErrorSerialize:
    def core_error_serialize(self, error, status):
        return {
            "status": status,
            "description": status.phrase,
            "message": error.message,
        }

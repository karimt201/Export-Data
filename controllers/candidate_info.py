import helpers.exceptions as exceptions
import http
import services.data_handler as dh
import flask as fk
import models as md
import services.tokens as tk
import re


# Controllers
class AddCandidateController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _AddCandidateValidator()
    
    @property
    def handler(self):
        return  _CandidateBusinessHandler()

    @property
    def serializer(self):
        return _CandidateSerializer()

    def create(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response), http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class UpdateCandidateController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _CandidateBusinessHandler()

    @property
    def serializer(self):
        return  _CandidateSerializer()

    def update(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.update(id,self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadAllCandidateController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _CandidateBusinessHandler()

    @property
    def serializer(self):
        return _CandidateSerializer()

    def get_all(self):
        try:
            self.validator.validate(self.token)
            response = self.handler.get_all()
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class ReadCandidateController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _CandidateBusinessHandler()

    @property
    def serializer(self):
        return _CandidateSerializer()

    def get(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.get(id)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class DeleteCandidateController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')
        
    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _CandidateBusinessHandler()

    @property
    def serializer(self):
        return _DeleteSerializer()

    def delete(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.delete(id)
            return self.serializer.serialize(id),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class AddCandidateSkillsController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _AddSkillsValidator()

    @property
    def handler(self):
        return _SkillsBusinessHandler()

    @property
    def serializer(self):
        return _SkillsSerializer()

    def create(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

        
class UpdateCandidateSkillsController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _SkillsBusinessHandler()

    @property
    def serializer(self):
        return _SkillsSerializer()

    def update(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.update(id,self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadAllCandidateSkillsController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _SkillsBusinessHandler()

    @property
    def serializer(self):
        return _SkillsSerializer()

    def get_all(self):
        try:
            self.validator.validate(self.token)
            response = self.handler.get_all()
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class ReadCandidateSkillsController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _SkillsBusinessHandler()

    @property
    def serializer(self):
        return _SkillsSerializer()

    def get(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.get(id)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class DeleteCandidateSkillsController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _SkillsBusinessHandler()

    @property
    def serializer(self):
        return _DeleteSerializer()

    def delete(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.delete(id)
            return self.serializer.serialize(id),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

    
class AddCandidateApplicationController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _AddApplicationValidator()

    @property
    def handler(self):
        return _ApplicationBusinessHandler()

    @property
    def serializer(self):
        return _ApplicationSerializer()

    def create(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

    
class UpdateCandidateApplicationController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ApplicationBusinessHandler()

    @property
    def serializer(self):
        return _ApplicationSerializer()

    def update(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.update(id,self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class ReadAllCandidateApplicationController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ApplicationBusinessHandler()

    @property
    def serializer(self):
        return _ApplicationSerializer()

    def get_all(self):
        try:
            self.validator.validate(self.token)
            response = self.handler.get_all()
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadCandidateApplicationController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ApplicationBusinessHandler()

    @property
    def serializer(self):
        return _ApplicationSerializer()

    def get(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.get(id)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class DeleteCandidateApplicationController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property        
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ApplicationBusinessHandler()

    @property
    def serializer(self):
        return _DeleteSerializer()

    def delete(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.delete(id)
            return self.serializer.serialize(id),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class AddCandidateExperienceController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _AddExperienceValidator()

    @property
    def handler(self):
        return _ExperienceBusinessHandler()

    @property
    def serializer(self):
        return _ExperienceSerializer()

    def create(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class UpdateCandidateExperienceController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ExperienceBusinessHandler()

    @property
    def serializer(self):
        return _ExperienceSerializer()

    def update(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.update(id,self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadAllCandidateExperienceController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ExperienceBusinessHandler()

    @property
    def serializer(self):
        return _ExperienceSerializer()

    def get_all(self):
        try:
            self.validator.validate(self.token)
            response = self.handler.get_all()
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class ReadCandidateExperienceController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ExperienceBusinessHandler()

    @property
    def serializer(self):
        return _ExperienceSerializer()

    def get(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.get(id)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class DeleteCandidateExperienceController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property        
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _ExperienceBusinessHandler()

    @property
    def serializer(self):
        return _DeleteSerializer()

    def delete(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.delete(id)
            return self.serializer.serialize(id),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class AddCandidateEducationController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _AddEducationValidator()

    @property
    def handler(self):
        return _EducationBusinessHandler()

    @property
    def serializer(self):
        return _EducationSerializer()

    def create(self):
        try:
            self.validator.validate(self.token,self.body_request)
            response = self.handler.post(self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class UpdateCandidateEducationController:
    def __init__(self, test_request=None):
        self.request = test_request or fk.request
        self.body_request = self.request.get_json()
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _EducationBusinessHandler()

    @property
    def serializer(self):
        return _EducationSerializer()

    def update(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.update(id,self.body_request)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)


class ReadAllCandidateEducationController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _EducationBusinessHandler()

    @property
    def serializer(self):
        return _EducationSerializer()

    def get_all(self):
        try:
            self.validator.validate(self.token)
            response = self.handler.get_all()
            return self.serializer.All_serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class ReadCandidateEducationController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')

    @property
    def validator(self):
        return _TokenValidator()
    
    @property
    def handler(self):
        return _EducationBusinessHandler()

    @property
    def serializer(self):
        return _EducationSerializer()

    def get(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.get(id)
            return self.serializer.serialize(response),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

class DeleteCandidateEducationController:
    def __init__(self,test_request=None):
        self.request = test_request or fk.request
        self.token = self.request.headers.get('Authorization')
        
    @property
    def validator(self):
        return _TokenValidator()

    @property
    def handler(self):
        return _EducationBusinessHandler()

    @property
    def serializer(self):
        return _DeleteSerializer()

    def delete(self,id):
        try:
            self.validator.validate(self.token)
            response = self.handler.delete(id)
            return self.serializer.serialize(id),http.HTTPStatus.OK
        except exceptions.NotFoundError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
        except (exceptions.RequiredInputError, exceptions.InvalidInputError) as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

    
# BusinessHandler
class _CandidateBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.operator = candidate_test or dh.CrudOperator(md.CandidateModel)
        self.token = token_test or tk.Token()

    def post(self, request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.create(request_body)
        return record

    def get_all(self):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        records = self.operator.get_all()
        if not records:
            raise exceptions.NotFoundError("Records does not exist")
        return records

    def get(self, _id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.get_one(_id)
        if not record:
            raise exceptions.NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.update(id,request_body)
        return record
    
    def delete(self,id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.delete(id)
        return record


class _ApplicationBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.operator = candidate_test or dh.CrudOperator(md.ApplicationModel)
        self.token = token_test or tk.Token()
        
    def post(self, request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.create(request_body)
        return record
    
    def get_all(self):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        records = self.operator.get_all()
        if not records:
            raise exceptions.NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.get_one(_id)
        if not record:
            raise exceptions.NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.update(id,request_body)
        return record
    
    def delete(self,id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.delete(id)
        return record


class _ExperienceBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.operator = candidate_test or dh.CrudOperator(md.ExperienceModel)
        self.token = token_test or tk.Token()

    def post(self, request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.create(request_body)
        return record
    
    def get_all(self):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        records = self.operator.get_all()
        if not records:
            raise exceptions.NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.get_one(_id)
        if not record:
            raise exceptions.NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.update(id,request_body)
        return record
    
    def delete(self,id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.delete(id)
        return record


class _EducationBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.operator = candidate_test or dh.CrudOperator(md.EducationModel)
        self.token = token_test or tk.Token()

    def post(self, request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.create(request_body)
        return record
    
    def get_all(self):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        records = self.operator.get_all()
        if not records:
            raise exceptions.NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.get_one(_id)
        if not record:
            raise exceptions.NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.update(id,request_body)
        return record
    
    def delete(self,id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.delete(id)
        return record

# TODO: How to implement a good transaction ?  > Mid level
# Lambda function, decorator

class _SkillsBusinessHandler:
    def __init__(self, operator_test=None,token_test=None):
        self.operator = operator_test or dh.CrudOperator(md.SkillModel)
        self.token = token_test or tk.Token()

    def post(self, request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.create(request_body)
        return record    
    
    def get_all(self):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        records = self.operator.get_all()
        if not records:
            raise exceptions.NotFoundError("Records does not exist")
        return records
    
    def get(self, _id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.get_one(_id)
        if not record:
            raise exceptions.NotFoundError("Record does not exist")
        return record
    
    def update(self,id,request_body):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.update(id,request_body)
        return record
    
    def delete(self,id):
        token = self.token.verify_token()
        self.operator.get_one(token['user_id'])
        record = self.operator.delete(id)
        return record
    

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"
# Validation
class _AddCandidateValidator:
    
    def validate(self, token,body):
        self.is_valid_token(token)
        self.is_valid_name(body.get("name"))
        self.is_valid_age(body.get("age"))
        self.is_valid_email(body.get("email"))
        self.is_valid_phone(body.get("phone"))
        
    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")

    def is_valid_name(self, name):
        if not name:
            raise exceptions.RequiredInputError("name is required")
        self._is_valid_name(name)

    def _is_valid_name(self, name):
        if not isinstance(name, str):
            raise exceptions.InvalidInputError("name is not valid string")

    def is_valid_age(self, age):
        if not age:
            raise exceptions.RequiredInputError("age is required")
        self._is_valid_age(age)

    def _is_valid_age(self, age):
        if not isinstance(age, int):
            raise exceptions.InvalidInputError("age is not valid int")

    def is_valid_email(self, email):
        if not email:
            raise exceptions.RequiredInputError("email is required")
        self._is_valid_email(email)

    def _is_valid_email(self, email):
        if not re.match(EMAIL_REGEX, email):
            raise exceptions.InvalidInputError("email is not valid")

    def is_valid_phone(self, phone):
        if not phone:
            raise exceptions.RequiredInputError("phone is required")
        self._is_valid_phone(phone)
        
    def _is_valid_phone(self, phone):
        if not isinstance(phone, str):
            raise exceptions.InvalidInputError("phone must be a string number")


class _AddApplicationValidator:
    
    def validate(self,token, body):
        self.is_valid_token(token)
        self.is_valid_date(body.get("date"))
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")
        
    def is_valid_date(self, date):
        if not date:
            raise exceptions.RequiredInputError("date is required")
        self._is_valid_date(date)
        
    def _is_valid_date(self, date):
        if not isinstance(date, str):
            raise exceptions.InvalidInputError("date is not valid string")

    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions.RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions.InvalidInputError("candidate_id is not valid int")


class _AddExperienceValidator:
    
    def validate(self,token,body):
        self.is_valid_token(token)
        self.is_valid_company(body.get("company"))
        self.is_valid_position(body.get("position"))
        self.is_valid_start_date(body.get("start_date"))
        self.is_valid_end_date(body.get("end_date"))
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")
        
    def is_valid_company(self, company):
        if not company:
            raise exceptions.RequiredInputError("company is required")
        self._is_valid_company(company)

    def _is_valid_company(self, company):
        if not isinstance(company, str):
            raise exceptions.InvalidInputError("company is not valid string")

    def is_valid_position(self, position):
        if not position:
            raise exceptions.RequiredInputError("position is required")
        self._is_valid_position(position)

    def _is_valid_position(self, position):
        if not isinstance(position, str):
            raise exceptions.InvalidInputError("position is not valid string")

    def is_valid_start_date(self, start_date):
        if not start_date:
            raise exceptions.RequiredInputError("start_date is required")
        self._is_valid_start_date(start_date)

    def _is_valid_start_date(self, start_date):
        if not isinstance(start_date, str):
            raise exceptions.InvalidInputError("start_date is not valid date string")

    def is_valid_end_date(self, end_date):
        if not end_date:
            raise exceptions.RequiredInputError("end_date is required")
        self._is_valid_end_date(end_date)
    
    def _is_valid_end_date(self, end_date):
        if not isinstance(end_date, str):
            raise exceptions.InvalidInputError("end_date is not valid date string")
        
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions.RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions.InvalidInputError("candidate_id is not valid int")

        
class _AddEducationValidator:
    
    def validate(self,token, body):
        self.is_valid_token(token)
        self.is_valid_degree(body.get("degree"))
        self.is_valid_graduation_year(body.get("graduation_year"))
        self.is_valid_institution(body.get("institution"))
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")
        
    def is_valid_degree(self, degree):
        if not degree:
            raise exceptions.RequiredInputError("degree is required")
        self._is_valid_degree(degree)

    def _is_valid_degree(self, degree):
        if not isinstance(degree, str):
            raise exceptions.InvalidInputError("degree is not valid string")

    def is_valid_graduation_year(self, graduation_year):
        if not graduation_year:
            raise exceptions.RequiredInputError("graduation_year is required")
        self._is_valid_graduation_year(graduation_year)

    def _is_valid_graduation_year(self, graduation_year):
        if not isinstance(graduation_year, (int)):
            raise exceptions.InvalidInputError("graduation_year is not valid int")

    def is_valid_institution(self, institution):
        if not institution:
            raise exceptions.RequiredInputError("institution is required")
        self._is_valid_institution(institution)

    def _is_valid_institution(self, institution):
        if not isinstance(institution, str):
            raise exceptions.InvalidInputError("institution is not valid string")
        
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions.RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions.InvalidInputError("candidate_id is not valid int")


class _AddSkillsValidator:
    
    def validate(self,token, body):
        self.is_valid_token(token)
        self.is_valid_name(body.get("name"))
        self.is_valid_candidate_id(body.get("candidate_id"))

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")
        
    def is_valid_name(self, name):
        if not name:
            raise exceptions.RequiredInputError("name is required")
        self._is_valid_name(name)

    def _is_valid_name(self, name):
        if not isinstance(name, str):
            raise exceptions.InvalidInputError("name is not valid string")
        
    def is_valid_candidate_id(self, candidate_id):
        if not candidate_id:
            raise exceptions.RequiredInputError("candidate_id is required")
        self._is_valid_candidate_id(candidate_id)

    def _is_valid_candidate_id(self, candidate_id):
        if not isinstance(candidate_id, (int)):
            raise exceptions.InvalidInputError("candidate_id is not valid int")



class _TokenValidator:

    def validate(self,token):
        self.is_valid_token(token)

    def is_valid_token(self, token):
        if not token:
            raise exceptions.RequiredInputError("token is missing")

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

        
class _DeleteSerializer:

    def serialize(self, id):
        return {
            "message":f"record id {id} has been removed successfully"
        }

# ErrorSerialize
class _ErrorSerialize:
    def core_error_serialize(self, error, status):
        return self._get_serialized_response(error, status), status

    def _get_serialized_response(self, error, status):
        return {
            "status": status.phrase,
            "description": status.description,
            "message": error.message,
        }

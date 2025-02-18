import exceptions
import http
import data_handler as dh
import flask as fk
import models as md
import datetime as dt
import tokens as tk
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from extensions import app

# Builder interface
class Info:

    def date_validator(self):
        raise exceptions._NotImplementError("children must implement this method")

    def date_handler(self):
        raise exceptions._NotImplementError("children must implement this method")

    def date_serializer(self):
        raise exceptions._NotImplementError("children must implement this method")


# Builders
class _AddCandidateSkillsBuilder(Info):
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.candidate = None
        self.skill = None

    def validator(self, validator_test=None):
        return validator_test or _AddSkillsValidator()

    def request(self, request_test=None):
        return request_test or fk.request.get_json()

    def skills_handler(self, skills_handler_test=None):
        return skills_handler_test or _SkillsBusinessHandler()

    def candidate_handler(self, candidate_handler_test=None):
        return candidate_handler_test or _CandidateBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _SkillsSerializer()

    def date_validator(self, Validator_test=None):
        return self.validator(Validator_test).validate(self.body_request)

    def date_handler(self, handler_test=None, request_test=None):
        candidate_id = self.request(request_test).get("candidate_id")
        self.candidate = self.candidate_handler(handler_test).get(candidate_id)
        self.skill = self.skills_handler(handler_test).post(
            self.body_request, candidate_id
        )
        return self.skill

    def date_serializer(self, serializer_test=None):
        return self.serializer(serializer_test).serialize(self.skill, self.candidate)


class _AddCandidateApplicationBuilder(Info):
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddApplicationValidator()

    def application_handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ApplicationSerializer()

    def date_validator(self, validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self, handler_test=None):
        self.response = self.application_handler(handler_test).post(self.body_request)

    def date_serializer(self, serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response)


class _AddCandidateExperienceBuilder(Info):
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddExperienceValidator()

    def experience_handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _ExperienceSerializer()

    def date_validator(self, validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self, handler_test=None):
        self.response = self.experience_handler(handler_test).post(self.body_request)

    def date_serializer(self, serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response)


class _AddCandidateEducationBuilder(Info):
    def __init__(self, body_request=None):
        self.body_request = body_request or fk.request.get_json()
        self.response = None

    def validator(self, validator_test=None):
        return validator_test or _AddEducationValidator()

    def education_handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

    def serializer(self, serializer_test=None):
        return serializer_test or _EducationSerializer()

    def date_validator(self, validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self, handler_test=None):
        self.response = self.education_handler(handler_test).post(self.body_request)

    def date_serializer(self, serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response)




class _AddCandidateSkillsController:
    def __init__(self):
        self.add_candidate_skills = _AddCandidateSkillsBuilder()
        
    def add(self):
        try:
            self.add_candidate_skills.date_validator()
            self.add_candidate_skills.date_handler()
            return self.add_candidate_skills.date_serializer()
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        
class _AddCandidateEducationController:
    def __init__(self):
        self.add_candidate_education = _AddCandidateEducationBuilder()
        
    def add(self):
        try:
            self.add_candidate_education.date_validator()
            self.add_candidate_education.date_handler()
            return self.add_candidate_education.date_serializer()
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,

class _AddCandidateExperienceController:
    def __init__(self):
        self.add_candidate_experience = _AddCandidateExperienceBuilder()
        
    def add(self):
        try:
            self.add_candidate_experience.date_validator()
            self.add_candidate_experience.date_handler()
            return self.add_candidate_experience.date_serializer()
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
    
class _AddCandidateApplicationController:
    def __init__(self):
        self.add_candidate_application = _AddCandidateApplicationBuilder()
        
    def add(self):
        try:
            self.add_candidate_application.date_validator()
            self.add_candidate_application.date_handler()
            return self.add_candidate_application.date_serializer()
        except exceptions._RequiredInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND,
        except exceptions._InvalidInputError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,
        except exceptions._InvalidFieldError as exc:
            return _ErrorSerialize().core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST),http.HTTPStatus.BAD_REQUEST,

# BusinessHandler / wrapper
class _ApplicationBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.ApplicationModel)
        self.token = token_test or tk.Token().verify_token()
        
    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record

class _ExperienceBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.ExperienceModel)
        self.token = token_test or tk.Token().verify_token()

    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record


class _EducationBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.EducationModel)
        self.token = token_test or tk.Token().verify_token()

    def post(self, request_body):
        self.data.get_one(self.token['user_id'])
        record = self.data.create(request_body)
        return record


class _SkillsBusinessHandler:
    def __init__(self, candidate_test=None,token_test=None):
        self.data = candidate_test or dh.CrudOperator(md.SkillModel)
        self.token = token_test or tk.Token().verify_token()

    def candidate_handler(self, candidate_handler_test=None):
        return candidate_handler_test or _CandidateBusinessHandler()
    
    def post(self, request_body, candidate_id,candidate_handler_test=None):
        self.data.get_one(self.token['user_id'])
        skill_name = request_body.get("name")
        candidate = self.candidate_handler(candidate_handler_test).get(candidate_id)
        skill = self.data.user_filter_data(name=skill_name).first()
        if not skill:
            skill = self.data.create_many(request_body)
        if skill in candidate.skills:
            raise exceptions._InvalidInputError("this candidate has this skill already")
        candidate.skills.append(skill)
        self.data.commit()
        return skill



class _CandidateBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.CandidateModel)

    def get(self, _id):
        record = self.data.get_one(_id)
        if not record:
            raise exceptions._NotFoundError("Record does not exist")
        return record


# Validation
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
class _ApplicationSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, application,status_test=None):
        return (
            {
                "Application_date": application.date,
                "candidate_name": application.candidate.name,
            },self.http_test(status_test).OK
        )


class _ExperienceSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, experience,status_test=None):
        return {
            "company": experience.company,
            "position": experience.position,
            "start_date": experience.start_date,
            "end_date": experience.end_date,
            "candidate_name": experience.candidate.name,
        }, self.http_test(status_test).OK


class _EducationSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, education,status_test=None):
        return {
            "degree": education.degree,
            "graduation_year": education.graduation_year,
            "institution": education.institution,
            "candidate_name": education.candidate.name,
        }, self.http_test(status_test).OK


class _SkillsSerializer:

    def http_test(self,status_test=None):
        return status_test or http.HTTPStatus
    
    def serialize(self, skill, candidate,status_test=None):
        return {
            "skill_id": skill.id,
            "skill_name": skill.name,
            "candidate_id": candidate.id,
            "candidate_name": candidate.name,
        }, self.http_test(status_test).OK

# ErrorSerialize
class _ErrorSerialize:
    def core_error_serialize(self, error, status):
        return {
            "status": status,
            "description": status.phrase,
            "message": error.message,
        }

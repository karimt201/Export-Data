import exceptions
import datetime
import http
import data_handler as dh
import flask as fk
import models as md
import datetime as dt

# Builder interface
class info:

    def date_validator(self):
        raise exceptions._NotImplementError("children must implement this method")

    def date_handler(self,candidate_id):
        raise exceptions._NotImplementError("children must implement this method")

    def date_serializer(self):
        raise exceptions._NotImplementError("children must implement this method")

# Builders
class _AddCandidateSkillsController(info):
    def __init__(self, body_request=None):
        self.body_request = body_request
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

    def date_validator(self,Validator_test=None):
        return self.validator(Validator_test).validate(self.body_request)

    def date_handler(self,request_test=None,handler_test=None):
        candidate_id = self.request(request_test).get('candidate_id')
        self.candidate = self.candidate_handler(handler_test).get(candidate_id)
        self.skill = self.skills_handler(handler_test).post(self.body_request,candidate_id)
        return self.skill
    
    def date_serializer(self,serializer_test=None):
        return self.serializer(serializer_test).serialize(self.skill, self.candidate)



class _AddCandidateApplicationController(info):
    def __init__(self, body_request=None):
        self.body_request = body_request
        self.response = None
        self.candidate_data = None

    
    def validator(self, validator_test=None):
        return validator_test or _AddApplicationValidator()

    
    def application_handler(self, handler_test=None):
        return handler_test or _ApplicationBusinessHandler()

    
    def candidate_handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    
    def serializer(self, serializer_test=None):
        return serializer_test or _ApplicationSerializer()

    def date_validator(self,validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self,handler_test=None):
        self.response = self.application_handler(handler_test).post(self.body_request)
        self.candidate_data = self.candidate_handler(handler_test).get(self.response.candidate_id)
        
    def date_serializer(self,serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response, self.candidate_data)
        


class _AddCandidateExperienceController(info):
    def __init__(self, body_request=None):
        self.body_request = body_request
        self.response = None
        self.candidate_data = None

    
    def validator(self, validator_test=None):
        return validator_test or _AddExperienceValidator()

    
    def experience_handler(self, handler_test=None):
        return handler_test or _ExperienceBusinessHandler()

    
    def candidate_handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    
    def serializer(self, serializer_test=None):
        return serializer_test or _ExperienceSerializer()

    def date_validator(self,validator_test):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self,handler_test=None):
        self.response = self.experience_handler(handler_test).post(self.body_request)
        self.candidate_data =  self.candidate_handler(handler_test).get(self.response.candidate_id)

    def date_serializer(self,serializer_test):
        return self.serializer(serializer_test).serialize(self.response,self.candidate_data)
        


class _AddCandidateEducationController(info):
    def __init__(self, body_request=None):
        self.body_request = body_request
        self.response = None
        self.candidate_data = None

    
    def validator(self, validator_test=None):
        return validator_test or _AddEducationValidator()

    
    def education_handler(self, handler_test=None):
        return handler_test or _EducationBusinessHandler()

    
    def candidate_handler(self, handler_test=None):
        return handler_test or _CandidateBusinessHandler()

    
    def serializer(self, serializer_test=None):
        return serializer_test or _EducationSerializer()

    def date_validator(self,validator_test=None):
        return self.validator(validator_test).validate(self.body_request)

    def date_handler(self,handler_test=None):
        self.response = self.education_handler(handler_test).post(self.body_request)
        self.candidate_data =  self.candidate_handler(handler_test).get(self.response.candidate_id)

    def date_serializer(self,serializer_test=None):
        return self.serializer(serializer_test).serialize(self.response,self.candidate_data)
        

# info query paramater
CandidatesInfo = {
    "skills": _AddCandidateSkillsController,
    "education": _AddCandidateEducationController,
    "experience": _AddCandidateExperienceController,
    "applications": _AddCandidateApplicationController,
}

# builder Director
class _Candidateinfo:
    def __init__(self, info, request_body):
        self.get_candidate_info = info
        self.candidate_info_return = None
        self.request_body = request_body

    
    def candidates_info(self, candidate_info_test=None):
        return candidate_info_test or CandidatesInfo
    
    def info(self,candidate_info_test):
        candidate_info = self.candidates_info(candidate_info_test).get(self.get_candidate_info)
        self.candidate_info_return = candidate_info(self.request_body)
        return self.candidate_info_return

    def post(self,request_test=None,info_test=None):
        info_obj = self.info(info_test)
        info_obj.date_validator()
        info_obj.date_handler()
        return info_obj.date_serializer()


# BusinessHandler / wrapper
class _ApplicationBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.ApplicationModel)

    def post(self, request_body):
        record = self.data.create(request_body)
        return record


class _ExperienceBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.ExperienceModel)

    def post(self, request_body):
        record = self.data.create(request_body)
        return record


class _EducationBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.EducationModel)

    def post(self, request_body):
        record = self.data.create(request_body)
        return record


class _SkillsBusinessHandler:
    def __init__(self, candidate_test=None):
        self.data = candidate_test or dh.CrudOperator(md.SkillModel)

    def post(self, request_body, candidate_id):
        skill_name = request_body.get("name")
        candidate = _CandidateBusinessHandler().get(candidate_id)
        skill = self.data.filter_data(skill_name)
        if not skill:
            skill = self.add_post(request_body)
        if skill in candidate.skills:
            raise exceptions._InvalidInputError("this candidate has this skill already")
        candidate.skills.append(skill)
        self.data.commit()
        return skill

    def add_post(self, request_body):
        record = self.data.create_many(request_body)
        return record

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

    def validate(self, body):
        self.is_valid_date(body.get("date"))

    def is_valid_date(self, date):
        if not date:
            raise exceptions._RequiredInputError("date is required")
        self._is_valid_date(date)

    def _is_valid_date(self, date):
        try:
            dt.datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            raise exceptions._InvalidInputError(
                f"{date} is not in valid date format (YYYY-MM-DD)"
            )


class _AddExperienceValidator:

    def validate(self, body):
        self.is_valid_company(body.get("company"))
        self.is_valid_position(body.get("position"))
        self.is_valid_start_date(body.get("start_date"))
        self.is_valid_end_date(body.get("end_date"))

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

    def is_valid_start_date(self, start_date):
        if not start_date:
            raise exceptions._RequiredInputError("start_date is required")
        self._is_valid_start_date(start_date)

    def _is_valid_start_date(self, start_date):
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            return True
        except ValueError:
            raise exceptions._InvalidInputError(
                f"{start_date} is not in valid date format (YYYY-MM-DD)"
            )

    def is_valid_end_date(self, end_date):
        if not end_date:
            raise exceptions._RequiredInputError("end_date is required")
        self._is_valid_start_date(end_date)

    def _is_valid_end_date(self, end_date):
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
            return True
        except ValueError:
            raise exceptions._InvalidInputError(
                f"{end_date} is not in valid date format (YYYY-MM-DD)"
            )


class _AddEducationValidator:

    def validate(self, body):
        self.is_valid_degree(body.get("degree"))
        self.is_valid_graduation_year(body.get("graduation_year"))
        self.is_valid_institution(body.get("institution"))

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


class _AddSkillsValidator:

    def validate(self, body):
        self.is_valid_name(body.get("name"))

    def is_valid_name(self, name):
        if not name:
            raise exceptions._RequiredInputError("name is required")
        self._is_valid_name(name)

    def _is_valid_name(self, name):
        if not isinstance(name, str):
            raise exceptions._InvalidInputError("name is not valid string")


# Serialization
class _ApplicationSerializer:

    def serialize(self, Application, candidate_name):
        return {
            "Application_date": Application.date,
            "candidate_name": candidate_name.name,
        },http.HTTPStatus.OK,


class _ExperienceSerializer:

    def serialize(self, Experience, candidate_name):
        return {
            "company": Experience.company,
            "position": Experience.position,
            "start_date": Experience.start_date,
            "end_date": Experience.end_date,
            "candidate_name": candidate_name.name,
        },http.HTTPStatus.OK


class _EducationSerializer:

    def serialize(self, education, candidate_name):
        return {
            "degree": education.degree,
            "graduation_year": education.graduation_year,
            "institution": education.institution,
            "candidate_name": candidate_name.name,
        },http.HTTPStatus.OK


class _SkillsSerializer:

    def serialize(self, skill, candidate):
        return {
            "skill_id": skill.id,
            "skill_name": skill.name,
            "candidate_id": candidate.id,
            "candidate_name": candidate.name,
        },http.HTTPStatus.OK


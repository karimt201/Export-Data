import unittest
from assertpy import assert_that
import sys
import os
# import controllers.candidate_info as candidate_info

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import controllers.candidate_info as candidate_info
import helpers.exceptions as exceptions



class TestInfoInterface(unittest.TestCase):
    def test_info_interface(self):
        info = candidate_info.info()
        with self.assertRaises(exceptions._NotImplementError) as date_Validator_exc:
            info.date_validator()
        assert_that(str(date_Validator_exc.exception)).is_equal_to(
            "children must implement this method"
        )
        with self.assertRaises(exceptions._NotImplementError) as date_handler_exc:
            info.date_handler("candidate_id")
        assert_that(str(date_handler_exc.exception)).is_equal_to(
            "children must implement this method"
        )
        with self.assertRaises(exceptions._NotImplementError) as date_Serializer_exc:
            info.date_serializer()
        assert_that(str(date_Serializer_exc.exception)).is_equal_to(
            "children must implement this method"
        )
    
class TestAddCandidateSkillsController(unittest.TestCase):
    def setUp(self):
        self.CandidateSkills = candidate_info._AddCandidateSkillsController({"name":"Read"})
        self.skills_double = CandidateSkillsDouble()

    def test_candidate_skills(self):
        # test_date_validate
        Validator = self.CandidateSkills.date_validator(self.skills_double)
        assert_that(Validator.get("name")).is_equal_to("Read")
        self.skills_double.assert_that_validate_name_hold_the_body_request({"name":"Read"})
        # test_date_handler
        date_handler = self.CandidateSkills.date_handler(self.skills_double,self.skills_double)
        assert_that(date_handler[0].get("name")).is_equal_to("Read")
        assert_that(date_handler[1]).is_equal_to("candidate_id")
        self.skills_double.assert_that_date_handler_hold_the_candidate_id("candidate_id")
        # test_date_serialize
        Serializer = self.CandidateSkills.date_serializer(self.skills_double)
        assert_that(Serializer[0][0].get("name")).is_equal_to("Read")
        assert_that(Serializer[0][1]).is_equal_to("candidate_id")
        assert_that(Serializer[1]).is_equal_to("candidate_id")
        self.skills_double.assert_that_date_serialize_hold_the_skill_and_candidate_id([{"name":"Read"},"candidate_id"])
        self.skills_double.assert_that_date_serialize_hold_the_candidate_id("candidate_id")


class CandidateSkillsDouble:
    def __init__(self):
        self.body_request=None
        self.candidate_id = None
        self.skill = None
        self.candidate = None
        
    def validate(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return self.candidate_id
    
    def post(self,body_request,candidate_id):
        self.body_request = body_request
        self.candidate_id = candidate_id
        return ([self.body_request,self.candidate_id])
    
    def serialize(self,skill,candidate):
        self.skill = skill
        self.candidate = candidate
        return ([self.skill,self.candidate])
    
    def assert_that_validate_name_hold_the_body_request(self,body_request):
        assert_that(self.body_request).is_equal_to(body_request)

    def assert_that_date_handler_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
    
    def assert_that_date_serialize_hold_the_skill_and_candidate_id(self,skill):
        assert_that(self.skill).is_equal_to(skill)
        
    def assert_that_date_serialize_hold_the_candidate_id(self, candidate):
        assert_that(self.candidate).is_equal_to(candidate)
    
class TestAddCandidateApplicationController(unittest.TestCase):
    def setUp(self):
        self.Candidate_application = candidate_info._AddCandidateApplicationController({"date":2025})
        self.application_double = CandidateApplicationDouble()

    def test_candidate_application(self):
        # test_date_validate
        validator = self.Candidate_application.date_validator(self.application_double)
        assert_that(validator.get("date")).is_equal_to(2025)
        self.application_double.assert_that_validate_name_hold_the_body_request({"date":2025})
        # date_handler
        self.Candidate_application.date_handler(self.application_double)
        # # test_date_serialize
        Serializer = self.Candidate_application.date_serializer(self.application_double)
        assert_that(Serializer.get('date')).is_equal_to(2025)
        self.application_double.assert_that_date_serialize_hold_the_skill({"date":2025})


class CandidateApplicationDouble:
    def __init__(self):
        self.body_request=None
        self.candidate_id = None
        self.skill = None
        self.candidate = None
        
    def validate(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def post(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def serialize(self,skill):
        self.skill = skill
        return self.skill
    
    def assert_that_validate_name_hold_the_body_request(self,body_request):
        assert_that(self.body_request).is_equal_to(body_request)
    
    def assert_that_date_serialize_hold_the_skill(self,skill):
        assert_that(self.skill).is_equal_to(skill)
        
    
class TestAddCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.Candidate_experience = candidate_info._AddCandidateExperienceController({"date":2025})
        self.experience_double = CandidateExperienceDouble()

    def test_candidate_application(self):
        # test_date_validate
        validator = self.Candidate_experience.date_validator(self.experience_double)
        assert_that(validator.get("date")).is_equal_to(2025)
        self.experience_double.assert_that_validate_name_hold_the_body_request({"date":2025})
        # date_handler
        self.Candidate_experience.date_handler(self.experience_double)
        # # test_date_serialize
        Serializer = self.Candidate_experience.date_serializer(self.experience_double)
        assert_that(Serializer.get('date')).is_equal_to(2025)
        self.experience_double.assert_that_date_serialize_hold_the_skill({"date":2025})


class CandidateExperienceDouble:
    def __init__(self):
        self.body_request=None
        self.skill = None
        
    def validate(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def post(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def serialize(self,skill):
        self.skill = skill
        return self.skill
    
    def assert_that_validate_name_hold_the_body_request(self,body_request):
        assert_that(self.body_request).is_equal_to(body_request)
    
    def assert_that_date_serialize_hold_the_skill(self,skill):
        assert_that(self.skill).is_equal_to(skill)
        
class TestAddCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.Candidate_education = candidate_info._AddCandidateEducationController({"date":2025})
        self.education_double = CandidateEducationDouble()
        
    def test_candidate_application(self):
        # test_date_validate
        validator = self.Candidate_education.date_validator(self.education_double)
        assert_that(validator.get("date")).is_equal_to(2025)
        self.education_double.assert_that_validate_name_hold_the_body_request({"date":2025})
        # date_handler
        self.Candidate_education.date_handler(self.education_double)
        # # test_date_serialize
        Serializer = self.Candidate_education.date_serializer(self.education_double)
        assert_that(Serializer.get('date')).is_equal_to(2025)
        self.education_double.assert_that_date_serialize_hold_the_skill({"date":2025})


class CandidateEducationDouble:
    def __init__(self):
        self.body_request=None
        self.skill = None
        
    def validate(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def post(self,body_request):
        self.body_request = body_request
        return self.body_request
    
    def serialize(self,skill):
        self.skill = skill
        return self.skill
    
    def assert_that_validate_name_hold_the_body_request(self,body_request):
        assert_that(self.body_request).is_equal_to(body_request)
    
    def assert_that_date_serialize_hold_the_skill(self,skill):
        assert_that(self.skill).is_equal_to(skill)
        
        
class TestCandidateinfo(unittest.TestCase):
    def setUp(self):
        self.candidate_info = candidate_info._Candidateinfo("skills",{"name":"Read"})
        self.info_double = infoDouble()
        self.candidate_info_double = CandidateinfoDouble({"name":"Read"})
        
    def test_candidate_info(self):
        # test_post
        info = self.candidate_info.post(self.candidate_info_double,self.info_double)
        assert_that(info).is_equal_to("success")
        self.candidate_info_double.assert_that_candidate_info_hold_the_request_body({"name":"Read"})
        self.info_double.assert_that_info_hold_the_candidate_id("skills")

class CandidateinfoDouble:
    def __init__(self,request_body=None):
        self.request_body = request_body
        
    
    def date_validator(self):
        return "validation success"
    
    def date_handler(self):
        return "success"
    
    def date_serializer(self):
        return "success"
    
        
    def assert_that_candidate_info_hold_the_request_body(self,request_body):
        assert_that(self.request_body).is_equal_to(request_body)
        
class infoDouble:
    def __init__(self):
        self.get_candidate_info = None
        
    def get(self,get_candidate_info):
        self.get_candidate_info = get_candidate_info
        return CandidateinfoDouble
    
    def assert_that_info_hold_the_candidate_id(self,get_candidate_info):
        assert_that(self.get_candidate_info).is_equal_to(get_candidate_info)

class TestApplicationBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.application_handler_double = ApplicationHandlerDouble()
        self.application_handler = candidate_info._ApplicationBusinessHandler(self.application_handler_double)
        
    def test_application_handler(self):
        # test_post
        application = self.application_handler.post({"name":"Read"})
        assert_that(application.get('name')).is_equal_to("Read")
        self.application_handler_double.assert_that_application_handler_hold_the_request_body({"name":"Read"})
        
class ApplicationHandlerDouble:
    def __init__(self):
        self.request_body = None
        
    def create(self,request_body):
        self.request_body = request_body
        return self.request_body
        
    def assert_that_application_handler_hold_the_request_body(self,request_body):
        assert_that(self.request_body).is_equal_to(request_body)
        

class TestExperienceBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.experience_handler_double = ExperienceHandlerDouble()
        self.experience_handler = candidate_info._ExperienceBusinessHandler(self.experience_handler_double)
        
    def test_experience_handler(self):
        # test_post
        experience = self.experience_handler.post({"name":"Read"})
        assert_that(experience.get('name')).is_equal_to("Read")
        self.experience_handler_double.assert_that_experience_handler_hold_the_request_body({"name":"Read"})
        
class ExperienceHandlerDouble:
    def __init__(self):
        self.request_body = None
        
    def create(self,request_body):
        self.request_body = request_body
        return self.request_body
        
    def assert_that_experience_handler_hold_the_request_body(self,request_body):
        assert_that(self.request_body).is_equal_to(request_body)
        

class TestEducationBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.education_handler_double = EducationHandlerDouble()
        self.education_handler = candidate_info._EducationBusinessHandler(self.education_handler_double)
        
    def test_education_handler(self):
        # test_post
        education = self.education_handler.post({"name":"Read"})
        assert_that(education.get('name')).is_equal_to("Read")
        self.education_handler_double.assert_that_education_handler_hold_the_request_body({"name":"Read"})
        
class EducationHandlerDouble:
    def __init__(self):
        self.request_body = None
        
    def create(self,request_body):
        self.request_body = request_body
        return self.request_body
        
    def assert_that_education_handler_hold_the_request_body(self,request_body):
        assert_that(self.request_body).is_equal_to(request_body)
        

class TestSkillsBusinessHandler(unittest.TestCase):
    def test_skills_handler(self):
        self.skills_handler_double = SkillsHandlerDouble()
        self.skills_handler = candidate_info._SkillsBusinessHandler(self.skills_handler_double)
        # test_post
        skill = self.skills_handler.post({"name":"Read"},1,self.skills_handler_double)
        assert_that(skill).is_equal_to("Read")
        self.skills_handler_double.assert_that_skills_handler_hold_the_candidate_id(1)
        self.skills_handler_double.assert_that_skills_handler_hold_the_skill_name("Read")
        
    def test_skills_handler_exceptions(self):
        self.skills_handler_double_exceptions = SkillsHandlerDoubleExceptions()
        self.skills_handler = candidate_info._SkillsBusinessHandler(self.skills_handler_double_exceptions)
        # test_post
        with self.assertRaises(exceptions._InvalidInputError) as skills_handler_exc:
            self.skills_handler.post({"name":"Read"},1,self.skills_handler_double_exceptions)
        assert_that(str(skills_handler_exc.exception)).is_equal_to(
            "this candidate has this skill already"
        )
        self.skills_handler_double_exceptions.assert_that_skills_handler_hold_the_candidate_id(1)
        self.skills_handler_double_exceptions.assert_that_skills_handler_hold_the_skill_name("Read")
        
    def test_skills_handler_and_add_skill(self):
        self.skills_handler_add_skill_double = SkillsHandlerDoubleAddSkill()
        self.skills_handler = candidate_info._SkillsBusinessHandler(self.skills_handler_add_skill_double)
        # test_post
        skill = self.skills_handler.post({"name":"Read"},1,self.skills_handler_add_skill_double)
        assert_that(skill.get('name')).is_equal_to("Read")
        self.skills_handler_add_skill_double.assert_that_skills_handler_hold_the_candidate_id(1)
        self.skills_handler_add_skill_double.assert_that_skills_handler_hold_the_skill_name("Read")
        self.skills_handler_add_skill_double.assert_that_skills_handler_hold_the_request_body({"name":"Read"})

class SkillsHandlerDouble:
    def __init__(self):
        self.skill_name = None
        self.candidate_id = None

    def filter_data(self,skill_name):
        self.skill_name = skill_name
        return self.skill_name

    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return self

    @property
    def skills(self):
        return []

    def commit(self):
        return "success"
        
    def assert_that_skills_handler_hold_the_skill_name(self,skill_name):
        assert_that(self.skill_name).is_equal_to(skill_name)
        
    def assert_that_skills_handler_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
        
class SkillsHandlerDoubleExceptions:
    def __init__(self):
        self.skill_name = None
        self.candidate_id = None


    def filter_data(self,skill_name):
        self.skill_name = skill_name
        return self.skill_name

    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return self

    def add_post(self):
        return "success"

    @property
    def skills(self):
        return ["Read"]

    def commit(self):
        return "success"

    def assert_that_skills_handler_hold_the_skill_name(self,skill_name):
        assert_that(self.skill_name).is_equal_to(skill_name)
        
    def assert_that_skills_handler_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
        
class SkillsHandlerDoubleAddSkill:
    def __init__(self):
        self.skill_name = None
        self.request_body = None
        self.candidate_id = None

    def filter_data(self,skill_name):
        self.skill_name = skill_name
        return None

    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return self

    def add_post(self):
        return "success"

    @property
    def skills(self):
        return []

    def commit(self):
        return "success"

    def create_many(self,request_body):
        self.request_body=request_body
        return self.request_body

    def assert_that_skills_handler_hold_the_skill_name(self,skill_name):
        assert_that(self.skill_name).is_equal_to(skill_name)
        
    def assert_that_skills_handler_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
        
    def assert_that_skills_handler_hold_the_request_body(self,request_body):
        assert_that(self.request_body).is_equal_to(request_body)
        
class TestCandidateBusinessHandler(unittest.TestCase):        
    def test_candidate_handler(self):
        self.candidate_handler_double = CandidateHandlerDouble()
        self.candidate_handler = candidate_info._CandidateBusinessHandler(self.candidate_handler_double)
        # test_post
        candidate = self.candidate_handler.get(1)
        assert_that(candidate).is_equal_to(1)
        self.candidate_handler_double.assert_that_candidate_handler_hold_the_candidate_id(1)
        
    def test_candidate_handler_exceptions(self):
        self.candidate_handler_double_exceptions = CandidateHandlerDoubleExceptions()
        self.candidate_handler = candidate_info._CandidateBusinessHandler(self.candidate_handler_double_exceptions)        # test_post
        with self.assertRaises(exceptions._NotFoundError) as candidate_handler_exc:
            self.candidate_handler.get(1)
        assert_that(str(candidate_handler_exc.exception)).is_equal_to(
            "Record does not exist"
        )
        self.candidate_handler_double_exceptions.assert_that_candidate_handler_hold_the_candidate_id(1)
        
class CandidateHandlerDouble:
    def __init__(self):
        self.candidate_id = None
        
    def get_one(self,candidate_id):
        self.candidate_id = candidate_id
        return self.candidate_id
        
    def assert_that_candidate_handler_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
        
class CandidateHandlerDoubleExceptions:
    def __init__(self):
        self.candidate_id = None
        
    def get_one(self,candidate_id):
        self.candidate_id = candidate_id
        return None
        
    def assert_that_candidate_handler_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
   
class TestAddApplicationValidator(unittest.TestCase):
    def setUp(self):
        self.add_application_validator = candidate_info._AddApplicationValidator()
        self.add_application_validator_double = AddApplicationValidatorDouble()
        
    def test_add_application_validator(self):
        application_validator = self.add_application_validator.validate({"date":"2010-10-10"},self.add_application_validator_double)
        with self.assertRaises(exceptions._RequiredInputError) as application_validator_exc:
            self.add_application_validator.validate({"name":"karim"},self.add_application_validator_double)
        assert_that(str(application_validator_exc.exception)).is_equal_to(
            "date is required"
        )
        assert_that(application_validator).is_equal_to("%Y-%m-%d")
        self.add_application_validator_double.assert_that_application_validator_hold_the_date("2010-10-10")
        self.add_application_validator_double.assert_that_application_validator_hold_the_date_format("%Y-%m-%d")

class AddApplicationValidatorDouble:
    def __init__(self):
        self.date = None
        self.date_format = None

    def get(self,date):
        self.date = date
        return self.date

    def strptime(self,date,date_format):
        self.date = date
        self.date_format = date_format
        return self.date_format

    def assert_that_application_validator_hold_the_date(self,date):
        assert_that(self.date).is_equal_to(date)
        
    def assert_that_application_validator_hold_the_date_format(self,date_format):
        assert_that(self.date_format).is_equal_to(date_format)
        

class TestAddExperienceValidator(unittest.TestCase):
    def setUp(self):
        self.add_experience_validator = candidate_info._AddExperienceValidator()
        self.add_experience_validator_double = AddExperienceValidatorDouble()
        
    def test_add_experience_validator(self):
        data = {
            "company":"arete",
            "position":"backend",
            "start_date":"2010-10-10",
            "end_date":"2010-10-15"
        }
        self.add_experience_validator.validate(data,self.add_experience_validator_double)
        with self.assertRaises(exceptions._RequiredInputError) as experience_company_validator_exc:
            self.add_experience_validator.validate({"name":"karim"},self.add_experience_validator_double)
        assert_that(str(experience_company_validator_exc.exception)).is_equal_to(
            "company is required"
        )
        with self.assertRaises(exceptions._RequiredInputError) as experience_position_validator_exc:
            self.add_experience_validator.validate({"company":"arete"},self.add_experience_validator_double)
        assert_that(str(experience_position_validator_exc.exception)).is_equal_to(
            "position is required"
        )
        with self.assertRaises(exceptions._RequiredInputError) as experience_start_date_validator_exc:
            self.add_experience_validator.validate({
            "company":"arete",
            "position":"backend"},self.add_experience_validator_double)
        assert_that(str(experience_start_date_validator_exc.exception)).is_equal_to(
            "start_date is required"
        )
        with self.assertRaises(exceptions._RequiredInputError) as experience_end_date_validator_exc:
            self.add_experience_validator.validate({
            "company":"arete",
            "position":"backend",
            "start_date":"2010-10-10"},self.add_experience_validator_double)
        assert_that(str(experience_end_date_validator_exc.exception)).is_equal_to(
            "end_date is required"
        )
        self.add_experience_validator_double.assert_that_experience_validator_hold_the_date("2010-10-10")
        self.add_experience_validator_double.assert_that_experience_validator_hold_the_date_format("%Y-%m-%d")

class AddExperienceValidatorDouble:
    def __init__(self):
        self.date = None
        self.date_format = None
    
    def get(self,date):
        self.date = date
        return self.date
    
    def strptime(self,date,date_format):
        self.date = date
        self.date_format = date_format
        return self.date_format
    
    def assert_that_experience_validator_hold_the_date(self,date):
        assert_that(self.date).is_equal_to(date)
        
    def assert_that_experience_validator_hold_the_date_format(self,date_format):
        assert_that(self.date_format).is_equal_to(date_format)

class TestAddEducationValidator(unittest.TestCase):
    def setUp(self):
        self.add_education_validator = candidate_info._AddEducationValidator()
        
    def test_add_education_validator(self):
        data = {
            "degree":"high school",
            "graduation_year":2023,
            "institution":"GUC"
        }
        self.add_education_validator.validate(data)
        with self.assertRaises(exceptions._RequiredInputError) as education_degree_validator_exc:
            self.add_education_validator.validate({"name":"karim"})
        assert_that(str(education_degree_validator_exc.exception)).is_equal_to(
            "degree is required"
        )
        with self.assertRaises(exceptions._RequiredInputError) as education_graduation_year_validator_exc:
            self.add_education_validator.validate({"degree":"high school"})
        assert_that(str(education_graduation_year_validator_exc.exception)).is_equal_to(
            "graduation_year is required"
        )
        with self.assertRaises(exceptions._RequiredInputError) as education_institution_validator_exc:
            self.add_education_validator.validate({
            "degree":"high school",
            "graduation_year":2023})
        assert_that(str(education_institution_validator_exc.exception)).is_equal_to(
            "institution is required"
        )
    
class TestAddSkillsValidator(unittest.TestCase):
    def setUp(self):
        self.add_skills_validator = candidate_info._AddSkillsValidator()
        
    def test_add_skills_validator(self):
        data = {
            "name":"learning",
        }
        self.add_skills_validator.validate(data)
        with self.assertRaises(exceptions._RequiredInputError) as skills_name_validator_exc:
            self.add_skills_validator.validate({})
        assert_that(str(skills_name_validator_exc.exception)).is_equal_to(
            "name is required"
        )
        
class TestApplicationSerializer(unittest.TestCase):
    def setUp(self):
        self.application_serializer = candidate_info._ApplicationSerializer()
        self.application_serializer_double = ApplicationSerializerDouble()
        self.status_double = StatusDouble()

    def test_application_serializer(self):
        application_serializer = self.application_serializer.serialize(self.application_serializer_double,self.status_double)
        assert_that(application_serializer[0].get('Application_date')).is_equal_to("2010-2-2")
        assert_that(application_serializer[1]).is_equal_to("ok")

class ApplicationSerializerDouble:
    def __init__(self):
        self.date = "2010-2-2"
        self.name = "karim"
        self.candidate = self

class TestExperienceSerializer(unittest.TestCase):
    def setUp(self):
        self.experience_serializer = candidate_info._ExperienceSerializer()
        self.experience_serializer_double = ExperienceSerializerDouble()
        self.status_double = StatusDouble()

    def test_experience_serializer(self):
        experience_serializer = self.experience_serializer.serialize(self.experience_serializer_double,self.status_double)
        assert_that(experience_serializer[0].get('company')).is_equal_to("arete")
        assert_that(experience_serializer[1]).is_equal_to("ok")

class ExperienceSerializerDouble:
    def __init__(self):
        self.company = "arete"
        self.position = "developer"
        self.start_date = "2010-2-2"
        self.end_date = "2010-2-10"
        self.name = "karim"
        self.candidate = self

class TestEducationSerializer(unittest.TestCase):
    def setUp(self):
        self.education_serializer = candidate_info._EducationSerializer()
        self.education_serializer_double = EducationSerializerDouble()
        self.status_double = StatusDouble()
        
    def test_experience_serializer(self):
        education_serializer = self.education_serializer.serialize(self.education_serializer_double,self.status_double)
        assert_that(education_serializer[0].get('institution')).is_equal_to("GUC")
        assert_that(education_serializer[1]).is_equal_to("ok")

class EducationSerializerDouble:
    def __init__(self):
        self.degree = "commerce"
        self.graduation_year = 2023
        self.institution = "GUC"
        self.name = "karim"
        self.candidate = self


class TestSkillsSerializer(unittest.TestCase):
    def setUp(self):
        self.skills_serializer = candidate_info._SkillsSerializer()
        self.skills_serializer_double = SkillsSerializerDouble()
        self.candidate_serializer_double = CandidateSerializerDouble()
        self.status_double = StatusDouble()
        
    def test_skills_serializer(self):
        skills_serializer = self.skills_serializer.serialize(self.skills_serializer_double,self.candidate_serializer_double,self.status_double)
        assert_that(skills_serializer[0].get('skill_name')).is_equal_to("Reading")
        assert_that(skills_serializer[1]).is_equal_to("ok")
        
class SkillsSerializerDouble:
    def __init__(self):
        self.id = 1
        self.name = "Reading"
        
class CandidateSerializerDouble:
    def __init__(self):
        self.id = 1
        self.name = "karim"
        
class StatusDouble:
    def __init__(self):
        self.OK = "ok"

if __name__ == "__main__":
    unittest.main()

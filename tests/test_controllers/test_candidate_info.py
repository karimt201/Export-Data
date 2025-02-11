import unittest
from assertpy import assert_that
import sys
import os
# import controllers.candidate_info as candidate_info

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from controllers import candidate_info
import exceptions



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
        date_handler = self.CandidateSkills.date_handler(1,self.skills_double)
        assert_that(date_handler[0].get("name")).is_equal_to("Read")
        assert_that(date_handler[1]).is_equal_to(1)
        self.skills_double.assert_that_date_handler_hold_the_candidate_id(1)

        # test_date_serialize
        Serializer = self.CandidateSkills.date_serializer(self.skills_double)
        assert_that(Serializer[0][0].get("name")).is_equal_to("Read")
        assert_that(Serializer[0][1]).is_equal_to(1)
        assert_that(Serializer[1]).is_equal_to(1)
        self.skills_double.assert_that_date_serialize_hold_the_skill_and_candidate_id([{"name":"Read"},1])
        self.skills_double.assert_that_date_serialize_hold_the_candidate_id(1)


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
        self.Candidate_application = candidate_info._AddCandidateApplicationController({"name":"Read"})
        self.application_double = CandidateApplicationDouble()

    def test_candidate_application(self):
        # test_date_validate
        Validator = self.Candidate_application.date_validator(self.application_double)
        assert_that(Validator.get("name")).is_equal_to("Read")
        self.application_double.assert_that_validate_name_hold_the_body_request({"name":"Read"})
        # date_handler
        self.Candidate_application.date_handler(1,self.application_double)
        # # test_date_serialize
        Serializer = self.Candidate_application.date_serializer(self.application_double)
        assert_that(Serializer[0][0].get("name")).is_equal_to("Read")
        assert_that(Serializer[0][1]).is_equal_to(1)
        assert_that(Serializer[1]).is_equal_to(1)
        self.application_double.assert_that_date_serialize_hold_the_skill_and_candidate_id([{"name":"Read"},1])
        self.application_double.assert_that_date_serialize_hold_the_candidate_id(1)


class CandidateApplicationDouble:
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
 
        
class TestAddCandidateExperienceController(unittest.TestCase):
    def setUp(self):
        self.Candidate_experience = candidate_info._AddCandidateExperienceController({"name":"Read"})
        self.experience_double = CandidateExperienceDouble()

    def test_candidate_experience(self):
        # test_date_validate
        Validator = self.Candidate_experience.date_validator(self.experience_double)
        assert_that(Validator.get("name")).is_equal_to("Read")
        self.experience_double.assert_that_validate_name_hold_the_body_request({"name":"Read"})
        # date_handler
        self.Candidate_experience.date_handler(1,self.experience_double)
        # # test_date_serialize
        Serializer = self.Candidate_experience.date_serializer(self.experience_double)
        assert_that(Serializer[0][0].get("name")).is_equal_to("Read")
        assert_that(Serializer[0][1]).is_equal_to(1)
        assert_that(Serializer[1]).is_equal_to(1)
        self.experience_double.assert_that_date_serialize_hold_the_skill_and_candidate_id([{"name":"Read"},1])
        self.experience_double.assert_that_date_serialize_hold_the_candidate_id(1)


class CandidateExperienceDouble:
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
        
class TestAddCandidateEducationController(unittest.TestCase):
    def setUp(self):
        self.Candidate_education = candidate_info._AddCandidateEducationController({"name":"Read"})
        self.education_double = CandidateEducationDouble()

    def test_candidate_education(self):
        # test_date_validate
        Validator = self.Candidate_education.date_validator(self.education_double)
        assert_that(Validator.get("name")).is_equal_to("Read")
        self.education_double.assert_that_validate_name_hold_the_body_request({"name":"Read"})
        # date_handler
        self.Candidate_education.date_handler(1,self.education_double)
        # # test_date_serialize
        Serializer = self.Candidate_education.date_serializer(self.education_double)
        assert_that(Serializer[0][0].get("name")).is_equal_to("Read")
        assert_that(Serializer[0][1]).is_equal_to(1)
        assert_that(Serializer[1]).is_equal_to(1)
        self.education_double.assert_that_date_serialize_hold_the_skill_and_candidate_id([{"name":"Read"},1])
        self.education_double.assert_that_date_serialize_hold_the_candidate_id(1)


class CandidateEducationDouble:
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

class TestCandidateinfo(unittest.TestCase):
    def setUp(self):
        self.candidate_info = candidate_info._Candidateinfo("skills",{"name":"Read"})
        self.info_double = infoDouble()
        self.candidate_info_double = CandidateinfoDouble({"name":"Read"})
        
    def test_candidate_info(self):
        # test_post
        info = self.candidate_info.post(self.candidate_info_double,self.info_double)
        assert_that(info).is_equal_to("success")
        self.candidate_info_double.assert_that_candidate_info_hold_the_candidate_id("candidate_id")
        self.candidate_info_double.assert_that_candidate_info_hold_the_request_body({"name":"Read"})
        self.info_double.assert_that_info_hold_the_candidate_id("skills")

class CandidateinfoDouble:
    def __init__(self,request_body=None):
        self.candidate_id = None
        self.request_body = request_body
        
    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return "success"
    
    def date_validator(self):
        return "validation success"
    
    def date_handler(self,candidate_id):
        self.candidate_id = candidate_id

    def date_serializer(self):
        return "success"
    
    def assert_that_candidate_info_hold_the_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
        
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
        application = self.application_handler.post({"name":"Read"},1)
        assert_that(application).is_equal_to("success")
        
class ApplicationHandlerDouble:
    def create(self,request_body):
        return "success"
        
if __name__ == "__main__":
    unittest.main()

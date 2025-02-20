import unittest
from assertpy import assert_that
import sys
import os
# import controllers.candidate_info as candidate_info

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import controllers.export_candidate as export_candidate
import data_handler as dh
import exceptions


class TestCreateExtension(unittest.TestCase):
    def test_create_extension(self):
        create_extension = export_candidate.CreateExtension()
        with self.assertRaises(exceptions._NotImplementError) as prepare_data_exc:
            create_extension.prepare_data()
        assert_that(str(prepare_data_exc.exception)).is_equal_to(
            "children must implement this method"
        )
        with self.assertRaises(exceptions._NotImplementError) as create_file_exc:
            create_extension.create_file("extension")
        assert_that(str(create_file_exc.exception)).is_equal_to(
            "children must implement this method"
        )
        with self.assertRaises(exceptions._NotImplementError) as save_file_exc:
            create_extension.save_file("filename")
        assert_that(str(save_file_exc.exception)).is_equal_to(
            "children must implement this method"
        )

class TestCreateExtensionController(unittest.TestCase):
    def setUp(self):
        self.create_extension_page_double = CreateExtensionPageDouble()
        self.create_extension_per_page_double = CreateExtensionPerPageDouble()
        self.create_extension_candidate_id_double = CreateExtensionCandidateIdDouble()
        self.create_extension_handler_double = CreateExtensionHandlerDouble()
        self.create_extension_controller = export_candidate._CreateExtensionController()
        
    def test_create_extension(self):
        self.create_extension_controller.prepare_data(
            self.create_extension_page_double,
            self.create_extension_per_page_double,
            self.create_extension_candidate_id_double,
            self.create_extension_handler_double
            )
        self.create_extension_controller.create_file(self.create_extension_page_double)
        self.create_extension_controller.save_file("filename",self.create_extension_page_double)
        self.create_extension_page_double.assert_that_create_extension_hold_the_page("page")
        self.create_extension_page_double.assert_that_create_extension_hold_the_type(int)
        self.create_extension_page_double.assert_that_create_extension_hold_the_serializer_name("karim")
        self.create_extension_page_double.assert_that_create_extension_hold_the_serializer_date("2024-2-10")
        self.create_extension_page_double.assert_that_create_extension_hold_the_row_data_position("fullstack")
        self.create_extension_page_double.assert_that_create_extension_hold_the_filename("filename")
        self.create_extension_per_page_double.assert_that_create_extension_hold_the_per_page("per_page")
        self.create_extension_per_page_double.assert_that_create_extension_hold_the_num_of_item_in_page(3)
        self.create_extension_per_page_double.assert_that_create_extension_hold_the_type(int)
        self.create_extension_candidate_id_double.assert_that_create_extension_hold_candidate_id("candidate_id")
        self.create_extension_handler_double.assert_that_create_extension_hold_candidate_id("candidate_id")
        
    
    def test_create_extension_candidate_id_equal_none(self):
        create_extension_candidate_id_none_double = CreateExtensionCandidateIdNoneDouble()

        self.create_extension_controller.prepare_data(
            self.create_extension_page_double,
            self.create_extension_per_page_double,
            create_extension_candidate_id_none_double,
            self.create_extension_handler_double
            )
        self.create_extension_controller.create_file(self.create_extension_page_double)
        self.create_extension_controller.save_file("filename",self.create_extension_page_double)
        self.create_extension_handler_double.assert_that_create_extension_hold_the_page("page")
        self.create_extension_handler_double.assert_that_create_extension_hold_the_per_page("per_page")
        create_extension_candidate_id_none_double.assert_that_create_extension_hold_candidate_id("candidate_id")
    
    def test_create_extension_page_equal_none(self):
        create_extension_page_none_double = CreateExtensionPageNoneDouble()

        self.create_extension_controller.prepare_data(
            create_extension_page_none_double,
            self.create_extension_per_page_double,
            self.create_extension_candidate_id_double,
            self.create_extension_handler_double
            )
        self.create_extension_controller.create_file(self.create_extension_page_double)
        self.create_extension_controller.save_file("filename",self.create_extension_page_double)
        create_extension_page_none_double.assert_that_create_extension_hold_the_page("page")
        create_extension_page_none_double.assert_that_create_extension_hold_the_type(int)
        create_extension_page_none_double.assert_that_create_extension_hold_the_serializer_date("2024-2-10")
        create_extension_page_none_double.assert_that_create_extension_hold_the_serializer_name("karim")
    

class CreateExtensionPageDouble:
    def __init__(self):
        self.page = None
        self.type = None
        self.serializer = None
        self.extension_file = None
        self.row_data = None
        self.filename = None
        
    def get(self,page,type):
        self.page = page
        self.type = type
        return self.page
    
    def RowExcelData(self,serializer):
        self.serializer = serializer
        return self.serializer
    
    def DataManger(self,extension_file):
        self.extension_file = extension_file
        return self
    
    def save(self,row_data,filename):
        self.row_data = row_data
        self.filename = filename
        return "success"
    
    def assert_that_create_extension_hold_the_page(self,page):
        assert_that(self.page).is_equal_to(page)
    
    def assert_that_create_extension_hold_the_type(self,type):
        assert_that(self.type).is_equal_to(type)
    
    def assert_that_create_extension_hold_the_serializer_name(self,serializer_name):
        assert_that(self.serializer[0].get('name')).is_equal_to(serializer_name)
        
    def assert_that_create_extension_hold_the_serializer_date(self,serializer_date):
        assert_that(self.serializer[0].get('date')).is_equal_to(serializer_date)
    
    def assert_that_create_extension_hold_the_row_data_position(self,row_data):
        assert_that(self.row_data[0].get('position')).is_equal_to(row_data)
    
    def assert_that_create_extension_hold_the_filename(self,filename):
        assert_that(self.filename).is_equal_to(filename)
    
    
class CreateExtensionPageNoneDouble:
    def __init__(self):
        self.page = None
        self.type = None
        self.serializer = None
        self.extension_file = None
        self.row_data = None
        self.filename = None
        
    def get(self,page,type):
        self.page = page
        self.type = type
        return None
    
    def RowExcelData(self,serializer):
        self.serializer = serializer
        return self.serializer
    
    def DataManger(self,extension_file):
        self.extension_file = extension_file
        return self
    
    def save(self,row_data,filename):
        self.row_data = row_data
        self.filename = filename
        return self.filename
    
    def assert_that_create_extension_hold_the_page(self,page):
        assert_that(self.page).is_equal_to(page)
    
    def assert_that_create_extension_hold_the_type(self,type):
        assert_that(self.type).is_equal_to(type)
    
    def assert_that_create_extension_hold_the_serializer_name(self,serializer_name):
        assert_that(self.serializer[0].get('name')).is_equal_to(serializer_name)
        
    def assert_that_create_extension_hold_the_serializer_date(self,serializer_date):
        assert_that(self.serializer[0].get('date')).is_equal_to(serializer_date)
    
class CreateExtensionPerPageDouble:
    def __init__(self):
        self.per_page = None
        self.num_of_item_in_page = None
        self.type = None
    
    def get(self,per_page,num_of_item_in_page,type):
        self.per_page = per_page
        self.num_of_item_in_page = num_of_item_in_page
        self.type = type
        return self.per_page
    
    def assert_that_create_extension_hold_the_per_page(self,per_page):
        assert_that(self.per_page).is_equal_to(per_page)
        
    def assert_that_create_extension_hold_the_num_of_item_in_page(self,num_of_item_in_page):
        assert_that(self.num_of_item_in_page).is_equal_to(num_of_item_in_page)
    
    def assert_that_create_extension_hold_the_type(self,type):
        assert_that(self.type).is_equal_to(type)
    
class CreateExtensionCandidateIdDouble:
    def __init__(self):
        self.candidate_id = None

    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return self.candidate_id
    
    def assert_that_create_extension_hold_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
    
class CreateExtensionCandidateIdNoneDouble:
    def __init__(self):
        self.candidate_id = None
    
    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return None
    
    def assert_that_create_extension_hold_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
    
class CreateExtensionHandlerDouble:
    def __init__(self):
        self.candidate_id = None
        self.page = None
        self.per_page = None
        self.name = "karim"
        self.age = 25
        self.email = "karim@gmail.com"
        self.phone = "01016767542"
        self.skills = [self]
        self.education = [self]
        self.experience = [self]
        self.applications = [self]
        self.degree = "high school"
        self.graduation_year = 2025
        self.institution = "cairo unverisity"
        self.company = "arete"
        self.position = "fullstack"
        self.start_date = "2025-2-1"
        self.end_date = "2025-2-10"
        self.date = "2024-2-10"
        
    def get(self,candidate_id):
        self.candidate_id = candidate_id
        return self
    
    def get_paginated(self,page, per_page):
        self.page = page
        self.per_page = per_page
        return self
    
    def get_all(self):
        return self
    
    def assert_that_create_extension_hold_candidate_id(self,candidate_id):
        assert_that(self.candidate_id).is_equal_to(candidate_id)
        
    def assert_that_create_extension_hold_the_page(self,page):
        assert_that(self.page).is_equal_to(page)
        
    def assert_that_create_extension_hold_the_per_page(self,per_page):
        assert_that(self.per_page).is_equal_to(per_page)


class TestCandidateController(unittest.TestCase):
    def setUp(self):
        self.candidate_request_body_double = CandidateRequestBodyDouble()
        self.candidate_operation_double = CandidateOperationDouble()
        self.candidate_info_double = CandidateInfoDouble()
        self.add_candidate_double = AddCandidateDouble()
        self.candidate_controller = export_candidate._CandidateController(self.candidate_request_body_double)
        
    def test_candidate_controller(self):
        self.candidate_controller.create(
            self.candidate_operation_double,
            self.candidate_info_double,
            self.add_candidate_double
            )
        
class CandidateOperationDouble:
    def __init__(self):
        self.id = 1
        self.name = "karim"
        self.age = 25
        self.email = "karim@gmail.com"
        self.phone = "01016767542"
        self.skills = [self]
        self.education = [self]
        self.experience = [self]
        self.applications = [self]
        self.degree = "high school"
        self.graduation_year = 2025
        self.institution = "cairo unverisity"
        self.company = "arete"
        self.position = "fullstack"
        self.start_date = "2025-2-1"
        self.end_date = "2025-2-10"
        self.date = "2024-2-10"
        
    def get(self,operation):
        return None
    
    def export(self,file_name):
        return self
    
class CandidateInfoDouble:
    def get(self,info):
        return None
    
    def post(self):
        return 1

class CandidateRequestBodyDouble:
    def get(self,fileName):
        self.fileName=fileName
        return self.fileName

class AddCandidateDouble:
    def post(self,request_body):
        self.request_body=request_body
        return self.request_body

class TestCrudOperator(unittest.TestCase):
    def setUp(self):
        self.crud_operator_model_post_double = CrudOperatorPostModelDouble
        self.crud_operator_model_double = CrudOperatorModelDouble()
    
    def test_get_operator(self):
        crud_operator_session_double = CrudOperatorSessionDouble()

        crud_operator = dh.CrudOperator(self.crud_operator_model_double,crud_operator_session_double)
        crud_operator.get_all()
        crud_operator.get_one(1)
        crud_operator.get_paginated(1,3)
        crud_operator_session_double.assert_that_crud_operator_session_get_by_id(1)

        with self.assertRaises(exceptions._InvalidFieldError) as crud_operator_exc:
            crud_operator.create({"name":"karim"})
        assert_that(str(crud_operator_exc.exception)).is_equal_to(
            f"name field is not valid"
        )
        crud_operator.commit()
        crud_operator.filter_data("karim")
        self.crud_operator_model_double.assert_that_crud_operator_model_get_by_page_number(1)
        self.crud_operator_model_double.assert_that_crud_operator_model_get_per_page(3)
        self.crud_operator_model_double.assert_that_crud_operator_model_paginate_error_out(False)
        self.crud_operator_model_double.assert_that_crud_operator_model_filter_by_name("name")
        
    def test_get_operator(self):
        crud_operator_session_double = CrudOperatorSessionDouble()

        crud_operator = dh.CrudOperator(self.crud_operator_model_post_double,crud_operator_session_double)
        crud_operator.create({"id":1,"phone":"01016767542"})
        crud_operator.create_many({"id":1,"phone":"01016767542"})

        crud_operator_session_double.assert_that_crud_operator_session_add_new_record_by_phone("01016767542")
        
        
class CrudOperatorPostModelDouble:
    id = 1
    phone = "01016767542"
    
    def __init__(self,**filtered_data):
        self.filtered_data = filtered_data

class CrudOperatorModelDouble:
    
    def __init__(self):
        self.query = self
        self.page = None
        self.per_page = None
        self.error_out = None
        self.name = None
        
    def all(self):
        return "success"
    
    def paginate(self,page,per_page,error_out):
        self.page = page
        self.per_page = per_page
        self.error_out = error_out
        return self.page
    
    def filter_by(self,name):
        self.name = name
        return self
    
    def first(self):
        return "success"

    def assert_that_crud_operator_model_get_by_page_number(self,page):
        assert_that(self.page).is_equal_to(page)
        
    def assert_that_crud_operator_model_get_per_page(self,per_page):
        assert_that(self.per_page).is_equal_to(per_page)
        
    def assert_that_crud_operator_model_paginate_error_out(self,error_out):
        assert_that(self.error_out).is_equal_to(error_out)
        
    def assert_that_crud_operator_model_filter_by_name(self,name):
        assert_that(self.name).is_equal_to(name)
        
        
class CrudOperatorSessionDouble:
    def __init__(self):
        self.model = None
        self.id = None
        self.record = None
        
    def get(self,model,id):
        self.model = model
        self.id = id
        return self.id
    
    def commit(self):
        pass
    
    def add(self,record):
        self.record = record
        return self.record
    
    def assert_that_crud_operator_session_get_by_id(self,id):
        assert_that(self.id).is_equal_to(id)
        
    def assert_that_crud_operator_session_add_new_record_by_phone(self,record):
        assert_that(self.record.phone).is_equal_to(record)

class TestExtensionCreator(unittest.TestCase):
    def setUp(self):
        self.extension_creator_double = ExtensionCreatorDouble()
        self.extension_creator = export_candidate._ExtensionCreator("csv",self.extension_creator_double)
    def test_extension_creator(self):
        self.extension_creator.export("filename.csv",self.extension_creator_double)
        self.extension_creator_double.assert_that_extension_creator_hold_extension("csv")
        self.extension_creator_double.assert_that_extension_creator_hold_extension("csv")
        self.extension_creator_double.assert_that_extension_creator_hold_filename("filename.csv")
        self.extension_creator_double.assert_that_extension_creator_hold_operation("csv")

class ExtensionCreatorDouble:
    def __init__(self):
        self.extension = None
        self.filename = None
        
    def prepare_data(self):
        return "success"
    
    def create_file(self,extension):
        self.extension = extension
        return self.extension
    
    def save_file(self,filename):
        self.filename = filename
        return self.filename
    
    def get(self,operation):
        self.operation = operation
        return self.operation
    
    def assert_that_extension_creator_hold_extension(self,extension):
        assert_that(self.extension).is_equal_to(extension)

    def assert_that_extension_creator_hold_filename(self,filename):
        assert_that(self.filename).is_equal_to(filename)
        
    def assert_that_extension_creator_hold_operation(self,operation):
        assert_that(self.operation).is_equal_to(operation)
    

class TestCandidateBusinessHandler(unittest.TestCase):
    def setUp(self):
        self.candidate_business_handler_double = CandidateBusinessHandlerDouble()
        self.candidate_business_handler = export_candidate._CandidateBusinessHandler(self.candidate_business_handler_double)
    
    def test_candidate_business_handler(self):
        self.candidate_business_handler.post({"name":"karim"})
        self.candidate_business_handler.get_all()
        self.candidate_business_handler.get(1)
        self.candidate_business_handler.get_paginated(1,3)
        self.candidate_business_handler_double.assert_that_candidate_business_handler_hold_request_body({"name":"karim"})
        self.candidate_business_handler_double.assert_that_candidate_business_handler_hold_candidate_id(1)
        self.candidate_business_handler_double.assert_that_candidate_business_handler_hold_page(1)
        self.candidate_business_handler_double.assert_that_candidate_business_handler_hold_per_page(3)

class CandidateBusinessHandlerDouble:
    def __init__(self):
        self.request_body = None
        self.id = None
        self.page = None
        self.per_page = None
        
    def create(self,request_body):
        self.request_body = request_body
        return "success"
    
    def get_all(self):
        return "success"
    
    def get_one(self,id):
        self.id = id
        return "success"
    
    def get_paginated(self,page,per_page):
        self.page = page
        self.per_page = per_page
        return {"page":self.page , "per_page":self.per_page}
    
    def assert_that_candidate_business_handler_hold_request_body(self,request_body):
        assert_that(self.request_body).is_equal_to(request_body)
        
    def assert_that_candidate_business_handler_hold_candidate_id(self,id):
        assert_that(self.id).is_equal_to(id)

    def assert_that_candidate_business_handler_hold_page(self,page):
        assert_that(self.page).is_equal_to(page)
        
    def assert_that_candidate_business_handler_hold_per_page(self,per_page):
        assert_that(self.per_page).is_equal_to(per_page)

class TestCreateExtensionValidator(unittest.TestCase):
    def setUp(self):
        self.create_extension_validator = export_candidate._CreateExtensionValidator()
        
    def test_add_skills_validator(self):
        data = {
            "filename":"learn.csv",
        }
        self.create_extension_validator.validate(data)
        with self.assertRaises(exceptions._RequiredInputError) as create_extension_filename_validator_exc:
            self.create_extension_validator.validate({})
        assert_that(str(create_extension_filename_validator_exc.exception)).is_equal_to(
            "filename is required"
        )
        with self.assertRaises(exceptions._InvalidInputError) as create_extension_filename_validator_exc:
            self.create_extension_validator.validate({"filename":1})
        assert_that(str(create_extension_filename_validator_exc.exception)).is_equal_to(
            "filename is not valid string"
        )
        
class TestAddCandidateValidator(unittest.TestCase):
    def setUp(self):
        self.add_candidate_validator = export_candidate._AddCandidateValidator()
        
    def test_add_candidate_validator(self):
        data = {
            "name":"karim",
            "age":26,
            "email":"karim@gmail.com",
            "phone":"01016767542",
        }
        self.add_candidate_validator.validate(data)
        with self.assertRaises(exceptions._RequiredInputError) as add_candidate_name_validator_exc:
            self.add_candidate_validator.validate({})
        assert_that(str(add_candidate_name_validator_exc.exception)).is_equal_to(
            "name is required"
        )
        with self.assertRaises(exceptions._InvalidInputError) as add_candidate_name_validator_exc:
            self.add_candidate_validator.validate({"name":1})
        assert_that(str(add_candidate_name_validator_exc.exception)).is_equal_to(
            "name is not valid string"
        )
        with self.assertRaises(exceptions._RequiredInputError) as add_candidate_age_validator_exc:
            self.add_candidate_validator.validate({"name":"karim"})
        assert_that(str(add_candidate_age_validator_exc.exception)).is_equal_to(
            "age is required"
        )
        with self.assertRaises(exceptions._InvalidInputError) as add_candidate_name_validator_exc:
            self.add_candidate_validator.validate({"name":"karim","age":"1"})
        assert_that(str(add_candidate_name_validator_exc.exception)).is_equal_to(
            "age is not valid int"
        )
        with self.assertRaises(exceptions._RequiredInputError) as add_candidate_email_validator_exc:
            self.add_candidate_validator.validate({"name":"karim","age":26})
        assert_that(str(add_candidate_email_validator_exc.exception)).is_equal_to(
            "Email is required"
        )
        with self.assertRaises(exceptions._InvalidInputError) as add_candidate_email_validator_exc:
            self.add_candidate_validator.validate({"name":"karim","age":26,"email":"karim"})
        assert_that(str(add_candidate_email_validator_exc.exception)).is_equal_to(
            "Email is not valid"
        )
        with self.assertRaises(exceptions._RequiredInputError) as add_candidate_phone_validator_exc:
            self.add_candidate_validator.validate({"name":"karim","age":26,"email":"karim@gmail.com"})
        assert_that(str(add_candidate_phone_validator_exc.exception)).is_equal_to(
            "phone is required"
        )
        with self.assertRaises(exceptions._InvalidInputError) as add_candidate_phone_validator_exc:
            self.add_candidate_validator.validate({"name":"karim","age":26,"email":"karim@gmail.com","phone":1})
        assert_that(str(add_candidate_phone_validator_exc.exception)).is_equal_to(
            "phone must be a number"
        )

class TestErrorSerialize(unittest.TestCase):
    def setUp(self):
        self.error_serialize = export_candidate._ErrorSerialize()
        
    def test_error_serialize(self):
        self.error_serialize_status_double = ErrorSerializeStatusDouble()
        self.error_serialize_error_double = ErrorSerializeErrorDouble()
        self.error_serialize.core_error_serialize(self.error_serialize_error_double,self.error_serialize_status_double)
    
class ErrorSerializeStatusDouble:
    def __init__(self):
        self.status = self
        self.phrase = "phrase"
        
class ErrorSerializeErrorDouble:
    def __init__(self):
        self.error = self
        self.message = "message"
        

if __name__ == "__main__":
    unittest.main()

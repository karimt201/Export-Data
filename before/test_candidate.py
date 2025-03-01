# import unittest
# from assertpy import assert_that
# import reportlab.lib.pagesizes as pagesizes
# import openpyxl as xl
# import reportlab.lib as lib
# import controllers.writer as writer
# import controllers.candidate as candidate
# # import controllers.writer as excel
# # import Serializer as sr
# # import validator as vd
# import exceptions as ex
# import data_handler as dh
# import data_handler as dh
# import app as app
# import exceptions



# class TestCrudOperator(unittest.TestCase):

#     def test_crud_operator(self):
#         model_double = ModelDouble()
#         session_double = SessionDouble()
#         crud_operator = dh.CrudOperator(model_double, session_double)
#         crud_operator_obj = dh.CrudOperator(ModelDouble, session_double)
#         data = [{"name": "karim"}, {"name": "omar"}]
#         assert_that(crud_operator.get_all()).is_equal_to("all success")
#         assert_that(crud_operator.get_one(1)).is_equal_to("one success")
#         assert_that(crud_operator_obj.post_list(data)).is_equal_to(
#             [{"name": "karim"}, {"name": "omar"}]
#         )
#         assert_that(crud_operator_obj.post_list(data[0])).is_equal_to({"name": "karim"})


# class ModelDouble:

#     def __init__(self, data=None):
#         self.data = data

#     @property
#     def query(self):
#         return self

#     def all(self):
#         return "all success"

#     def get(self, id):
#         return "one success"


# class SessionDouble:

#     def get(self, model, id):
#         return "one success"

#     def add(self, new_candidate):
#         pass

#     def commit(self):
#         pass


# class TestDatabaseHandler(unittest.TestCase):
#     def test_data_handler(self):

#         data_handler_double = DatabaseHandlerDouble()
#         with self.assertRaises(ex._NotFoundError) as get_all_exc:
#             dh.database_handle(data_handler_double).get_all()
#         assert_that(str(get_all_exc.exception)).is_equal_to("Records does not exist")
#         with self.assertRaises(ex._NotFoundError) as paginated_exc:
#             dh.database_handle(data_handler_double).get_paginated_for_test()
#         assert_that(str(paginated_exc.exception)).is_equal_to("No Records in this Page")
#         with self.assertRaises(ex._NotFoundError) as get_exc:
#             dh.database_handle(data_handler_double).get(100)
#         assert_that(str(get_exc.exception)).is_equal_to("Record does not exist")
#         with self.assertRaises(ex._InvalidInputError) as post_all_data_types_exc:
#             dh.database_handle(data_handler_double).post_all_data_types(())
#         assert_that(str(post_all_data_types_exc.exception)).is_equal_to(
#             "invalid input, only accept dict data or list of dicts"
#         )


# class DatabaseHandlerDouble:
#     def get_all(self):
#         pass

#     def get_paginated(self, page, per_page):
#         return self

#     @property
#     def items(self):
#         pass

#     def get_one(self, id):
#         pass

#     def post_list(self, request_body):
#         pass

#     def post_one(self, request_body):
#         pass


# class TestValidator(unittest.TestCase):
#     def test_validator(self):
#         required_input_error_double = RequiredInputError({"name": "ahmed"})
#         invalid_input_error_double = InvalidInputError({"name": 4})
#         with self.assertRaises(ex._RequiredInputError) as exc:
#             vd._DataValidator(required_input_error_double)._All_validate()
#         with self.assertRaises(ex._InvalidInputError) as ec:
#             vd._DataValidator(invalid_input_error_double)._All_validate()
#         assert_that(str(exc.exception)).is_equal_to("Name is required")
#         assert_that(str(ec.exception)).is_equal_to("Name is not valid string")


# class RequiredInputError:
#     def __init__(self, user_request):
#         self.user_request = user_request

#     def get(self, item):
#         pass


# class InvalidInputError:
#     def __init__(self, user_request):
#         self.user_request = user_request

#     def get(self, item):
#         return self.user_request[item]


# class TestSerializer(unittest.TestCase):

#     def test_serializer(self):
#         user = {
#             "id": 1,
#             "name": "ahmed",
#             "email": "ahmed@gmail.com",
#             "compatibility": 22,
#             "sourcing": "internal-hiring",
#             "status": "Rejected",
#         }

#         serializer_double = SerializerDouble(user)
#         serializer_test = sr._DataSerializer(
#             serializer_double, "success"
#         )._All_serialize()
#         assert_that(serializer_test["id"]).is_equal_to(1)
#         assert_that(serializer_test["name"]).is_equal_to("ahmed")
#         assert_that(serializer_test["email"]).is_equal_to("ahmed@gmail.com")
#         assert_that(serializer_test["compatibility"]).is_equal_to(22)
#         assert_that(serializer_test["sourcing"]).is_equal_to("internal-hiring")
#         assert_that(serializer_test["status"]).is_equal_to("Rejected")
#         assert_that(serializer_test["filename"]).is_equal_to("success")
#         serializer_double.assert_that_id_called_with(1)
#         serializer_double.assert_that_name_called_with("ahmed")
#         serializer_double.assert_that_email_called_with("ahmed@gmail.com")
#         serializer_double.assert_that_compatibility_called_with(22)
#         serializer_double.assert_that_sourcing_called_with("internal-hiring")
#         serializer_double.assert_that_status_called_with("Rejected")


# class SerializerDouble:
#     def __init__(self, user):
#         self.given_user = user
#         self.id = self.given_user["id"]
#         self.name = self.given_user["name"]
#         self.email = self.given_user["email"]
#         self.compatibility = self.given_user["compatibility"]
#         self.sourcing = self.given_user["sourcing"]
#         self.status = self.given_user["status"]

#     def name(self, name):
#         self.given_user["name"] = name

#     def email(self, email):
#         self.given_user["email"] = email

#     def compatibility(self, compatibility):
#         self.given_user["compatibility"] = compatibility

#     def sourcing(self, sourcing):
#         self.given_user["sourcing"] = sourcing

#     def status(self, status):
#         self.given_user["status"] = status

#     def assert_that_id_called_with(self, id):
#         assert_that(self.given_user["id"]).is_equal_to(id)

#     def assert_that_name_called_with(self, name):
#         assert_that(self.given_user["name"]).is_equal_to(name)

#     def assert_that_email_called_with(self, email):
#         assert_that(self.given_user["email"]).is_equal_to(email)

#     def assert_that_compatibility_called_with(self, compatibility):
#         assert_that(self.given_user["compatibility"]).is_equal_to(compatibility)

#     def assert_that_sourcing_called_with(self, sourcing):
#         assert_that(self.given_user["sourcing"]).is_equal_to(sourcing)

#     def assert_that_status_called_with(self, status):
#         assert_that(self.given_user["status"]).is_equal_to(status)



# class TestCreateExtension(unittest.TestCase):
#     def __init__(self):
#         self.error_create_extension = candidate.CreateExtension()
        
#     def test_prepare_data_raise_exception(self):
#         with self.assertRaises(exceptions._NotImplementError) as prepare_data_exc:
#             self.error_create_extension.prepare_data()
#         assert_that(str(prepare_data_exc.exception)).is_equal_to(
#             "children must implement this method"
#         )
#     def test_create_file_raise_exception(self):
#         with self.assertRaises(exceptions._NotImplementError) as create_file_exc:
#             self.error_create_extension.create_file("extension")
#         assert_that(str(create_file_exc.exception)).is_equal_to(
#             "children must implement this method"
#         )
#     def test_save_file_raise_exception(self):
#         with self.assertRaises(exceptions._NotImplementError) as save_file_exc:
#             self.error_create_extension.save_file("filename")
#         assert_that(str(save_file_exc.exception)).is_equal_to(
#             "children must implement this method"
#         )


# if __name__ == "__main__":
#     unittest.main()

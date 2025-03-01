# from flask import request
# # import validator as vd
# import Serializer as sr
# import exceptions
# import http
# import data_handler as dh
# import models as md
# import re





# class CandidateController:

#     def __init__(self, candidate_test=None):
#         self._request_data = candidate_test or request.get_json()

#     @property
#     def handler(self):
#         return _BusinessHandler()

#     def candidate_creator(self):
#         try:
#             _AddCandidateValidator(self._request_data)._All_validate()
#             new_candidates = self.handler.post(self._request_data)
#             return _Serializer(new_candidates)._request_serialize(),http.HTTPStatus.CREATED,
#         except exceptions._RequiredInputError as exc:
#             return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.NOT_FOUND)
#         except exceptions._InvalidInputError as exc:
#             return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)
#         except exceptions._InvalidFieldError as exc:
#             return _ErrorSerialize()._core_error_serialize(exc, http.HTTPStatus.BAD_REQUEST)

    # TODO: Add controller for each of the methods below
    # def get_all_candidates(self):
    #     try:
    #         candidates = dh.database_handle().get_all()
    #         return sr._DataSerializer(candidates)._All_serialize(), http.HTTPStatus.OK
    #     except exceptions._NotFoundError as exc:
    #         return (
    #             sr._DataSerializer()._core_error_serialize(
    #                 exc, http.HTTPStatus.NOT_FOUND
    #             ),
    #             http.HTTPStatus.NOT_FOUND,
    #         )

    # def get_all_candidates_paginated(self):
    #     try:
    #         pagination = dh.database_handle().get_paginated(page=1, per_page=5)
    #         return sr._DataSerializer(pagination)._All_serialize(), http.HTTPStatus.OK
    #     except exceptions._NotFoundError as exc:
    #         return sr._DataSerializer()._core_error_serialize(
    #             exc, http.HTTPStatus.NOT_FOUND
    #         )

    # def get_candidate(self, candidate_id):
    #     try:
    #         candidate = dh.database_handle().get(candidate_id)
    #         return sr._DataSerializer(candidate)._All_serialize(), http.HTTPStatus.OK
    #     except exceptions._NotFoundError as exc:
    #         return sr._DataSerializer()._core_error_serialize(
    #             exc, http.HTTPStatus.NOT_FOUND
    #         )



# class _BusinessHandler:
#     def __init__(self, candidate_test=None):
#         self.operator = candidate_test or dh.CrudOperator(md.CandidateModel)

#     def post(self, request_data):
#         if request_data.get("age") < 30:
#             raise exceptions._InvalidInputError("Age must be greater than 30")
#         record = self.operator.create(request_data)
#         return record



# class _AddCandidateValidator:
#     def __init__(self, json_body=None):
#         self.json_body = json_body

#     def _All_validate(self):
#         if isinstance(self.json_body, list):
#             for body in self.json_body:
#                 self.validate(body)
#         else:
#             self.validate(self.json_body)

#     def validate(self, body):
#         self.is_valid_name(body.get("name"))
#         self.is_valid_age(body.get("age"))
#         self.is_valid_email(body.get("email"))
#         self.is_valid_compatibility(body.get("compatibility"))
#         self.is_valid_sourcing(body.get("sourcing"))
#         self.is_valid_status(body.get("status"))

#     def is_valid_name(self, name):
#         if not name:
#             raise exceptions._RequiredInputError("Name is required")
#         self._is_valid_name(name)

#     def _is_valid_name(self, name):
#         if not isinstance(name, str):
#             raise exceptions._InvalidInputError("Name is not valid string")
        
#     def is_valid_age(self, age):
#         if not age:
#             raise exceptions._RequiredInputError("Age is required")
#         self._is_valid_age(age)

#     def _is_valid_age(self, age):
#         if not isinstance(age, int):
#             raise exceptions._InvalidInputError("Age is not valid int")

#     def is_valid_email(self, email):
#         if not email:
#             raise exceptions._RequiredInputError("Email is required")
#         self._is_valid_email(email)

#     def _is_valid_email(self, email):
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise exceptions._InvalidInputError("Email is not valid")

#     def is_valid_compatibility(self, compatibility):
#         if compatibility is not None:
#             if not compatibility:
#                 raise exceptions._RequiredInputError("Compatibility is required")
#             self._is_valid_compatibility(compatibility)
#         else:
#             return compatibility

#     def _is_valid_compatibility(self, compatibility):
#         if not isinstance(compatibility, (int)):
#             raise exceptions._InvalidInputError("Compatibility must be a number")

#     def is_valid_sourcing(self, sourcing):
#         if not sourcing:
#             raise exceptions._RequiredInputError("Sourcing is required")
#         self._is_valid_sourcing(sourcing)

#     def _is_valid_sourcing(self, sourcing):
#         if not isinstance(sourcing, str):
#             raise exceptions._InvalidInputError("Sourcing is not valid string")

#     def is_valid_status(self, status):
#         if not status:
#             raise exceptions._RequiredInputError("Status is required")
#         self._is_valid_status(status)

#     def _is_valid_status(self, status):
#         if not isinstance(status, str):
#             raise exceptions._InvalidInputError("Status is not valid string")



# class _Serializer:
#     def __init__(self, user=None, filename=None):
#         self.user = user
#         self.filename = filename

#     def _data_serialize(self):
#         if isinstance(self.user, list):
#             return [self.serialize(user) for user in self.user]
#         return self.serialize(self.user)

#     def _All_serialize(self):
#         if isinstance(self.user, list):
#             return [self.all_serialize(user) for user in self.user]
#         return self.all_serialize(self.user)

#     def _request_serialize(self):
#         if isinstance(self.user, list):
#             return [self.request_serialize(user) for user in self.user]
#         return self.request_serialize(self.user)

#     def serialize(self, user=None):
#         user = user or self.user
#         return {
#             "name": user.name,
#             "email": user.email,
#             "compatibility": user.compatibility,
#             "sourcing": user.sourcing,
#             "status": user.status,
#         }

#     def all_serialize(self, user=None):
#         user = user or self.user
#         return {
#             "id": user.id,
#             "name": user.name,
#             "email": user.email,
#             "compatibility": user.compatibility,
#             "sourcing": user.sourcing,
#             "status": user.status,
#             "filename": self.filename,
#         }

#     def request_serialize(self, user=None):
#         user = user or self.user
#         return {
#             "name": user["name"],
#             "email": user["email"],
#             "compatibility": user["compatibility"],
#             "sourcing": user["sourcing"],
#             "status": user["status"],
#         }
# class _ErrorSerialize:
#     def _core_error_serialize(self, error, status):
#         return {
#             "status": status,
#             "description": status.phrase,
#             "message": error.message,
#         }


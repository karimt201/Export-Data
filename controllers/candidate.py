from flask import request
import validator as vd
import Serializer as sr
import exceptions
import http
import data_handler as dh

import models as md


class CandidateController:

    def __init__(self, candidate_test=None):
        self._request_data = candidate_test or request.get_json()

    @property
    def handler(self):
        return _DataHandler()

    def candidate_creator(self):
        try:
            _DataValidator(self._request_data)._All_validate()
            new_candidates = self.handler.post(self._request_data)
            return sr._DataSerializer(new_candidates)._request_serialize(), http.HTTPStatus.CREATED
        except exceptions._RequiredInputError as exc:
            return sr._DataSerializer()._core_error_serialize(
                exc, http.HTTPStatus.NOT_FOUND
            )
        except exceptions._InvalidInputError as exc:
            return sr._DataSerializer()._core_error_serialize(
                exc, http.HTTPStatus.BAD_REQUEST
            )

    # TODO: Add controller for each of the methods below
    def get_all_candidates(self):
        try:
            candidates = dh.database_handle().get_all()
            return sr._DataSerializer(candidates)._All_serialize(), http.HTTPStatus.OK
        except exceptions._NotFoundError as exc:
            return (
                sr._DataSerializer()._core_error_serialize(
                    exc, http.HTTPStatus.NOT_FOUND
                ),
                http.HTTPStatus.NOT_FOUND,
            )

    def get_all_candidates_paginated(self):
        try:
            pagination = dh.database_handle().get_paginated(page=1, per_page=5)
            return sr._DataSerializer(pagination)._All_serialize(), http.HTTPStatus.OK
        except exceptions._NotFoundError as exc:
            return sr._DataSerializer()._core_error_serialize(
                exc, http.HTTPStatus.NOT_FOUND
            )

    def get_candidate(self, candidate_id):
        try:
            candidate = dh.database_handle().get(candidate_id)
            return sr._DataSerializer(candidate)._All_serialize(), http.HTTPStatus.OK
        except exceptions._NotFoundError as exc:
            return sr._DataSerializer()._core_error_serialize(
                exc, http.HTTPStatus.NOT_FOUND
            )





class CreateCandidateController:
    def create(self, operation):
        try:
            _DataValidator(request_body).validate()
            candidate_id = request_body.get('candidateId')
            file_name = request_body.get('fileName')
            record = _ExtensionCreator(operation, candidate_id).create(file_name)
            return _Serializer(record).serialize(), http.HTTPStatus.CREATED
        except:
            # TODO: Enhance the exception handling
            pass

class _BusinessHandler:
    def __init__(self, candidate_test=None):
        self.operator = candidate_test or dh.CrudOperator(md.CandidateModel)

    def post(self, request_data):
        if request_data.get('age') < 30:
            raise exceptions._InvalidInputError('Age must be greater than 30')
        record = self.operator.create(request_data)
        return record


Builder = {
    'pdf': PDFBuilder,
    'csv': CSVBuilder,
    'xlsx': XLSXBuilder
}



class _ExtensionCreator:
    def __init__(self, operation, candidate_id=None):
        self.operation = operation
        self.candidate_id = candidate_id

    def create(self, file_name):
        return Builder.get(self.operation).create(file_name)


class _DataValidator:
    pass

class _Serializer:
    pass

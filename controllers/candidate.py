from flask import  request
import validator as vd
import Serializer as sr
import exceptions
import http
import data_handler as dh

class CandidateController:
  
  def __init__(self,candidate_test=None):
    self.request_data = candidate_test or request.get_json()
  def candidate_creator(self):
    try:
      vd._DataValidator(self.request_data)._All_validate()
      new_candidates = dh._database_handle()._post_all_data_types(self.request_data)
      return sr._DataSerializer(new_candidates)._All_serialize(), http.HTTPStatus.CREATED
    except exceptions._RequiredInputError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND)  
    except exceptions._InvalidInputError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.BAD_REQUEST) 
      
  def get_all_candidates(self):
    try:
      candidates = dh._database_handle()._get_all()
      return sr._DataSerializer(candidates)._All_serialize(),http.HTTPStatus.OK 
    except exceptions._NotFoundError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND 

  def get_all_candidates_paginated(self):
    try:
      pagination = dh._database_handle()._get_paginated(page=1,per_page=5)
      return sr._DataSerializer(pagination)._All_serialize(),http.HTTPStatus.OK
    except exceptions._NotFoundError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND) 
    
  def get_candidate(self,candidate_id):
    try:
      candidate = dh._database_handle()._get(candidate_id)
      return sr._DataSerializer(candidate)._All_serialize(),http.HTTPStatus.OK
    except exceptions._NotFoundError as exc:
      return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND) 

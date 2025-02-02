from db import db
from flask import  request
import exceptions
import models as md


class _CrudOperator:
  def __init__(self, model, session=None):
    self.model = model
    self.session = session or db.session

  def get_all(self):
    return self.model.query.all()
              
  def get_one(self, _id):
    return self.model.query.get(_id)
  
  def get_paginated(self,page,per_page):
    page = request.args.get("page",page,type=int)
    per_page = request.args.get("per_page",per_page,type=int)
    return self.model.query.paginate(page=page,per_page=per_page,error_out=False)
  
  def unique_fields(self,existing_field):
    return self.model.query.filter_by(existing_field).first()

  def post_list(self,request_data):
    new_candidates = []
    for data in request_data:
      new_candidate = self.model(data)
      self.session.add(new_candidate)
      new_candidates.append(new_candidate)
    self.session.commit()
    return new_candidates
  
  def post_one(self,request_data):
    new_candidate = self.model(request_data)
    db.session.add(new_candidate)
    new_candidates = [new_candidate]
    self.session.commit()
    return new_candidates
  
class database_handle:
  def __init__(self):
    self.data= _CrudOperator(md.CandidateModel)
    
  def get_all(self):
    records = self.data.get_all()
    if not records : raise exceptions._NotFoundError("Records does not exist")
    return records
  
  def get_paginated(self,page,per_page):
    pagination = self.data.get_paginated(page,per_page)
    if not pagination.items : raise exceptions._NotFoundError("No Records in this Page")
    return pagination.items
  
  def get(self,_id):
    record = self.data.get_one(_id)
    if not record : raise exceptions._NotFoundError("Record does not exist")
    return record
  

  def list_data(self,request_body):
    add_records = self.data.post_list(request_body)
    return add_records
  
  def dict_data(self,request_body):
    add_records = self.data.post_one(request_body)
    return add_records
  
  def post_all_data_types(self,request_data):
    if isinstance(request_data,list):
      candidates = self.list_data(request_data)
    elif isinstance(request_data,dict) :
      candidates = self.dict_data(request_data)
    else:
      raise exceptions._InvalidInputError("invalid input, only accept dict data or list of dicts")
    return candidates
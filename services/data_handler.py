import helpers.exceptions as exceptions
import models as md

class CrudOperator:
    def __init__(self, model, session_test=None):
        self.model = model
        self.session = session_test or md.db.session

    def get_all(self):
        return self.model.query.all()
    
    def get_one(self, _id):
        return self.session.get(self.model, _id)
    
    def get_paginated(self,page,per_page):
        return self.model.query.paginate(page=page,per_page=per_page,error_out=False)

    def create(self, request_data):
        self._filter(request_data)
        record = self.model(**request_data)
        self.session.add(record)
        self.session.commit()
        return record
    
    def update(self,_id,request_data):
        record = self.get_one(_id)
        if not record :
            raise exceptions.NotFoundError(f"record with id {_id} not found")
        self._filter(request_data)
        
        for key,value in request_data.items() :
            setattr(record,key,value)
            
        self.session.commit()
        return record
    
    def delete(self,_id):
        record = self.get_one(_id)
        if not record :
            raise exceptions.NotFoundError(f"record with id {_id} not found")
        self.session.delete(record)
        self.session.commit()
        return record
    
    def _filter(self, data):
        for attr in data.keys():
            if not hasattr(self.model, attr): raise exceptions.InvalidFieldError(f"{attr} field is not valid")
        return data
    
    def _filter_data(self, data):
        filter_data={}
        for key,value in data.items():
            if  hasattr(self.model, key): filter_data[key]=value
        return filter_data
    
    @property
    def user_filter_data(self):
        return self.model.query.filter_by
                
    
    
import exceptions
import models as md


class CrudOperator:
    def __init__(self, model, session_test=None):
        self.model = model
        self.session = session_test or md.db.session

    def get_all(self):
        return self.model.query.all()
    
    def get_one(self, _id):
        # return self.session.query(self.model).get(_id)
        return self.session.get(self.model, _id)


    def get_paginated(self,page,per_page):
        return self.model.query.paginate(page=page,per_page=per_page,error_out=False)

    def create(self, request_data):
        filtered_data = self._filter(request_data)
        record = self.model(**filtered_data)
        self.session.add(record)
        self.session.commit()
        return record
    
    
    def create_many(self, request_data):
        filtered_data = self._filter_data(request_data)
        record = self.model(**filtered_data)
        self.session.add(record)
        # self.session.commit()
        return record
    
    def create_user(self,request_data,email,password):
        self._filter(request_data)
        record = self.model(email=email,password=password)
        self.session.add(record)
        self.session.commit()
        return record
    
    def commit(self):
        self.session.commit()

    def _filter(self, data):
        # TODO: Change this to accept only the model attributes using hasattr
        for attr in data.keys():
            if not hasattr(self.model, attr): raise exceptions._InvalidFieldError(f"{attr} field is not valid")
        return data
    
    def _filter_data(self, data):
        filter_data={}
        for key,value in data.items():
            if  hasattr(self.model, key): filter_data[key]=value
        return filter_data
    
    def filter_data(self,name):
        return self.model.query.filter_by(name=name).first()
    
    @property
    def user_filter_data(self):
        return self.model.query.filter_by
                
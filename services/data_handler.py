import helpers.exceptions as exceptions
import models as md

class CrudOperator:
    def __init__(self, model, session_test=None):
        self.model = model
        self.session = session_test or md.db.session

    def get_all(self):
        """
        Retrieves all records from the database.

        :return: A list of all records.
        """
        return self.model.query.all()
    
    def get_one(self, _id):
        """
        Retrieves a single record by ID.

        :param _id: The ID of the record to retrieve.
        
        :return: The retrieved record.
        
        """
        return self.session.get(self.model, _id)
    
    def get_paginated(self,page,per_page):
        """
        Retrieves paginated records from the database.

        :param page: The page number to retrieve.
        
        :param per_page: The number of records per page.
        
        :return: A paginated list of records.
        """
        return self.model.query.paginate(page=page,per_page=per_page,error_out=False)

    def create(self, request_data):
        """
        Creates a new record in the database.

        :param request_data: The data to create the record.
        
        :return: The created record.
        """
        self._filter(request_data)
        record = self.model(**request_data)
        self.session.add(record)
        self.session.commit()
        return record
    
    def update(self,_id,request_data):
        """
        Updates an existing record in the database.

        :param _id: The ID of the record to update.
        
        :param request_data: The data to update the record.
        
        :return: The updated record.
        """
        record = self.get_one(_id)
        if not record :
            raise exceptions.NotFoundError(f"record with id {_id} not found")
        self._filter(request_data)
        
        for key,value in request_data.items() :
            setattr(record,key,value)
            
        self.session.commit()
        return record
    
    def delete(self,_id):
        """
        Deletes a record from the database.

        :param _id: The ID of the record to delete.
        
        :return: The deleted record.
        """
        record = self.get_one(_id)
        if not record :
            raise exceptions.NotFoundError(f"record with id {_id} not found")
        self.session.delete(record)
        self.session.commit()
        return record
    
    def _filter(self, data):
        """
        Validates and filters data for database operations.

        :param data: The data to filter.
        
        :return: The filtered data.
        
        :raises exceptions.InvalidFieldError: If an invalid field is found.
        """
        for attr in data.keys():
            if not hasattr(self.model, attr): raise exceptions.InvalidFieldError(f"{attr} field is not valid")
        return data
    
    def _filter_data(self, data):
        """
        Filters data to include only valid model attributes.

        :param data: The data to filter.
        
        :return: The filtered data.
        """
        filter_data={}
        for key,value in data.items():
            if  hasattr(self.model, key): filter_data[key]=value
        return filter_data
    
    @property
    def user_filter_data(self):
        """
        Returns a filter query for the model.

        :return: A filter query for the model.
        """
        return self.model.query.filter_by
                
    
    
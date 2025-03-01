from flask import request
import exceptions
import models as md


class CrudOperator:
    def __init__(self, model, session=None):
        self.model = model
        self.session = session or md.db.session

    def get_all(self):
        return self.model.query.all()
    
    def get_one(self, _id):
        # return self.session.query(self.model).get(_id)
        return self.session.get(self.model, _id)
    # 
    def get_paginated(self,page,per_page):
        # page = page or request.args.get("page", page, type=int)
        # per_page = per_page or request.args.get("per_page", per_page, type=int)
        return self.model.query.paginate(page=page,per_page=per_page,error_out=False)
    
    # def post_list(self, request_data):
    #     for data in request_data:
    #         self.session.add(self.model(data))
    #     self.session.commit()
    #     return request_data

    def create(self, request_data):
        filtered_data = self._filter(request_data)
        record = self.model(**filtered_data)
        self.session.add(record)
        self.session.commit()
        return record

    def _filter(self, data):
        # TODO: Change this to accept only the model attributes using hasattr
        for attr in data.keys():
            if not hasattr(self.model, attr): raise exceptions._InvalidFieldError(f"{attr} field is not valid")
        return data
                
        


# class database_handle:
#     def __init__(self, date_test=None):
#         self.data = date_test or CrudOperator(md.CandidateModel)

#     def get_all(self):
#         records = self.data.get_all()
#         if not records:
#             raise exceptions._NotFoundError("Records does not exist")
#         return records

#     def get_paginated(self, page, per_page):
#         pagination = self.data.get_paginated(page, per_page)
#         if not pagination.items:
#             raise exceptions._NotFoundError("No Records in this Page")
#         return pagination.items

#     def get_paginated_for_test(self):
#         return self.get_paginated(10, 10)

#     def get(self, _id):
#         record = self.data.get_one(_id)
#         if not record:
#             raise exceptions._NotFoundError("Record does not exist")
#         return record

#     def list_data(self, request_body):
#         add_records = self.data.post_list(request_body)
#         return add_records
# 
#     def dict_data(self, request_body):
#         add_records = self.data.post_one(request_body)
#         return add_records
# 
#     def post_all_data_types(self, request_data):
#         if isinstance(request_data, list):
#             candidates = self.list_data(request_data)
#         elif isinstance(request_data, dict):
#             candidates = self.dict_data(request_data)
#         else:
#             raise exceptions._InvalidInputError(
#                 "invalid input, only accept dict data or list of dicts"
#             )
#         return candidates

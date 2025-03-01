# import flask as fk
# import csv
# import controllers.writer as DW
# import Serializer as sr
# import exceptions
# import data_handler as dh
# import models as md




# class CSVCreator(DW.DataWriter):

#     def __init__(self, test_csv_writer=None):
#         self.test_csv_writer = test_csv_writer or csv

#     def write_export_files(self, data, filename):

#         with open(filename, "w", newline="") as csv_file:
#             wr = self.test_csv_writer.writer(csv_file)
#             wr.writerow(data.header)
#             wr.writerows(data.rows)

#         return filename
    
# import controllers.candidate as bd
# class _CandidateController(bd.BuilderInterface):
#     def __init__(self):
#         self.candidate = None
#         self.row_data = None
#         self.csv_file = None
        
#     @property
#     def handler(self,business_handler_test=None):
#         return business_handler_test or _CandidateBusinessHandler()
    
#     @property
#     def request(self,request_test=None):
#         return request_test or fk.request.args.get
    
#     def prepare_data(self):
#         page = self.request("page", type=int)
#         per_page = self.request("per_page", 3 , type=int)
#         candidate_id = self.request("candidateId")
#         if candidate_id :
#             self.candidate = self.handler.get(candidate_id)
#         elif page:
#             self.candidate = self.handler.get_paginated(page,per_page)
#         else:
#             self.candidate = self.handler.get_all()
#         serializer = sr._DataSerializer(self.candidate)._data_serialize()
#         self.row_data = DW.RowExcelData(serializer)
    
#     def create_file(self,exten):
#         self.csv_file = exten
    
#     def save_file(self,filename):
#         manger = DW.DataManger(self.csv_file)
#         manger.save(self.row_data, filename)
#         return self.candidate

# class _CandidateBusinessHandler:
#     def __init__(self, candidate_test=None):
#         self.data = candidate_test or dh.CrudOperator(md.CandidateModel)
        
#     def post(self, request_body):
#         if request_body.get("age") < 30:
#             raise exceptions._InvalidInputError("Age must be greater than 30")
#         record = self.data.create(request_body)
#         return record
    
#     def get_all(self):
#         records = self.data.get_all()
#         if not records:
#             raise exceptions._NotFoundError("Records does not exist")
#         return records
    
#     def get(self, _id):
#         record = self.data.get_one(_id)
#         if not record:
#             raise exceptions._NotFoundError("Record does not exist")
#         return record
    
#     def get_paginated(self, page, per_page):
#         pagination = self.data.get_paginated(page, per_page)
#         if not pagination.items:
#             raise exceptions._NotFoundError("No Records in this Page")
#         return pagination.items


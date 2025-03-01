# import openpyxl as wb
# import controllers.writer as DW
# import Serializer as sr
# import exceptions
# import http
# import data_handler as dh
# import controllers.candidate as bd
# import models as md


# class ExcelCreator(DW.DataWriter):

#     def __init__(self, test_excel_writer=None):
#         self.wb = test_excel_writer or wb.Workbook()

#     def write_export_files(self, data, filename):
#         ws = self.wb.active
#         ws.append(data.header)
#         for row in data.rows:
#             ws.append(row)
#         return self.wb.save(filename)


# class ExcelController:

#     def create_excel(self):
#         try:
#             candidate = dh.database_handle().get_all()
#             Serializer = sr._DataSerializer(candidate)._data_serialize()
#             row_data = DW.RowExcelData(Serializer)
#             xlsx_file = ExcelCreator()
#             manger = DW.DataManger(xlsx_file)
#             self.create_excel_manger(manger, row_data, "Export_All_candidate.xlsx")
#             return self.create_excel_Serializer(candidate, "Export_All_candidate.xlsx")
#         except exceptions._NotFoundError as exc:
#             return (
#                 sr._DataSerializer()._core_error_serialize(
#                     exc, http.HTTPStatus.NOT_FOUND
#                 ),
#                 http.HTTPStatus.NOT_FOUND,
#             )

    # def create_excel_pagenited(self):
    #   try:
    #     candidate = dh.database_handle().get_paginated(page=1,per_page=3)
    #     Serializer = sr._DataSerializer(candidate)._data_serialize()
    #     row_data = DW.RowExcelData(Serializer)
    #     xlsx_file = ExcelCreator()
    #     manger = DW.DataManger(xlsx_file)
    #     manger.save(row_data,"Export_candidate_paginated.xlsx")
    #     return sr._DataSerializer(candidate,"Export_candidate_paginated.xlsx")._All_serialize(),http.HTTPStatus.OK
    #   except exceptions._NotFoundError as exc:
    #     return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

#     def create_excel_record(self, candidate_id):
#         try:
#             candidate = dh.database_handle().get(candidate_id)
#             Serializer = sr._DataSerializer(candidate)._data_serialize()
#             row_data = DW.RowExcelData([Serializer])
#             xlsx_file = ExcelCreator()
#             manger = DW.DataManger(xlsx_file)
#             self.create_excel_manger(manger, row_data, "Export_One_candidate.xlsx")
#             return self.create_excel_Serializer(candidate, "Export_One_candidate.xlsx")
#         except exceptions._NotFoundError as exc:
#             return (
#                 sr._DataSerializer()._core_error_serialize(
#                     exc, http.HTTPStatus.NOT_FOUND
#                 ),
#                 http.HTTPStatus.NOT_FOUND,
#             )

#     def create_excel_manger(self, manger, row_data, filename):
#         return manger.save(row_data, filename)

#     def create_excel_Serializer(self, candidate, filename):
#         return (
#             sr._DataSerializer(candidate, filename)._All_serialize(),
#             http.HTTPStatus.OK,
#         )

# class AllCandidateExcelBuilder(bd.BuilderInterface):
#     def __init__(self):
#         self.candidate = None
#         self.row_data = None
#         self.excel_file = None
        
#     @property
#     def handler(self):
#         return _BusinessHandler()
    
#     def prepare_data(self):
#         self.candidate = self.handler.get_all()
#         serializer = sr._DataSerializer(self.candidate)._data_serialize()
#         self.row_data = DW.RowExcelData(serializer)
    
#     def create_file(self,exten):
#         self.excel_file = exten
    
#     def save_file(self,filename):
#         manger = DW.DataManger(self.excel_file)
#         manger.save(self.row_data, filename)
#         return self.candidate


# class CandidateExcelBuilder(bd.BuilderInterface):
#     def __init__(self):
#         self.candidate = None
#         self.row_data = None
#         self.excel_file = None
        
#     @property
#     def handler(self):
#         return _BusinessHandler()
    
#     def prepare_data(self,candidate_id):
#         self.candidate = self.handler.get(candidate_id)
#         serializer = sr._DataSerializer(self.candidate)._data_serialize()
#         self.row_data = DW.RowExcelData([serializer])
    
#     def create_file(self):
#         self.excel_file = ExcelCreator()
    
#     def save_file(self,filename):
#         manger = DW.DataManger(self.excel_file)
#         manger.save(self.row_data, filename)
#         return self.candidate



# class _BusinessHandler:
#     def __init__(self, candidate_test=None):
#         self.data = candidate_test or dh.CrudOperator(md.CandidateModel)
        
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
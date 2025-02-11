# import reportlab.platypus as platypus
# import reportlab.lib as lib
# import reportlab.lib.pagesizes as pagesizes
# import controllers.writer as DW
# import Serializer as sr
# import exceptions
# import http
# import data_handler as dh
# # import builder as bd
# import controllers.candidate as bd
# import models as md


# class PDFCreator(DW.DataWriter):

#     def __init__(self, test_pdf_lib=None):
#         self.pdf_lib = test_pdf_lib or platypus

#     def write_export_files(self, data, filename):

#         pdf = self.pdf_lib.SimpleDocTemplate(filename, pagesize=pagesizes.A4)
#         table = self.pdf_lib.Table([data.header] + data.rows)
#         table_style = [
#             ("BACKGROUND", (0, 0), (-1, 0), lib.colors.grey),
#             ("GRID", (0, 0), (-1, -1), 1, lib.colors.black),
#         ]
#         style = self.pdf_lib.TableStyle(table_style)
#         table.setStyle(style)
#         return pdf.build([table])


# class PdfController:

#     def create_pdf(self):
#         try:
#             candidate = dh.database_handle().get_all()
#             Serializer = sr._DataSerializer(candidate)._data_serialize()
#             row_data = DW.RowExcelData(Serializer)
#             Pdf_file = PDFCreator()
#             manger = DW.DataManger(Pdf_file)
#             self.create_pdf_manger(manger, row_data, "Export_All_candidate.pdf")
#             return self.create_pdf_Serializer(candidate, "Export_All_candidate.pdf")
#         except exceptions._NotFoundError as exc:
#             return (
#                 sr._DataSerializer()._core_error_serialize(
#                     exc, http.HTTPStatus.NOT_FOUND
#                 ),
#                 http.HTTPStatus.NOT_FOUND,
#             )

#     # def create_pdf_paginated(self):
#     #   try:
#     #     candidate = dh.database_handle().get_paginated(page=1,per_page=3)
#     #     Serializer = sr._DataSerializer(candidate)._data_serialize()
#     #     row_data = DW.RowExcelData(Serializer)
#     #     Pdf_file = PDFCreator()
#     #     manger = DW.DataManger(Pdf_file)
#     #     manger.save(row_data,"Export_candidate_paginated.pdf")
#     #     return sr._DataSerializer(candidate,"Export_candidate_paginated.pdf")._All_serialize(),http.HTTPStatus.OK
#     #   except exceptions._NotFoundError as exc:
#     #     return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

#     # def create_pdf_record(self, candidate_id):
#     #     try:
#     #         candidate = dh.database_handle().get(candidate_id)
#     #         Serializer = sr._DataSerializer(candidate)._data_serialize()
#     #         row_data = DW.RowExcelData([Serializer])
#     #         Pdf_file = PDFCreator()
#     #         manger = DW.DataManger(Pdf_file)
#     #         self.create_pdf_manger(manger, row_data, "Export_One_candidate.pdf")
#     #         return self.create_pdf_Serializer(candidate, "Export_One_candidate.pdf")
#     #     except exceptions._NotFoundError as exc:
#     #         return (
#     #             sr._DataSerializer()._core_error_serialize(
#     #                 exc, http.HTTPStatus.NOT_FOUND
#     #             ),
#     #             http.HTTPStatus.NOT_FOUND,
#     #         )

#     # def create_pdf_manger(self, manger, row_data, filename):
#     #     return manger.save(row_data, filename)

#     # def create_pdf_Serializer(self, candidate, filename):
#     #     return (
#     #         sr._DataSerializer(candidate, filename)._All_serialize(),
#     #         http.HTTPStatus.OK,
#     #     )

# class AllCandidatePdfBuilder(bd.BuilderInterface):
#     def __init__(self):
#         self.candidate = None
#         self.row_data = None
#         self.pdf_file = None
        
#     @property
#     def handler(self):
#         return _BusinessHandler()
    
#     def prepare_data(self):
#         self.candidate = self.handler.get_all()
#         serializer = sr._DataSerializer(self.candidate)._data_serialize()
#         self.row_data = DW.RowExcelData(serializer)
    
#     def create_file(self):
#         self.pdf_file = PDFCreator()
    
#     def save_file(self,filename):
#         manger = DW.DataManger(self.pdf_file)
#         manger.save(self.row_data, filename)
#         return self.candidate


# class CandidatePdfBuilder(bd.BuilderInterface):
#     def __init__(self):
#         self.candidate = None
#         self.row_data = None
#         self.pdf_file = None
        
#     @property
#     def handler(self):
#         return _BusinessHandler()
    
#     def prepare_data(self,candidate_id):
#         self.candidate = self.handler.get(candidate_id)
#         serializer = sr._DataSerializer(self.candidate)._data_serialize()
#         self.row_data = DW.RowExcelData([serializer])
    
#     def create_file(self):
#         self.pdf_file = PDFCreator()
    
#     def save_file(self,filename):
#         manger = DW.DataManger(self.pdf_file)
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
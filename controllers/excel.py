import openpyxl as wb
import controllers.DataWriter as DW
import Serializer as sr
import exceptions
import http
import data_handler as dh


class ExcelCreator(DW.DataWriter):

    def __init__(self, test_excel_writer=None):
        self.wb = test_excel_writer or wb.Workbook()

    def write_export_files(self, data, filename):
        ws = self.wb.active
        ws.append(data.header)
        for row in data.rows:
            ws.append(row)
        return self.wb.save(filename)


class ExcelController:

    def create_excel(self):
        try:
            candidate = dh.database_handle().get_all()
            Serializer = sr._DataSerializer(candidate)._data_serialize()
            row_data = DW.RowExcelData(Serializer)
            xlsx_file = ExcelCreator()
            manger = DW.DataManger(xlsx_file)
            self.create_excel_manger(manger, row_data, "Export_All_candidate.xlsx")
            return self.create_excel_Serializer(candidate, "Export_All_candidate.xlsx")
        except exceptions._NotFoundError as exc:
            return (
                sr._DataSerializer()._core_error_serialize(
                    exc, http.HTTPStatus.NOT_FOUND
                ),
                http.HTTPStatus.NOT_FOUND,
            )

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

    def create_excel_record(self, candidate_id):
        try:
            candidate = dh.database_handle().get(candidate_id)
            Serializer = sr._DataSerializer(candidate)._data_serialize()
            row_data = DW.RowExcelData([Serializer])
            xlsx_file = ExcelCreator()
            manger = DW.DataManger(xlsx_file)
            self.create_excel_manger(manger, row_data, "Export_One_candidate.xlsx")
            return self.create_excel_Serializer(candidate, "Export_One_candidate.xlsx")
        except exceptions._NotFoundError as exc:
            return (
                sr._DataSerializer()._core_error_serialize(
                    exc, http.HTTPStatus.NOT_FOUND
                ),
                http.HTTPStatus.NOT_FOUND,
            )

    def create_excel_manger(self, manger, row_data, filename):
        return manger.save(row_data, filename)

    def create_excel_Serializer(self, candidate, filename):
        return (
            sr._DataSerializer(candidate, filename)._All_serialize(),
            http.HTTPStatus.OK,
        )

import reportlab.platypus as platypus
import reportlab.lib as lib
import reportlab.lib.pagesizes as pagesizes
import controllers.DataWriter as DW
import Serializer as sr
import exceptions
import http
import data_handler as dh


class PDFCreator(DW.DataWriter):

    def __init__(self, test_pdf_lib=None):
        self.pdf_lib = test_pdf_lib or platypus

    def write_export_files(self, data, filename):

        pdf = self.pdf_lib.SimpleDocTemplate(filename, pagesize=pagesizes.A4)
        table = self.pdf_lib.Table([data.header] + data.rows)
        table_style = [
            ("BACKGROUND", (0, 0), (-1, 0), lib.colors.grey),
            ("GRID", (0, 0), (-1, -1), 1, lib.colors.black),
        ]
        style = self.pdf_lib.TableStyle(table_style)
        table.setStyle(style)
        return pdf.build([table])


class PdfController:

    def create_pdf(self):
        try:
            candidate = dh.database_handle().get_all()
            Serializer = sr._DataSerializer(candidate)._data_serialize()
            row_data = DW.RowExcelData(Serializer)
            Pdf_file = PDFCreator()
            manger = DW.DataManger(Pdf_file)
            self.create_pdf_manger(manger, row_data, "Export_All_candidate.pdf")
            return self.create_pdf_Serializer(candidate, "Export_All_candidate.pdf")
        except exceptions._NotFoundError as exc:
            return (
                sr._DataSerializer()._core_error_serialize(
                    exc, http.HTTPStatus.NOT_FOUND
                ),
                http.HTTPStatus.NOT_FOUND,
            )

    # def create_pdf_paginated(self):
    #   try:
    #     candidate = dh.database_handle().get_paginated(page=1,per_page=3)
    #     Serializer = sr._DataSerializer(candidate)._data_serialize()
    #     row_data = DW.RowExcelData(Serializer)
    #     Pdf_file = PDFCreator()
    #     manger = DW.DataManger(Pdf_file)
    #     manger.save(row_data,"Export_candidate_paginated.pdf")
    #     return sr._DataSerializer(candidate,"Export_candidate_paginated.pdf")._All_serialize(),http.HTTPStatus.OK
    #   except exceptions._NotFoundError as exc:
    #     return sr._DataSerializer()._core_error_serialize(exc,http.HTTPStatus.NOT_FOUND),http.HTTPStatus.NOT_FOUND

    def create_pdf_record(self, candidate_id):
        try:
            candidate = dh.database_handle().get(candidate_id)
            Serializer = sr._DataSerializer(candidate)._data_serialize()
            row_data = DW.RowExcelData([Serializer])
            Pdf_file = PDFCreator()
            manger = DW.DataManger(Pdf_file)
            self.create_pdf_manger(manger, row_data, "Export_One_candidate.pdf")
            return self.create_pdf_Serializer(candidate, "Export_One_candidate.pdf")
        except exceptions._NotFoundError as exc:
            return (
                sr._DataSerializer()._core_error_serialize(
                    exc, http.HTTPStatus.NOT_FOUND
                ),
                http.HTTPStatus.NOT_FOUND,
            )

    def create_pdf_manger(self, manger, row_data, filename):
        return manger.save(row_data, filename)

    def create_pdf_Serializer(self, candidate, filename):
        return (
            sr._DataSerializer(candidate, filename)._All_serialize(),
            http.HTTPStatus.OK,
        )

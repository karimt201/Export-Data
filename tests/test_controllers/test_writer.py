import unittest
from assertpy import assert_that
import reportlab.lib.pagesizes as pagesizes
import openpyxl as xl
import reportlab.lib as lib
# import controllers.writer as writer
# import controllers
# from /./.controllers import writer
# from ..controllers import writer
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from controllers import writer

import exceptions


class TestDataWriter(unittest.TestCase):
    
    def test_write_raise_exception(self):
        data_writer = writer.DataWriter()
        with self.assertRaises(exceptions._NotImplementError) as write_export_files_exc:
            data_writer.write_export_files("data", "filename")
        assert_that(str(write_export_files_exc.exception)).is_equal_to(
            "children must implement this method"
        )
        
        

class TestExcelCreator(unittest.TestCase):

    def test_write(self):
        workbook = WorkBookDouble()
        creator = writer.ExcelCreator(workbook)
        data = ExcelDataDouble(headers=["name", "age"], rows=[["test", 20]])
        result = creator.write_export_files(data, "success.xlsx")
        assert_that(result).is_equal_to("success.xlsx")
        assert_that(workbook.active[0]).is_equal_to(["name", "age"])
        assert_that(workbook.active[1]).is_equal_to(["test", 20])
        workbook.assert_that_save_called_with("success.xlsx")
        workbook.assert_that_active_hold_the_data([["name", "age"], ["test", 20]])

    def test_calls_real_workbook(self):
        creator = writer.ExcelCreator()
        assert_that(creator.wb).is_instance_of(xl.Workbook)


class WorkBookDouble:
    def __init__(self):
        self.active = []
        self.given_file_name = None

    def save(self, filename):
        self.given_file_name = filename
        return filename

    def assert_that_save_called_with(self, filename):
        assert_that(self.given_file_name).is_equal_to(filename)

    def assert_that_active_hold_the_data(self, data):
        assert_that(self.active).is_equal_to(data)


class ExcelDataDouble:
    def __init__(self, headers, rows):
        self.header = headers
        self.rows = rows



class TestCSVCreator(unittest.TestCase):

    def test_sava_csv(self):
        writer_double = CsvWriterDouble()
        creator = writer.CSVCreator(writer_double)
        data = ExcelDataDouble(headers=["name", "age"], rows=[["test", 20]])
        result = creator.write_export_files(data, "success.csv")
        assert_that(result).is_equal_to("success.csv")
        writer_double.assert_that_writerow_hold_the_header(["name", "age"])
        writer_double.assert_that_writerows_hold_the_rows([["test", 20]])


class CsvWriterDouble:

    def __init__(self):
        self.given_header = None
        self.given_rows = None
        self.given_csv_file = None

    def writer(self, csv_file):
        self.given_csv_file = csv_file
        return self

    def writerow(self, header):
        self.given_header = header
        return header

    def writerows(self, rows):
        self.given_rows = rows
        return rows

    def assert_that_writerow_hold_the_header(self, header):
        assert_that(self.given_header).is_equal_to(header)

    def assert_that_writerows_hold_the_rows(self, rows):
        assert_that(self.given_rows).is_equal_to(rows)


class TestPdfCreator(unittest.TestCase):

    def test_write(self):
        pdf_writer = PdfWriterDouble()
        creator = writer.PDFCreator(pdf_writer)
        data = ExcelDataDouble(headers=["name", "age"], rows=[["test", 20]])
        result = creator.write_export_files(data, "success.pdf")
        assert_that(result).is_equal_to("success.pdf")
        pdf_writer.assert_that_simple_doc_template_file_name_called_with("success.pdf")
        pdf_writer.assert_that_simple_doc_template_page_size_called_with(pagesizes.A4)
        pdf_writer.assert_that_table_hold_the_tabledata([["name", "age"], ["test", 20]])
        pdf_writer.assert_that_table_style_called_with(
            [
                ("BACKGROUND", (0, 0), (-1, 0), lib.colors.grey),
                ("GRID", (0, 0), (-1, -1), 1, lib.colors.black),
            ]
        )


class PdfWriterDouble:

    def __init__(self):
        self.given_file_name = None
        self.given_page_size = None
        self.given_table_data = None
        self.give_style_table = None

    def SimpleDocTemplate(self, filename, pagesize):
        self.given_file_name = filename
        self.given_page_size = pagesize
        return PdfDouble(self.given_file_name)

    def Table(self, tabledata):
        self.given_table_data = tabledata
        return PdfDouble()

    def TableStyle(self, styletable):
        self.give_style_table = styletable

    def assert_that_simple_doc_template_file_name_called_with(self, filename):
        assert_that(self.given_file_name).is_equal_to(filename)

    def assert_that_simple_doc_template_page_size_called_with(self, pagesize):
        assert_that(self.given_page_size).is_equal_to(pagesize)

    def assert_that_table_hold_the_tabledata(self, tabledata):
        assert_that(self.given_table_data).is_equal_to(tabledata)

    def assert_that_table_style_called_with(self, styletable):
        assert_that(self.give_style_table).is_equal_to(styletable)


class PdfDouble:

    def __init__(self, filename=None):
        self.given_file_name = filename

    def setStyle(self, styledata):
        self.given_style_data = styledata

    def build(self, tabledata):
        self.given_table_data = tabledata
        return self.given_file_name


class TestRowExcelData(unittest.TestCase):

    def setUp(self):
        self.row_excel_data = writer.RowExcelData([{"name": "test", "age": 20}])

    def test_data_is_empty(self):
        row_excel_data = writer.RowExcelData([])
        assert_that(row_excel_data.header).is_empty()
        assert_that(row_excel_data.rows).is_empty()

    def test_headers(self):
        assert_that(self.row_excel_data.header).contains("name", "age")

    def test_rows(self):
        assert_that(self.row_excel_data.rows).is_length(1)
        assert_that(self.row_excel_data.rows[0]).contains("test", 20)


class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.writer = WriterDouble()
        self.data_manager = writer.DataManger(self.writer)

    def test_save(self):
        save = self.data_manager.save("data", "success.xlsx")
        assert_that(save).is_equal_to("success.xlsx")
        self.writer.assert_write_is_called_with("data", "success.xlsx")


class WriterDouble:

    def __init__(self):
        self.given_data = None
        self.given_filename = None

    def write_export_files(self, data, filename):
        self.given_data = data
        self.given_filename = filename
        return filename

    def assert_write_is_called_with(self, data, filename):
        assert_that(self.given_data).is_equal_to(data)
        assert_that(self.given_filename).is_equal_to(filename)


class TestError(unittest.TestCase):

    def test_read(self):
        error = writer.Error()
        result = error.read("filename")
        assert_that(result).is_equal_to("success")
        

if __name__ == "__main__":
    unittest.main()

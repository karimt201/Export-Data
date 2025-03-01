import unittest
from assertpy import assert_that
import reportlab.lib.pagesizes as pagesizes
import openpyxl as xl
import reportlab.lib as lib
import controllers.writer as writer
# import controllers.writer as excel
# import Serializer as sr
# import validator as vd
import exceptions as ex
import data_handler as dh
import data_handler as dh
import app as app
import exceptions


class TestCsvController(unittest.TestCase):

    def test_csv_controller(self):
        csv_controller_spy = CsvControllerSpy()
        csv_manger = csv_controller_spy.create_csv_manger("All", "Success", "now")
        with app.app.app_context():
            create_csv = csv_controller_spy.create_csv()
            create_csv_record = csv_controller_spy.create_csv_record(1)
        assert_that(csv_manger).is_equal_to("All Success")
        assert_that(create_csv).is_equal_to("Success")
        assert_that(create_csv_record).is_equal_to("Success")


class CsvControllerSpy(csv.CsvController):

    def create_csv_manger(self, manger, row_data, filename):
        return "All Success"

    def create_csv_Serializer(self, candidate, filename):
        return "Success"


class TestCsvController(unittest.TestCase):

    def test_csv_controller(self):
        csv_controller_spy = CsvControllerSpy()
        csv_manger = csv_controller_spy.create_csv_manger("All", "Success", "now")
        with app.app.app_context():
            create_csv = csv_controller_spy.create_csv()
            create_csv_record = csv_controller_spy.create_csv_record(1)
        assert_that(csv_manger).is_equal_to("All Success")
        assert_that(create_csv).is_equal_to("Success")
        assert_that(create_csv_record).is_equal_to("Success")


class CsvControllerSpy(csv.CsvController):

    def create_csv_manger(self, manger, row_data, filename):
        return "All Success"

    def create_csv_Serializer(self, candidate, filename):
        return "Success"


class TestExcelController(unittest.TestCase):

    def test_excel_controller(self):
        excel_controller_spy = ExcelControllerSpy()
        excel_manger = excel_controller_spy.create_excel_manger("All", "Success", "now")
        with app.app.app_context():
            create_excel = excel_controller_spy.create_excel()
            # create_csv_paginated =csv_controller_spy.create_csv_paginated()
            create_excel_record = excel_controller_spy.create_excel_record(1)
        assert_that(excel_manger).is_equal_to("All Success")
        assert_that(create_excel).is_equal_to("Success")
        # assert_that(create_csv_paginated).is_equal_to('Success')
        assert_that(create_excel_record).is_equal_to("Success")


class ExcelControllerSpy(excel.ExcelController):

    def create_excel_manger(self, manger, row_data, filename):
        return "All Success"

    def create_excel_Serializer(self, candidate, filename):
        return "Success"


class TestPdfController(unittest.TestCase):

    def test_pdf_controller(self):
        pdf_controller_spy = PdfControllerSpy()
        pdf_manger = pdf_controller_spy.create_pdf_manger("All", "Success", "now")
        with app.app.app_context():
            create_pdf = pdf_controller_spy.create_pdf()
            # create_csv_paginated =csv_controller_spy.create_csv_paginated()
            create_pdf_record = pdf_controller_spy.create_pdf_record(1)
        assert_that(pdf_manger).is_equal_to("All Success")
        assert_that(create_pdf).is_equal_to("Success")
        # assert_that(create_csv_paginated).is_equal_to('Success')
        assert_that(create_pdf_record).is_equal_to("Success")


class PdfControllerSpy(pdf.PdfController):

    def create_pdf_manger(self, manger, row_data, filename):
        return "All Success"

    def create_pdf_Serializer(self, candidate, filename):
        return "Success"


class TestCrudOperator(unittest.TestCase):

    def test_crud_operator(self):
        model_double = ModelDouble()
        session_double = SessionDouble()
        crud_operator = dh.CrudOperator(model_double, session_double)
        crud_operator_obj = dh.CrudOperator(ModelDouble, session_double)
        data = [{"name": "karim"}, {"name": "omar"}]
        assert_that(crud_operator.get_all()).is_equal_to("all success")
        assert_that(crud_operator.get_one(1)).is_equal_to("one success")
        assert_that(crud_operator_obj.post_list(data)).is_equal_to(
            [{"name": "karim"}, {"name": "omar"}]
        )
        assert_that(crud_operator_obj.post_list(data[0])).is_equal_to({"name": "karim"})


class ModelDouble:

    def __init__(self, data=None):
        self.data = data

    @property
    def query(self):
        return self

    def all(self):
        return "all success"

    def get(self, id):
        return "one success"


class SessionDouble:

    def get(self, model, id):
        return "one success"

    def add(self, new_candidate):
        pass

    def commit(self):
        pass


class TestDatabaseHandler(unittest.TestCase):
    def test_data_handler(self):

        data_handler_double = DatabaseHandlerDouble()
        with self.assertRaises(ex._NotFoundError) as get_all_exc:
            dh.database_handle(data_handler_double).get_all()
        assert_that(str(get_all_exc.exception)).is_equal_to("Records does not exist")
        with self.assertRaises(ex._NotFoundError) as paginated_exc:
            dh.database_handle(data_handler_double).get_paginated_for_test()
        assert_that(str(paginated_exc.exception)).is_equal_to("No Records in this Page")
        with self.assertRaises(ex._NotFoundError) as get_exc:
            dh.database_handle(data_handler_double).get(100)
        assert_that(str(get_exc.exception)).is_equal_to("Record does not exist")
        with self.assertRaises(ex._InvalidInputError) as post_all_data_types_exc:
            dh.database_handle(data_handler_double).post_all_data_types(())
        assert_that(str(post_all_data_types_exc.exception)).is_equal_to(
            "invalid input, only accept dict data or list of dicts"
        )


class DatabaseHandlerDouble:
    def get_all(self):
        pass

    def get_paginated(self, page, per_page):
        return self

    @property
    def items(self):
        pass

    def get_one(self, id):
        pass

    def post_list(self, request_body):
        pass

    def post_one(self, request_body):
        pass


class TestValidator(unittest.TestCase):
    def test_validator(self):
        required_input_error_double = RequiredInputError({"name": "ahmed"})
        invalid_input_error_double = InvalidInputError({"name": 4})
        with self.assertRaises(ex._RequiredInputError) as exc:
            vd._DataValidator(required_input_error_double)._All_validate()
        with self.assertRaises(ex._InvalidInputError) as ec:
            vd._DataValidator(invalid_input_error_double)._All_validate()
        assert_that(str(exc.exception)).is_equal_to("Name is required")
        assert_that(str(ec.exception)).is_equal_to("Name is not valid string")


class RequiredInputError:
    def __init__(self, user_request):
        self.user_request = user_request

    def get(self, item):
        pass


class InvalidInputError:
    def __init__(self, user_request):
        self.user_request = user_request

    def get(self, item):
        return self.user_request[item]


class TestSerializer(unittest.TestCase):

    def test_serializer(self):
        user = {
            "id": 1,
            "name": "ahmed",
            "email": "ahmed@gmail.com",
            "compatibility": 22,
            "sourcing": "internal-hiring",
            "status": "Rejected",
        }

        serializer_double = SerializerDouble(user)
        serializer_test = sr._DataSerializer(
            serializer_double, "success"
        )._All_serialize()
        assert_that(serializer_test["id"]).is_equal_to(1)
        assert_that(serializer_test["name"]).is_equal_to("ahmed")
        assert_that(serializer_test["email"]).is_equal_to("ahmed@gmail.com")
        assert_that(serializer_test["compatibility"]).is_equal_to(22)
        assert_that(serializer_test["sourcing"]).is_equal_to("internal-hiring")
        assert_that(serializer_test["status"]).is_equal_to("Rejected")
        assert_that(serializer_test["filename"]).is_equal_to("success")
        serializer_double.assert_that_id_called_with(1)
        serializer_double.assert_that_name_called_with("ahmed")
        serializer_double.assert_that_email_called_with("ahmed@gmail.com")
        serializer_double.assert_that_compatibility_called_with(22)
        serializer_double.assert_that_sourcing_called_with("internal-hiring")
        serializer_double.assert_that_status_called_with("Rejected")


class SerializerDouble:
    def __init__(self, user):
        self.given_user = user
        self.id = self.given_user["id"]
        self.name = self.given_user["name"]
        self.email = self.given_user["email"]
        self.compatibility = self.given_user["compatibility"]
        self.sourcing = self.given_user["sourcing"]
        self.status = self.given_user["status"]

    def name(self, name):
        self.given_user["name"] = name

    def email(self, email):
        self.given_user["email"] = email

    def compatibility(self, compatibility):
        self.given_user["compatibility"] = compatibility

    def sourcing(self, sourcing):
        self.given_user["sourcing"] = sourcing

    def status(self, status):
        self.given_user["status"] = status

    def assert_that_id_called_with(self, id):
        assert_that(self.given_user["id"]).is_equal_to(id)

    def assert_that_name_called_with(self, name):
        assert_that(self.given_user["name"]).is_equal_to(name)

    def assert_that_email_called_with(self, email):
        assert_that(self.given_user["email"]).is_equal_to(email)

    def assert_that_compatibility_called_with(self, compatibility):
        assert_that(self.given_user["compatibility"]).is_equal_to(compatibility)

    def assert_that_sourcing_called_with(self, sourcing):
        assert_that(self.given_user["sourcing"]).is_equal_to(sourcing)

    def assert_that_status_called_with(self, status):
        assert_that(self.given_user["status"]).is_equal_to(status)


class TestError(unittest.TestCase):

    def test_read(self):
        error = writer.Error()
        result = error.read("filename")
        assert_that(result).is_equal_to("success")

    def test_write_raise_exception(self):
        error = writer.Error()
        with self.assertRaises(writer._NotImplementError) as exc:
            error.write_export_files("data", "filename")
        assert_that(str(exc.exception)).is_equal_to(
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
        creator = excel.ExcelCreator()
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


if __name__ == "__main__":
    unittest.main()

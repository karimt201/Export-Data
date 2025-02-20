import exceptions
import openpyxl as wb
import csv
import reportlab.platypus as platypus
import reportlab.lib as lib
import reportlab.lib.pagesizes as pagesizes

class DataWriter:
    def write_export_files(self, data, filename):
        raise exceptions._NotImplementError("children must implement this method")


class ExcelCreator(DataWriter):

    def __init__(self, test_excel_writer=None):
        self.wb = test_excel_writer or wb.Workbook()

    def write_export_files(self, data, filename):
        ws = self.wb.active
        ws.append(data.header)
        for row in data.rows:
            ws.append(row)
        return self.wb.save(filename)


class CSVCreator(DataWriter):

    def __init__(self, test_csv_writer=None):
        self.test_csv_writer = test_csv_writer or csv

    def write_export_files(self, data, filename):

        with open(filename, "w", newline="") as csv_file:
            wr = self.test_csv_writer.writer(csv_file)
            wr.writerow(data.header)
            wr.writerows(data.rows)

        return filename

class PDFCreator(DataWriter):

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

class RowExcelData:

    def __init__(self, data):
        self._data = data

    @property
    def header(self):
        return list(self._data and self._data[0].keys())

    @property
    def rows(self):
        return [list(row.values()) for row in self._data]


class DataManger:

    def __init__(self, writer: DataWriter):
        self.writer = writer

    def save(self, data, filename):
        return self.writer.write_export_files(data, filename)

import flask as flask
import controllers.pdf as pdf

pdf_blp = flask.Blueprint("pdf",__name__)

@pdf_blp.route('/pdf', methods=['GET'])
def create_pdf():
  return pdf.PdfController().create_pdf()

@pdf_blp.route('/pdf/', methods=['GET'])
def create_pdf_paginated():
  return pdf.PdfController().create_pdf_paginated()
  
@pdf_blp.route('/pdf/<int:candidates_id>', methods=['GET'])
def create_pdf_record(candidates_id):
  return pdf.PdfController().create_pdf_record(candidates_id)
    
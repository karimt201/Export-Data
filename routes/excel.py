import flask as flask
import controllers.excel as excel

excel_blp = flask.Blueprint("excel", __name__)


@excel_blp.route("/excel", methods=["GET"])
def create_excel():
    return excel.ExcelController().create_excel()


@excel_blp.route("/excel/", methods=["GET"])
def create_excel_pagenited():
    return excel.ExcelController().create_excel_pagenited()


@excel_blp.route("/excel/<int:candidate_id>", methods=["GET"])
def create_excel_record(candidate_id):
    return excel.ExcelController().create_excel_record(candidate_id)

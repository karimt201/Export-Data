import flask as flask
import controllers.csv as csv

csv_blp = flask.Blueprint("csv", __name__)


@csv_blp.route("/csv", methods=["GET"])
def create_csv():
    return csv.CsvController().create_csv()


@csv_blp.route("/csv/", methods=["GET"])
def create_csv_paginated():
    return csv.CsvController().create_csv_paginated()


@csv_blp.route("/csv/<int:candidate_id>", methods=["GET"])
def create_csv_record(candidate_id):
    return csv.CsvController().create_csv_record(candidate_id)

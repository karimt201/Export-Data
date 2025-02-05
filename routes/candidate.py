import flask as flask
import controllers.candidate as candidate

candidate_blp = flask.Blueprint("candidate", __name__)


@candidate_blp.route("/candidate?operation=pdf", methods=["POST"])
def candidate_creator():
    return candidate.PostCandidateController().candidate_creator()


@candidate_blp.route("/candidate?operation=<operation>", methods=["POST"])
def candidate_creator(operation):
    return candidate.CreateCandidateController(operation).create()


@candidate_blp.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    return candidate.GetCandidateController().get_candidate(candidate_id)


@candidate_blp.route("/candidate", methods=["GET"])
def get_all_candidates():
    return candidate.AllCandidateController().get_all_candidates()


@candidate_blp.route("/candidate/", methods=["GET"])
def get_all_candidates_paginated():
    return candidate.AllPaginatedCandidateController().get_all_candidates_paginated()


import flask as flask
import controllers.candidate as candidate

candidate_blp = flask.Blueprint("candidate", __name__)


@candidate_blp.route("/candidate", methods=["POST"])
def candidate_creator():
    return candidate.CandidateController().candidate_creator()


@candidate_blp.route("/candidate", methods=["GET"])
def get_all_candidates():
    return candidate.CandidateController().get_all_candidates()


@candidate_blp.route("/candidate/", methods=["GET"])
def get_all_candidates_paginated():
    return candidate.CandidateController().get_all_candidates_paginated()


@candidate_blp.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    return candidate.CandidateController().get_candidate(candidate_id)

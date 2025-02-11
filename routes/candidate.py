import flask as flask
import controllers.candidate as candidate


candidate_blp = flask.Blueprint("candidate", __name__)

@candidate_blp.route("/candidates", methods=["POST"])
def all_candidate_export():
    return candidate._CandidateController().create()


# @candidate_blp.route("/candidates/<int:candidate_id>", methods=["POST"])
# def all_candidate_export(candidate_id):
#     return candidate._CandidateController().create()

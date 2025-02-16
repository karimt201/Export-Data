import flask as flask
import controllers.candidate as candidate


candidate_blp = flask.Blueprint("candidate", __name__)

@candidate_blp.route("/candidates", methods=["POST"])
def all_candidate_export():
    return candidate._CandidateController().create()


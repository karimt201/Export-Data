import flask as flask
import controllers.candidate as candidate
import controllers.candidate_info as candidate_info


candidate_blp = flask.Blueprint("candidate", __name__)

@candidate_blp.route("/candidate", methods=["POST"])
def all_candidate_export():
    return candidate._CandidateController().create()

@candidate_blp.route("/candidate/skills", methods=["POST"])
def add_candidate_skill():
    return candidate_info._AddCandidateSkillsController().add()

@candidate_blp.route("/candidate/education", methods=["POST"])
def add_candidate_education():
    return candidate_info._AddCandidateEducationController().add()

@candidate_blp.route("/candidate/experience", methods=["POST"])
def add_candidate_experience():
    return candidate_info._AddCandidateExperienceController().add()

@candidate_blp.route("/candidate/application", methods=["POST"])
def add_candidate_application():
    return candidate_info._AddCandidateApplicationController().add()


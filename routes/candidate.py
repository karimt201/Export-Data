import flask as flask
import controllers.export_candidate as export_candidate
import controllers.candidate_info as candidate_info


candidate_blp = flask.Blueprint("candidate", __name__)

@candidate_blp.route("/export/candidates", methods=["POST"])
def all_candidate_export():
    return export_candidate.ExportAllCandidateController(flask.request).export_all_records()

@candidate_blp.route("/export/candidate", methods=["POST"])
def candidate_export():
    return export_candidate.ExportCandidateController(flask.request).export_record()

@candidate_blp.route("/candidates", methods=["POST"])
def add_candidate():
    return candidate_info.AddCandidateController(flask.request).create()

@candidate_blp.route("/candidates", methods=["GET"])
def get_all_candidate():
    return candidate_info.ReadAllCandidateController(flask.request).get_all()

@candidate_blp.route("/candidates/<int:candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    return candidate_info.ReadCandidateController(flask.request).get(candidate_id)

@candidate_blp.route("/candidates/<int:candidate_id>", methods=["PUT"])
def update_candidate(candidate_id):
    return candidate_info.UpdateCandidateController(flask.request).update(candidate_id)

@candidate_blp.route("/candidates/<int:candidate_id>", methods=["DELETE"])
def delete_candidate(candidate_id):
    return candidate_info.DeleteCandidateController(flask.request).delete(candidate_id)

@candidate_blp.route("/candidates/skills", methods=["POST"])
def add_candidate_skill():
    return candidate_info.AddCandidateSkillsController(flask.request).create()

@candidate_blp.route("/candidates/skills", methods=["GET"])
def get_all_candidate_skills():
    return candidate_info.ReadAllCandidateSkillsController(flask.request).get_all()

@candidate_blp.route("/candidates/skills/<int:skills_id>", methods=["GET"])
def get_candidate_skill(skills_id):
    return candidate_info.ReadCandidateSkillsController(flask.request).get(skills_id)

@candidate_blp.route("/candidates/skills/<int:skills_id>", methods=["PUT"])
def update_candidate_skill(skills_id):
    return candidate_info.UpdateCandidateSkillsController(flask.request).update(skills_id)

@candidate_blp.route("/candidates/skills/<int:skills_id>", methods=["DELETE"])
def delete_candidate_skill(skills_id):
    return candidate_info.DeleteCandidateSkillsController(flask.request).delete(skills_id)

@candidate_blp.route("/candidates/education", methods=["POST"])
def add_candidate_education():
    return candidate_info.AddCandidateEducationController(flask.request).create()

@candidate_blp.route("/candidates/education", methods=["GET"])
def get_all_candidate_education():
    return candidate_info.ReadAllCandidateEducationController(flask.request).get_all()

@candidate_blp.route("/candidates/education/<int:education_id>", methods=["GET"])
def get_candidate_education(education_id):
    return candidate_info.ReadCandidateEducationController(flask.request).get(education_id)

@candidate_blp.route("/candidates/education/<int:education_id>", methods=["PUT"])
def update_candidate_education(education_id):
    return candidate_info.UpdateCandidateEducationController(flask.request).update(education_id)

@candidate_blp.route("/candidates/education/<int:education_id>", methods=["DELETE"])
def delete_candidate_education(education_id):
    return candidate_info.DeleteCandidateEducationController(flask.request).delete(education_id)

@candidate_blp.route("/candidates/experience", methods=["POST"])
def add_candidate_experience():
    return candidate_info.AddCandidateExperienceController(flask.request).create()

@candidate_blp.route("/candidates/experience", methods=["GET"])
def get_all_candidate_experience():
    return candidate_info.ReadAllCandidateExperienceController(flask.request).get_all()

@candidate_blp.route("/candidates/experience/<int:experience_id>", methods=["GET"])
def get_candidate_experience(experience_id):
    return candidate_info.ReadCandidateExperienceController(flask.request).get(experience_id)

@candidate_blp.route("/candidates/experience/<int:experience_id>", methods=["PUT"])
def update_candidate_experience(experience_id):
    return candidate_info.UpdateCandidateExperienceController(flask.request).update(experience_id)

@candidate_blp.route("/candidates/experience/<int:experience_id>", methods=["DELETE"])
def delete_candidate_experience(experience_id):
    return candidate_info.DeleteCandidateExperienceController(flask.request).delete(experience_id)

@candidate_blp.route("/candidates/application", methods=["POST"])
def add_candidate_application():
    return candidate_info.AddCandidateApplicationController(flask.request).create()

@candidate_blp.route("/candidates/application", methods=["GET"])
def get_all_candidate_application():
    return candidate_info.ReadAllCandidateApplicationController(flask.request).get_all()

@candidate_blp.route("/candidates/application/<int:application_id>", methods=["GET"])
def get_candidate_application(application_id):
    return candidate_info.ReadCandidateApplicationController(flask.request).get(application_id)

@candidate_blp.route("/candidates/application/<int:application_id>", methods=["PUT"])
def update_candidate_application(application_id):
    return candidate_info.UpdateCandidateApplicationController(flask.request).update(application_id)

@candidate_blp.route("/candidates/application/<int:application_id>", methods=["DELETE"])
def delete_candidate_application(application_id):
    return candidate_info.DeleteCandidateApplicationController(flask.request).delete(application_id)

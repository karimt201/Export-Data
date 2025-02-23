import flask as flask
import controllers.export_candidate as export_candidate
import controllers.candidate_info as candidate_info


candidate_blp = flask.Blueprint("candidate", __name__)

@candidate_blp.route("/export/candidates", methods=["POST"])
def all_candidate_export():
    return export_candidate.ExportAllCandidateController().export_all_candidate()

@candidate_blp.route("/export/candidate", methods=["POST"])
def candidate_export():
    return export_candidate.ExportCandidateController().export_candidate()

@candidate_blp.route("/candidates", methods=["POST"])
def add_candidate():
    return candidate_info.AddCandidateController().create()

@candidate_blp.route("/candidates", methods=["GET"])
def get_all_candidate():
    return candidate_info.ReadAllCandidateController().get_all()

@candidate_blp.route("/candidates/<int:candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    return candidate_info.ReadCandidateController().get(candidate_id)

@candidate_blp.route("/candidates/<int:candidate_id>", methods=["PUT"])
def update_candidate(candidate_id):
    return candidate_info.UpdateCandidateController().update(candidate_id)

@candidate_blp.route("/candidates/<int:candidate_id>", methods=["DELETE"])
def delete_candidate(candidate_id):
    return candidate_info.DeleteCandidateController().delete(candidate_id)

@candidate_blp.route("/candidates/skills", methods=["POST"])
def add_candidate_skill():
    return candidate_info.AddCandidateSkillsController().create()

@candidate_blp.route("/candidates/skills", methods=["GET"])
def get_all_candidate_skills():
    return candidate_info.ReadAllCandidateSkillsController().get_all()

@candidate_blp.route("/candidates/skills/<int:skills_id>", methods=["GET"])
def get_candidate_skill(skills_id):
    return candidate_info.ReadCandidateSkillsController().get(skills_id)

@candidate_blp.route("/candidates/skills/<int:skills_id>", methods=["PUT"])
def update_candidate_skill(skills_id):
    return candidate_info.UpdateCandidateSkillsController().update(skills_id)

@candidate_blp.route("/candidates/skills/<int:skills_id>", methods=["DELETE"])
def delete_candidate_skill(skills_id):
    return candidate_info.DeleteCandidateSkillsController().delete(skills_id)

@candidate_blp.route("/candidates/education", methods=["POST"])
def add_candidate_education():
    return candidate_info.AddCandidateEducationController().create()

@candidate_blp.route("/candidates/education", methods=["GET"])
def get_all_candidate_education():
    return candidate_info.ReadAllCandidateEducationController().get_all()

@candidate_blp.route("/candidates/education/<int:education_id>", methods=["GET"])
def get_candidate_education(education_id):
    return candidate_info.ReadCandidateEducationController().get(education_id)

@candidate_blp.route("/candidates/education/<int:education_id>", methods=["PUT"])
def update_candidate_education(education_id):
    return candidate_info.UpdateCandidateEducationController().update(education_id)

@candidate_blp.route("/candidates/education/<int:education_id>", methods=["DELETE"])
def delete_candidate_education(education_id):
    return candidate_info.DeleteCandidateEducationController().delete(education_id)

@candidate_blp.route("/candidates/experience", methods=["POST"])
def add_candidate_experience():
    return candidate_info.AddCandidateExperienceController().create()

@candidate_blp.route("/candidates/experience", methods=["GET"])
def get_all_candidate_experience():
    return candidate_info.ReadAllCandidateExperienceController().get_all()

@candidate_blp.route("/candidates/experience/<int:experience_id>", methods=["GET"])
def get_candidate_experience(experience_id):
    return candidate_info.ReadCandidateExperienceController().get(experience_id)

@candidate_blp.route("/candidates/experience/<int:experience_id>", methods=["PUT"])
def update_candidate_experience(experience_id):
    return candidate_info.UpdateCandidateExperienceController().update(experience_id)

@candidate_blp.route("/candidates/experience/<int:experience_id>", methods=["DELETE"])
def delete_candidate_experience(experience_id):
    return candidate_info.DeleteCandidateExperienceController().delete(experience_id)

@candidate_blp.route("/candidates/application", methods=["POST"])
def add_candidate_application():
    return candidate_info._AddCandidateApplicationController().create()

@candidate_blp.route("/candidates/application", methods=["GET"])
def get_all_candidate_application():
    return candidate_info.ReadAllCandidateApplicationController().get_all()

@candidate_blp.route("/candidates/application/<int:application_id>", methods=["GET"])
def get_candidate_application(application_id):
    return candidate_info.ReadCandidateApplicationController().get(application_id)

@candidate_blp.route("/candidates/application/<int:application_id>", methods=["PUT"])
def update_candidate_application(application_id):
    return candidate_info.UpdateCandidateApplicationController().update(application_id)

@candidate_blp.route("/candidates/application/<int:application_id>", methods=["DELETE"])
def delete_candidate_application(application_id):
    return candidate_info.DeleteCandidateApplicationController().delete(application_id)

import flask as flask
import controllers.export_candidate as export_candidate
import controllers.candidate_info as candidate_info


candidate_blp = flask.Blueprint("candidate", __name__)

@candidate_blp.route("/export/candidates", methods=["POST"])
def all_candidate_export():
    return export_candidate._ExportController().export_all_candidate()

@candidate_blp.route("/export/candidate", methods=["POST"])
def candidate_export():
    return export_candidate._ExportController().export_candidate()

@candidate_blp.route("/candidate", methods=["POST"])
def add_candidate():
    return candidate_info._CandidateController().create()

@candidate_blp.route("/candidate", methods=["GET"])
def get_all_candidate():
    return candidate_info._CandidateController().get_all()

@candidate_blp.route("/candidate/<int:candidate_id>", methods=["GET"])
def get_candidate(candidate_id):
    return candidate_info._CandidateController().get(candidate_id)

@candidate_blp.route("/candidate/<int:candidate_id>", methods=["PUT"])
def update_candidate(candidate_id):
    return candidate_info._CandidateController().update(candidate_id)

@candidate_blp.route("/candidate/<int:candidate_id>", methods=["DELETE"])
def delete_candidate(candidate_id):
    return candidate_info._CandidateController().delete(candidate_id)

@candidate_blp.route("/candidate/skills", methods=["POST"])
def add_candidate_skill():
    return candidate_info._CandidateSkillsController().create()

@candidate_blp.route("/candidate/skills", methods=["GET"])
def get_all_candidate_skills():
    return candidate_info._CandidateSkillsController().get_all()

@candidate_blp.route("/candidate/skills/<int:skills_id>", methods=["GET"])
def get_candidate_skill(skills_id):
    return candidate_info._CandidateSkillsController().get(skills_id)

@candidate_blp.route("/candidate/skills/<int:skills_id>", methods=["PUT"])
def update_candidate_skill(skills_id):
    return candidate_info._CandidateSkillsController().update(skills_id)

@candidate_blp.route("/candidate/skills/<int:skills_id>", methods=["DELETE"])
def delete_candidate_skill(skills_id):
    return candidate_info._CandidateSkillsController().delete(skills_id)


@candidate_blp.route("/candidate/education", methods=["POST"])
def add_candidate_education():
    return candidate_info._CandidateEducationController().create()

@candidate_blp.route("/candidate/education", methods=["GET"])
def get_all_candidate_education():
    return candidate_info._CandidateEducationController().get_all()

@candidate_blp.route("/candidate/education/<int:education_id>", methods=["GET"])
def get_candidate_education(education_id):
    return candidate_info._CandidateEducationController().get(education_id)

@candidate_blp.route("/candidate/education/<int:education_id>", methods=["PUT"])
def update_candidate_education(education_id):
    return candidate_info._CandidateEducationController().update(education_id)

@candidate_blp.route("/candidate/education/<int:education_id>", methods=["DELETE"])
def delete_candidate_education(education_id):
    return candidate_info._CandidateEducationController().delete(education_id)

@candidate_blp.route("/candidate/experience", methods=["POST"])
def add_candidate_experience():
    return candidate_info._CandidateExperienceController().create()

@candidate_blp.route("/candidate/experience", methods=["GET"])
def get_all_candidate_experience():
    return candidate_info._CandidateExperienceController().get_all()

@candidate_blp.route("/candidate/experience/<int:experience_id>", methods=["GET"])
def get_candidate_experience(experience_id):
    return candidate_info._CandidateExperienceController().get(experience_id)

@candidate_blp.route("/candidate/experience/<int:experience_id>", methods=["PUT"])
def update_candidate_experience(experience_id):
    return candidate_info._CandidateExperienceController().update(experience_id)

@candidate_blp.route("/candidate/experience/<int:experience_id>", methods=["DELETE"])
def delete_candidate_experience(experience_id):
    return candidate_info._CandidateExperienceController().delete(experience_id)

@candidate_blp.route("/candidate/application", methods=["POST"])
def add_candidate_application():
    return candidate_info._CandidateApplicationController().create()

@candidate_blp.route("/candidate/application", methods=["GET"])
def get_all_candidate_application():
    return candidate_info._CandidateApplicationController().get_all()

@candidate_blp.route("/candidate/application/<int:application_id>", methods=["GET"])
def get_candidate_application(application_id):
    return candidate_info._CandidateApplicationController().get(application_id)

@candidate_blp.route("/candidate/application/<int:application_id>", methods=["PUT"])
def update_candidate_application(application_id):
    return candidate_info._CandidateApplicationController().update(application_id)

@candidate_blp.route("/candidate/application/<int:application_id>", methods=["DELETE"])
def delete_candidate_application(application_id):
    return candidate_info._CandidateApplicationController().delete(application_id)

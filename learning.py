import models
from db import db

session = models.db.session
a = session.query(models.CandidateModel).get(1)  

print(a)

# with a.app.app_context():
#     s = models.CandidateModel.query.all()
#     b = db.session.get(models.CandidateModel, 1)
#     c = models.CandidateModel.query.paginate(page=1,per_page=2)

# for a in c:
#     print(a.name)

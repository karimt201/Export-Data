# import models
# from db import db
# import app as a
# session = models.db.session
# # a = session.query(models.CandidateModel).get(1)  

# # print(a)

# with a.app.app_context():
#     s = models.CandidateModel.query.all()
#     b = models.db.session.get(models.CandidateModel, 1)
#     c = models.CandidateModel.query.paginate(page=1,per_page=2)

# for h in c:
#     print(h.name)
# s = {
#     "a":1,
#     "b":"omar",
#     "c":"ali"
# }
# for key, value in s.items():
#     print(f"this key {key} and this is value {value}")
# class FormBuilder:
#     def __init__(self):
#         self.fields = []

#     def add_text_field(self, name, placeholder=""):
#         self.fields.append(f'Text Field: {name}, Placeholder: {placeholder}')
#         return self  # لتسهيل الـ Chaining (ربط الدوال ببعضها)

#     def add_checkbox(self, name, label=""):
#         self.fields.append(f'Checkbox: {name}, Label: {label}')
#         return self

#     def add_dropdown(self, name, options):
#         self.fields.append(f'Dropdown: {name}, Options: {options}')
#         return self

#     def build(self):
#         return f"Form with fields: {self.fields}"

# # استخدام الـ Builder
# form = (FormBuilder()
#         .add_text_field("username", "Enter your name")
#         .add_checkbox("subscribe", "Subscribe to newsletter")
#         .add_dropdown("gender", ["Male", "Female", "Other"])
#         .build())

# print(form)

# def _filter(self, data):
#         # TODO: Change this to accept only the model attributes using hasattr
#         for attr in data:
#             if hasattr(self.model, attr):
#                 return data

# import jwt
# import datetime

# SECRET_KEY = "my_secret_key"

# payload = {
#     "username" : "karim",
#     "role" : "admin",
#     "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
# }

# token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")

# print( token)
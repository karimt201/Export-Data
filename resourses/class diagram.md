flowchart LR
    %% Interface
    CurdOperation["CurdOperation Interface"]
    Auth["Auth Interface"]
    Export["Export Interface"]

    %% Classes
    _CandidateController["_CandidateController"]
    _AddCandidateBuilder["_AddCandidateBuilder"]
    _UpdateCandidateBuilder["_UpdateCandidateBuilder"]
    _ReadCandidateBuilder["_ReadCandidateBuilder"]
    _ReadAllCandidateBuilder["_ReadAllCandidateBuilder"]
    _DeleteCandidateBuilder["_DeleteCandidateBuilder"]
    _CandidateSkillsController["_CandidateSkillsController"]
    _AddCandidateSkillsBuilder["_AddCandidateSkillsBuilder"]
    _UpdateCandidateSkillsBuilder["_UpdateCandidateSkillsBuilder"]
    _ReadCandidateSkillsBuilder["_ReadCandidateSkillsBuilder"]
    _ReadAllCandidateSkillsBuilder["_ReadAllCandidateSkillsBuilder"]
    _DeleteCandidateSkillsBuilder["_DeleteCandidateSkillsBuilder"]
    _CandidateEducationController["_CandidateEducationController"]
    _AddCandidateEducationBuilder["_AddCandidateEducationBuilder"]
    _UpdateCandidateEducationBuilder["_UpdateCandidateEducationBuilder"]
    _ReadCandidateEducationBuilder["_ReadCandidateEducationBuilder"]
    _ReadAllCandidateEducationBuilder["_ReadAllCandidateEducationBuilder"]
    _DeleteCandidateEducationBuilder["_DeleteCandidateEducationBuilder"]
    _CandidateExperienceController["_CandidateExperienceController"]
    _AddCandidateExperienceBuilder["_AddCandidateExperienceBuilder"]
    _UpdateCandidateExperienceBuilder["_UpdateCandidateExperienceBuilder"]
    _ReadCandidateExperienceBuilder["_ReadCandidateExperienceBuilder"]
    _ReadAllCandidateExperienceBuilder["_ReadAllCandidateExperienceBuilder"]
    _DeleteCandidateExperienceBuilder["_DeleteCandidateExperienceBuilder"]
    _CandidateApplicationController["_CandidateApplicationController"]
    _AddCandidateApplicationBuilder["_AddCandidateApplicationBuilder"]
    _UpdateCandidateApplicationBuilder["_UpdateCandidateApplicationBuilder"]
    _ReadCandidateApplicationBuilder["_ReadCandidateApplicationBuilder"]
    _ReadAllCandidateApplicationBuilder["_ReadAllCandidateApplicationBuilder"]
    _DeleteCandidateApplicationBuilder["_DeleteCandidateApplicationBuilder"]
    _AddCandidateValidator["_AddCandidateValidator"]
    _CandidateBusinessHandler["_CandidateBusinessHandler"]
    _CandidateSerializer["_CandidateSerializer"]
    _TokenValidator["_TokenValidator"]
    _DeleteSerializer["_DeleteSerializer"]
    _AddSkillsValidator["_AddSkillsValidator"]
    _SkillsBusinessHandler["_SkillsBusinessHandler"]
    _SkillsSerializer["_SkillsSerializer"]
    _AddApplicationValidator["_AddApplicationValidator"]
    _ApplicationBusinessHandler["_ApplicationBusinessHandler"]
    _ApplicationSerializer["_ApplicationSerializer"]
    _AddExperienceValidator["_AddExperienceValidator"]
    _ExperienceBusinessHandler["_ExperienceBusinessHandler"]
    _ExperienceSerializer["_ExperienceSerializer"]
    _AddEducationValidator["_AddEducationValidator"]
    _EducationBusinessHandler["_EducationBusinessHandler"]
    _EducationSerializer["_EducationSerializer"]
    CrudOperator["CrudOperator"]
    Token["Token"]
    CandidateModel["CandidateModel"]
    ApplicationModel["ApplicationModel"]
    ExperienceModel["ExperienceModel"]
    EducationModel["EducationModel"]
    SkillModel["SkillModel"]
    _LoginController["_LoginController"]
    _LoginBuilder["_LoginBuilder"]
    _LoginValidator["_LoginValidator"]
    _LoginBusinessHandler["_LoginBusinessHandler"]
    _LoginSerializer["_LoginSerializer"]
    _UserController["_UserController"]
    _AddUserBuilder["_AddUserBuilder"]
    _UserValidator["_UserValidator"]
    _UserBusinessHandler["_UserBusinessHandler"]
    _RegisterSerializer["_RegisterSerializer"]
    _UpdateUserBuilder["_UpdateUserBuilder"]
    _UserSerializer["_UserSerializer"]
    _ReadUserBuilder["_ReadUserBuilder"]
    _ReadAllUserBuilder["_ReadAllUserBuilder"]
    _DeleteUserBuilder["_DeleteUserBuilder"]
    _ExportController["_ExportController"]
    _ExportAllCandidateBuilder["_ExportAllCandidateBuilder"]
    _ExportCandidateBuilder["_ExportCandidateBuilder"]
    _CreateExtensionValidator["_CreateExtensionValidator"]
    _ExtensionCreator["_ExtensionCreator"]
    _ExportCandidateSerializer["_ExportCandidateSerializer"]
    _CreateExtensionBuilder["_CreateExtensionBuilder"]
    ExcelCreator["ExcelCreator"]
    CSVCreator["CSVCreator"]
    PDFCreator["PDFCreator"]
    _DataSerializer["_DataSerializer"]
    RowExcelData["RowExcelData"]
    DataManger["DataManger"]
    
    %% Relationships
    CurdOperation --> _CandidateController
    _CandidateController --> _AddCandidateBuilder
    _AddCandidateBuilder --> _AddCandidateValidator
    _AddCandidateBuilder --> _CandidateBusinessHandler
    _CandidateBusinessHandler --> CrudOperator
    _CandidateBusinessHandler --> CandidateModel
    _CandidateBusinessHandler --> Token
    _AddCandidateBuilder --> _CandidateSerializer
    _CandidateController --> _UpdateCandidateBuilder
    _UpdateCandidateBuilder --> _TokenValidator
    _UpdateCandidateBuilder --> _CandidateBusinessHandler 
    _UpdateCandidateBuilder --> _CandidateSerializer
    _CandidateController --> _ReadAllCandidateBuilder
    _ReadAllCandidateBuilder --> _TokenValidator
    _ReadAllCandidateBuilder --> _CandidateBusinessHandler
    _ReadAllCandidateBuilder --> _CandidateSerializer
    _CandidateController --> _ReadCandidateBuilder
    _ReadCandidateBuilder --> _TokenValidator
    _ReadCandidateBuilder --> _CandidateBusinessHandler
    _ReadCandidateBuilder --> _CandidateSerializer
    _CandidateController --> _DeleteCandidateBuilder
    _DeleteCandidateBuilder--> _TokenValidator
    _DeleteCandidateBuilder--> _CandidateBusinessHandler
    _DeleteCandidateBuilder--> _DeleteSerializer
    CurdOperation --> _CandidateSkillsController
    _CandidateSkillsController --> _AddCandidateSkillsBuilder
    _AddCandidateSkillsBuilder --> _AddSkillsValidator
    _AddCandidateSkillsBuilder --> _SkillsBusinessHandler
    _AddCandidateSkillsBuilder --> _CandidateBusinessHandler
    _SkillsBusinessHandler --> CrudOperator
    _SkillsBusinessHandler --> SkillModel
    _SkillsBusinessHandler --> Token
    _SkillsBusinessHandler --> _CandidateBusinessHandler
    _AddCandidateSkillsBuilder --> _SkillsSerializer
    _CandidateSkillsController --> _UpdateCandidateSkillsBuilder
    _UpdateCandidateSkillsBuilder --> _TokenValidator
    _UpdateCandidateSkillsBuilder --> _SkillsBusinessHandler 
    _UpdateCandidateSkillsBuilder --> _SkillsSerializer
    _CandidateSkillsController --> _ReadCandidateSkillsBuilder
    _ReadCandidateSkillsBuilder --> _TokenValidator
    _ReadCandidateSkillsBuilder --> _SkillsBusinessHandler
    _ReadCandidateSkillsBuilder --> _SkillsSerializer
    _CandidateSkillsController --> _ReadAllCandidateSkillsBuilder
    _ReadAllCandidateSkillsBuilder --> _TokenValidator
    _ReadAllCandidateSkillsBuilder --> _SkillsBusinessHandler
    _ReadAllCandidateSkillsBuilder --> _SkillsSerializer
    _CandidateSkillsController --> _DeleteCandidateSkillsBuilder
    _DeleteCandidateSkillsBuilder--> _TokenValidator
    _DeleteCandidateSkillsBuilder--> _SkillsBusinessHandler
    _DeleteCandidateSkillsBuilder--> _DeleteSerializer
    CurdOperation --> _CandidateEducationController
    _CandidateEducationController --> _AddCandidateEducationBuilder
    _AddCandidateEducationBuilder --> _AddEducationValidator
    _AddCandidateEducationBuilder --> _EducationBusinessHandler
    _EducationBusinessHandler --> CrudOperator
    _EducationBusinessHandler --> EducationModel
    _EducationBusinessHandler --> Token
    _AddCandidateEducationBuilder --> _EducationSerializer
    _CandidateEducationController --> _UpdateCandidateEducationBuilder
    _UpdateCandidateEducationBuilder --> _TokenValidator
    _UpdateCandidateEducationBuilder --> _EducationBusinessHandler 
    _UpdateCandidateEducationBuilder --> _EducationSerializer
    _CandidateEducationController --> _ReadCandidateEducationBuilder
    _ReadCandidateEducationBuilder --> _TokenValidator
    _ReadCandidateEducationBuilder --> _EducationBusinessHandler
    _ReadCandidateEducationBuilder --> _EducationSerializer
    _CandidateEducationController --> _ReadAllCandidateEducationBuilder
    _ReadAllCandidateEducationBuilder --> _TokenValidator
    _ReadAllCandidateEducationBuilder --> _EducationBusinessHandler
    _ReadAllCandidateEducationBuilder --> _EducationSerializer
    _CandidateEducationController --> _DeleteCandidateEducationBuilder
    _DeleteCandidateEducationBuilder --> _TokenValidator
    _DeleteCandidateEducationBuilder --> _EducationBusinessHandler
    _DeleteCandidateEducationBuilder --> _DeleteSerializer
    CurdOperation --> _CandidateExperienceController
    _CandidateExperienceController --> _AddCandidateExperienceBuilder
    _AddCandidateExperienceBuilder --> _AddExperienceValidator
    _AddCandidateExperienceBuilder --> _ExperienceBusinessHandler
    _ExperienceBusinessHandler --> CrudOperator
    _ExperienceBusinessHandler --> ExperienceModel
    _ExperienceBusinessHandler --> Token
    _AddCandidateExperienceBuilder --> _ExperienceSerializer
    _CandidateExperienceController --> _UpdateCandidateExperienceBuilder
    _UpdateCandidateExperienceBuilder --> _TokenValidator
    _UpdateCandidateExperienceBuilder --> _ExperienceBusinessHandler 
    _UpdateCandidateExperienceBuilder --> _ExperienceSerializer
    _CandidateExperienceController --> _ReadCandidateExperienceBuilder
    _ReadCandidateExperienceBuilder --> _TokenValidator
    _ReadCandidateExperienceBuilder --> _ExperienceBusinessHandler
    _ReadCandidateExperienceBuilder --> _ExperienceSerializer
    _CandidateExperienceController --> _ReadAllCandidateExperienceBuilder
    _ReadAllCandidateExperienceBuilder --> _TokenValidator
    _ReadAllCandidateExperienceBuilder --> _ExperienceBusinessHandler
    _ReadAllCandidateExperienceBuilder --> _ExperienceSerializer
    _CandidateExperienceController --> _DeleteCandidateExperienceBuilder
    _DeleteCandidateExperienceBuilder --> _TokenValidator
    _DeleteCandidateExperienceBuilder --> _ExperienceBusinessHandler
    _DeleteCandidateExperienceBuilder --> _DeleteSerializer
    CurdOperation --> _CandidateApplicationController
    _CandidateApplicationController --> _AddCandidateApplicationBuilder
    _AddCandidateApplicationBuilder --> _AddApplicationValidator
    _AddCandidateApplicationBuilder --> _ApplicationBusinessHandler
    _ApplicationBusinessHandler --> CrudOperator
    _ApplicationBusinessHandler --> ApplicationModel
    _ApplicationBusinessHandler --> Token
    _AddCandidateApplicationBuilder --> _ApplicationSerializer
    _CandidateApplicationController --> _UpdateCandidateApplicationBuilder
    _UpdateCandidateApplicationBuilder --> _TokenValidator
    _UpdateCandidateApplicationBuilder --> _ApplicationBusinessHandler 
    _UpdateCandidateApplicationBuilder --> _ApplicationSerializer
    _CandidateApplicationController --> _ReadCandidateApplicationBuilder
    _ReadCandidateApplicationBuilder --> _TokenValidator
    _ReadCandidateApplicationBuilder --> _ApplicationBusinessHandler
    _ReadCandidateApplicationBuilder --> _ApplicationSerializer
    _CandidateApplicationController --> _ReadAllCandidateApplicationBuilder
    _ReadAllCandidateApplicationBuilder --> _TokenValidator
    _ReadAllCandidateApplicationBuilder --> _ApplicationBusinessHandler
    _ReadAllCandidateApplicationBuilder --> _ApplicationSerializer
    _CandidateApplicationController --> _DeleteCandidateApplicationBuilder
    _DeleteCandidateApplicationBuilder --> _TokenValidator
    _DeleteCandidateApplicationBuilder --> _ApplicationBusinessHandler
    _DeleteCandidateApplicationBuilder --> _DeleteSerializer
    CurdOperation --> _UserController
    _UserController --> _AddUserBuilder
    _AddUserBuilder --> _UserValidator
    _AddUserBuilder --> _UserBusinessHandler
    _UserBusinessHandler --> CrudOperator
    _UserBusinessHandler --> UserModel
    _UserBusinessHandler --> Token
    _AddUserBuilder --> _RegisterSerializer
    _UserController --> _UpdateUserBuilder
    _UpdateUserBuilder --> _TokenValidator
    _UpdateUserBuilder --> _UserBusinessHandler 
    _UpdateUserBuilder --> _UserSerializer
    _UserController --> _ReadUserBuilder
    _ReadUserBuilder --> _TokenValidator
    _ReadUserBuilder --> _UserBusinessHandler
    _ReadUserBuilder --> _UserSerializer
    _UserController --> _ReadAllUserBuilder
    _ReadAllUserBuilder --> _TokenValidator
    _ReadAllUserBuilder --> _UserBusinessHandler
    _ReadAllUserBuilder --> _UserSerializer
    _UserController --> _DeleteUserBuilder
    _DeleteUserBuilder --> _TokenValidator
    _DeleteUserBuilder --> _UserBusinessHandler
    _DeleteUserBuilder --> _DeleteSerializer
    Auth --> _LoginController
    _LoginController --> _LoginBuilder
    _LoginBuilder --> _LoginValidator
    _LoginBuilder --> _LoginBusinessHandler
    _LoginBusinessHandler --> CrudOperator
    _LoginBusinessHandler --> UserModel
    _LoginBuilder --> _LoginSerializer
    Export --> _ExportController
    _ExportController --> _ExportCandidateBuilder
    _ExportController --> _ExportAllCandidateBuilder
    _ExportCandidateBuilder --> _CreateExtensionValidator
    _ExportCandidateBuilder --> _ExtensionCreator
    _ExtensionCreator --> PDFCreator
    _ExtensionCreator --> CSVCreator
    _ExtensionCreator --> ExcelCreator
    _ExtensionCreator --> _CreateExtensionBuilder
    _CreateExtensionBuilder --> _DataSerializer
    _CreateExtensionBuilder --> RowExcelData
    _CreateExtensionBuilder --> DataManger
    _ExportCandidateBuilder --> _ExportCandidateSerializer
    _ExportAllCandidateBuilder --> _CreateExtensionValidator
    _ExportAllCandidateBuilder --> _ExtensionCreator
    _ExportAllCandidateBuilder --> _ExportCandidateSerializer

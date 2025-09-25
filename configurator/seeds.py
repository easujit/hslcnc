
FORM_VISIT_OPD={"kind":"form","name":"visit_opd","fields":[
 {"id":"height_cm","label":"Height (cm)","type":"number","required":True,"min":50,"max":250},
 {"id":"weight_kg","label":"Weight (kg)","type":"number","required":True,"min":2,"max":400},
 {"id":"hba1c","label":"HbA1c (%)","type":"number","required":True,"min":0,"max":20,"step":0.1},
 {"id":"bmi","label":"BMI","type":"number","readOnly":True,"visible":True},
 {"id":"book_educator","label":"Book Diabetes Educator session","type":"boolean","visible":False},
]}
RULES_VISIT_OPD={"kind":"rule","name":"visit_opd_rules","rules":[
 {"when":"height_cm and weight_kg","then":[{"set_field":{"id":"bmi","expr":"round(weight_kg / ((height_cm/100)**2), 1)"}}]},
 {"when":"hba1c is not None and hba1c >= 9","then":[{"set_visibility":{"id":"book_educator","visible":True}},{"banner":{"level":"warning","text":"High HbA1c — consider educator session"}}]},
]}
WORKFLOW_VISIT_OPD={"kind":"workflow","name":"high_hba1c_followup","trigger":{"on":"submit","form":"visit_opd"},"if":"hba1c is not None and hba1c >= 9","do":[
 {"notify":{"channel":"endocrinology_on_call","message":"High HbA1c ({{hba1c}}%) for patient {{patient_id}}"}},
 {"create_task":{"team":"diabetes_education","summary":"Schedule educator session","details":"HbA1c={{hba1c}}","due_in_days":7}}]}

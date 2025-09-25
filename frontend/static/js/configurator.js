
const formName="visit_opd";
async function getJSON(u){const r=await fetch(u);return r.json();}
async function postJSON(u,d){const r=await fetch(u,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(d)});return r.json();}
document.getElementById("loadForm").onclick=async()=>{
  const data=await getJSON(`/api/config/effective/form/${formName}/`);
  document.getElementById("formJson").value=JSON.stringify(data.spec,null,2);
};
document.getElementById("addField").onclick=()=>{
  let txt=document.getElementById("formJson").value.trim();
  let json=txt?JSON.parse(txt):{"kind":"form","name":formName,"fields":[]};
  json.fields=json.fields||[];
  json.fields.push({id:document.getElementById("f_id").value.trim(),label:document.getElementById("f_label").value.trim(),type:document.getElementById("f_type").value,required:document.getElementById("f_required").checked});
  document.getElementById("formJson").value=JSON.stringify(json,null,2);
};
document.getElementById("publishForm").onclick=async()=>{
  const body=JSON.parse(document.getElementById("formJson").value||"{}");
  const res=await postJSON(`/api/config/publish/form/${formName}/`, body);
  alert("Form published. Version "+res.version);
};
function renderRuleParams(){
  const sel=document.getElementById("r_action").value;
  const box=document.getElementById("r_params");
  if(sel==="set_field"){box.innerHTML=`Field ID <input id="ra_id" size="12"/> Expr <input id="ra_expr" size="26" placeholder="round(weight_kg / ((height_cm/100)**2), 1)"/>`;}
  else if(sel==="set_visibility"){box.innerHTML=`Field ID <input id="ra_id" size="12"/> Visible <select id="ra_visible"><option>true</option><option>false</option></select>`;}
  else{box.innerHTML=`Text <input id="ra_text" size="40" placeholder="High HbA1c — consider educator session"/>`;}
}
document.getElementById("r_action").onchange=renderRuleParams; renderRuleParams();
document.getElementById("loadRules").onclick=async()=>{
  const data=await getJSON(`/api/config/effective/rules/${formName}/`);
  document.getElementById("rulesJson").value=JSON.stringify(data.spec,null,2);
};
document.getElementById("addRule").onclick=()=>{
  let txt=document.getElementById("rulesJson").value.trim();
  let json=txt?JSON.parse(txt):{"kind":"rule","name":formName+"_rules","rules":[]};
  json.rules=json.rules||[];
  const when=document.getElementById("r_when").value;
  const sel=document.getElementById("r_action").value;
  let action;
  if(sel==="set_field"){action={"set_field":{"id":document.getElementById("ra_id").value,"expr":document.getElementById("ra_expr").value}};}
  else if(sel==="set_visibility"){action={"set_visibility":{"id":document.getElementById("ra_id").value,"visible":document.getElementById("ra_visible").value==="true"}};}
  else{action={"banner":{"level":"warning","text":document.getElementById("ra_text").value}};}
  json.rules.push({"when":when,"then":[action]});
  document.getElementById("rulesJson").value=JSON.stringify(json,null,2);
};
document.getElementById("publishRules").onclick=async()=>{
  const body=JSON.parse(document.getElementById("rulesJson").value||"{}");
  const res=await postJSON(`/api/config/publish/rules/${formName}/`, body);
  alert("Rules published. Version "+res.version);
};
document.getElementById("loadWorkflow").onclick=async()=>{
  const data=await getJSON(`/api/config/effective/workflow/high_hba1c_followup/`);
  document.getElementById("workflowJson").value=JSON.stringify(data.spec,null,2);
};
document.getElementById("publishWorkflow").onclick=async()=>{
  let spec={};
  try{spec=JSON.parse(document.getElementById("workflowJson").value);}catch{
    spec={"kind":"workflow","name":"high_hba1c_followup","trigger":JSON.parse(document.getElementById("w_trigger").value),"if":document.getElementById("w_if").value,"do":JSON.parse(document.getElementById("w_do").value)};
  }
  const res=await postJSON(`/api/config/publish/workflow/high_hba1c_followup/`, spec);
  alert("Workflow published. Version "+res.version);
};

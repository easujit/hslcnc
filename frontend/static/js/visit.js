
const formName="visit_opd";
function uuidv4(){return'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g,function(c){const r=Math.random()*16|0,v=c==='x'?r:(r&0x3|0x8);return v.toString(16);});}
async function evaluate(){
  const values={height_cm:parseFloat(document.getElementById("height_cm").value)||null,weight_kg:parseFloat(document.getElementById("weight_kg").value)||null,hba1c:parseFloat(document.getElementById("hba1c").value)||null,book_educator:document.getElementById("book_educator").checked};
  const res=await fetch(`/api/runtime/rules/evaluate/${formName}/`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({values})});
  const data=await res.json();
  (data.setField||[]).forEach(sf=>{if(sf.id==="bmi") document.getElementById("bmi").value=sf.value??"";});
  let visible=false; (data.visibility||[]).forEach(v=>{if(v.id==="book_educator") visible=v.visible;});
  document.getElementById("book_ed_wrap").style.display=visible?"block":"none";
  document.getElementById("warnings").textContent=(data.warnings||[]).join(" | ");
}
["height_cm","weight_kg","hba1c","book_educator"].forEach(id=>document.getElementById(id).addEventListener("input", evaluate));
document.getElementById("submitBtn").onclick=async()=>{
  const idem=uuidv4();
  const payload={patient_id:document.getElementById("patient_id").value||"P123",values:{height_cm:parseFloat(document.getElementById("height_cm").value)||null,weight_kg:parseFloat(document.getElementById("weight_kg").value)||null,hba1c:parseFloat(document.getElementById("hba1c").value)||null,book_educator:document.getElementById("book_educator").checked}};
  const res=await fetch(`/api/submit/forms/${formName}/submit/`,{method:"POST",headers:{"Content-Type":"application/json","Idempotency-Key":idem},body:JSON.stringify(payload)});
  const data=await res.json();
  if(res.ok){document.getElementById("submitStatus").textContent=`Saved visit ${data.visit_id}. Warnings: ${(data.warnings||[]).join(",")}`;}
  else{document.getElementById("submitStatus").textContent=`Error: ${JSON.stringify(data)}`;}
};
evaluate();


async function loadVisits(){
  const r = await fetch('/api/clinical/visits/');
  const data = await r.json();
  const tbody = document.querySelector('#visitsTbl tbody');
  tbody.innerHTML = '';
  data.forEach(v => {
    const tr = document.createElement('tr');
    const cd = v.custom_data || {};
    tr.innerHTML = `<td>${v.id}</td><td>${v.patient}</td><td>${v.created_at}</td>
      <td>${cd.height_cm ?? ""}</td><td>${cd.weight_kg ?? ""}</td><td>${cd.bmi ?? ""}</td>
      <td>${cd.hba1c ?? ""}</td><td>${cd.book_educator ? "Yes" : ""}</td>`;
    tbody.appendChild(tr);
  });
}
document.getElementById('refresh').onclick = loadVisits;
loadVisits();

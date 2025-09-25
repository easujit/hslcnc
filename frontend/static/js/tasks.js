
async function loadTasks(){
  const r = await fetch('/api/orchestrator/tasks/');
  const data = await r.json();
  const tbody = document.querySelector('#tasksTbl tbody');
  tbody.innerHTML = '';
  data.forEach(t => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${t.id}</td><td>${t.team}</td><td>${t.summary}</td><td>${t.details}</td>
      <td>${t.due_at}</td><td>${t.status}</td><td>${t.created_at}</td>`;
    tbody.appendChild(tr);
  });
}
async function processEvents(){
  await fetch('/api/orchestrator/process-now/', {method:'POST'});
  await loadTasks();
}
document.getElementById('refresh').onclick = loadTasks;
document.getElementById('process').onclick = processEvents;
loadTasks();

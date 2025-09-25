
async function loadNotifications(){
  const r = await fetch('/api/orchestrator/notifications/');
  const data = await r.json();
  const tbody = document.querySelector('#notifTbl tbody');
  tbody.innerHTML = '';
  data.forEach(n => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>${n.id}</td><td>${n.channel}</td><td>${n.message}</td><td>${n.status}</td><td>${n.created_at}</td>`;
    tbody.appendChild(tr);
  });
}
async function processEvents(){
  await fetch('/api/orchestrator/process-now/', {method:'POST'});
  await loadNotifications();
}
document.getElementById('refresh').onclick = loadNotifications;
document.getElementById('process').onclick = processEvents;
loadNotifications();

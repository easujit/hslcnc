export async function api(path, opts={}){
  const res = await fetch('/api'+path, {
    ...opts,
    headers: { 'Content-Type': 'application/json', ...(opts.headers || {}) },
    body: opts.body ? JSON.stringify(opts.body) : undefined
  })
  if(!res.ok){
    const txt = await res.text()
    throw new Error(txt || res.statusText)
  }
  return res.json()
}

export function makeIdemKey(){
  return 'idem-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2)
}
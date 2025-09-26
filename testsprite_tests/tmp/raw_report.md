
# TestSprite AI Testing Report(MCP)

---

## 1️⃣ Document Metadata
- **Project Name:** hospital_lcnc
- **Date:** 2025-09-27
- **Prepared by:** TestSprite AI Team

---

## 2️⃣ Requirement Validation Summary

#### Test TC001
- **Test Name:** User Login and Dashboard Access
- **Test Code:** [TC001_User_Login_and_Dashboard_Access.py](./TC001_User_Login_and_Dashboard_Access.py)
- **Test Error:** Login validation error blocks testing. The username 'sk' is not accepted as a valid email address. Testing cannot proceed further until this is resolved.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
[ERROR] Failed to load patients: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>ValueError
          at /api/clinical/patients/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>ValueError
       at /api/clinical/patients/</h1>
  <pre class="exception_value">signal only works in main thread of the main interpreter</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/clinical/patients/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>ValueError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>signal only works in main thread of the main interpreter</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</span>, line 58, in signal</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>clinical.views.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 01:57:00 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4345979136">
              
                <ol start="48" class="pre-context" id="pre4345979136">
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4345979136">
                  
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4345979136', 'post4345979136')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345979136">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4345971072">
              
                <ol start="190" class="pre-context" id="pre4345971072">
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4345971072">
                  
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345971072', 'post4345971072')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345971072">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4345977152">
              
                <ol start="49" class="pre-context" id="pre4345977152">
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4345977152">
                  
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4345977152', 'post4345977152')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345977152">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da82c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4346663744">
              
                <ol start="98" class="pre-context" id="pre4346663744">
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4346663744">
                  
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4346663744', 'post4346663744')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346663744">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;clinical.views.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x103013890&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4345985856">
              
                <ol start="502" class="pre-context" id="pre4345985856">
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4345985856">
                  
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4345985856', 'post4345985856')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345985856">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x103013890&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x103013890&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4345980288">
              
                <ol start="462" class="pre-context" id="pre4345980288">
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4345980288">
                  
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4345980288', 'post4345980288')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345980288">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,
 &#x27;view&#x27;: &lt;clinical.views.WrappedAPIView object at 0x103013890&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x103013890&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4345981632">
              
                <ol start="473" class="pre-context" id="pre4345981632">
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4345981632">
                  
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4345981632', 'post4345981632')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345981632">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x103013890&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4345979008">
              
                <ol start="499" class="pre-context" id="pre4345979008">
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4345979008">
                  
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345979008', 'post4345979008')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345979008">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x103013890&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x103013890&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4345984256">
              
                <ol start="43" class="pre-context" id="pre4345984256">
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4345984256">
                  
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4345984256', 'post4345984256')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345984256">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function with_timeout.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102da8400&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x103013890&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py</code>, line 27, in wrapper
          

          
            <div class="context" id="c4345978880">
              
                <ol start="20" class="pre-context" id="pre4345978880">
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>def timeout_handler(signum, frame):</pre></li>
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>    raise TimeoutError(&quot;Operation timed out&quot;)</pre></li>
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>def with_timeout(seconds=30):</pre></li>
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>    def decorator(func):</pre></li>
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>        def wrapper(*args, **kwargs):</pre></li>
                
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>            # Set the signal handler</pre></li>
                
                </ol>
              
              <ol start="27" class="context-line">
                <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='28' class="post-context" id="post4345978880">
                  
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>            signal.alarm(seconds)</pre></li>
                  
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>            </pre></li>
                  
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>            try:</pre></li>
                  
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>                result = func(*args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>                return result</pre></li>
                  
                  <li onclick="toggle('pre4345978880', 'post4345978880')"><pre>            finally:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345978880">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function patients_list at 0x102da8360&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>seconds</td>
                    <td class="code"><pre>30</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</code>, line 58, in signal
          

          
            <div class="context" id="c4346407616">
              
                <ol start="51" class="pre-context" id="pre4346407616">
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>    def decorator(wrapper):</pre></li>
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>        wrapper.__doc__ = wrapped.__doc__</pre></li>
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>        return wrapper</pre></li>
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>    return decorator</pre></li>
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>@_wraps(_signal.signal)</pre></li>
                
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>def signal(signalnum, handler):</pre></li>
                
                </ol>
              
              <ol start="58" class="context-line">
                <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='59' class="post-context" id="post4346407616">
                  
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>    return _int_to_enum(handler, Handlers)</pre></li>
                  
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>@_wraps(_signal.getsignal)</pre></li>
                  
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>def getsignal(signalnum):</pre></li>
                  
                  <li onclick="toggle('pre4346407616', 'post4346407616')"><pre>    handler = _signal.getsignal(signalnum)</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346407616">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;function timeout_handler at 0x102d63e20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>signalnum</td>
                    <td class="code"><pre>&lt;Signals.SIGALRM: 14&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="ValueError at /api/clinical/patients/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://127.0.0.1:8000/api/clinical/patients/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py", line 27, in wrapper
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py", line 58, in signal
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exception Type: ValueError at /api/clinical/patients/
Exception Value: signal only works in main thread of the main interpreter
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/consent&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/clinical/patients/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;GET&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x1031747f0&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async loadPatients (http://localhost:5174/src/pages/ConsentManagement.jsx:70:20) (at http://localhost:5174/src/pages/ConsentManagement.jsx:72:14)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/03b18a11-1c8d-404e-b9ce-7725fddd9081
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC002
- **Test Name:** Login Failure with Invalid Credentials
- **Test Code:** [TC002_Login_Failure_with_Invalid_Credentials.py](./TC002_Login_Failure_with_Invalid_Credentials.py)
- **Test Error:** Login validation failed: invalid credentials allowed login without error message. Stopping further tests due to critical issue.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/950676f5-ef77-48f5-8d7d-9ea5dfe7cb3d
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC003
- **Test Name:** Dynamic Form Configuration Create and Update
- **Test Code:** [TC003_Dynamic_Form_Configuration_Create_and_Update.py](./TC003_Dynamic_Form_Configuration_Create_and_Update.py)
- **Test Error:** Testing stopped due to inability to add new fields in the form configurator UI. The issue prevents verifying creation and modification of form configurations including adding/hiding fields, setting validations, and workflows. Please investigate and fix this critical functionality.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/dc0da1fa-e2c0-4e0b-854e-52fb7c1b5b4b
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC004
- **Test Name:** Form Configuration Rollback Functionality
- **Test Code:** [TC004_Form_Configuration_Rollback_Functionality.py](./TC004_Form_Configuration_Rollback_Functionality.py)
- **Test Error:** Rollback functionality test failed. The rollback action does not trigger any change or confirmation in the UI after selecting a previous version. This issue prevents completing the verification of rollback functionality within the required timeframe. Reporting this issue for developer investigation and stopping further testing.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/1da6813f-52ef-42e3-98d4-52841133a1f0
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC005
- **Test Name:** Patient Management - CRUD Operations
- **Test Code:** [TC005_Patient_Management___CRUD_Operations.py](./TC005_Patient_Management___CRUD_Operations.py)
- **Test Error:** Testing stopped due to backend UnboundLocalError preventing patient record creation. Issue reported for developer fix. Patient record CRUD validation could not be completed.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 429 () (at https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3DAPI%2520to%2520create%2520patient%2520record%2520with%2520external%2520ID%2520and%2520custom%2520data%2520localhost:8000%26udm%3D14%26sei%3D0PbWaIgK5Yyd6w-F-K6ZAg&q=EhAkBQIBQDIBqjS7mtGvQRqOGNDt28YGIjBw8Q362piHhaNvj5fSQNsJNx7oIMZzLGnrvUimiho0akdSxqK4lg5fdpLQPpl5oAsyAVJaAUM:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&co=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbTo0NDM.&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=normal&s=Q4NuKX5QaUAv2VmdTOnBA52GVZdHmlVbJ7X0uXzWz_Kd9UeI2E5dZQdELORlDCDCHSMtxDJKYsdzzoFU7U5bQWBIeeG_EUlGv8PtsG052g8ANmUGfThxD6Hk8djt5_kaFbXCh2u4Us1IHo6oby1jBFSwaUDWfTzt78-SMYilLfUA14by8MCv9VwrasCBPMNTyZcJ8AoC8HkR8rhfoeH7RUY69KbrDK6HjW6Wbash-z5fIQ_xvdWF9xS0HLoxQRZKFNXISDXOEyO_BFSzWZ2KX1Ea0a3P1PY&anchor-ms=20000&execute-ms=15000&cb=z2ycrf12sq5b:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/bframe?hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&bft=0dAFcWeA6uLj1WUSFRjNj4fj53sGhL6OIBEyavv6-qEhOMZicCYDFQEQ_pOtWxQIn8xHGkDbWQfgHFJAokYKdii11PH_gq1aZx-g:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/patients:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/clinical/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:8000/api/clinical/patients/:0:0)
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/submit/forms/visit_opd/submit/:0:0)
[ERROR] Save error: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>UnboundLocalError
          at /api/submit/forms/visit_opd/submit/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>UnboundLocalError
       at /api/submit/forms/visit_opd/submit/</h1>
  <pre class="exception_value">cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>POST</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/submit/forms/visit_opd/submit/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>UnboundLocalError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/submission/views.py</span>, line 248, in submit_visit_opd</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>quotas.rate_limiting.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 02:00:06 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4345119680">
              
                <ol start="48" class="pre-context" id="pre4345119680">
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4345119680">
                  
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4345119680', 'post4345119680')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345119680">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>UnboundLocalError(&quot;cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value&quot;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4348710336">
              
                <ol start="190" class="pre-context" id="pre4348710336">
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4348710336">
                  
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348710336', 'post4348710336')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348710336">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d63240&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d63240&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4348710848">
              
                <ol start="49" class="pre-context" id="pre4348710848">
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4348710848">
                  
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4348710848', 'post4348710848')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348710848">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d63ba0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4348712256">
              
                <ol start="49" class="pre-context" id="pre4348712256">
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4348712256">
                  
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4348712256', 'post4348712256')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348712256">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d639c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4346053056">
              
                <ol start="98" class="pre-context" id="pre4346053056">
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4346053056">
                  
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4346053056', 'post4346053056')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346053056">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;quotas.rate_limiting.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4345217472">
              
                <ol start="502" class="pre-context" id="pre4345217472">
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4345217472">
                  
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4345217472', 'post4345217472')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345217472">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4345226432">
              
                <ol start="462" class="pre-context" id="pre4345226432">
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4345226432">
                  
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4345226432', 'post4345226432')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345226432">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,
 &#x27;view&#x27;: &lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>UnboundLocalError(&quot;cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value&quot;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4348664640">
              
                <ol start="473" class="pre-context" id="pre4348664640">
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4348664640">
                  
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4348664640', 'post4348664640')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348664640">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>UnboundLocalError(&quot;cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value&quot;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4348659968">
              
                <ol start="499" class="pre-context" id="pre4348659968">
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4348659968">
                  
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4348659968', 'post4348659968')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348659968">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4348662208">
              
                <ol start="43" class="pre-context" id="pre4348662208">
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4348662208">
                  
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4348662208', 'post4348662208')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348662208">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function tenant_limited.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102d63b00&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x103013410&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/quotas/rate_limiting.py</code>, line 181, in wrapper
          

          
            <div class="context" id="c4348661504">
              
                <ol start="174" class="pre-context" id="pre4348661504">
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>                        &quot;error&quot;: &quot;rate limit&quot;,</pre></li>
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>                        &quot;message&quot;: f&quot;Rate limit exceeded for {metric}&quot;,</pre></li>
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>                        &quot;quota_info&quot;: quota_info</pre></li>
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>                    },</pre></li>
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>                    status=429</pre></li>
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>                )</pre></li>
                
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>            </pre></li>
                
                </ol>
              
              <ol start="181" class="context-line">
                <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>            return view_func(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='182' class="post-context" id="post4348661504">
                  
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>        return wrapper</pre></li>
                  
                  <li onclick="toggle('pre4348661504', 'post4348661504')"><pre>    return decorator</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348661504">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_current_tenant</td>
                    <td class="code"><pre>&lt;function get_current_tenant at 0x1027c4c20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>is_allowed</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>metric</td>
                    <td class="code"><pre>&#x27;submit&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>quota_info</td>
                    <td class="code"><pre>{&#x27;message&#x27;: &#x27;No quota limits defined&#x27;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>tenant_id</td>
                    <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function submit_visit_opd at 0x102d63a60&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/submission/views.py</code>, line 248, in submit_visit_opd
          

          
            <div class="context" id="c4346430464">
              
                <ol start="241" class="pre-context" id="pre4346430464">
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>        tenant_id = get_current_tenant()</pre></li>
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>        </pre></li>
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>        Task.objects.create(</pre></li>
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>            tenant_id=tenant_id,</pre></li>
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>            team=&quot;care&quot;,</pre></li>
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>            summary=f&quot;Create Consent for New Patient {ext}&quot;,</pre></li>
                
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>            details=f&quot;Patient {name} ({ext}) has been registered. Please create appropriate consent for data collection. Data categories needed: demographics, vitals, labs, diagnosis, medications. Purpose: treatment.&quot;,</pre></li>
                
                </ol>
              
              <ol start="248" class="context-line">
                <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>            due_at=now() + timedelta(hours=24),  # Due in 24 hours
                                ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='249' class="post-context" id="post4346430464">
                  
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>            status=&quot;open&quot;</pre></li>
                  
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>        )</pre></li>
                  
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>        print(f&quot;Created consent reminder task for new patient {ext}&quot;)</pre></li>
                  
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>    # Determine visit status based on consent</pre></li>
                  
                  <li onclick="toggle('pre4346430464', 'post4346430464')"><pre>    visit_status = &#x27;completed&#x27;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346430464">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>ExtensionHook</td>
                    <td class="code"><pre>&lt;class &#x27;extensions.models.ExtensionHook&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>Task</td>
                    <td class="code"><pre>&lt;class &#x27;orchestrator.models.Task&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>_</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
                  <tr>
                    <td>call_http</td>
                    <td class="code"><pre>&lt;function call_http at 0x102b06a20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>create_webhook_headers</td>
                    <td class="code"><pre>&lt;function create_webhook_headers at 0x102f92ca0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>eval_out</td>
                    <td class="code"><pre>{&#x27;errors&#x27;: [],
 &#x27;setField&#x27;: [{&#x27;id&#x27;: &#x27;bmi&#x27;, &#x27;value&#x27;: 142.9},
              {&#x27;id&#x27;: &#x27;diabetes_educator_required&#x27;, &#x27;value&#x27;: False}],
 &#x27;visibility&#x27;: [{&#x27;id&#x27;: &#x27;diabetes_educator&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;guardian_name&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;guardian_relationship&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;birth_certificate_upload&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;patient_id&#x27;, &#x27;visible&#x27;: False}],
 &#x27;warnings&#x27;: [&quot;visibility error for {&#x27;id&#x27;: &#x27;&#x27;, &#x27;when&#x27;: &#x27;&#x27;}: invalid syntax &quot;
              &#x27;(&lt;unknown&gt;, line 0)&#x27;]}</pre></td>
                  </tr>
                
                  <tr>
                    <td>existing</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>ext</td>
                    <td class="code"><pre>&#x27;patient-12345&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>field</td>
                    <td class="code"><pre>{&#x27;data_category&#x27;: &#x27;documents&#x27;,
 &#x27;id&#x27;: &#x27;birth_certificate_upload&#x27;,
 &#x27;label&#x27;: &#x27;Upload Birth Certificate&#x27;,
 &#x27;required&#x27;: False,
 &#x27;type&#x27;: &#x27;file&#x27;,
 &#x27;visible&#x27;: False}</pre></td>
                  </tr>
                
                  <tr>
                    <td>field_id</td>
                    <td class="code"><pre>&#x27;weight_kg&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>field_value</td>
                    <td class="code"><pre>70</pre></td>
                  </tr>
                
                  <tr>
                    <td>form_config</td>
                    <td class="code"><pre>&lt;Config: form:visit_opd:v45 (published)&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>idem</td>
                    <td class="code"><pre>&#x27;idem-mg1aq1j4-x089cf3lh6n&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>is_new_patient</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
                  <tr>
                    <td>matches_criteria</td>
                    <td class="code"><pre>&lt;function matches_criteria at 0x102f92d40&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>name</td>
                    <td class="code"><pre>30</pre></td>
                  </tr>
                
                  <tr>
                    <td>patient</td>
                    <td class="code"><pre>&lt;Patient: patient-12345 - 30&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>patient_exists</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>
                
                  <tr>
                    <td>patient_id</td>
                    <td class="code"><pre>&#x27;patient-12345&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>payload</td>
                    <td class="code"><pre>{&#x27;age&#x27;: 170,
 &#x27;bmi&#x27;: 142.9,
 &#x27;diabetes_educator_required&#x27;: False,
 &#x27;external_id&#x27;: &#x27;patient-12345&#x27;,
 &#x27;hba1c&#x27;: 5.5,
 &#x27;height_cm&#x27;: 70,
 &#x27;name&#x27;: 30,
 &#x27;weight_kg&#x27;: 70}</pre></td>
                  </tr>
                
                  <tr>
                    <td>pre_hooks</td>
                    <td class="code"><pre>&lt;QuerySet []&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>rules</td>
                    <td class="code"><pre>{&#x27;calculations&#x27;: [{&#x27;expr&#x27;: &#x27;round(weight_kg / ((height_cm/100) ** 2), 1)&#x27;,
                   &#x27;set&#x27;: &#x27;bmi&#x27;,
                   &#x27;when&#x27;: &#x27;height_cm and weight_kg&#x27;}],
 &#x27;purpose&#x27;: &#x27;treatment&#x27;,
 &#x27;set_fields&#x27;: [{&#x27;id&#x27;: &#x27;diabetes_educator_required&#x27;,
                 &#x27;value&#x27;: &#x27;(hba1c is not None) and (hba1c &gt;= 9)&#x27;}],
 &#x27;visibility&#x27;: [{&#x27;id&#x27;: &#x27;diabetes_educator&#x27;,
                 &#x27;when&#x27;: &#x27;(hba1c is not None) and (hba1c &gt;= 9)&#x27;},
                {&#x27;id&#x27;: &#x27;guardian_name&#x27;,
                 &#x27;when&#x27;: &#x27;(age is not None) and (age &lt; 18)&#x27;},
                {&#x27;id&#x27;: &#x27;guardian_relationship&#x27;,
                 &#x27;when&#x27;: &#x27;(age is not None) and (age &lt; 18)&#x27;},
                {&#x27;id&#x27;: &#x27;birth_certificate_upload&#x27;,
                 &#x27;when&#x27;: &#x27;(age is not None) and (age &lt; 18)&#x27;},
                {&#x27;id&#x27;: &#x27;&#x27;, &#x27;when&#x27;: &#x27;&#x27;},
                {&#x27;id&#x27;: &#x27;patient_id&#x27;, &#x27;when&#x27;: &#x27;False&#x27;}]}</pre></td>
                  </tr>
                
                  <tr>
                    <td>sf</td>
                    <td class="code"><pre>{&#x27;id&#x27;: &#x27;diabetes_educator_required&#x27;, &#x27;value&#x27;: False}</pre></td>
                  </tr>
                
                  <tr>
                    <td>sub</td>
                    <td class="code"><pre>&lt;Submission: visit_opd - idem-mg1aq1j4-x089cf3lh6n&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>tenant_id</td>
                    <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>validation_errors</td>
                    <td class="code"><pre>[]</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="UnboundLocalError at /api/submit/forms/visit_opd/submit/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: POST
Request URL: http://127.0.0.1:8000/api/submit/forms/visit_opd/submit/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/quotas/rate_limiting.py", line 181, in wrapper
    return view_func(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/submission/views.py", line 248, in submit_visit_opd
    due_at=now() + timedelta(hours=24),  # Due in 24 hours
                   ^^^^^^^^^

Exception Type: UnboundLocalError at /api/submit/forms/visit_opd/submit/
Exception Value: cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;140&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_IDEMPOTENCY_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/visit&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/submit/forms/visit_opd/submit/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;POST&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x1031195a0&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async save (http://localhost:5174/src/pages/Visit.jsx:144:19) (at http://localhost:5174/src/pages/Visit.jsx:157:14)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/16b1fa52-0d9f-4ea0-ae80-2d58ade395e4
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC006
- **Test Name:** Visit Management - Status Tracking and Updates
- **Test Code:** [TC006_Visit_Management___Status_Tracking_and_Updates.py](./TC006_Visit_Management___Status_Tracking_and_Updates.py)
- **Test Error:** The testing of visit creation, status tracking, and status update functionality was attempted via both API and UI. The UI visit creation form did not load, blocking UI-based testing. The API endpoint /api/clinical/visits/ was explored and found to only allow OPTIONS and GET methods, preventing visit creation via POST. Therefore, no visits could be created or updated during testing. The task is not fully completed due to these limitations. Further investigation or fixes may be needed to enable visit creation via API or UI.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 429 () (at https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3DVisit%2520Management%2520API%2520create%2520new%2520patient%2520visit%2520with%2520status%26udm%3D14%26sei%3D2PbWaPuTIfbsseMPiODYGA&q=EhAkBQIBQDIBqjS7mtGvQRqOGNnt28YGIjDs1blSOWnLaFhjiY8QjBog5MF-weWZx2WWdVrCubXZxK2-vHVm_a_JvnKp5RoRbfcyAVJaAUM:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&co=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbTo0NDM.&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=normal&s=O1bhpR9RmdCNx8Fw8UXxypVi9wAsiQFY9VO6Xzn9CFtR-vndR_dWRclgi4soCOVg-gQbi9aMy_mZVTGeID-zK4QWW4pnCTnqt8iBnEvcQNU38u_xBEiAWH-aJ-vOHIBuANLLv__YUI7NtwqdtGHjeo723OIe72zu0nvc7FpdWI9IhAEexDz3xcKdyKEx7I19aWb5GbaRhM1BlEhF_4QbDxkmp_ADTFkURZfMYOh5SWXVbQPetB1o0D6PrIMPCnJuhGIQhM60aCroV2mskZJvEgE4u3BVU50&anchor-ms=20000&execute-ms=15000&cb=k956aaw30rl2:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/bframe?hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&bft=0dAFcWeA6zift46fRGWfWAPyrXijaB8OmW-Lzf_PnZi-Hai1EdVCQWrbsyvd9ArzMj_6vcjMLtK5co7RF2s6o39q_7lmbvtlFGMg:0:0)
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: net::ERR_EMPTY_RESPONSE (at http://localhost:5174/api/config/effective/form/visit_opd/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/visits:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/clinical/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 429 () (at https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dhow%2520to%2520send%2520POST%2520request%2520with%2520JSON%2520body%2520and%2520basic%2520auth%2520in%2520browser%2520or%2520API%2520client%26udm%3D14%26sei%3DQ_fWaP3fIfCVseMP4vjdqAQ&q=EhAkBQIBQDIBqjS7mtGvQRqOGMTu28YGIjCxwnpnqIuiMH_yHXtHfm1Disi-mq-6haEXs3JaYXkxKc2SWd2Rt-LDEUSk95GmbKcyAVJaAUM:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&co=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbTo0NDM.&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=normal&s=maFcLQ5ebkam_bHBr8g5-VbaEkY8mAjCZ8j5gNHuj9qH_YsTEC6PaZPuCWgcf_HcNNBq6R0Y6kzEN-qCx8Y_oDW-JyTK9ONjbBbrqpHoA61Qu77TmB_kw-uz7Ev6n1JwpuVCzAthbsCr211nYdIfjYMFw5fruYgu10FHc1f7sNgvZNN2rKd8s4uEtkIP2pth3Ls2Ny-TF0qlrinjrueebidGHeMdgL_vaVci9_DHDYtFhfiYbfTRrgSyRvqGKaJuQXmHFALmimEoKhCBAJHvqfMZPfplvqk&anchor-ms=20000&execute-ms=15000&cb=93cbwip2jpo7:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/bframe?hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&bft=0dAFcWeA7gGFrphwfRqnFYzw6LMDP1RIuVlGUHbF_z2Ap1kfDwAwOW0JV9ErcaURA8WPPKlBQO4Owx4H65suPkWW3lUxPx9xdH2Q:0:0)
[ERROR] Failed to load resource: the server responded with a status of 429 () (at https://www.google.com/sorry/index?continue=https://www.google.com/search%3Fq%3Dcurl%2520POST%2520request%2520with%2520JSON%2520body%2520and%2520basic%2520auth%26udm%3D14%26sei%3DVvfWaIDiE4mwwcsPyYiAwAk&q=EhAkBQIBQDIBqjS7mtGvQRqOGNfu28YGIjDwntv69V71nqkPzS6IqJmEQbFEioU0DVtsKKQ6QjgJS0vxUKNsfX03wPTWWuDkuzkyAVJaAUM:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/anchor?ar=1&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&co=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbTo0NDM.&hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&size=normal&s=nIpMWgKv0wqSI2inay4BNp4npqKBUItkcZMKXtbpTdeX9ADUdEAgW1-7uuVkFN5I1r3JsYLyP3fCkbhZukpaZjrhj5fYUDW_myAn6dmUZCEEVc54Z-AzIpLsUm8s9lo-JXPUsRg173oMISeG6k5St2lLX45E_rD2z13gXs4athBOMRYEiNtvTg4HpEhcrYbb9LX-qTTZv0XrSgj5BntEGisXPytVNQ9YEZ8sfB0mbdIE1j8cFzD59vZoXTQGyB9gRww-GpSafU_y9pWuN6SkHVEjnbJg8AY&anchor-ms=20000&execute-ms=15000&cb=gnfb0mbpoh4y:0:0)
[WARNING] An iframe which has both allow-scripts and allow-same-origin for its sandbox attribute can escape its sandboxing. (at https://www.google.com/recaptcha/enterprise/bframe?hl=en&v=XrIDux0s7SoNe6_IHkjGC92W&k=6LdLLIMbAAAAAIl-KLj9p1ePhM-4LCCDbjtJLqRO&bft=0dAFcWeA70zcmR-kcky_3f54eGB5tWT0IhoLuJW5N6HMBtErEqIBR_wSjR6yDUPmbjMcBauE3_HA3nN0OuLij2iaMyqPT6_YFuIA:0:0)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/7bbe8c4e-8b19-4175-a1e1-aba6b9b270d2
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC007
- **Test Name:** Consent Management Creation and Compliance
- **Test Code:** [TC007_Consent_Management_Creation_and_Compliance.py](./TC007_Consent_Management_Creation_and_Compliance.py)
- **Test Error:** Consent creation failed due to backend ValueError related to signal handling in non-main thread. This blocks further testing of consent creation, listing, and audit trails. Recommend backend fix before continuing tests.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
[ERROR] Failed to load patients: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>ValueError
          at /api/clinical/patients/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>ValueError
       at /api/clinical/patients/</h1>
  <pre class="exception_value">signal only works in main thread of the main interpreter</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/clinical/patients/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>ValueError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>signal only works in main thread of the main interpreter</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</span>, line 58, in signal</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>clinical.views.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 01:56:04 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4347838080">
              
                <ol start="48" class="pre-context" id="pre4347838080">
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4347838080">
                  
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4347838080', 'post4347838080')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347838080">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4347830080">
              
                <ol start="190" class="pre-context" id="pre4347830080">
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4347830080">
                  
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347830080', 'post4347830080')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347830080">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4347831488">
              
                <ol start="49" class="pre-context" id="pre4347831488">
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4347831488">
                  
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4347831488', 'post4347831488')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347831488">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da82c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4344822528">
              
                <ol start="98" class="pre-context" id="pre4344822528">
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4344822528">
                  
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4344822528', 'post4344822528')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4344822528">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;clinical.views.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4347826496">
              
                <ol start="502" class="pre-context" id="pre4347826496">
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4347826496">
                  
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4347826496', 'post4347826496')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347826496">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4347833088">
              
                <ol start="462" class="pre-context" id="pre4347833088">
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4347833088">
                  
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4347833088', 'post4347833088')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347833088">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,
 &#x27;view&#x27;: &lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4347826560">
              
                <ol start="473" class="pre-context" id="pre4347826560">
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4347826560">
                  
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4347826560', 'post4347826560')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347826560">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4347827136">
              
                <ol start="499" class="pre-context" id="pre4347827136">
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4347827136">
                  
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4347827136', 'post4347827136')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347827136">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4347827584">
              
                <ol start="43" class="pre-context" id="pre4347827584">
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4347827584">
                  
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4347827584', 'post4347827584')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347827584">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function with_timeout.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102da8400&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0d590&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py</code>, line 27, in wrapper
          

          
            <div class="context" id="c4347832640">
              
                <ol start="20" class="pre-context" id="pre4347832640">
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>def timeout_handler(signum, frame):</pre></li>
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>    raise TimeoutError(&quot;Operation timed out&quot;)</pre></li>
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre></pre></li>
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>def with_timeout(seconds=30):</pre></li>
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>    def decorator(func):</pre></li>
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>        def wrapper(*args, **kwargs):</pre></li>
                
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>            # Set the signal handler</pre></li>
                
                </ol>
              
              <ol start="27" class="context-line">
                <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='28' class="post-context" id="post4347832640">
                  
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>            signal.alarm(seconds)</pre></li>
                  
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>            </pre></li>
                  
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>            try:</pre></li>
                  
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>                result = func(*args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>                return result</pre></li>
                  
                  <li onclick="toggle('pre4347832640', 'post4347832640')"><pre>            finally:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4347832640">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function patients_list at 0x102da8360&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>seconds</td>
                    <td class="code"><pre>30</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</code>, line 58, in signal
          

          
            <div class="context" id="c4345424128">
              
                <ol start="51" class="pre-context" id="pre4345424128">
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>    def decorator(wrapper):</pre></li>
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>        wrapper.__doc__ = wrapped.__doc__</pre></li>
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>        return wrapper</pre></li>
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>    return decorator</pre></li>
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>@_wraps(_signal.signal)</pre></li>
                
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>def signal(signalnum, handler):</pre></li>
                
                </ol>
              
              <ol start="58" class="context-line">
                <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='59' class="post-context" id="post4345424128">
                  
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>    return _int_to_enum(handler, Handlers)</pre></li>
                  
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>@_wraps(_signal.getsignal)</pre></li>
                  
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>def getsignal(signalnum):</pre></li>
                  
                  <li onclick="toggle('pre4345424128', 'post4345424128')"><pre>    handler = _signal.getsignal(signalnum)</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345424128">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;function timeout_handler at 0x102d63e20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>signalnum</td>
                    <td class="code"><pre>&lt;Signals.SIGALRM: 14&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="ValueError at /api/clinical/patients/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://127.0.0.1:8000/api/clinical/patients/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py", line 27, in wrapper
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py", line 58, in signal
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exception Type: ValueError at /api/clinical/patients/
Exception Value: signal only works in main thread of the main interpreter
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/consent&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/clinical/patients/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;GET&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x10317aad0&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async loadPatients (http://localhost:5174/src/pages/ConsentManagement.jsx:70:20) (at http://localhost:5174/src/pages/ConsentManagement.jsx:72:14)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/18e4b651-4c9e-45be-aaa7-84bb670b6b5b
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC008
- **Test Name:** Consent Validation for Operations
- **Test Code:** [TC008_Consent_Validation_for_Operations.py](./TC008_Consent_Validation_for_Operations.py)
- **Test Error:** Consent verification testing for granted consent scenarios succeeded. However, testing for missing or insufficient consent scenarios failed because the system incorrectly shows consent as granted and does not return denial responses. This is a critical issue that prevents full verification of consent denial behavior. Reporting this issue and stopping further testing as per instructions.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
[ERROR] Failed to load patients: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>ValueError
          at /api/clinical/patients/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>ValueError
       at /api/clinical/patients/</h1>
  <pre class="exception_value">signal only works in main thread of the main interpreter</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/clinical/patients/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>ValueError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>signal only works in main thread of the main interpreter</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</span>, line 58, in signal</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>clinical.views.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 01:55:55 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4345987776">
              
                <ol start="48" class="pre-context" id="pre4345987776">
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4345987776">
                  
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4345987776', 'post4345987776')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345987776">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4345991232">
              
                <ol start="190" class="pre-context" id="pre4345991232">
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4345991232">
                  
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345991232', 'post4345991232')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345991232">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4345992192">
              
                <ol start="49" class="pre-context" id="pre4345992192">
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4345992192">
                  
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4345992192', 'post4345992192')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345992192">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da82c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4345990848">
              
                <ol start="98" class="pre-context" id="pre4345990848">
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4345990848">
                  
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4345990848', 'post4345990848')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345990848">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;clinical.views.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4345992320">
              
                <ol start="502" class="pre-context" id="pre4345992320">
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4345992320">
                  
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4345992320', 'post4345992320')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345992320">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4345994176">
              
                <ol start="462" class="pre-context" id="pre4345994176">
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4345994176">
                  
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4345994176', 'post4345994176')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345994176">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,
 &#x27;view&#x27;: &lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4346000064">
              
                <ol start="473" class="pre-context" id="pre4346000064">
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4346000064">
                  
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4346000064', 'post4346000064')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346000064">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4345996032">
              
                <ol start="499" class="pre-context" id="pre4345996032">
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4345996032">
                  
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345996032', 'post4345996032')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345996032">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4345999552">
              
                <ol start="43" class="pre-context" id="pre4345999552">
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4345999552">
                  
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4345999552', 'post4345999552')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345999552">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function with_timeout.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102da8400&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102f0de50&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py</code>, line 27, in wrapper
          

          
            <div class="context" id="c4345988416">
              
                <ol start="20" class="pre-context" id="pre4345988416">
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>def timeout_handler(signum, frame):</pre></li>
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>    raise TimeoutError(&quot;Operation timed out&quot;)</pre></li>
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>def with_timeout(seconds=30):</pre></li>
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>    def decorator(func):</pre></li>
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>        def wrapper(*args, **kwargs):</pre></li>
                
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>            # Set the signal handler</pre></li>
                
                </ol>
              
              <ol start="27" class="context-line">
                <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='28' class="post-context" id="post4345988416">
                  
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>            signal.alarm(seconds)</pre></li>
                  
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>            </pre></li>
                  
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>            try:</pre></li>
                  
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>                result = func(*args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>                return result</pre></li>
                  
                  <li onclick="toggle('pre4345988416', 'post4345988416')"><pre>            finally:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345988416">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function patients_list at 0x102da8360&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>seconds</td>
                    <td class="code"><pre>30</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</code>, line 58, in signal
          

          
            <div class="context" id="c4345996928">
              
                <ol start="51" class="pre-context" id="pre4345996928">
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>    def decorator(wrapper):</pre></li>
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>        wrapper.__doc__ = wrapped.__doc__</pre></li>
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>        return wrapper</pre></li>
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>    return decorator</pre></li>
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>@_wraps(_signal.signal)</pre></li>
                
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>def signal(signalnum, handler):</pre></li>
                
                </ol>
              
              <ol start="58" class="context-line">
                <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='59' class="post-context" id="post4345996928">
                  
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>    return _int_to_enum(handler, Handlers)</pre></li>
                  
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>@_wraps(_signal.getsignal)</pre></li>
                  
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>def getsignal(signalnum):</pre></li>
                  
                  <li onclick="toggle('pre4345996928', 'post4345996928')"><pre>    handler = _signal.getsignal(signalnum)</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345996928">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;function timeout_handler at 0x102d63e20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>signalnum</td>
                    <td class="code"><pre>&lt;Signals.SIGALRM: 14&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="ValueError at /api/clinical/patients/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://127.0.0.1:8000/api/clinical/patients/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py", line 27, in wrapper
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py", line 58, in signal
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exception Type: ValueError at /api/clinical/patients/
Exception Value: signal only works in main thread of the main interpreter
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/consent&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/clinical/patients/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;GET&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x1030b1d20&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async loadPatients (http://localhost:5174/src/pages/ConsentManagement.jsx:70:20) (at http://localhost:5174/src/pages/ConsentManagement.jsx:72:14)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/62235b03-281a-4d86-9642-2cd2380db54b
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC009
- **Test Name:** RBAC Enforcement at Field, Record, and Workflow Levels
- **Test Code:** [TC009_RBAC_Enforcement_at_Field_Record_and_Workflow_Levels.py](./TC009_RBAC_Enforcement_at_Field_Record_and_Workflow_Levels.py)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/28ccb2fb-0ee5-4413-9a6e-9f11f7467882
- **Status:** ✅ Passed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC010
- **Test Name:** Form Submission Idempotency and Duplication Prevention
- **Test Code:** [TC010_Form_Submission_Idempotency_and_Duplication_Prevention.py](./TC010_Form_Submission_Idempotency_and_Duplication_Prevention.py)
- **Test Error:** Testing stopped. The system failed to prevent duplicate submissions using idempotency keys. The first submission succeeded and saved the data, but repeated submissions with the same key created new drafts instead of being rejected or ignored. Validation for missing or invalid fields was not tested due to this critical failure.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/ae360d64-aefa-46e0-b975-e2e2d91e22a8
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC011
- **Test Name:** Orchestration Workflow Execution and Retry
- **Test Code:** [TC011_Orchestration_Workflow_Execution_and_Retry.py](./TC011_Orchestration_Workflow_Execution_and_Retry.py)
- **Test Error:** The orchestrator can execute workflows and manage tasks as confirmed by successful triggering of orchestration process execution via API. Task failure simulation was successful by causing validation error in the form. However, the retry of failed tasks could not be tested because the API endpoint /api/orchestrator/retry-failed-tasks/ does not exist, resulting in a 404 error. Notifications list API and verification of notification delivery were not tested due to this limitation. Overall, the core orchestration and failure simulation work, but retry and notification verification remain unverified due to missing API support.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: net::ERR_EMPTY_RESPONSE (at http://localhost:5174/api/config/publish/workflow/visit_opd/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/orchestrator/trigger:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/orchestrator/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 405 (Method Not Allowed) (at http://localhost:8000/api/orchestrator/process-now/:0:0)
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 405 (Method Not Allowed) (at http://localhost:8000/api/orchestrator/process-now/:0:0)
[ERROR] Failed to load resource: the server responded with a status of 404 (Not Found) (at http://localhost:8000/api/orchestrator/retry-failed-tasks/:0:0)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/6912e674-59ff-403c-bbdd-8d3a92218347
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC012
- **Test Name:** Multi-Tenancy Data Isolation and Customization
- **Test Code:** [TC012_Multi_Tenancy_Data_Isolation_and_Customization.py](./TC012_Multi_Tenancy_Data_Isolation_and_Customization.py)
- **Test Error:** Testing stopped due to critical backend error preventing validation of tenant data isolation and configuration visibility. Error details reported to development team.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/submit/forms/visit_opd/submit/:0:0)
[ERROR] Save error: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>UnboundLocalError
          at /api/submit/forms/visit_opd/submit/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>UnboundLocalError
       at /api/submit/forms/visit_opd/submit/</h1>
  <pre class="exception_value">cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>POST</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/submit/forms/visit_opd/submit/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>UnboundLocalError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/submission/views.py</span>, line 248, in submit_visit_opd</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>quotas.rate_limiting.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 01:57:22 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4345809280">
              
                <ol start="48" class="pre-context" id="pre4345809280">
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4345809280">
                  
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4345809280', 'post4345809280')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345809280">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>UnboundLocalError(&quot;cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value&quot;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4345815488">
              
                <ol start="190" class="pre-context" id="pre4345815488">
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4345815488">
                  
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345815488', 'post4345815488')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345815488">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d63240&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d63240&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4345822464">
              
                <ol start="49" class="pre-context" id="pre4345822464">
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4345822464">
                  
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4345822464', 'post4345822464')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345822464">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d63ba0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4345822784">
              
                <ol start="49" class="pre-context" id="pre4345822784">
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4345822784">
                  
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4345822784', 'post4345822784')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345822784">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102d639c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4345817152">
              
                <ol start="98" class="pre-context" id="pre4345817152">
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4345817152">
                  
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4345817152', 'post4345817152')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345817152">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;quotas.rate_limiting.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4345817408">
              
                <ol start="502" class="pre-context" id="pre4345817408">
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4345817408">
                  
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4345817408', 'post4345817408')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345817408">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4345821056">
              
                <ol start="462" class="pre-context" id="pre4345821056">
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4345821056">
                  
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4345821056', 'post4345821056')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345821056">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,
 &#x27;view&#x27;: &lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>UnboundLocalError(&quot;cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value&quot;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4345812096">
              
                <ol start="473" class="pre-context" id="pre4345812096">
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4345812096">
                  
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4345812096', 'post4345812096')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345812096">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>UnboundLocalError(&quot;cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value&quot;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4345812736">
              
                <ol start="499" class="pre-context" id="pre4345812736">
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4345812736">
                  
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4345812736', 'post4345812736')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345812736">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4345822144">
              
                <ol start="43" class="pre-context" id="pre4345822144">
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4345822144">
                  
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4345822144', 'post4345822144')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345822144">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function tenant_limited.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102d63b00&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;quotas.rate_limiting.WrappedAPIView object at 0x102f0d090&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/quotas/rate_limiting.py</code>, line 181, in wrapper
          

          
            <div class="context" id="c4345816576">
              
                <ol start="174" class="pre-context" id="pre4345816576">
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>                        &quot;error&quot;: &quot;rate limit&quot;,</pre></li>
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>                        &quot;message&quot;: f&quot;Rate limit exceeded for {metric}&quot;,</pre></li>
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>                        &quot;quota_info&quot;: quota_info</pre></li>
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>                    },</pre></li>
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>                    status=429</pre></li>
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>                )</pre></li>
                
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>            </pre></li>
                
                </ol>
              
              <ol start="181" class="context-line">
                <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>            return view_func(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='182' class="post-context" id="post4345816576">
                  
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>        return wrapper</pre></li>
                  
                  <li onclick="toggle('pre4345816576', 'post4345816576')"><pre>    return decorator</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345816576">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_current_tenant</td>
                    <td class="code"><pre>&lt;function get_current_tenant at 0x1027c4c20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>is_allowed</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>metric</td>
                    <td class="code"><pre>&#x27;submit&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>quota_info</td>
                    <td class="code"><pre>{&#x27;message&#x27;: &#x27;No quota limits defined&#x27;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>tenant_id</td>
                    <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function submit_visit_opd at 0x102d63a60&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/submission/views.py</code>, line 248, in submit_visit_opd
          

          
            <div class="context" id="c4345822592">
              
                <ol start="241" class="pre-context" id="pre4345822592">
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>        tenant_id = get_current_tenant()</pre></li>
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>        </pre></li>
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>        Task.objects.create(</pre></li>
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>            tenant_id=tenant_id,</pre></li>
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>            team=&quot;care&quot;,</pre></li>
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>            summary=f&quot;Create Consent for New Patient {ext}&quot;,</pre></li>
                
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>            details=f&quot;Patient {name} ({ext}) has been registered. Please create appropriate consent for data collection. Data categories needed: demographics, vitals, labs, diagnosis, medications. Purpose: treatment.&quot;,</pre></li>
                
                </ol>
              
              <ol start="248" class="context-line">
                <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>            due_at=now() + timedelta(hours=24),  # Due in 24 hours
                                ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='249' class="post-context" id="post4345822592">
                  
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>            status=&quot;open&quot;</pre></li>
                  
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>        )</pre></li>
                  
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>        print(f&quot;Created consent reminder task for new patient {ext}&quot;)</pre></li>
                  
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>    # Determine visit status based on consent</pre></li>
                  
                  <li onclick="toggle('pre4345822592', 'post4345822592')"><pre>    visit_status = &#x27;completed&#x27;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345822592">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>ExtensionHook</td>
                    <td class="code"><pre>&lt;class &#x27;extensions.models.ExtensionHook&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>Task</td>
                    <td class="code"><pre>&lt;class &#x27;orchestrator.models.Task&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>_</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
                  <tr>
                    <td>call_http</td>
                    <td class="code"><pre>&lt;function call_http at 0x102b06a20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>create_webhook_headers</td>
                    <td class="code"><pre>&lt;function create_webhook_headers at 0x102f92ca0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>eval_out</td>
                    <td class="code"><pre>{&#x27;errors&#x27;: [],
 &#x27;setField&#x27;: [{&#x27;id&#x27;: &#x27;bmi&#x27;, &#x27;value&#x27;: 24.2}],
 &#x27;visibility&#x27;: [{&#x27;id&#x27;: &#x27;guardian_name&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;guardian_relationship&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;birth_certificate_upload&#x27;, &#x27;visible&#x27;: False},
                {&#x27;id&#x27;: &#x27;patient_id&#x27;, &#x27;visible&#x27;: False}],
 &#x27;warnings&#x27;: [&quot;set_fields error for {&#x27;id&#x27;: &#x27;diabetes_educator_required&#x27;, &quot;
              &quot;&#x27;value&#x27;: &#x27;(hba1c is not None) and (hba1c &gt;= 9)&#x27;}: &#x27;&gt;=&#x27; not &quot;
              &quot;supported between instances of &#x27;NoneType&#x27; and &#x27;int&#x27;&quot;,
              &quot;visibility error for {&#x27;id&#x27;: &#x27;diabetes_educator&#x27;, &#x27;when&#x27;: &quot;
              &quot;&#x27;(hba1c is not None) and (hba1c &gt;= 9)&#x27;}: &#x27;&gt;=&#x27; not supported &quot;
              &quot;between instances of &#x27;NoneType&#x27; and &#x27;int&#x27;&quot;,
              &quot;visibility error for {&#x27;id&#x27;: &#x27;&#x27;, &#x27;when&#x27;: &#x27;&#x27;}: invalid syntax &quot;
              &#x27;(&lt;unknown&gt;, line 0)&#x27;]}</pre></td>
                  </tr>
                
                  <tr>
                    <td>existing</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>ext</td>
                    <td class="code"><pre>&#x27;patient_from_other_tenant&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>field</td>
                    <td class="code"><pre>{&#x27;data_category&#x27;: &#x27;documents&#x27;,
 &#x27;id&#x27;: &#x27;birth_certificate_upload&#x27;,
 &#x27;label&#x27;: &#x27;Upload Birth Certificate&#x27;,
 &#x27;required&#x27;: False,
 &#x27;type&#x27;: &#x27;file&#x27;,
 &#x27;visible&#x27;: False}</pre></td>
                  </tr>
                
                  <tr>
                    <td>field_id</td>
                    <td class="code"><pre>&#x27;weight_kg&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>field_value</td>
                    <td class="code"><pre>70</pre></td>
                  </tr>
                
                  <tr>
                    <td>form_config</td>
                    <td class="code"><pre>&lt;Config: form:visit_opd:v45 (published)&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>idem</td>
                    <td class="code"><pre>&#x27;idem-mg1amj7k-v70lrwh4rza&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>is_new_patient</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
                  <tr>
                    <td>matches_criteria</td>
                    <td class="code"><pre>&lt;function matches_criteria at 0x102f92d40&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>name</td>
                    <td class="code"><pre>&#x27;Unknown&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>patient</td>
                    <td class="code"><pre>&lt;Patient: patient_from_other_tenant - Unknown&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>patient_exists</td>
                    <td class="code"><pre>False</pre></td>
                  </tr>
                
                  <tr>
                    <td>patient_id</td>
                    <td class="code"><pre>&#x27;patient_from_other_tenant&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>payload</td>
                    <td class="code"><pre>{&#x27;age&#x27;: 30,
 &#x27;bmi&#x27;: 24.2,
 &#x27;external_id&#x27;: &#x27;patient_from_other_tenant&#x27;,
 &#x27;height_cm&#x27;: 170,
 &#x27;weight_kg&#x27;: 70}</pre></td>
                  </tr>
                
                  <tr>
                    <td>pre_hooks</td>
                    <td class="code"><pre>&lt;QuerySet []&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: POST &#x27;/api/submit/forms/visit_opd/submit/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>rules</td>
                    <td class="code"><pre>{&#x27;calculations&#x27;: [{&#x27;expr&#x27;: &#x27;round(weight_kg / ((height_cm/100) ** 2), 1)&#x27;,
                   &#x27;set&#x27;: &#x27;bmi&#x27;,
                   &#x27;when&#x27;: &#x27;height_cm and weight_kg&#x27;}],
 &#x27;purpose&#x27;: &#x27;treatment&#x27;,
 &#x27;set_fields&#x27;: [{&#x27;id&#x27;: &#x27;diabetes_educator_required&#x27;,
                 &#x27;value&#x27;: &#x27;(hba1c is not None) and (hba1c &gt;= 9)&#x27;}],
 &#x27;visibility&#x27;: [{&#x27;id&#x27;: &#x27;diabetes_educator&#x27;,
                 &#x27;when&#x27;: &#x27;(hba1c is not None) and (hba1c &gt;= 9)&#x27;},
                {&#x27;id&#x27;: &#x27;guardian_name&#x27;,
                 &#x27;when&#x27;: &#x27;(age is not None) and (age &lt; 18)&#x27;},
                {&#x27;id&#x27;: &#x27;guardian_relationship&#x27;,
                 &#x27;when&#x27;: &#x27;(age is not None) and (age &lt; 18)&#x27;},
                {&#x27;id&#x27;: &#x27;birth_certificate_upload&#x27;,
                 &#x27;when&#x27;: &#x27;(age is not None) and (age &lt; 18)&#x27;},
                {&#x27;id&#x27;: &#x27;&#x27;, &#x27;when&#x27;: &#x27;&#x27;},
                {&#x27;id&#x27;: &#x27;patient_id&#x27;, &#x27;when&#x27;: &#x27;False&#x27;}]}</pre></td>
                  </tr>
                
                  <tr>
                    <td>sf</td>
                    <td class="code"><pre>{&#x27;id&#x27;: &#x27;bmi&#x27;, &#x27;value&#x27;: 24.2}</pre></td>
                  </tr>
                
                  <tr>
                    <td>sub</td>
                    <td class="code"><pre>&lt;Submission: visit_opd - idem-mg1amj7k-v70lrwh4rza&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>tenant_id</td>
                    <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>validation_errors</td>
                    <td class="code"><pre>[]</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="UnboundLocalError at /api/submit/forms/visit_opd/submit/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: POST
Request URL: http://127.0.0.1:8000/api/submit/forms/visit_opd/submit/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/quotas/rate_limiting.py", line 181, in wrapper
    return view_func(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/submission/views.py", line 248, in submit_visit_opd
    due_at=now() + timedelta(hours=24),  # Due in 24 hours
                   ^^^^^^^^^

Exception Type: UnboundLocalError at /api/submit/forms/visit_opd/submit/
Exception Value: cannot access local variable &#x27;timedelta&#x27; where it is not associated with a value
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;94&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_IDEMPOTENCY_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/visit&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/submit/forms/visit_opd/submit/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;POST&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x1030cd660&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async save (http://localhost:5174/src/pages/Visit.jsx:144:19) (at http://localhost:5174/src/pages/Visit.jsx:157:14)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/511f910b-4d4a-4279-af7b-d6526c9420a2
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC013
- **Test Name:** Extensions System Runtime Hook Execution
- **Test Code:** [TC013_Extensions_System_Runtime_Hook_Execution.py](./TC013_Extensions_System_Runtime_Hook_Execution.py)
- **Test Error:** Testing of the runtime extensions system for runtime hooks and event subscriptions was partially successful. The runtime extension event was registered and triggered via form submission. However, the final step to create patient consent failed due to a backend ValueError: 'signal only works in main thread of the main interpreter'. This error prevented completion of the consent creation and further verification of extension hook processing and external integration effects. Please investigate and fix the backend error to enable full testing.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
[ERROR] Failed to load patients: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>ValueError
          at /api/clinical/patients/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>ValueError
       at /api/clinical/patients/</h1>
  <pre class="exception_value">signal only works in main thread of the main interpreter</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/clinical/patients/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>ValueError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>signal only works in main thread of the main interpreter</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</span>, line 58, in signal</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>clinical.views.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 01:59:36 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4348750144">
              
                <ol start="48" class="pre-context" id="pre4348750144">
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4348750144">
                  
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4348750144', 'post4348750144')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348750144">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4348751104">
              
                <ol start="190" class="pre-context" id="pre4348751104">
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4348751104">
                  
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348751104', 'post4348751104')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348751104">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4348750912">
              
                <ol start="49" class="pre-context" id="pre4348750912">
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4348750912">
                  
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4348750912', 'post4348750912')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348750912">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da82c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4346002176">
              
                <ol start="98" class="pre-context" id="pre4346002176">
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4346002176">
                  
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4346002176', 'post4346002176')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346002176">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;clinical.views.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4348751040">
              
                <ol start="502" class="pre-context" id="pre4348751040">
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4348751040">
                  
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4348751040', 'post4348751040')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348751040">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4348742400">
              
                <ol start="462" class="pre-context" id="pre4348742400">
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4348742400">
                  
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4348742400', 'post4348742400')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348742400">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,
 &#x27;view&#x27;: &lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4348742848">
              
                <ol start="473" class="pre-context" id="pre4348742848">
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4348742848">
                  
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4348742848', 'post4348742848')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348742848">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4348635136">
              
                <ol start="499" class="pre-context" id="pre4348635136">
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4348635136">
                  
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4348635136', 'post4348635136')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348635136">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4348640192">
              
                <ol start="43" class="pre-context" id="pre4348640192">
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4348640192">
                  
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4348640192', 'post4348640192')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348640192">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function with_timeout.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102da8400&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x10306f9b0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py</code>, line 27, in wrapper
          

          
            <div class="context" id="c4348628416">
              
                <ol start="20" class="pre-context" id="pre4348628416">
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>def timeout_handler(signum, frame):</pre></li>
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>    raise TimeoutError(&quot;Operation timed out&quot;)</pre></li>
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>def with_timeout(seconds=30):</pre></li>
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>    def decorator(func):</pre></li>
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>        def wrapper(*args, **kwargs):</pre></li>
                
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>            # Set the signal handler</pre></li>
                
                </ol>
              
              <ol start="27" class="context-line">
                <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='28' class="post-context" id="post4348628416">
                  
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>            signal.alarm(seconds)</pre></li>
                  
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>            </pre></li>
                  
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>            try:</pre></li>
                  
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>                result = func(*args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>                return result</pre></li>
                  
                  <li onclick="toggle('pre4348628416', 'post4348628416')"><pre>            finally:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348628416">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function patients_list at 0x102da8360&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>seconds</td>
                    <td class="code"><pre>30</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</code>, line 58, in signal
          

          
            <div class="context" id="c4348635392">
              
                <ol start="51" class="pre-context" id="pre4348635392">
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>    def decorator(wrapper):</pre></li>
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>        wrapper.__doc__ = wrapped.__doc__</pre></li>
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>        return wrapper</pre></li>
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>    return decorator</pre></li>
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre></pre></li>
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>@_wraps(_signal.signal)</pre></li>
                
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>def signal(signalnum, handler):</pre></li>
                
                </ol>
              
              <ol start="58" class="context-line">
                <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='59' class="post-context" id="post4348635392">
                  
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>    return _int_to_enum(handler, Handlers)</pre></li>
                  
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>@_wraps(_signal.getsignal)</pre></li>
                  
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>def getsignal(signalnum):</pre></li>
                  
                  <li onclick="toggle('pre4348635392', 'post4348635392')"><pre>    handler = _signal.getsignal(signalnum)</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4348635392">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;function timeout_handler at 0x102d63e20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>signalnum</td>
                    <td class="code"><pre>&lt;Signals.SIGALRM: 14&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="ValueError at /api/clinical/patients/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://127.0.0.1:8000/api/clinical/patients/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py", line 27, in wrapper
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py", line 58, in signal
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exception Type: ValueError at /api/clinical/patients/
Exception Value: signal only works in main thread of the main interpreter
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/consent&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/clinical/patients/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;GET&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x1030cd2a0&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async loadPatients (http://localhost:5174/src/pages/ConsentManagement.jsx:70:20) (at http://localhost:5174/src/pages/ConsentManagement.jsx:72:14)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/9faf243b-316c-43e4-9741-c7de2600b31a
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC014
- **Test Name:** Performance - Sub-second Form Loading
- **Test Code:** [TC014_Performance___Sub_second_Form_Loading.py](./TC014_Performance___Sub_second_Form_Loading.py)
- **Test Error:** The task to measure form loading performance and verify sub-second response time under normal and peak load conditions is incomplete. Despite multiple attempts to trigger form rendering and access version history or logs, no response time or error data was accessible or visible in the UI. Therefore, it was not possible to confirm if the system meets the sub-second load time requirement. Recommend enabling or exposing performance monitoring data for proper verification in future testing.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/de9835e4-f1e6-4224-9b08-e9b5aafb3407
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---

#### Test TC015
- **Test Name:** Audit Trail Integrity for All Data Changes
- **Test Code:** [TC015_Audit_Trail_Integrity_for_All_Data_Changes.py](./TC015_Audit_Trail_Integrity_for_All_Data_Changes.py)
- **Test Error:** Audit trail verification for consent changes failed due to UI issue where clicking Check button does not show audit details. Patient record changes audit trail verified successfully. Compliance with DPDP and ABDM audit requirements partially confirmed. Further testing stopped due to this issue.
Browser Console Logs:
[WARNING] ⚠️ React Router Future Flag Warning: React Router will begin wrapping state updates in `React.startTransition` in v7. You can use the `v7_startTransition` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_starttransition. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[WARNING] ⚠️ React Router Future Flag Warning: Relative route resolution within Splat routes is changing in v7. You can use the `v7_relativeSplatPath` future flag to opt-in early. For more information, see https://reactrouter.com/v6/upgrading/future#v7_relativesplatpath. (at http://localhost:5174/node_modules/.vite/deps/react-router-dom.js?v=0452945f:4390:12)
[ERROR] Failed to load resource: the server responded with a status of 500 (Internal Server Error) (at http://localhost:5174/api/clinical/patients/:0:0)
[ERROR] Failed to load patients: Error: <!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>ValueError
          at /api/clinical/patients/</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background-color:#fff; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; word-break: break-word; }
    summary { cursor: pointer; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th {
      padding:1px 6px 1px 3px; background:#fefefe; text-align:left;
      font-weight:normal; font-size:11px; border:1px solid #ddd;
    }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 10px 2px 40px; width: auto; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.cause { word-break: break-word; }
    ul.traceback li.frame { padding-bottom:1em; color:#4f4f4f; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; padding-left: 2px; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#464646; background-color:#dfdfdf; padding: 3px 2px; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands, summary.commands { margin-left: 40px; }
    div.commands a, summary.commands { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 10px 20px; }
    #template-not-exist .postmortem-section { margin-bottom: 3px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em; font-weight:normal; }
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #575757; font-size: 1.5em; margin: 10px 0 10px 0; }
    .append-bottom { margin-bottom: 10px; }
    .fname { user-select: all; }
  </style>
  
  <script>
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(document.querySelectorAll('ol.pre-context'));
      hideAll(document.querySelectorAll('ol.post-context'));
      hideAll(document.querySelectorAll('div.pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.textContent = link.textContent.trim() == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
  </script>
  
</head>
<body>
<div id="summary">
  <h1>ValueError
       at /api/clinical/patients/</h1>
  <pre class="exception_value">signal only works in main thread of the main interpreter</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>GET</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>http://127.0.0.1:8000/api/clinical/patients/</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>4.2.24</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>ValueError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>signal only works in main thread of the main interpreter</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td><span class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</span>, line 58, in signal</td>
    </tr>


    <tr>
      <th>Raised during:</th>
      <td>clinical.views.wrapper</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>3.13.7</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python313.zip&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13&#x27;,
 &#x27;/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload&#x27;,
 &#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages&#x27;,
 &#x27;/opt/homebrew/opt/python-tk@3.13/libexec&#x27;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Sat, 27 Sep 2025 01:59:19 +0530</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">
    Switch to copy-and-paste view</a></span>
  </h2>
  <div id="browserTraceback">
    <ul class="traceback">
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py</code>, line 55, in inner
          

          
            <div class="context" id="c4346542016">
              
                <ol start="48" class="pre-context" id="pre4346542016">
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>        return inner</pre></li>
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>    else:</pre></li>
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>        @wraps(get_response)</pre></li>
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>        def inner(request):</pre></li>
                
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="55" class="context-line">
                <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>                response = get_response(request)
                               ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='56' class="post-context" id="post4346542016">
                  
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>            except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>                response = response_for_exception(request, exc)</pre></li>
                  
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>            return response</pre></li>
                  
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre>        return inner</pre></li>
                  
                  <li onclick="toggle('pre4346542016', 'post4346542016')"><pre></pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346542016">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>get_response</td>
                    <td class="code"><pre>&lt;bound method BaseHandler._get_response of &lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py</code>, line 197, in _get_response
          

          
            <div class="context" id="c4346533120">
              
                <ol start="190" class="pre-context" id="pre4346533120">
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>        if response is None:</pre></li>
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>            wrapped_callback = self.make_view_atomic(callback)</pre></li>
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>            # If it is an asynchronous view, run it in a subthread.</pre></li>
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>            if iscoroutinefunction(wrapped_callback):</pre></li>
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>                wrapped_callback = async_to_sync(wrapped_callback)</pre></li>
                
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>            try:</pre></li>
                
                </ol>
              
              <ol start="197" class="context-line">
                <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>                response = wrapped_callback(request, *callback_args, **callback_kwargs)
                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='198' class="post-context" id="post4346533120">
                  
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>            except Exception as e:</pre></li>
                  
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>                response = self.process_exception_by_middleware(e, request)</pre></li>
                  
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>                if response is None:</pre></li>
                  
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>                    raise</pre></li>
                  
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346533120', 'post4346533120')"><pre>        # Complain if the view returned None (a common error).</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346533120">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>callback_kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CsrfViewMiddleware.process_view of &lt;CsrfViewMiddleware get_response=convert_exception_to_response.&lt;locals&gt;.inner&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x1021fa120&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>wrapped_callback</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da84a0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py</code>, line 56, in wrapper_view
          

          
            <div class="context" id="c4346539200">
              
                <ol start="49" class="pre-context" id="pre4346539200">
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>def csrf_exempt(view_func):</pre></li>
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    &quot;&quot;&quot;Mark a view function as being exempt from the CSRF view protection.&quot;&quot;&quot;</pre></li>
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    # view_func.csrf_exempt = True would also work, but decorators are nicer</pre></li>
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    # if they don&#x27;t have side effects, so return a new function.</pre></li>
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    @wraps(view_func)</pre></li>
                
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    def wrapper_view(*args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="56" class="context-line">
                <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>        return view_func(*args, **kwargs)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='57' class="post-context" id="post4346539200">
                  
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    wrapper_view.csrf_exempt = True</pre></li>
                  
                  <li onclick="toggle('pre4346539200', 'post4346539200')"><pre>    return wrapper_view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346539200">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>view_func</td>
                    <td class="code"><pre>&lt;function View.as_view.&lt;locals&gt;.view at 0x102da82c0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame django">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py</code>, line 105, in view
          

          
            <div class="context" id="c4345891456">
              
                <ol start="98" class="pre-context" id="pre4345891456">
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>            self = cls(**initkwargs)</pre></li>
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>            self.setup(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>            if not hasattr(self, &quot;request&quot;):</pre></li>
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>                raise AttributeError(</pre></li>
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>                    &quot;%s instance has no &#x27;request&#x27; attribute. Did you override &quot;</pre></li>
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>                    &quot;setup() and forget to call super()?&quot; % cls.__name__</pre></li>
                
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>                )</pre></li>
                
                </ol>
              
              <ol start="105" class="context-line">
                <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>            return self.dispatch(request, *args, **kwargs)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='106' class="post-context" id="post4345891456">
                  
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>        view.view_class = cls</pre></li>
                  
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>        view.view_initkwargs = initkwargs</pre></li>
                  
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>        # __name__ and __qualname__ are intentionally left unchanged as</pre></li>
                  
                  <li onclick="toggle('pre4345891456', 'post4345891456')"><pre>        # view_class should be used to robustly determine the name of the view</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345891456">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>cls</td>
                    <td class="code"><pre>&lt;class &#x27;clinical.views.WrappedAPIView&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>initkwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;WSGIRequest: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 509, in dispatch
          

          
            <div class="context" id="c4346540096">
              
                <ol start="502" class="pre-context" id="pre4346540096">
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>            response = handler(request, *args, **kwargs)</pre></li>
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>        except Exception as exc:</pre></li>
                
                </ol>
              
              <ol start="509" class="context-line">
                <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>            response = self.handle_exception(exc)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='510' class="post-context" id="post4346540096">
                  
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>        return self.response</pre></li>
                  
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>    def options(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4346540096', 'post4346540096')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346540096">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 469, in handle_exception
          

          
            <div class="context" id="c4346535296">
              
                <ol start="462" class="pre-context" id="pre4346535296">
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        exception_handler = self.get_exception_handler()</pre></li>
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        context = self.get_exception_handler_context()</pre></li>
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        response = exception_handler(exc, context)</pre></li>
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        if response is None:</pre></li>
                
                </ol>
              
              <ol start="469" class="context-line">
                <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>            self.raise_uncaught_exception(exc)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='470' class="post-context" id="post4346535296">
                  
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        response.exception = True</pre></li>
                  
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        return response</pre></li>
                  
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                  
                  <li onclick="toggle('pre4346535296', 'post4346535296')"><pre>        if settings.DEBUG:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346535296">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>context</td>
                    <td class="code"><pre>{&#x27;args&#x27;: (),
 &#x27;kwargs&#x27;: {},
 &#x27;request&#x27;: &lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,
 &#x27;view&#x27;: &lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;}</pre></td>
                  </tr>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>exception_handler</td>
                    <td class="code"><pre>&lt;function exception_handler at 0x102d41080&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 480, in raise_uncaught_exception
          

          
            <div class="context" id="c4346527936">
              
                <ol start="473" class="pre-context" id="pre4346527936">
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>    def raise_uncaught_exception(self, exc):</pre></li>
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>        if settings.DEBUG:</pre></li>
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>            request = self.request</pre></li>
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>            renderer_format = getattr(request.accepted_renderer, &#x27;format&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>            use_plaintext_traceback = renderer_format not in (&#x27;html&#x27;, &#x27;api&#x27;, &#x27;admin&#x27;)</pre></li>
                
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>            request.force_plaintext_errors(use_plaintext_traceback)</pre></li>
                
                </ol>
              
              <ol start="480" class="context-line">
                <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>        raise exc
             ^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='481' class="post-context" id="post4346527936">
                  
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>    # Note: Views are made CSRF exempt from within `as_view` as to prevent</pre></li>
                  
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>    # accidental removal of this exemption in cases where `dispatch` needs to</pre></li>
                  
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>    # be overridden.</pre></li>
                  
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>    def dispatch(self, request, *args, **kwargs):</pre></li>
                  
                  <li onclick="toggle('pre4346527936', 'post4346527936')"><pre>        &quot;&quot;&quot;</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346527936">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>exc</td>
                    <td class="code"><pre>ValueError(&#x27;signal only works in main thread of the main interpreter&#x27;)</pre></td>
                  </tr>
                
                  <tr>
                    <td>renderer_format</td>
                    <td class="code"><pre>&#x27;json&#x27;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>use_plaintext_traceback</td>
                    <td class="code"><pre>True</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py</code>, line 506, in dispatch
          

          
            <div class="context" id="c4346535232">
              
                <ol start="499" class="pre-context" id="pre4346535232">
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>            # Get the appropriate handler method</pre></li>
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>            if request.method.lower() in self.http_method_names:</pre></li>
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>                handler = getattr(self, request.method.lower(),</pre></li>
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>                                  self.http_method_not_allowed)</pre></li>
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>            else:</pre></li>
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>                handler = self.http_method_not_allowed</pre></li>
                
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre></pre></li>
                
                </ol>
              
              <ol start="506" class="context-line">
                <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>            response = handler(request, *args, **kwargs)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='507' class="post-context" id="post4346535232">
                  
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>        except Exception as exc:</pre></li>
                  
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>            response = self.handle_exception(exc)</pre></li>
                  
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>        self.response = self.finalize_response(request, response, *args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4346535232', 'post4346535232')"><pre>        return self.response</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346535232">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>()</pre></td>
                  </tr>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;bound method api_view.&lt;locals&gt;.decorator.&lt;locals&gt;.handler of &lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py</code>, line 50, in handler
          

          
            <div class="context" id="c4346530368">
              
                <ol start="43" class="pre-context" id="pre4346530368">
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        assert isinstance(http_method_names, (list, tuple)), \</pre></li>
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>            &#x27;@api_view expected a list of strings, received %s&#x27; % type(http_method_names).__name__</pre></li>
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        allowed_methods = set(http_method_names) | {&#x27;options&#x27;}</pre></li>
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        WrappedAPIView.http_method_names = [method.lower() for method in allowed_methods]</pre></li>
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        def handler(self, *args, **kwargs):</pre></li>
                
                </ol>
              
              <ol start="50" class="context-line">
                <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>            return func(*args, **kwargs)
                       ^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='51' class="post-context" id="post4346530368">
                  
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        for method in http_method_names:</pre></li>
                  
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>            setattr(WrappedAPIView, method.lower(), handler)</pre></li>
                  
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        WrappedAPIView.__name__ = func.__name__</pre></li>
                  
                  <li onclick="toggle('pre4346530368', 'post4346530368')"><pre>        WrappedAPIView.__module__ = func.__module__</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346530368">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function with_timeout.&lt;locals&gt;.decorator.&lt;locals&gt;.wrapper at 0x102da8400&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;clinical.views.WrappedAPIView object at 0x102e23df0&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py</code>, line 27, in wrapper
          

          
            <div class="context" id="c4346542208">
              
                <ol start="20" class="pre-context" id="pre4346542208">
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>def timeout_handler(signum, frame):</pre></li>
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>    raise TimeoutError(&quot;Operation timed out&quot;)</pre></li>
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre></pre></li>
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>def with_timeout(seconds=30):</pre></li>
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>    def decorator(func):</pre></li>
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>        def wrapper(*args, **kwargs):</pre></li>
                
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>            # Set the signal handler</pre></li>
                
                </ol>
              
              <ol start="27" class="context-line">
                <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>            old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='28' class="post-context" id="post4346542208">
                  
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>            signal.alarm(seconds)</pre></li>
                  
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>            </pre></li>
                  
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>            try:</pre></li>
                  
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>                result = func(*args, **kwargs)</pre></li>
                  
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>                return result</pre></li>
                  
                  <li onclick="toggle('pre4346542208', 'post4346542208')"><pre>            finally:</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4346542208">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>args</td>
                    <td class="code"><pre>(&lt;rest_framework.request.Request: GET &#x27;/api/clinical/patients/&#x27;&gt;,)</pre></td>
                  </tr>
                
                  <tr>
                    <td>func</td>
                    <td class="code"><pre>&lt;function patients_list at 0x102da8360&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>kwargs</td>
                    <td class="code"><pre>{}</pre></td>
                  </tr>
                
                  <tr>
                    <td>seconds</td>
                    <td class="code"><pre>30</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
        
        <li class="frame user">
          
            <code class="fname">/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py</code>, line 58, in signal
          

          
            <div class="context" id="c4345899520">
              
                <ol start="51" class="pre-context" id="pre4345899520">
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>    def decorator(wrapper):</pre></li>
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>        wrapper.__doc__ = wrapped.__doc__</pre></li>
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>        return wrapper</pre></li>
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>    return decorator</pre></li>
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre></pre></li>
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>@_wraps(_signal.signal)</pre></li>
                
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>def signal(signalnum, handler):</pre></li>
                
                </ol>
              
              <ol start="58" class="context-line">
                <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre> <span>…</span></li>
              </ol>
              
                <ol start='59' class="post-context" id="post4345899520">
                  
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>    return _int_to_enum(handler, Handlers)</pre></li>
                  
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre></pre></li>
                  
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>@_wraps(_signal.getsignal)</pre></li>
                  
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>def getsignal(signalnum):</pre></li>
                  
                  <li onclick="toggle('pre4345899520', 'post4345899520')"><pre>    handler = _signal.getsignal(signalnum)</pre></li>
                  
              </ol>
              
            </div>
          

          
            
              <details>
                <summary class="commands">Local vars</summary>
            
            <table class="vars" id="v4345899520">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>handler</td>
                    <td class="code"><pre>&lt;function timeout_handler at 0x102d63e20&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>signalnum</td>
                    <td class="code"><pre>&lt;Signals.SIGALRM: 14&gt;</pre></td>
                  </tr>
                
              </tbody>
            </table>
            </details>
          
        </li>
      
    </ul>
  </div>

  <form action="https://dpaste.com/" name="pasteform" id="pasteform" method="post">
  <div id="pastebinTraceback" class="pastebin">
    <input type="hidden" name="language" value="PythonConsole">
    <input type="hidden" name="title"
      value="ValueError at /api/clinical/patients/">
    <input type="hidden" name="source" value="Django Dpaste Agent">
    <input type="hidden" name="poster" value="Django">
    <textarea name="content" id="traceback_area" cols="140" rows="25">
Environment:


Request Method: GET
Request URL: http://127.0.0.1:8000/api/clinical/patients/

Django Version: 4.2.24
Python Version: 3.13.7
Installed Applications:
[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]
Installed Middleware:
[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]



Traceback (most recent call last):
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/core/handlers/base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/decorators/csrf.py", line 56, in wrapper_view
    return view_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/django/views/generic/base.py", line 105, in view
    return self.dispatch(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 509, in dispatch
    response = self.handle_exception(exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 469, in handle_exception
    self.raise_uncaught_exception(exc)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 480, in raise_uncaught_exception
    raise exc
    ^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/views.py", line 506, in dispatch
    response = handler(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/lib/python3.13/site-packages/rest_framework/decorators.py", line 50, in handler
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/clinical/views.py", line 27, in wrapper
    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.13/3.13.7/Frameworks/Python.framework/Versions/3.13/lib/python3.13/signal.py", line 58, in signal
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Exception Type: ValueError at /api/clinical/patients/
Exception Value: signal only works in main thread of the main interpreter
</textarea>
  <br><br>
  <input type="submit" value="Share this traceback on a public website">
  </div>
</form>

</div>


<div id="requestinfo">
  <h2>Request information</h2>


  
    <h3 id="user-info">USER</h3>
    <p>AnonymousUser</p>
  

  <h3 id="get-info">GET</h3>
  
    <p>No GET data</p>
  

  <h3 id="post-info">POST</h3>
  
    <p>No POST data</p>
  

  <h3 id="files-info">FILES</h3>
  
    <p>No FILES data</p>
  

  <h3 id="cookie-info">COOKIES</h3>
  
    <p>No cookie data</p>
  

  <h3 id="meta-info">META</h3>
  <table class="req">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>COMMAND_MODE</td>
          <td class="code"><pre>&#x27;unix2003&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>COMPOSER_NO_INTERACTION</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_LENGTH</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CONTENT_TYPE</td>
          <td class="code"><pre>&#x27;application/json&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_AGENT</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CURSOR_TRACE_ID</td>
          <td class="code"><pre>&#x27;ddd83383dda4465892eb901d0c954b79&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DJANGO_SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ELECTRON_RUN_AS_NODE</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_COLOR</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>GATEWAY_INTERFACE</td>
          <td class="code"><pre>&#x27;CGI/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOME</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_CELLAR</td>
          <td class="code"><pre>&#x27;/opt/homebrew/Cellar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_PREFIX</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HOMEBREW_REPOSITORY</td>
          <td class="code"><pre>&#x27;/opt/homebrew&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT</td>
          <td class="code"><pre>&#x27;*/*&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_ACCEPT_ENCODING</td>
          <td class="code"><pre>&#x27;gzip, deflate, br, zstd&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_CONNECTION</td>
          <td class="code"><pre>&#x27;close&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_HOST</td>
          <td class="code"><pre>&#x27;127.0.0.1:8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_REFERER</td>
          <td class="code"><pre>&#x27;http://localhost:5174/consent&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA</td>
          <td class="code"><pre>&#x27;&quot;Chromium&quot;;v=&quot;134&quot;, &quot;Not:A-Brand&quot;;v=&quot;24&quot;, &quot;HeadlessChrome&quot;;v=&quot;134&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_MOBILE</td>
          <td class="code"><pre>&#x27;?0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_CH_UA_PLATFORM</td>
          <td class="code"><pre>&#x27;&quot;Windows&quot;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_DEST</td>
          <td class="code"><pre>&#x27;empty&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_MODE</td>
          <td class="code"><pre>&#x27;cors&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_SEC_FETCH_SITE</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_USER_AGENT</td>
          <td class="code"><pre>(&#x27;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  (KHTML, like &#x27;
 &#x27;Gecko) Chrome/85.0.4183.102 Safari/537.36&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_DEPARTMENTS</td>
          <td class="code"><pre>&#x27;Endocrinology&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_ROLES</td>
          <td class="code"><pre>&#x27;Doctor&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>HTTP_X_TENANT</td>
          <td class="code"><pre>&#x27;TENANT_A&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>INFOPATH</td>
          <td class="code"><pre>&#x27;/opt/homebrew/share/info:/opt/homebrew/share/info:&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LC_CTYPE</td>
          <td class="code"><pre>&#x27;UTF-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGNAME</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MallocNanoZone</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NO_COLOR</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>OLDPWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>ORIGINAL_XDG_CURRENT_DESKTOP</td>
          <td class="code"><pre>&#x27;undefined&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PATH_INFO</td>
          <td class="code"><pre>&#x27;/api/clinical/patients/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PS1</td>
          <td class="code"><pre>&#x27;(venv) &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PWD</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>QUERY_STRING</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_ADDR</td>
          <td class="code"><pre>&#x27;127.0.0.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REMOTE_HOST</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>REQUEST_METHOD</td>
          <td class="code"><pre>&#x27;GET&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>RUN_MAIN</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SCRIPT_NAME</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_NAME</td>
          <td class="code"><pre>&#x27;1.0.0.127.in-addr.arpa&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PORT</td>
          <td class="code"><pre>&#x27;8000&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_PROTOCOL</td>
          <td class="code"><pre>&#x27;HTTP/1.1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_SOFTWARE</td>
          <td class="code"><pre>&#x27;WSGIServer/0.2&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHELL</td>
          <td class="code"><pre>&#x27;/bin/zsh&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHLVL</td>
          <td class="code"><pre>&#x27;1&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SSH_AUTH_SOCK</td>
          <td class="code"><pre>&#x27;/private/tmp/com.apple.launchd.PdWErTWdSN/Listeners&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TERM</td>
          <td class="code"><pre>&#x27;dumb&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TMPDIR</td>
          <td class="code"><pre>&#x27;/var/folders/b7/btb0jl993p990q47gcqd5kjr0000gp/T/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TZ</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USER</td>
          <td class="code"><pre>&#x27;sujitkumar&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VIRTUAL_ENV_PROMPT</td>
          <td class="code"><pre>&#x27;venv&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CODE_CACHE_PATH</td>
          <td class="code"><pre>(&#x27;/Users/sujitkumar/Library/Application &#x27;
 &#x27;Support/Cursor/CachedData/b753cece5c67c47cb5637199a5a5de2b7100c180&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CRASH_REPORTER_PROCESS_TYPE</td>
          <td class="code"><pre>&#x27;extensionHost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_CWD</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_ESM_ENTRYPOINT</td>
          <td class="code"><pre>&#x27;vs/workbench/api/node/extensionHostProcess&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_HANDLES_UNCAUGHT_ERRORS</td>
          <td class="code"><pre>&#x27;true&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_IPC_HOOK</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Library/Application Support/Cursor/1.6.-main.sock&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_L10N_BUNDLE_LOCATION</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_NLS_CONFIG</td>
          <td class="code"><pre>&#x27;{&quot;userLocale&quot;:&quot;en-gb&quot;,&quot;osLocale&quot;:&quot;en-in&quot;,&quot;resolvedLanguage&quot;:&quot;en&quot;,&quot;defaultMessagesFile&quot;:&quot;/Applications/Cursor.app/Contents/Resources/app/out/nls.messages.json&quot;,&quot;locale&quot;:&quot;en-gb&quot;,&quot;availableLanguages&quot;:{}}&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PID</td>
          <td class="code"><pre>&#x27;20858&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>VSCODE_PROCESS_TITLE</td>
          <td class="code"><pre>&#x27;extension-host  [1-3]&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_FLAGS</td>
          <td class="code"><pre>&#x27;0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>XPC_SERVICE_NAME</td>
          <td class="code"><pre>&#x27;0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>_</td>
          <td class="code"><pre>&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/venv/bin/python&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CFBundleIdentifier</td>
          <td class="code"><pre>&#x27;com.todesktop.230313mzl4w4u92&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>__CF_USER_TEXT_ENCODING</td>
          <td class="code"><pre>&#x27;0x1F6:0x0:0x0&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.errors</td>
          <td class="code"><pre>&lt;_io.TextIOWrapper name=&#x27;&lt;stderr&gt;&#x27; mode=&#x27;w&#x27; encoding=&#x27;utf-8&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.file_wrapper</td>
          <td class="code"><pre>&lt;class &#x27;wsgiref.util.FileWrapper&#x27;&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.input</td>
          <td class="code"><pre>&lt;django.core.handlers.wsgi.LimitedStream object at 0x1031298a0&gt;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multiprocess</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.multithread</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.run_once</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.url_scheme</td>
          <td class="code"><pre>&#x27;http&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>wsgi.version</td>
          <td class="code"><pre>(1, 0)</pre></td>
        </tr>
      
    </tbody>
  </table>


  <h3 id="settings-info">Settings</h3>
  <h4>Using settings module <code>diabetes_poc.settings</code></h4>
  <table class="req">
    <thead>
      <tr>
        <th>Setting</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      
        <tr>
          <td>ABSOLUTE_URL_OVERRIDES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>ADMINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>ALLOWED_HOSTS</td>
          <td class="code"><pre>[&#x27;*&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>APPEND_SLASH</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>AUTHENTICATION_BACKENDS</td>
          <td class="code"><pre>[&#x27;django.contrib.auth.backends.ModelBackend&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_PASSWORD_VALIDATORS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>AUTH_USER_MODEL</td>
          <td class="code"><pre>&#x27;auth.User&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>BASE_DIR</td>
          <td class="code"><pre>PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server&#x27;)</pre></td>
        </tr>
      
        <tr>
          <td>CACHES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.cache.backends.locmem.LocMemCache&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_KEY_PREFIX</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CACHE_MIDDLEWARE_SECONDS</td>
          <td class="code"><pre>600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_AGE</td>
          <td class="code"><pre>31449600</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_MASKED</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;csrftoken&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_FAILURE_VIEW</td>
          <td class="code"><pre>&#x27;django.views.csrf.csrf_failure&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_HEADER_NAME</td>
          <td class="code"><pre>&#x27;HTTP_X_CSRFTOKEN&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_TRUSTED_ORIGINS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>CSRF_USE_SESSIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DATABASES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;ATOMIC_REQUESTS&#x27;: False,
             &#x27;AUTOCOMMIT&#x27;: True,
             &#x27;CONN_HEALTH_CHECKS&#x27;: False,
             &#x27;CONN_MAX_AGE&#x27;: 0,
             &#x27;ENGINE&#x27;: &#x27;django.db.backends.sqlite3&#x27;,
             &#x27;HOST&#x27;: &#x27;&#x27;,
             &#x27;NAME&#x27;: PosixPath(&#x27;/Users/sujitkumar/Desktop/lcnc/hospital_lcnc/server/db.sqlite3&#x27;),
             &#x27;OPTIONS&#x27;: {},
             &#x27;PASSWORD&#x27;: &#x27;********************&#x27;,
             &#x27;PORT&#x27;: &#x27;&#x27;,
             &#x27;TEST&#x27;: {&#x27;CHARSET&#x27;: None,
                      &#x27;COLLATION&#x27;: None,
                      &#x27;MIGRATE&#x27;: True,
                      &#x27;MIRROR&#x27;: None,
                      &#x27;NAME&#x27;: None},
             &#x27;TIME_ZONE&#x27;: None,
             &#x27;USER&#x27;: &#x27;&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>DATABASE_ROUTERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FIELDS</td>
          <td class="code"><pre>1000</pre></td>
        </tr>
      
        <tr>
          <td>DATA_UPLOAD_MAX_NUMBER_FILES</td>
          <td class="code"><pre>100</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y, P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATETIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d %H:%M:%S&#x27;,
 &#x27;%Y-%m-%d %H:%M:%S.%f&#x27;,
 &#x27;%Y-%m-%d %H:%M&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S&#x27;,
 &#x27;%m/%d/%Y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%Y %H:%M&#x27;,
 &#x27;%m/%d/%y %H:%M:%S&#x27;,
 &#x27;%m/%d/%y %H:%M:%S.%f&#x27;,
 &#x27;%m/%d/%y %H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DATE_FORMAT</td>
          <td class="code"><pre>&#x27;N j, Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DATE_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%Y-%m-%d&#x27;,
 &#x27;%m/%d/%Y&#x27;,
 &#x27;%m/%d/%y&#x27;,
 &#x27;%b %d %Y&#x27;,
 &#x27;%b %d, %Y&#x27;,
 &#x27;%d %b %Y&#x27;,
 &#x27;%d %b, %Y&#x27;,
 &#x27;%B %d %Y&#x27;,
 &#x27;%B %d, %Y&#x27;,
 &#x27;%d %B %Y&#x27;,
 &#x27;%d %B, %Y&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>DB_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>DEBUG_PROPAGATE_EXCEPTIONS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>DECIMAL_SEPARATOR</td>
          <td class="code"><pre>&#x27;.&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_AUTO_FIELD</td>
          <td class="code"><pre>&#x27;django.db.models.BigAutoField&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_CHARSET</td>
          <td class="code"><pre>&#x27;utf-8&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER</td>
          <td class="code"><pre>&#x27;django.views.debug.ExceptionReporter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_EXCEPTION_REPORTER_FILTER</td>
          <td class="code"><pre>&#x27;django.views.debug.SafeExceptionReporterFilter&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FILE_STORAGE</td>
          <td class="code"><pre>&#x27;django.core.files.storage.FileSystemStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_FROM_EMAIL</td>
          <td class="code"><pre>&#x27;webmaster@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_INDEX_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DEFAULT_TABLESPACE</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>DISALLOWED_USER_AGENTS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.mail.backends.smtp.EmailBackend&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST</td>
          <td class="code"><pre>&#x27;localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_PASSWORD</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_HOST_USER</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_PORT</td>
          <td class="code"><pre>25</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_CERTFILE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SSL_KEYFILE</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_SUBJECT_PREFIX</td>
          <td class="code"><pre>&#x27;[Django] &#x27;</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_TIMEOUT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_LOCALTIME</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_SSL</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>EMAIL_USE_TLS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_DIRECTORY_PERMISSIONS</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_HANDLERS</td>
          <td class="code"><pre>[&#x27;django.core.files.uploadhandler.MemoryFileUploadHandler&#x27;,
 &#x27;django.core.files.uploadhandler.TemporaryFileUploadHandler&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_MAX_MEMORY_SIZE</td>
          <td class="code"><pre>2621440</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_PERMISSIONS</td>
          <td class="code"><pre>420</pre></td>
        </tr>
      
        <tr>
          <td>FILE_UPLOAD_TEMP_DIR</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FIRST_DAY_OF_WEEK</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>FIXTURE_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>FORCE_SCRIPT_NAME</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORMAT_MODULE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>FORM_RENDERER</td>
          <td class="code"><pre>&#x27;django.forms.renderers.DjangoTemplates&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>IGNORABLE_404_URLS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>INSTALLED_APPS</td>
          <td class="code"><pre>[&#x27;django.contrib.admin&#x27;,
 &#x27;django.contrib.auth&#x27;,
 &#x27;django.contrib.contenttypes&#x27;,
 &#x27;django.contrib.sessions&#x27;,
 &#x27;django.contrib.messages&#x27;,
 &#x27;django.contrib.staticfiles&#x27;,
 &#x27;rest_framework&#x27;,
 &#x27;core&#x27;,
 &#x27;quotas&#x27;,
 &#x27;consent&#x27;,
 &#x27;configurator&#x27;,
 &#x27;runtime_engine&#x27;,
 &#x27;submission&#x27;,
 &#x27;clinical&#x27;,
 &#x27;orchestrator&#x27;,
 &#x27;extensions&#x27;,
 &#x27;policies&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>INTERNAL_IPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES</td>
          <td class="code"><pre>[(&#x27;af&#x27;, &#x27;Afrikaans&#x27;),
 (&#x27;ar&#x27;, &#x27;Arabic&#x27;),
 (&#x27;ar-dz&#x27;, &#x27;Algerian Arabic&#x27;),
 (&#x27;ast&#x27;, &#x27;Asturian&#x27;),
 (&#x27;az&#x27;, &#x27;Azerbaijani&#x27;),
 (&#x27;bg&#x27;, &#x27;Bulgarian&#x27;),
 (&#x27;be&#x27;, &#x27;Belarusian&#x27;),
 (&#x27;bn&#x27;, &#x27;Bengali&#x27;),
 (&#x27;br&#x27;, &#x27;Breton&#x27;),
 (&#x27;bs&#x27;, &#x27;Bosnian&#x27;),
 (&#x27;ca&#x27;, &#x27;Catalan&#x27;),
 (&#x27;ckb&#x27;, &#x27;Central Kurdish (Sorani)&#x27;),
 (&#x27;cs&#x27;, &#x27;Czech&#x27;),
 (&#x27;cy&#x27;, &#x27;Welsh&#x27;),
 (&#x27;da&#x27;, &#x27;Danish&#x27;),
 (&#x27;de&#x27;, &#x27;German&#x27;),
 (&#x27;dsb&#x27;, &#x27;Lower Sorbian&#x27;),
 (&#x27;el&#x27;, &#x27;Greek&#x27;),
 (&#x27;en&#x27;, &#x27;English&#x27;),
 (&#x27;en-au&#x27;, &#x27;Australian English&#x27;),
 (&#x27;en-gb&#x27;, &#x27;British English&#x27;),
 (&#x27;eo&#x27;, &#x27;Esperanto&#x27;),
 (&#x27;es&#x27;, &#x27;Spanish&#x27;),
 (&#x27;es-ar&#x27;, &#x27;Argentinian Spanish&#x27;),
 (&#x27;es-co&#x27;, &#x27;Colombian Spanish&#x27;),
 (&#x27;es-mx&#x27;, &#x27;Mexican Spanish&#x27;),
 (&#x27;es-ni&#x27;, &#x27;Nicaraguan Spanish&#x27;),
 (&#x27;es-ve&#x27;, &#x27;Venezuelan Spanish&#x27;),
 (&#x27;et&#x27;, &#x27;Estonian&#x27;),
 (&#x27;eu&#x27;, &#x27;Basque&#x27;),
 (&#x27;fa&#x27;, &#x27;Persian&#x27;),
 (&#x27;fi&#x27;, &#x27;Finnish&#x27;),
 (&#x27;fr&#x27;, &#x27;French&#x27;),
 (&#x27;fy&#x27;, &#x27;Frisian&#x27;),
 (&#x27;ga&#x27;, &#x27;Irish&#x27;),
 (&#x27;gd&#x27;, &#x27;Scottish Gaelic&#x27;),
 (&#x27;gl&#x27;, &#x27;Galician&#x27;),
 (&#x27;he&#x27;, &#x27;Hebrew&#x27;),
 (&#x27;hi&#x27;, &#x27;Hindi&#x27;),
 (&#x27;hr&#x27;, &#x27;Croatian&#x27;),
 (&#x27;hsb&#x27;, &#x27;Upper Sorbian&#x27;),
 (&#x27;hu&#x27;, &#x27;Hungarian&#x27;),
 (&#x27;hy&#x27;, &#x27;Armenian&#x27;),
 (&#x27;ia&#x27;, &#x27;Interlingua&#x27;),
 (&#x27;id&#x27;, &#x27;Indonesian&#x27;),
 (&#x27;ig&#x27;, &#x27;Igbo&#x27;),
 (&#x27;io&#x27;, &#x27;Ido&#x27;),
 (&#x27;is&#x27;, &#x27;Icelandic&#x27;),
 (&#x27;it&#x27;, &#x27;Italian&#x27;),
 (&#x27;ja&#x27;, &#x27;Japanese&#x27;),
 (&#x27;ka&#x27;, &#x27;Georgian&#x27;),
 (&#x27;kab&#x27;, &#x27;Kabyle&#x27;),
 (&#x27;kk&#x27;, &#x27;Kazakh&#x27;),
 (&#x27;km&#x27;, &#x27;Khmer&#x27;),
 (&#x27;kn&#x27;, &#x27;Kannada&#x27;),
 (&#x27;ko&#x27;, &#x27;Korean&#x27;),
 (&#x27;ky&#x27;, &#x27;Kyrgyz&#x27;),
 (&#x27;lb&#x27;, &#x27;Luxembourgish&#x27;),
 (&#x27;lt&#x27;, &#x27;Lithuanian&#x27;),
 (&#x27;lv&#x27;, &#x27;Latvian&#x27;),
 (&#x27;mk&#x27;, &#x27;Macedonian&#x27;),
 (&#x27;ml&#x27;, &#x27;Malayalam&#x27;),
 (&#x27;mn&#x27;, &#x27;Mongolian&#x27;),
 (&#x27;mr&#x27;, &#x27;Marathi&#x27;),
 (&#x27;ms&#x27;, &#x27;Malay&#x27;),
 (&#x27;my&#x27;, &#x27;Burmese&#x27;),
 (&#x27;nb&#x27;, &#x27;Norwegian Bokmål&#x27;),
 (&#x27;ne&#x27;, &#x27;Nepali&#x27;),
 (&#x27;nl&#x27;, &#x27;Dutch&#x27;),
 (&#x27;nn&#x27;, &#x27;Norwegian Nynorsk&#x27;),
 (&#x27;os&#x27;, &#x27;Ossetic&#x27;),
 (&#x27;pa&#x27;, &#x27;Punjabi&#x27;),
 (&#x27;pl&#x27;, &#x27;Polish&#x27;),
 (&#x27;pt&#x27;, &#x27;Portuguese&#x27;),
 (&#x27;pt-br&#x27;, &#x27;Brazilian Portuguese&#x27;),
 (&#x27;ro&#x27;, &#x27;Romanian&#x27;),
 (&#x27;ru&#x27;, &#x27;Russian&#x27;),
 (&#x27;sk&#x27;, &#x27;Slovak&#x27;),
 (&#x27;sl&#x27;, &#x27;Slovenian&#x27;),
 (&#x27;sq&#x27;, &#x27;Albanian&#x27;),
 (&#x27;sr&#x27;, &#x27;Serbian&#x27;),
 (&#x27;sr-latn&#x27;, &#x27;Serbian Latin&#x27;),
 (&#x27;sv&#x27;, &#x27;Swedish&#x27;),
 (&#x27;sw&#x27;, &#x27;Swahili&#x27;),
 (&#x27;ta&#x27;, &#x27;Tamil&#x27;),
 (&#x27;te&#x27;, &#x27;Telugu&#x27;),
 (&#x27;tg&#x27;, &#x27;Tajik&#x27;),
 (&#x27;th&#x27;, &#x27;Thai&#x27;),
 (&#x27;tk&#x27;, &#x27;Turkmen&#x27;),
 (&#x27;tr&#x27;, &#x27;Turkish&#x27;),
 (&#x27;tt&#x27;, &#x27;Tatar&#x27;),
 (&#x27;udm&#x27;, &#x27;Udmurt&#x27;),
 (&#x27;uk&#x27;, &#x27;Ukrainian&#x27;),
 (&#x27;ur&#x27;, &#x27;Urdu&#x27;),
 (&#x27;uz&#x27;, &#x27;Uzbek&#x27;),
 (&#x27;vi&#x27;, &#x27;Vietnamese&#x27;),
 (&#x27;zh-hans&#x27;, &#x27;Simplified Chinese&#x27;),
 (&#x27;zh-hant&#x27;, &#x27;Traditional Chinese&#x27;)]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGES_BIDI</td>
          <td class="code"><pre>[&#x27;he&#x27;, &#x27;ar&#x27;, &#x27;ar-dz&#x27;, &#x27;ckb&#x27;, &#x27;fa&#x27;, &#x27;ur&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_CODE</td>
          <td class="code"><pre>&#x27;en-us&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_AGE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_HTTPONLY</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;django_language&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SAMESITE</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>LANGUAGE_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>LOCALE_PATHS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>LOGGING_CONFIG</td>
          <td class="code"><pre>&#x27;logging.config.dictConfig&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_REDIRECT_URL</td>
          <td class="code"><pre>&#x27;/accounts/profile/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGIN_URL</td>
          <td class="code"><pre>&#x27;/accounts/login/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>LOGOUT_REDIRECT_URL</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>MANAGERS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_ROOT</td>
          <td class="code"><pre>&#x27;&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MEDIA_URL</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MESSAGE_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.messages.storage.fallback.FallbackStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>MIDDLEWARE</td>
          <td class="code"><pre>[&#x27;django.middleware.security.SecurityMiddleware&#x27;,
 &#x27;django.contrib.sessions.middleware.SessionMiddleware&#x27;,
 &#x27;django.middleware.common.CommonMiddleware&#x27;,
 &#x27;django.middleware.csrf.CsrfViewMiddleware&#x27;,
 &#x27;django.contrib.auth.middleware.AuthenticationMiddleware&#x27;,
 &#x27;django.contrib.messages.middleware.MessageMiddleware&#x27;,
 &#x27;django.middleware.clickjacking.XFrameOptionsMiddleware&#x27;,
 &#x27;core.middleware.TenantContextMiddleware&#x27;,
 &#x27;policies.middleware.ClaimsMiddleware&#x27;,
 &#x27;consent.audit_middleware.AuditMiddleware&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>MIGRATION_MODULES</td>
          <td class="code"><pre>{}</pre></td>
        </tr>
      
        <tr>
          <td>MONTH_DAY_FORMAT</td>
          <td class="code"><pre>&#x27;F j&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>NUMBER_GROUPING</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_HASHERS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PASSWORD_RESET_TIMEOUT</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>PREPEND_WWW</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>REST_FRAMEWORK</td>
          <td class="code"><pre>{&#x27;DEFAULT_AUTHENTICATION_CLASSES&#x27;: [],
 &#x27;DEFAULT_PERMISSION_CLASSES&#x27;: [&#x27;rest_framework.permissions.AllowAny&#x27;]}</pre></td>
        </tr>
      
        <tr>
          <td>ROOT_URLCONF</td>
          <td class="code"><pre>&#x27;diabetes_poc.urls&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECRET_KEY_FALLBACKS</td>
          <td class="code"><pre>&#x27;********************&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CONTENT_TYPE_NOSNIFF</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_CROSS_ORIGIN_OPENER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_INCLUDE_SUBDOMAINS</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_PRELOAD</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_HSTS_SECONDS</td>
          <td class="code"><pre>0</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_PROXY_SSL_HEADER</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REDIRECT_EXEMPT</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_REFERRER_POLICY</td>
          <td class="code"><pre>&#x27;same-origin&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_HOST</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SECURE_SSL_REDIRECT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SERVER_EMAIL</td>
          <td class="code"><pre>&#x27;root@localhost&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_CACHE_ALIAS</td>
          <td class="code"><pre>&#x27;default&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_AGE</td>
          <td class="code"><pre>1209600</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_DOMAIN</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_HTTPONLY</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_NAME</td>
          <td class="code"><pre>&#x27;sessionid&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_PATH</td>
          <td class="code"><pre>&#x27;/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SAMESITE</td>
          <td class="code"><pre>&#x27;Lax&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_COOKIE_SECURE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_ENGINE</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.backends.db&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_EXPIRE_AT_BROWSER_CLOSE</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_FILE_PATH</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SAVE_EVERY_REQUEST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>SESSION_SERIALIZER</td>
          <td class="code"><pre>&#x27;django.contrib.sessions.serializers.JSONSerializer&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SETTINGS_MODULE</td>
          <td class="code"><pre>&#x27;diabetes_poc.settings&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATETIME_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SHORT_DATE_FORMAT</td>
          <td class="code"><pre>&#x27;m/d/Y&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SIGNING_BACKEND</td>
          <td class="code"><pre>&#x27;django.core.signing.TimestampSigner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>SILENCED_SYSTEM_CHECKS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_DIRS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_FINDERS</td>
          <td class="code"><pre>[&#x27;django.contrib.staticfiles.finders.FileSystemFinder&#x27;,
 &#x27;django.contrib.staticfiles.finders.AppDirectoriesFinder&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>STATICFILES_STORAGE</td>
          <td class="code"><pre>&#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_ROOT</td>
          <td class="code"><pre>None</pre></td>
        </tr>
      
        <tr>
          <td>STATIC_URL</td>
          <td class="code"><pre>&#x27;/static/&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>STORAGES</td>
          <td class="code"><pre>{&#x27;default&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.core.files.storage.FileSystemStorage&#x27;},
 &#x27;staticfiles&#x27;: {&#x27;BACKEND&#x27;: &#x27;django.contrib.staticfiles.storage.StaticFilesStorage&#x27;}}</pre></td>
        </tr>
      
        <tr>
          <td>TEMPLATES</td>
          <td class="code"><pre>[{&#x27;APP_DIRS&#x27;: True,
  &#x27;BACKEND&#x27;: &#x27;django.template.backends.django.DjangoTemplates&#x27;,
  &#x27;DIRS&#x27;: [],
  &#x27;OPTIONS&#x27;: {&#x27;context_processors&#x27;: [&#x27;django.template.context_processors.debug&#x27;,
                                     &#x27;django.template.context_processors.request&#x27;,
                                     &#x27;django.contrib.auth.context_processors.auth&#x27;,
                                     &#x27;django.contrib.messages.context_processors.messages&#x27;]}}]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_NON_SERIALIZED_APPS</td>
          <td class="code"><pre>[]</pre></td>
        </tr>
      
        <tr>
          <td>TEST_RUNNER</td>
          <td class="code"><pre>&#x27;django.test.runner.DiscoverRunner&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>THOUSAND_SEPARATOR</td>
          <td class="code"><pre>&#x27;,&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_FORMAT</td>
          <td class="code"><pre>&#x27;P&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>TIME_INPUT_FORMATS</td>
          <td class="code"><pre>[&#x27;%H:%M:%S&#x27;, &#x27;%H:%M:%S.%f&#x27;, &#x27;%H:%M&#x27;]</pre></td>
        </tr>
      
        <tr>
          <td>TIME_ZONE</td>
          <td class="code"><pre>&#x27;Asia/Kolkata&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>USE_DEPRECATED_PYTZ</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_I18N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_L10N</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_THOUSAND_SEPARATOR</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_TZ</td>
          <td class="code"><pre>True</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_HOST</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>USE_X_FORWARDED_PORT</td>
          <td class="code"><pre>False</pre></td>
        </tr>
      
        <tr>
          <td>WSGI_APPLICATION</td>
          <td class="code"><pre>&#x27;diabetes_poc.wsgi.application&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>X_FRAME_OPTIONS</td>
          <td class="code"><pre>&#x27;DENY&#x27;</pre></td>
        </tr>
      
        <tr>
          <td>YEAR_MONTH_FORMAT</td>
          <td class="code"><pre>&#x27;F Y&#x27;</pre></td>
        </tr>
      
    </tbody>
  </table>

</div>

  <div id="explanation">
    <p>
      You’re seeing this error because you have <code>DEBUG = True</code> in your
      Django settings file. Change that to <code>False</code>, and Django will
      display a standard page generated by the handler for this status code.
    </p>
  </div>

</body>
</html>

    at api (http://localhost:5174/src/lib/api.js:36:11)
    at async loadPatients (http://localhost:5174/src/pages/ConsentManagement.jsx:70:20) (at http://localhost:5174/src/pages/ConsentManagement.jsx:72:14)
- **Test Visualization and Result:** https://www.testsprite.com/dashboard/mcp/tests/8c77ac61-0d96-4082-8757-1fa4cf0383c1/2e488cce-3535-4d49-9f78-31c5a1bf1c38
- **Status:** ❌ Failed
- **Analysis / Findings:** {{TODO:AI_ANALYSIS}}.
---


## 3️⃣ Coverage & Matching Metrics

- **6.67** of tests passed

| Requirement        | Total Tests | ✅ Passed | ❌ Failed  |
|--------------------|-------------|-----------|------------|
| ...                | ...         | ...       | ...        |
---


## 4️⃣ Key Gaps / Risks
{AI_GNERATED_KET_GAPS_AND_RISKS}
---
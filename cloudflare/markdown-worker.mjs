// Optional: paste this ES module into a Cloudflare Worker.
// Use a Route in front of the existing GitHub Pages origin, not a Custom Domain.
// No Cloudflare API token or Workers AI binding needed.
function markdownPath(path) {
  if(path==="/"||path==="/index.html")return "/index.md";
  if(path==="/cv.html")return "/cv.md";
  const m=path.match(/^\/papers\/([a-z0-9-]+)\/(?:index\.html)?$/);
  return m?`/papers/${m[1]}/index.md`:null;
}
function prefersMarkdown(header) {
  const entries=header.toLowerCase().split(",").map(x=>{
    const [type,...params]=x.trim().split(";").map(x=>x.trim());
    const q=params.find(x=>x.startsWith("q="));
    return {type,q:q?Number(q.slice(2)):1};
  }).filter(x=>Number.isFinite(x.q)&&x.q>=0&&x.q<=1);
  const md=entries.filter(x=>x.type==="text/markdown").reduce((m,x)=>Math.max(m,x.q),0);
  const html=entries.filter(x=>x.type==="text/html").reduce((m,x)=>Math.max(m,x.q),0);
  return md>0&&md>=html;
}
function addVary(headers) {
  const vary=headers.get("Vary")||"";
  if(vary.trim()!=="*"&&!vary.toLowerCase().split(",").map(x=>x.trim()).includes("accept"))headers.set("Vary",vary?vary+", Accept":"Accept");
}
export default {
  async fetch(request) {
    const url=new URL(request.url);
    if(url.hostname!=="amahrous.com"||!["GET","HEAD"].includes(request.method))return fetch(request);
    const path=markdownPath(url.pathname);
    if(!path)return fetch(request);
    if(prefersMarkdown(request.headers.get("Accept")||"")) {
      try {
        const md=new URL(path,url.origin);
        // Public static file only; no forwarded credentials or conditional headers.
        const response=await fetch(new Request(md,{method:request.method,headers:{"Accept":"*/*"},redirect:"manual"}));
        const type=response.headers.get("Content-Type")||"";
        if(response.status===200&&!/text\/html|application\/xhtml/i.test(type)){
          const headers=new Headers(response.headers);
          for(const name of ["Content-Disposition","Content-Length","Content-Encoding","Content-Range","ETag","Last-Modified","Age","Expires"])headers.delete(name);
          headers.set("Content-Type","text/markdown; charset=utf-8");
          headers.set("X-Content-Type-Options","nosniff");
          // Avoid sharing a cached Markdown variant at the canonical HTML URL.
          headers.set("Cache-Control","private, no-store");
          addVary(headers);
          return new Response(request.method==="HEAD"?null:response.body,{status:200,headers});
        }
      } catch (_) { /* Preserve the normal site if Markdown is unavailable. */ }
    }
    const response=await fetch(request);
    const headers=new Headers(response.headers);
    addVary(headers);
    return new Response(response.body,{status:response.status,statusText:response.statusText,headers});
  }
};
export {markdownPath,prefersMarkdown,addVary};

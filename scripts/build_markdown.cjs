// Generated Markdown uses only the public, built HTML and publication metadata.
// No npm packages or model inference required. Node.js 18+.
function buildMarkdown(pages, papers, origin="https://amahrous.com") {
  const voids=new Set("area base br col embed hr img input link meta param source track wbr".split(" "));
  const named={amp:"&",lt:"<",gt:">",quot:'"',apos:"'",nbsp:" ",ndash:"–",mdash:"—",hellip:"…",minus:"−",times:"×",middot:"·",copy:"©",reg:"®"};
  const decode=s=>s.replace(/&(#x[0-9a-f]+|#[0-9]+|[a-z][a-z0-9]*);/gi,(m,k)=>{if(k[0]!=="#")return named[k]??m;const n=k[1].toLowerCase()==="x"?parseInt(k.slice(2),16):parseInt(k.slice(1),10);return n>0&&n<=0x10ffff?String.fromCodePoint(n):m});
  const esc=s=>s.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
  const mdtext=s=>s.replace(/[\\`*_[\]<>]/g,"\\$&");
  function parse(html){
    const root={tag:"root",a:{},c:[]};const stack=[root];
    html=html.replace(/<(script|style)\b[^>]*>[\s\S]*?<\/\1\s*>/gi,"");
    const tokens=html.match(/<!--[\s\S]*?-->|<![^>]*>|<\/?[A-Za-z][\w:.-]*(?:[^"'<>]|"[^"]*"|'[^']*')*>|[^<]+|</g)||[];
    for(const t of tokens){
      const cur=()=>stack[stack.length-1];
      if(t.startsWith("<!"))continue;
      const end=t.match(/^<\/([\w:.-]+)/);
      if(end){const tag=end[1].toLowerCase();for(let i=stack.length-1;i>0;i--)if(stack[i].tag===tag){stack.length=i;break}continue;}
      const start=t.match(/^<([A-Za-z][\w:.-]*)/);
      if(!start){cur().c.push(decode(t));continue;}
      const tag=start[1].toLowerCase(),a={};
      for(const m of t.slice(start[0].length,-1).matchAll(/([^\s=\/>]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>]+)))?/g))a[m[1].toLowerCase()]=decode(m[2]??m[3]??m[4]??"");
      // Accommodate implicit closing tags in tables and lists.
      if(["tr","td","th","li","p"].includes(tag)){
        const close=(tag==="td"||tag==="th")?["td","th"]:[tag];
        if(close.includes(cur().tag))stack.pop();
      }
      const node={tag,a,c:[]};cur().c.push(node);
      if(!voids.has(tag)&&!t.endsWith("/>"))stack.push(node);
    }
    return root;
  }
  const all=(n,p)=>typeof n==="string"?[]:[...(p(n)?[n]:[]),...n.c.flatMap(x=>all(x,p))];
  const plain=n=>typeof n==="string"?n:n.c.map(plain).join("");
  const cls=(n,c)=>(n.a.class||"").split(/\s+/).includes(c);
  const first=(n,p)=>all(n,p)[0];
  const norm=s=>s.replace(/\s+/g," ").trim();
  function absolute(h,base){
    if(!h)return "";
    if(/^(https?:|mailto:|tel:)/i.test(h))return h;
    if(h.startsWith("//"))return "https:"+h;
    if(/^[a-z][a-z0-9+.-]*:/i.test(h))return "";
    if(h.startsWith("#")||h.startsWith("?"))return base+h;
    const path=base.slice(origin.length).split(/[?#]/)[0];
    const raw=h.startsWith("/")?h:path.slice(0,path.lastIndexOf("/")+1)+h;
    const cut=raw.search(/[?#]/), tail=cut<0?"":raw.slice(cut), body=cut<0?raw:raw.slice(0,cut);
    const out=[];for(const s of body.split("/")){if(!s||s===".")continue;if(s==="..")out.pop();else out.push(s);}
    return origin+"/"+out.join("/")+(body.endsWith("/")&&out.length?"/":"")+tail;
  }
  const target=s=>s.replace(/ /g,"%20").replace(/\(/g,"%28").replace(/\)/g,"%29").replace(/</g,"%3C").replace(/>/g,"%3E");
  const mdLink=(label,url)=>url?`[${label}](${target(url)})`:label;
  function tex(n){
    const ann=first(n,x=>x.tag==="annotation"&&x.a.encoding==="application/x-tex");
    return (ann?plain(ann):n.a.alttext||plain(n)).trim();
  }
  const outputs={}, report=[];
  for(const page of pages){
    const tree=parse(page.html);
    const body=first(tree,n=>n.tag==="body");
    if(!body)throw Error("Missing body: "+page.path);
    const title=norm(plain(first(tree,n=>n.tag==="title")));
    const base=origin+"/"+(page.path.endsWith("index.html")?page.path.slice(0,-10):page.path);
    const mdPath=page.path.replace(/\.html$/,".md");
    const scope=page.path==="cv.html"?first(body,n=>cls(n,"cv-screen")):body;
    if(!scope)throw Error("Missing scope: "+page.path);
    const skip=n=>["head","nav","script","style","button"].includes(n.tag)||cls(n,"print-button")||cls(n,"cv-print")||cls(n,"paper-nav");
    function image(n,anchor){
      const label=norm(n.a.alt||"Figure");
      const url=n.a.src?.startsWith("data:")?base+"#"+(n.a.id||anchor||"full-text"):absolute(n.a.src||"",base);
      return {label,url,embedded:n.a.src?.startsWith("data:")};
    }
    function tableHTML(n,anchor){
      if(typeof n==="string")return esc(n);
      if(skip(n))return "";
      const a=n.a,tag=n.tag;
      if(tag==="math")return esc((a.display==="block"?"$$":"$")+tex(n)+(a.display==="block"?"$$":"$"));
      if(tag==="img"){const im=image(n,anchor);return `<a href="${esc(im.url)}">${esc(im.label)}${im.embedded?" (see source figure)":""}</a>`;}
      const inside=n.c.map(x=>tableHTML(x,a.id||anchor)).join("");
      if(tag==="a"){const url=absolute(a.href||"",base);return url?`<a href="${esc(url)}">${inside}</a>`:inside;}
      const allowed=new Set(["table","caption","thead","tbody","tfoot","tr","td","th","colgroup","col","sub","sup","em","i","strong","b","code","br","p","ul","ol","li"]);
      if(!allowed.has(tag))return inside;
      const at=["rowspan","colspan","scope","span"].filter(k=>a[k]&&/^[\w-]+$/.test(a[k])).map(k=>` ${k}="${esc(a[k])}"`).join("");
      return `<${tag}${at}>${voids.has(tag)?"":inside+`</${tag}>`}`;
    }
    function render(n,anchor="",depth=0){
      if(typeof n==="string")return mdtext(n.replace(/\s+/g," "));
      if(skip(n))return "";
      const tag=n.tag,a=n.a,next=a.id||anchor;
      if(tag==="math"){const t=tex(n);return a.display==="block"?`\n\n$$\n${t}\n$$\n\n`:`$${t}$`;}
      if(tag==="pre"){const t=plain(n).trimEnd(),runs=t.match(/`+/g)||[], fence="`".repeat(Math.max(3,...runs.map(r=>r.length+1)));return `\n\n${fence}${anchor==="citation"?"bibtex":""}\n${t}\n${fence}\n\n`;}
      if(tag==="img"){const im=image(n,anchor);return im.embedded?mdLink(mdtext(im.label+" (figure in original article)"),im.url):im.url?`![${mdtext(im.label)}](${target(im.url)})`:mdtext(im.label);}
      if(tag==="table")return "\n\n"+tableHTML(n,next)+"\n\n";
      if(tag==="br")return "  \n";
      if(tag==="hr")return "\n\n---\n\n";
      if(tag==="ul"||tag==="ol"){
        let i=0;return "\n"+n.c.map(x=>typeof x!=="string"&&x.tag==="li"?`${"  ".repeat(depth)}${tag==="ol"?++i+".":"-"} ${x.c.map(y=>render(y,next,depth+1)).join("").trim().replace(/\n(?!\n)/g,"\n"+ "  ".repeat(depth+1))}`:render(x,next,depth)).join("\n")+"\n\n";
      }
      const content=n.c.map(x=>render(x,next,depth)).join("");
      if(/^h[1-6]$/.test(tag))return `\n\n${"#".repeat(Number(tag[1]))} ${content.trim()}\n\n`;
      if(tag==="a")return mdLink(content.trim()||mdtext(a.title||a.href||""),absolute(a.href||"",base));
      if(tag==="strong"||tag==="b")return content.trim()?`**${content.trim()}**`:"";
      if(tag==="em"||tag==="i")return content.trim()?`*${content.trim()}*`:"";
      if(tag==="code"){const t=plain(n),fence="`".repeat(Math.max(1,...(t.match(/`+/g)||[]).map(x=>x.length+1)));return `${fence} ${t} ${fence}`;}
      if(tag==="sup"||tag==="sub")return `<${tag}>${content}</${tag}>`;
      if(tag==="blockquote")return "\n\n"+content.trim().split("\n").map(x=>"> "+x).join("\n")+"\n\n";
      if(["p","div","main","article","section","header","footer","figure","figcaption","details","summary","aside","li"].includes(tag))return "\n\n"+content.trim()+"\n\n";
      return content;
    }
    let content=render(scope).trim().replace(/\n[ \t]+\n/g,"\n\n").replace(/\n{3,}/g,"\n\n");
    const paper=papers.find(p=>page.path===`papers/${p.slug}/index.html`);
    if(!content.startsWith("# "))content="# "+(paper?paper.title:page.path==="index.html"?"Ahmed Mahrous — Academic Homepage":title)+"\n\n"+content;
    const lineEnd=content.indexOf("\n");
    content=content.slice(0,lineEnd)+"\n\nSource: "+mdLink(base,base)+"\n"+content.slice(lineEnd);
    content=content.replace(/\n{3,}/g,"\n\n").trim()+"\n";
    if(paper){
      for(const id of ["tldr","abstract","citation","full-text"])if(!first(scope,n=>n.a.id===id))throw Error(`Missing ${id}: ${paper.slug}`);
      if(!content.includes("## Abstract")||!content.includes("## Full text")||!content.includes("## Citation")||!content.includes("```bibtex"))throw Error("Missing required Markdown sections: "+paper.slug);
      if(!content.includes(paper.title))throw Error("Missing title: "+paper.slug);
    }
    if(content.includes("data:image/"))throw Error("Embedded image payload: "+page.path);
    const math=all(scope,n=>n.tag==="math").length,tables=all(scope,n=>n.tag==="table").length;
    const renderedTables=(content.match(/<table(?:\s|>)/g)||[]).length;
    if(renderedTables!==tables)throw Error(`Table mismatch ${page.path}: ${renderedTables} vs ${tables}`);
    outputs[mdPath]=content;
    const href=origin+"/"+mdPath;
    const alternate=`<link rel="alternate" type="text/markdown" href="${href}" title="Markdown version">`;
    const clean=page.html.replace(/<link rel="alternate" type="text\/markdown" href="[^"]*" title="Markdown version">/g,"");
    if(!clean.includes("</head>"))throw Error("Missing head: "+page.path);
    outputs[page.path]=clean.replace("</head>",alternate+"</head>");
    report.push({path:mdPath,chars:content.length,math,tables});
  }
  const llms=[
    "# Ahmed Mahrous",
    "",
    "> Academic research in artificial intelligence, learning, strategic behavior, and decentralized financial systems. These are Markdown versions of the public website, generated from its HTML.",
    "",
    "## Profile",
    "",
    "- [Academic homepage]("+origin+"/index.md): Biography, publication summaries, academic background, and links.",
    "- [Curriculum vitae]("+origin+"/cv.md): Education, publications, awards, teaching, and service.",
    "",
    "## Research publications",
    "",
    ...papers.map(p=>`- [${p.title}](${origin}/papers/${p.slug}/index.md): ${p.authors}. ${p.venue}, ${p.year}. ${p.summary}`),
    "",
    "## Optional",
    "",
    `- [Complete Markdown corpus](${origin}/llms-full.txt): Combined profile, CV, and research papers. Large file; individual pages are preferable for targeted retrieval.`,
    `- [XML sitemap](${origin}/sitemap.xml): Canonical HTML pages.`,
    `- [Site search](${origin}/.well-known/search?q=research): Cloudflare Search for Agents.`,
    ""
  ].join("\n");
  outputs["llms.txt"]=llms;
  outputs["llms-full.txt"]=["# Ahmed Mahrous — Complete public research corpus","",`Individual documents and canonical sources: ${origin}/llms.txt`,"",...pages.map(p=>outputs[p.path.replace(/\.html$/,".md")])].join("\n\n---\n\n")+"\n";
  return {outputs,report};
}

if (require.main === module) {
  const fs = require("node:fs");
  const path = require("node:path");
  const root = path.resolve(__dirname, "..");
  const docs = path.join(root, "docs");
  const papers = JSON.parse(fs.readFileSync(path.join(root, "publications.json"), "utf8"));
  const paths = ["index.html", "cv.html", ...papers.map(p => "papers/" + p.slug + "/index.html")];
  const pages = paths.map(p => ({path: p, html: fs.readFileSync(path.join(docs,p), "utf8")}));
  const {outputs,report} = buildMarkdown(pages,papers);
  if (process.argv.includes("--check")) {
    for (const [p,content] of Object.entries(outputs)) {
      if (!fs.existsSync(path.join(docs,p)) || fs.readFileSync(path.join(docs,p),"utf8") !== content)
        throw Error("Missing or stale Markdown output: "+p+"; run python3 build.py");
    }
  } else {
    for (const [p,content] of Object.entries(outputs)) fs.writeFileSync(path.join(docs,p),content,"utf8");
  }
  console.log(JSON.stringify(report,null,2));
  console.log("PASS: "+report.length+" Markdown pages and both llms files.");
}
module.exports = {buildMarkdown};

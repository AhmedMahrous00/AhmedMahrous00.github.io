import json, html
from pathlib import Path
root=Path(__file__).parent
papers=json.loads((root/'publications.json').read_text())
(root/'publications.json').write_text(json.dumps(papers,indent=2)+'\n')
e=html.escape
def author_html(text):
 return e(text).replace("Roberto Di Pietro", '<a href="https://cemse.kaust.edu.sa/profiles/roberto-di-pietro">Roberto Di Pietro</a>')
def paper_links(p):
 links=[]
 if p.get('url'):links.append('<a href="'+e(p.get('url') or ('papers/'+p['slug']+'/'))+'">'+e(p['label'])+'</a>')
 if p.get('html'):links.append('<a href="'+e(p['html'])+'">Full-text HTML</a>')
 if p.get('code'):links.append('<a href="'+e(p['code'])+'">Code &amp; data</a>')
 return '<p>['+'] ['.join(links)+']</p>' if links else ''
style='''.profile{display:flex;align-items:center;gap:24px;margin:1.2em 0}.profile p{margin:0}.portrait{display:block;width:190px;height:190px;object-fit:cover}@media(max-width:480px){.profile{align-items:flex-start;flex-direction:column;gap:14px}}html{color-scheme:light}body{margin:24px auto;padding:0 24px;max-width:1040px;font-family:"Times New Roman",Times,serif;font-size:17px;line-height:1.43;color:#111;background:white}h1{font-size:2em;line-height:1.15;margin:0.67em 0}h2{font-size:1.5em;margin:1.3em 0 .5em}h3{font-size:1.08em;margin:0 0 .15em}a{color:#0000ee;text-decoration:underline}a:visited{color:#551a8b}a:focus-visible{outline:2px solid #000;outline-offset:3px}p{margin:.7em 0}nav{margin:1.2em 0}.research-entry{display:grid;grid-template-columns:72px 1fr;gap:16px;margin:1.3em 0 1.6em}.research-entry p{margin:.22em 0}.year{padding-top:1px}.bio{max-width:900px}footer{border-top:1px solid #bbb;margin:2.5em 0 1em;padding-top:.6em;font-size:.88em;color:#444}ul{padding-left:24px}li{margin:.35em 0}@media(max-width:600px){body{padding:0 16px;margin:18px auto;font-size:16px}.research-entry{grid-template-columns:1fr;gap:3px}.year{font-weight:bold}h1{font-size:1.8em}}@media print{body{max-width:none;margin:0;font-size:11pt}.print-button,nav{display:none}a{color:inherit}footer{display:none}.research-entry{break-inside:avoid}}'''
(root/'docs/style.css').write_text(style)
def page(title,body,prefix=''):
 return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+e(title)+'</title><meta name="description" content="Ahmed Mahrous — research on learning, strategic behavior, and decentralized financial systems at KAUST."><link rel="stylesheet" href="'+prefix+'style.css"></head><body>'+body+'</body></html>'
entries=''
for p in papers:
 entries+=f'<article class="research-entry"><div class="year">{p["year"]}:</div><div><h3><a href="papers/{p["slug"]}/">{e(p["title"])}</a></h3><p>{author_html(p["authors"])}</p><p><em>{e(p["venue"])}</em></p><p>{e(p["summary"])}</p>{paper_links(p)}</div></article>'
intro='''<h1>Ahmed Mahrous’s homepage</h1>
<div class="profile"><a href="assets/ahmed-mahrous.jpeg" aria-label="View portrait of Ahmed Mahrous"><img class="portrait" src="assets/ahmed-mahrous.jpeg" width="190" height="190" alt="Ahmed Mahrous"></a><p>Ahmed Mahrous<br>Ph.D. candidate<br><a href="https://www.kaust.edu.sa/">King Abdullah University of Science and Technology (KAUST)</a><br>Thuwal, Saudi Arabia<br><a href="mailto:ahmed.mahrous@kaust.edu.sa">ahmed.mahrous@kaust.edu.sa</a></p></div>
<div class="bio"><p>I study learning and strategic behavior in decentralized financial systems. My research combines mathematical modeling, simulation, and empirical analysis to understand how incentives, information, and feedback shape these systems.</p>
<p>I am a Ph.D. candidate at KAUST, advised by <a href="https://cemse.kaust.edu.sa/profiles/roberto-di-pietro">Roberto Di Pietro</a>. My work spans performative prediction, decentralized finance, stablecoins, market manipulation, and financial social media.</p></div>
<p>[<a href="cv.html">CV</a>] &nbsp; [<a href="https://orcid.org/0000-0003-4694-5336">ORCID</a>] &nbsp; [<a href="https://cri-lab.net">Research group</a>] &nbsp; [<a href="https://github.com/AhmedMahrous00">GitHub</a>]</p>
<nav aria-label="Page sections"><a href="#research">Research</a> · <a href="#education">Education</a> · <a href="#teaching">Teaching &amp; service</a></nav>'''
education='''<h2 id="education">Education</h2><ul><li>Ph.D. candidate, KAUST. Advisor: <a href="https://cemse.kaust.edu.sa/profiles/roberto-di-pietro">Roberto Di Pietro</a>.<br>Thesis: <em>Learning and Strategic Behavior in Decentralized Financial Systems.</em></li><li>M.Sc. in Finance, Qatar University, 2023.</li><li>B.Sc. in Business, with a focus on Finance and Information Systems.</li></ul>'''
teaching='''<h2 id="teaching">Teaching and service</h2><p>Teaching assistant for Introduction to Cybersecurity and Introduction to Cryptography, M.Eng. program, KAUST.</p><p>Conference reviewer: ICAIF, NeurIPS, and ICBC.</p><p>Journal reviewer: <em>Financial Innovation</em>; <em>Blockchain: Research and Applications</em>; <em>Computer Networks</em>.</p>'''
footer='<footer>Last updated: October 2026.</footer>'
(root/'docs/index.html').write_text(page('Ahmed Mahrous — Academic Homepage',intro+'<main><h2 id="research">Research</h2><p>Selected publications and accepted papers.</p>'+entries+education+teaching+'</main>'+footer))
cv='<p><a href="./">← Homepage</a></p><h1>Ahmed Mahrous</h1><p>Ph.D. candidate, KAUST<br><a href="mailto:ahmed.mahrous@kaust.edu.sa">ahmed.mahrous@kaust.edu.sa</a> · <a href="https://orcid.org/0000-0003-4694-5336">ORCID</a></p><p class="print-button"><button onclick="window.print()">Print / save as PDF</button></p><h2>Research interests</h2><p>Learning and strategic behavior; decentralized finance; stablecoins; market manipulation; financial social media.</p>'+education+'<h2>Selected publications and accepted papers</h2><ol>'
for p in papers:cv+='<li>'+author_html(p['authors'])+'. <a href="'+e(p.get('url') or ('papers/'+p['slug']+'/'))+'">'+e(p['title'])+'</a>. <em>'+e(p['venue'])+'</em>, '+p['year']+'.</li>'
cv+='</ol>'+teaching+footer
(root/'docs/cv.html').write_text(page('Ahmed Mahrous — CV',cv))
for p in papers:
 out=root/'docs/papers'/p['slug'];out.mkdir(parents=True,exist_ok=True)
 body='<p><a href="../../#research">← Ahmed Mahrous’s homepage</a></p><h1>'+e(p['title'])+'</h1><p>'+author_html(p['authors'])+'</p><p><em>'+e(p['venue'])+'</em> · '+p['year']+'</p><h2>Overview</h2><p>'+e(p['summary'])+'</p>'+paper_links(p)+footer
 (out/'index.html').write_text(page(p['title']+' — Ahmed Mahrous',body,'../../'))
print('Built homepage, printable CV, and',len(papers),'paper pages.')

# Machine-readable descriptions use the same factual content as the visible pages.
from urllib.parse import urlparse
base='https://amahrous.com'
urls=[]
for path in (root/'docs').rglob('*.html'):
 rel=path.relative_to(root/'docs').as_posix()
 suffix=rel[:-10] if rel.endswith('index.html') else rel
 url=base+'/'+suffix
 urls.append(url)
 doc=path.read_text()
 extra='<link rel="canonical" href="'+url+'">'
 paper=next((item for item in papers if suffix=='papers/'+item['slug']+'/'),None)
 if paper:
  schema={'@context':'https://schema.org','@type':'ScholarlyArticle','headline':paper['title'],'author':[{'@type':'Person','name':name} for name in paper['authors'].replace(', and ', ', ').replace(' and ', ', ').split(', ')],'description':paper['summary'],'url':url,'datePublished':paper['year']}
  if paper.get('url'):schema['sameAs']=paper['url']
  extra+='<meta name="citation_title" content="'+e(paper['title'])+'"><meta name="citation_publication_date" content="'+paper['year']+'">'
  for name in schema['author']:extra+='<meta name="citation_author" content="'+e(name['name'])+'">'
  doc=doc.replace('content="Ahmed Mahrous — research on learning, strategic behavior, and decentralized financial systems at KAUST."','content="'+e(paper['summary'])+'"')
 else:
  schema={'@context':'https://schema.org','@type':'ProfilePage','url':url,'mainEntity':{'@type':'Person','name':'Ahmed Mahrous','affiliation':{'@type':'Organization','name':'King Abdullah University of Science and Technology'},'sameAs':['https://orcid.org/0000-0003-4694-5336','https://github.com/AhmedMahrous00']}}
 extra+='<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\u003c')+'</script>'
 path.write_text(doc.replace('</head>',extra+'</head>'))
(root/'docs/sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(url)+'</loc></url>' for url in sorted(urls))+'</urlset>')
(root/'docs/robots.txt').write_text('User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nSitemap: '+base+'/sitemap.xml\n')

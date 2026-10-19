import json, html, re
from pathlib import Path
root=Path(__file__).parent
papers=json.loads((root/'publications.json').read_text())
abstracts=json.loads((root/'abstracts.json').read_text())
(root/'publications.json').write_text(json.dumps(papers,indent=2)+'\n')
e=html.escape
def clean_reading_text(fragment):
 # Keep article content and actual figure captions; omit conversion scaffolding.
 fragment=re.sub(r'<p class="page-source">.*?</p>', '', fragment, flags=re.S)
 fragment=re.sub(r'<details class="text-transcription">.*?</details>', lambda match: ''.join(re.findall(r'<figure\b.*?</figure>', match.group(0), flags=re.S)), fragment, flags=re.S)
 fragment=re.sub(r'<figcaption><a href="paper\.pdf#page=\d+">(?:Mathematical passage|Passage with inline symbols|Table with inline symbols), PDF page \d+</a></figcaption>', '', fragment)
 fragment=re.sub(r' aria-label="PDF page \d+"', '', fragment)
 # Two caption glyphs were checked against the original papers.
 fragment=fragment.replace('1/<sup>[unmapped symbol]</sup> <em>i</em><sup><em>p</em></sup> <em>i</em><sup>2, where</sup><sup>_pi_is the relative frequency</sup>', '1/(∑<sub>i</sub> <em>p</em><sub>i</sub><sup>2</sup>), where <em>p</em><sub>i</sub> is the relative frequency')
 fragment=fragment.replace('✓=Yes; [unmapped symbol]=No; ♢=Partial', '✓=Yes; ✗=No; ♢=Partial')
 return fragment
def author_names(p):
 return p['authors'].replace(', and ', ', ').replace(' and ', ', ').split(', ')
def bibtex(p):
 b=p['citation']
 names=[]
 for name in author_names(p):
  if name=='Roberto Di Pietro':names.append('Di Pietro, Roberto')
  else:
   given,family=name.rsplit(' ',1);names.append(family+', '+given)
 fields={'author':' and '.join(names),'title':p['title'],'year':p['year']}
 fields.update({k:v for k,v in b.items() if k not in ('type','source','date')})
 if b.get('doi'):fields['url']='https://doi.org/'+b['doi']
 else:fields['url']='https://amahrous.com/papers/'+p['slug']+'/'
 lines=[]
 for k,v in fields.items():
  v=str(v).replace('&',r'\&')
  if k=='pages':v=v.replace('-','--')
  if k=='title':v='{'+v+'}'
  lines.append('  '+k+' = {'+v+'}')
 return '@'+b['type']+'{'+p['slug']+'-'+p['year']+',\n'+',\n'.join(lines)+'\n}\n'
def citation_html(p):
 b=p['citation'];container=b.get('journal',b.get('booktitle',''))
 detail=container
 if b.get('volume'):detail+=', '+b['volume']
 if b.get('number'):detail+='('+b['number']+')'
 if b.get('pages'):detail+=', '+b['pages'].replace('-','–')
 text=p['authors']+'. '+p['year']+'. '+p['title']+'. '+detail+'.'
 result='<section id="citation"><h2>Citation</h2><p>'+e(text)
 if b.get('doi'):result+=' <a href="https://doi.org/'+e(b['doi'])+'">doi:'+e(b['doi'])+'</a>.'
 result+='</p>'
 return result+'<p><a href="citation.bib" download>Download .bib</a></p><pre>'+e(bibtex(p))+'</pre></section>'
def author_html(text):
 return e(text).replace("Roberto Di Pietro", '<a href="https://cemse.kaust.edu.sa/profiles/roberto-di-pietro">Roberto Di Pietro</a>')
def award_html(p):
 return '<p class="paper-award"><strong>'+e(p['award'])+'</strong></p>' if p.get('award') else ''
def paper_links(p,on_paper=False):
 links=[]
 if p.get('pdf'):links.append('<a class="pdf-button" href="'+e(p['pdf'])+'" target="_blank" rel="noopener" type="application/pdf">PDF</a>')
 prefix='' if on_paper else '/papers/'+p['slug']+'/'
 links.append('<a href="'+prefix+'#full-text">'+('Read full text' if on_paper else 'HTML')+'</a>')
 links.append('<a href="'+prefix+'#citation">'+('Cite' if on_paper else 'BibTeX')+'</a>')
 return '<p>'+' · '.join(links)+'</p>'
style='''.pdf-button{display:inline-block;padding:3px 10px;border:1px solid currentColor;border-radius:3px;text-decoration:none;font-size:.9em}.pdf-button:hover{background:#f0f0ff}.profile{display:flex;align-items:center;gap:24px;margin:1.2em 0}.profile p{margin:0}.portrait{display:block;width:190px;height:190px;object-fit:cover}@media(max-width:480px){.profile{align-items:flex-start;flex-direction:column;gap:14px}}html{color-scheme:light}body{margin:24px auto;padding:0 24px;max-width:1040px;font-family:"Times New Roman",Times,serif;font-size:17px;line-height:1.43;color:#111;background:white}h1{font-size:2em;line-height:1.15;margin:0.67em 0}h2{font-size:1.5em;margin:1.3em 0 .5em}h3{font-size:1.08em;margin:0 0 .15em}a{color:#0000ee;text-decoration:underline}a:visited{color:#551a8b}a:focus-visible{outline:2px solid #000;outline-offset:3px}p{margin:.7em 0}nav{margin:1.2em 0}.research-entry{display:grid;grid-template-columns:72px 1fr;gap:16px;margin:1.3em 0 1.6em}.research-entry p{margin:.22em 0}.year{padding-top:1px}.bio{max-width:900px}footer{border-top:1px solid #bbb;margin:2.5em 0 1em;padding-top:.6em;font-size:.88em;color:#444}ul{padding-left:24px}li{margin:.35em 0}@media(max-width:600px){body{padding:0 16px;margin:18px auto;font-size:16px}.research-entry{grid-template-columns:1fr;gap:3px}.year{font-weight:bold}h1{font-size:1.8em}}@media print{body{max-width:none;margin:0;font-size:11pt}.print-button,nav{display:none}a{color:inherit}footer{display:none}.research-entry{break-inside:avoid}}'''
(root/'docs/style.css').write_text(style+'''\npre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:.82em;padding:1em;background:#f6f6f6}#citation{margin-top:2em}.paper-body{max-width:900px;margin:0 auto}.paper-body p{text-align:left}.paper-body img{max-width:100%;height:auto}.paper-body figure{margin:1.3em 0}.paper-body figcaption{font-size:.88em;color:#444}.source-page{margin-top:1.8em}.math-excerpt{text-align:center}.table-scroll{overflow-x:auto}.source-footnote{font-size:.85em}.paper-body table{display:block;overflow:auto;max-width:100%;border-collapse:collapse;font-size:.9em}.paper-body th,.paper-body td{padding:.35em .6em;border:1px solid #ccc}.paper-body h2,.paper-body h3,.paper-body h4{margin-top:1.4em}.paper-body h3{font-size:1.2em}.paper-body a{overflow-wrap:anywhere}.paper-body section{scroll-margin-top:1em}.paper-nav{font-size:.95em}.abstract{max-width:900px}.paper-body math{font-family:math}.paper-body math[display="block"]{display:block;overflow-x:auto;overflow-y:hidden;padding:.4em 0}.paper-body .ltx_equation,.paper-body .ltx_equationgroup{overflow-x:auto;margin:1em 0}.paper-body .ltx_eqn_table{display:table;width:100%;border:0}.paper-body .ltx_eqn_table td{border:0;padding:.15em .25em;vertical-align:middle}.paper-body .ltx_eqn_eqno{white-space:nowrap;text-align:right}.paper-body .ltx_eqn_center_padleft,.paper-body .ltx_eqn_center_padright{width:50%}.paper-body .ltx_eqn_cell{white-space:nowrap}.paper-body .ltx_figure{text-align:center}.paper-body .ltx_figure figcaption{text-align:left}.paper-body .ltx_graphics{max-width:100%;height:auto}.paper-body .ltx_tabular{margin:.6em auto}.paper-body .ltx_biblist{padding-left:1.7em}.paper-body .ltx_bibitem{margin:.6em 0}.paper-body .ltx_ref_tag{white-space:nowrap}.paper-body h5,.paper-body h6{font-size:1em;margin:1.2em 0 .4em}.paper-body .ltx_title{line-height:1.25}.paper-body .ltx_item{list-style:none;position:relative}.paper-body .ltx_item>.ltx_tag_item{position:absolute;right:calc(100% + .5em);top:0;white-space:nowrap}html{scroll-padding-top:1em}@media(max-width:600px){.paper-body{overflow-wrap:anywhere}.paper-body figure{margin:1em 0}}\n''')
for asset in ('theme.css', 'theme.js'):
 (root/'docs'/asset).write_text((root/asset).read_text())
def page(title,body,prefix=''):
 return '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+e(title)+'</title><meta name="description" content="Ahmed Mahrous — research on learning, strategic behavior, and decentralized financial systems at KAUST."><meta name="color-scheme" content="light dark"><script src="'+prefix+'theme.js?v=1"></script><link rel="stylesheet" href="'+prefix+'style.css"><link rel="stylesheet" href="'+prefix+'theme.css?v=1"></head><body><div class="theme-toolbar" hidden><label for="theme-choice">Theme</label> <select id="theme-choice"><option value="system">System</option><option value="light">Light</option><option value="dark">Dark</option></select></div>'+body+'</body></html>'
entries=''
for p in papers:
 entries+=f'<article class="research-entry"><div class="year">{p["year"]}:</div><div><h3><a href="papers/{p["slug"]}/">{e(p["title"])}</a></h3><p>{author_html(p["authors"])}</p><p><em>{e(p["venue"])}</em></p>{award_html(p)}<p>{e(p["summary"])}</p>{paper_links(p)}</div></article>'
intro='''<h1>Ahmed Mahrous’s homepage</h1>
<div class="profile"><a href="assets/ahmed-mahrous.jpeg" aria-label="View portrait of Ahmed Mahrous"><img class="portrait" src="assets/ahmed-mahrous.jpeg" width="190" height="190" alt="Ahmed Mahrous"></a><p>Ahmed Mahrous<br>Ph.D. candidate in Computer Science<br><a href="https://www.kaust.edu.sa/">King Abdullah University of Science and Technology (KAUST)</a><br>Thuwal, Saudi Arabia<br><a href="mailto:ahmed.mahrous@kaust.edu.sa">ahmed.mahrous@kaust.edu.sa</a></p></div>
<div class="bio"><p>I work on artificial intelligence and decentralized finance. I study how learning algorithms, incentives, and strategic behavior shape markets, while also exploring how AI models can make reliable predictions.</p>
<p>I am a Ph.D. candidate in Computer Science at KAUST, advised by <a href="https://cemse.kaust.edu.sa/profiles/roberto-di-pietro">Roberto Di Pietro</a>. My research combines mathematical modeling, empirical analysis, and machine learning, with work on AI methodology as well as applications to stablecoins, prediction markets, financial manipulation detection, and investor sentiment.</p></div>
<p>[<a href="cv.html">CV</a>] &nbsp; [<a href="https://orcid.org/0000-0003-4694-5336">ORCID</a>] &nbsp; [<a href="https://cri-lab.net">Research group</a>] &nbsp; [<a href="https://github.com/AhmedMahrous00">GitHub</a>]</p>
<nav aria-label="Page sections"><a href="#research">Research</a> · <a href="#education">Education</a> · <a href="#awards">Awards &amp; scholarships</a> · <a href="#teaching">Teaching &amp; service</a></nav>'''
intro=intro.replace('[<a href="https://orcid.org/', '[<a href="https://scholar.google.com/citations?user=kOy2h6EAAAAJ&amp;hl=en">Google Scholar</a>] &nbsp; [<a href="https://orcid.org/')
education='''<h2 id="education">Education</h2><ul><li>Ph.D. candidate in Computer Science, KAUST. Advisor: <a href="https://cemse.kaust.edu.sa/profiles/roberto-di-pietro">Roberto Di Pietro</a>.<br>Thesis: <em>Learning and Strategic Behavior in Decentralized Financial Systems.</em></li><li>M.Sc. in Finance, Qatar University, 2023.</li><li>B.Sc. in Business, with a focus on Finance and Information Systems.</li></ul>'''
homepage_education=education.replace('M.Sc. in Finance, Qatar University, 2023.', 'M.Sc. in Finance, 2023.')
education=education.replace('Ph.D. candidate in Computer Science, KAUST.', 'Ph.D. candidate in Computer Science, KAUST. GPA: 3.89/4.00.').replace('M.Sc. in Finance, Qatar University, 2023.', 'M.Sc. in Finance, Qatar University, 2023. GPA: 4.00/4.00.').replace('B.Sc. in Business, with a focus on Finance and Information Systems.', 'B.Sc. in Business, with a focus on Finance and Information Systems. GPA: 3.93/4.00.')
awards='<h2 id="awards">Awards and scholarships</h2><ul><li>Best Student Paper Award, IEEE IDSTA.</li><li>CEMSE Dean’s List, KAUST.</li><li>KAUST Fellowship, fully funded doctoral fellowship.</li><li>Graduate Student Research Award (GSRA), Qatar National Research Fund, full master’s scholarship.</li><li>Order of Excellence Award, Qatar University’s highest undergraduate academic honor.</li><li>Full Undergraduate Scholarship.</li></ul>'
teaching='''<h2 id="teaching">Teaching and service</h2><p>Teaching assistant for Introduction to Cybersecurity and Introduction to Cryptography, M.Eng. program, KAUST.</p><p>Conference reviewer: ICAIF, NeurIPS, and ICBC.</p><p>Journal reviewer: <em>Financial Innovation</em>; <em>Blockchain: Research and Applications</em>; <em>Computer Networks</em>.</p>'''
footer='<footer>Last updated: October 2026.</footer>'
(root/'docs/index.html').write_text(page('Ahmed Mahrous — Academic Homepage',intro+'<main><h2 id="research">Research</h2><p>Selected publications and accepted papers. <a href="publications.bib" download>Download all citations (.bib)</a>.</p>'+entries+homepage_education+awards+teaching+'</main>'+footer))
cv='<p><a href="./">← Homepage</a></p><h1>Ahmed Mahrous</h1><p>Ph.D. candidate in Computer Science, KAUST<br><a href="mailto:ahmed.mahrous@kaust.edu.sa">ahmed.mahrous@kaust.edu.sa</a> · <a href="https://orcid.org/0000-0003-4694-5336">ORCID</a></p><p class="print-button"><button onclick="window.print()">Print / save as PDF</button></p><h2>Research interests</h2><p>Learning and strategic behavior; decentralized finance; stablecoins; market manipulation; financial social media.</p>'+education+awards+'<h2>Selected publications and accepted papers</h2><ol>'
for p in papers:cv+='<li>'+author_html(p['authors'])+'. <a href="'+e(p.get('pdf') or ('papers/'+p['slug']+'/'))+'">'+e(p['title'])+'</a>. <em>'+e(p['venue'])+'</em>, '+p['year']+'.'+award_html(p)+paper_links(p)+'</li>'
cv+='</ol>'+teaching+footer
(root/'docs/cv.html').write_text(page('Ahmed Mahrous — CV',cv))
for p in papers:
 out=root/'docs/papers'/p['slug'];out.mkdir(parents=True,exist_ok=True)
 fulltext=clean_reading_text((root/'content'/(p['slug']+'.html')).read_text())
 abstract='<section class="abstract" id="abstract"><h2>Abstract</h2>'+''.join('<p>'+e(para)+'</p>' for para in abstracts[p['slug']].split('\n\n'))+'</section>'
 body='<p><a href="../../#research">← Ahmed Mahrous’s homepage</a></p><main><article><header><h1>'+e(p['title'])+'</h1><p>'+author_html(p['authors'])+'</p><p><em>'+e(p['venue'])+'</em> · '+p['year']+'</p>'+award_html(p)+paper_links(p,on_paper=True)+'</header><section id="tldr"><h2>TL;DR</h2><p>'+e(p['summary'])+'</p></section>'+abstract+citation_html(p)+'<section id="full-text"><h2>Full text</h2><div class="paper-body">'+fulltext+'</div></section></article></main>'+footer
 (out/'index.html').write_text(page(p['title']+' — Ahmed Mahrous',body,'../../'))
 (out/'citation.bib').write_text(bibtex(p))
(root/'docs/publications.bib').write_text('\n'.join(bibtex(p) for p in papers))
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
  schema={'@context':'https://schema.org','@type':'ScholarlyArticle','@id':url+'#paper','headline':paper['title'],'name':paper['title'],'author':[{'@type':'Person','name':name,**({'@id':'https://orcid.org/0000-0003-4694-5336','sameAs':'https://scholar.google.com/citations?user=kOy2h6EAAAAJ'} if name=='Ahmed Mahrous' else {})} for name in author_names(paper)],'description':paper['summary'],'abstract':abstracts[paper['slug']],'url':url,'inLanguage':'en','datePublished':paper['year'],'mainEntityOfPage':url}
  if paper.get('award'):schema['award']=paper['award']
  if paper.get('url'):schema['sameAs']=paper['url']
  if paper.get('pdf'):
   pdf_url=base+paper['pdf'] if paper['pdf'].startswith('/') else paper['pdf']
   schema['encoding']={'@type':'MediaObject','contentUrl':pdf_url,'encodingFormat':'application/pdf'}
   extra+='<meta name="citation_pdf_url" content="'+e(pdf_url)+'">'
  extra+='<meta name="citation_title" content="'+e(paper['title'])+'"><meta name="citation_publication_date" content="'+paper['year']+'">'
  for name in schema['author']:extra+='<meta name="citation_author" content="'+e(name['name'])+'">'
  b=paper['citation']
  tags={'doi':'doi','journal':'journal_title','booktitle':'conference_title','volume':'volume','number':'issue','isbn':'isbn'}
  for field,tag in tags.items():
   if b.get(field):extra+='<meta name="citation_'+tag+'" content="'+e(b[field])+'">'
  if b.get('pages'):
   pages=b['pages'].split('-')
   extra+='<meta name="citation_firstpage" content="'+e(pages[0])+'">'
   if len(pages)>1:extra+='<meta name="citation_lastpage" content="'+e(pages[-1])+'">'
  extra+='<link rel="alternate" type="application/x-bibtex" href="'+url+'citation.bib" title="BibTeX citation">'
  if b.get('doi'):schema['identifier']={'@type':'PropertyValue','propertyID':'DOI','value':b['doi']};schema['sameAs']='https://doi.org/'+b['doi']
  schema['isPartOf']={'@type':'Periodical' if b.get('journal') else 'CreativeWork','name':b.get('journal',b.get('booktitle'))}
  if b.get('volume'):schema['volumeNumber']=b['volume']
  if b.get('number'):schema['issueNumber']=b['number']
  if b.get('pages'):schema['pagination']=b['pages']
  doc=doc.replace('content="Ahmed Mahrous — research on learning, strategic behavior, and decentralized financial systems at KAUST."','content="'+e(paper['summary'])+'"')
 else:
  schema={'@context':'https://schema.org','@type':'ProfilePage','url':url,'mainEntity':{'@type':'Person','@id':'https://orcid.org/0000-0003-4694-5336','name':'Ahmed Mahrous','url':base+'/','affiliation':{'@type':'Organization','name':'King Abdullah University of Science and Technology'},'sameAs':['https://orcid.org/0000-0003-4694-5336','https://scholar.google.com/citations?user=kOy2h6EAAAAJ','https://github.com/AhmedMahrous00']}}
 extra+='<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\u003c')+'</script>'
 path.write_text(doc.replace('</head>',extra+'</head>'))
(root/'docs/sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(url)+'</loc></url>' for url in sorted(urls))+'</urlset>')
(root/'docs/robots.txt').write_text('User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nSitemap: '+base+'/sitemap.xml\n')

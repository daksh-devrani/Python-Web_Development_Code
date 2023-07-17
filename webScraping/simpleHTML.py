from bs4 import BeautifulSoup

simple_HTML='''<html>
<head></head>
<body>
<h1>this is a title</h1>
<p class="subtitle">this is a subtitle</p>
<p>this is without class</p>
<ul>
    <li>daksh</li>
    <li>diyvansh</li>
    <li>Daksh</li>
</ul>
</body>
</html>'''

soup=BeautifulSoup(simple_HTML,'html.parser')


def find_title():
    title=soup.find('h1')
    print(title.string)


def find_list():
    list_1=soup.find_all('li')
    content= [i.string for i in list_1]
    print(content)


def find_subtitle():
    subtitle=soup.find('p',{'class':'subtitle'})
    print(subtitle.string)


def find_paragraph():
    paragraph=soup.find_all('p')
    content=[p for p in paragraph if 'subtitle' not in p.attrs.get('class',[])] #give default if none is returned
    print(content[0].string)

find_title()
find_list()
find_subtitle()
find_paragraph()
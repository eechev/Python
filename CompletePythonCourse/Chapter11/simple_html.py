from bs4 import BeautifulSoup


SIMPLE_HTML = """ <html>
<head></head>
<body>
<h1>My First Heading</h1>
<p class="subtitle">My first paragraph with a class subtitle.</p>
<p>This is another paragraph without a class.</p>
<p class="heading">This is another paragraph without a class heading.</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title(soup):
    return soup.find("h1")


def find_list_items(soup):
    return soup.find_all("li")

def find_all_paragraphs(soup):
    return soup.find_all("p")

def find_paragraph_with_class(soup):
    return soup.find_all("p", {"class": "subtitle"})

def find_paragraphs_with_no_class(soup):
    return soup.find_all("p", {"class": None})

def find_paragraphs_with_no_subtitle_class(soup):
    paragraphs = soup.find_all("p")
    # this example will throw an error when the paragraph doesn't have a class because it is None
    #return [p for p in paragraphs if 'subtitle' not in p.attrs.get("class")]
    # this is the way to overcome this error
    return [p for p in paragraphs if 'subtitle' not in p.attrs.get("class", [])]

title = find_title(simple_soup)
print(title.get_text() if title else "No title found")

list_items = find_list_items(simple_soup)
print([item.get_text() for item in list_items])

paragraphs = find_all_paragraphs(simple_soup)
print([paragraph.get_text() for paragraph in paragraphs])

paragraph_with_class = find_paragraph_with_class(simple_soup)
print([paragraph.get_text() for paragraph in paragraph_with_class])

paragraph_without_class = find_paragraphs_with_no_class(simple_soup)
print([paragraph.get_text() for paragraph in paragraph_without_class])

paragraph_with_no_subtitle = find_paragraphs_with_no_subtitle_class(simple_soup)
print([paragraph.get_text() for paragraph in paragraph_with_no_subtitle])
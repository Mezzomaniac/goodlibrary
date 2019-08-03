from collections import namedtuple
import csv
from bs4 import BeautifulSoup
import requests


Book = namedtuple('Book', 'author title libraries')
# TODO: Differentiate between print and electronic editions

def search(file, libraries):
    books = process_file(file)
    for book in data:
        for library in libraries:
            # TODO: Search asynchronously
            book[library] = library(book)
    return books

def process_file(file)
    with open(file) as file:
        data = csv.reader(file)
        return (Book(col[ ], col[ ]) for row in data for col in row)

def perth(book):
    URL = 'https://perth.ent.sirsidynix.net.au/client/en_AU/internal/search/results?qu=&qu=TITLE%3D{}+&qu=AUTHOR%3D{}+'
    title = '+'.join(book.title.split())
    author = '+'.join(book.author.split())
    response = requests.get(URL.format(title, author)
    soup = BS(r.text, 'html5lib')
    search_results = (result.parent for result in soup.find(id='searchViewDISCOVERY_ALL').find_all(text=book.title))
    # TODO: Extract and return availability status

def stirling(book):
    URL = 'https://libraries.stirling.wa.gov.au/client/en_GB/stirling'

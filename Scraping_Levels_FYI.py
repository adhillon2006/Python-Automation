import requests
from bs4 import BeautifulSoup

url = 'https://levelsfyi.com/google-levels-salary/'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml') # lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language
table = soup.findAll('table')[2] # extract 3 table on the page
df = pd.read_html(str(table)) # convert table into dataframe

df[0] # view table

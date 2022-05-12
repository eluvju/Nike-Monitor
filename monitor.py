import requests
import json
from bs4 import BeautifulSoup

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
url = 'https://www.nike.com.br/Snkrs/Feed'

##
class_list = set()
##

page = requests.get(url, headers=headers)

soup=BeautifulSoup(page.content,'html.parser')

###

tags = {tag.name for tag in soup.find_all()}
  
# iterate all tags
for tag in tags:
  
    # find all element of tag
    for i in soup.find_all( tag ):
  
        # if tag has attribute of class
        if i.has_attr( "class" ):
  
            if len( i['class'] ) != 0:
                class_list.add(" ".join( i['class']))
  
print( class_list )


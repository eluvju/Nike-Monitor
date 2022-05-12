import request

url = https://www.nike.com.br/Snkrs/Feed

html = request.get(url=url)

print(html.text)
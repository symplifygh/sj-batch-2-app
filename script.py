import requests
from bs4 import BeautifulSoup

URL="https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR"
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>Currency App</title>
</head>
<body>
    <h1>1 USD = {}</h1>
</body>
</html>
'''


response = requests.get(URL)



if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    tag = soup.find_all("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod")[0]
    value = tag.text
    with open("index.html", "w") as f:
        f.write(HTML_TEMPLATE.format(value))
else:
    print("Request Failed")
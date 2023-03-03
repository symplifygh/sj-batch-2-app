import requests
from bs4 import BeautifulSoup
import datetime

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
    <p>Updated at {}</p>
</body>
</html>
'''

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    tag = soup.find_all("p", class_="result__BigRate-sc-1bsijpp-1 iGrAod")[0]
    value = tag.text
    currentdate = datetime.datetime.now()
    with open("index.html", "w") as f:
        f.write(HTML_TEMPLATE.format(value, currentdate))
else:
    print("Request Failed")
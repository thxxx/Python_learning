import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

url = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows :
    items = row.find_all("td")
    name = items[0].text
    code =items[2].text
    if name and code:
        if name != "No universal currency":
            country = {
                'name':name.capitalize(),
                'code':code,
            }
        countries.append(country)


def ask() -> str:
  try:
    num = int(input("#: "))
    if num > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[num]
      result = country['code']
      print(result)
  except ValueError:
    print("That wasn't a number.")
    ask()

def ask_amount(first:str, second:str):
  try:
    money = input(f"How many {first} do you want to convert to {second}? \n")
  except ValueError:
    print("That wasn't a numbet")
    ask_amount()

  print(money)

print("Where are you from? Choose a country by number")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

ask()
print("Now choose another country.")
ask()

#ask_amount(first_country,second_country)


"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

print(format_currency(5000, "KRW", locale="ko_KR"))
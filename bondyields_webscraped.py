from bs4 import BeautifulSoup
import requests
import pandas as pd






TenYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx"
TwoYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd02y?countrycode=bx"
FiveYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd05y?countrycode=bx"
page10y = requests.get(TenYearTreasury)
page2y = requests.get(TwoYearTreasury)
page5y = requests.get(FiveYearTreasury)


soup10Y = BeautifulSoup(page10y.content, 'html.parser')
TenYearYield = soup10Y.find_all("span", class_ = "value")

for i in TenYearYield:
    print(i.text,end="\n"*2)
    


# print(TenYearYield.text)

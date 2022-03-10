from asyncio import constants
from bs4 import BeautifulSoup
import requests
import pandas as pd

import numpy as np
TenYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx"
TwoYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd02y?countrycode=bx"
FiveYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd05y?countrycode=bx"
page10y = requests.get(TenYearTreasury)
page2y = requests.get(TwoYearTreasury)
page5y = requests.get(FiveYearTreasury)


soup10Y = BeautifulSoup(page10y.content, 'html.parser')
TenYearYield = soup10Y.find_all("bg-quote", class_ = "value")

#this loop prints out the text of all the span with the class "value +" in the list printed out by this the value that we want is the last one
def US10Y():
        for i in TenYearYield:
            Yield10Array=[] 
            Yield10Array.append(i.text)
            #print(i.text,end="\n"*2)
            return(Yield10Array[0])
            

print(US10Y())
      
    




# print(TenYearYield.text)

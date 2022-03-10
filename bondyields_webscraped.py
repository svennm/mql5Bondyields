from asyncio import constants
from bs4 import BeautifulSoup
import requests
import pandas as pd

import numpy as np
ThreeMonthBill = "https://www.marketwatch.com/investing/bond/tmubmusd03m?countrycode=bx"
TenYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx"
TwoYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd02y?countrycode=bx"
FiveYearTreasury = "https://www.marketwatch.com/investing/bond/tmubmusd05y?countrycode=bx"
page3m = requests.get(ThreeMonthBill)
page10y = requests.get(TenYearTreasury)
page2y = requests.get(TwoYearTreasury)
page5y = requests.get(FiveYearTreasury)

#soup for the 10y US 
soup10Y = BeautifulSoup(page10y.content, 'html.parser')
TenYearYield = soup10Y.find_all("bg-quote", class_ = "value")
#soup for the 5y US
soup5Y = BeautifulSoup(page5y.content, 'html.parser')
FiveYearYield = soup5Y.find_all("bg-quote", class_ = "value")
#soup for the 2y US
soup2Y = BeautifulSoup(page2y.content, 'html.parser')
TwoYearYield = soup2Y.find_all("bg-quote", class_ = "value")
#soup for the 3m US
soup3m = BeautifulSoup(page3m.content, 'html.parser')
ThreeMonthYield = soup3m.find_all("bg-quote", class_ = "value")



#this loop prints out the text of all the span with the class "value +" in the list printed out by this the value that we want is the last one
def US10Y():
        for i in TenYearYield:
            Yield10Array=[] 
            Yield10Array.append(i.text)
            #print(i.text,end="\n"*2)
            return(Yield10Array[0])
            
def US5Y():
        for i in FiveYearYield:
            Yield5Array=[]
            Yield5Array.append(i.text)
            #print(i.text,end="\n"*2)
            return(Yield5Array[0])

def US2Y():
        for i in TwoYearYield:
            Yield2Array=[]
            Yield2Array.append(i.text)
            #print(i.text,end="\n"*2)
            return(Yield2Array[0])

def US3m():
        for i in ThreeMonthYield:
            Yield3mArray=[]
            Yield3mArray.append(i.text)
            #print(i.text,end="\n"*2)
            return(Yield3mArray[0])


print(US10Y())
print(US5Y())
print(US2Y())
print(US3m())
      
    




# print(TenYearYield.text)

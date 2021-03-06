import enum
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser = webdriver.Chrome("/Users/abhi1/Desktop/Python/C-127/venv/chromedriver.exe")
browser.get(url)
time.sleep(10)
def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]

    planet_data = []
    for i in range(0,494):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            templist = []
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    templist.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try :
                        templist.append(li_tag.contents[0])
                    except:
                        templist.append("") 
            planet_data.append(templist)
        browser.find_elements_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv","w")as f:
        csvWriter=csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planet_data)

scrape()


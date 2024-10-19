from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
driver = webdriver.Chrome(options=options)
driver.get("https://ph.indeed.com/jobs?q=software+engineer&l=Cebu+City,+Cebu&from=searchOnHP&vjk=9c965703860005b0")
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.prettify())
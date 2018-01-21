#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:48:58 2018

@author: jingyu
"""

from selenium import webdriver
from bs4 import BeautifulSoup

path_to_chromedriver = '/Users/jingyu/Documents/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = "https://www.ngoforum.org.kh/local-ngos/"
browser.get(url)

# //*[@id="adminForm"]/table/tbody
# //*[@id="adminForm"]/table/tbody/tr[1]
#//*[@id="adminForm"]/table/tbody/tr[1]/td[1]
#//*[@id="adminForm"]/table/tbody/tr[1]/td[2]
#//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a

data = {"name":[], "website":[], "address":[], "contact_number":[]}

table_trs = browser.find_elements_by_xpath('//*[@id="adminForm"]/table/tbody/tr')


for tr in table_trs:
    td = tr.find_elements_by_xpath(".//td")
    
    # initialize fields to None
    name = website = address = contact = None
    
    # get info 
    name = td[0].find_elements_by_xpath(".//a")[0].text
    contact = td[1].text
    
    #click into detail page
    browser.find_elements_by_xpath('//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a')[0].click()
    html = browser.page_source
    soup = BeautifulSoup(html)
    address = soup.find("span", attrs={"class":"contact-street"}).text
    print(address)
#    try:
#        address = browser.find_element_by_class_name('contact-street').text
#        print(address)
#        contact = browser.find_element_by_class_name('contact-emailto:').contents
#        print(contact)
#        
#    except:
#        continue
#    
    
    

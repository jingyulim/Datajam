#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 12:48:58 2018

@author: jingyu
"""

from selenium import webdriver

path_to_chromedriver = '/Users/jingyu/Documents/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = "https://www.ngoforum.org.kh/local-ngos/"
browser.get(url)

# //*[@id="adminForm"]/table/tbody
# //*[@id="adminForm"]/table/tbody/tr[1]
#//*[@id="adminForm"]/table/tbody/tr[1]/td[1]
#//*[@id="adminForm"]/table/tbody/tr[1]/td[2]
#//*[@id="adminForm"]/table/tbody/tr[1]/td[1]/a

data = {"name":[], "address":[], "contact_number":[], "email":[]}

table_trs = browser.find_elements_by_xpath('//*[@id="adminForm"]/table/tbody/tr')


for tr in table_trs:
    td = tr.find_elements_by_xpath(".//td")
    
    # initialize fields to None
    name = address = contact = email = None
    
    # get name and contact number
    name = td[0].find_elements_by_xpath(".//a")[0].text
    contact = td[1].text
    
    # click into detail page 
    # get address and email
    td[0].find_elements_by_xpath(".//a")[0].click()
    address = browser.find_element_by_class_name('contact-street').text

    # access span tag that contains the email address 
    span = browser.find_element_by_class_name('contact-emailto')
    email = span.find_element_by_css_selector('a').text
    
    # add details into data
    data["name"].append(name)
    data["address"].append(address)
    data["contact_number"].append(contact)
    data["email"].append(email)
    
    # go back to previous page
    browser.back()
 
    
    
    

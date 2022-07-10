
from selenium import webdriver
# -- coding: utf-8 --
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
import datetime
#driver = webdriver.Chrome(executable_path=r"C:/Users/shume/journey/Mulakat/chromedriver.exe")
#driver = webdriver.Firefox(executable_path=r'W:/geckodriver.exe')
driver = webdriver.Chrome()
preplybase="https://preply.com/en/online/turkish-tutors?skippresearch=true&page="
i=1
prepurls=[]
tutorNames=[]
itutor=0
while i<2:
    prepurls.append(preplybase+str(i))
    i=i+1
for prepurl in prepurls:
    time.sleep(1)
    driver.get(prepurl)
    tutors=driver.find_elements(by=By.CLASS_NAME, value="styles_TutorCardWrapper__0Awqa")
    for tutor in tutors:
        activestudents0="0 active students"
        totalLessons0="0 lessons"
        cls = tutor.get_attribute("class")
        if(cls=="styles_TutorCardWrapper__0Awqa"):
            itutor=itutor+1
            tutor_name= tutor.find_element(by=By.CLASS_NAME, value="styles_FullNameHeading__XOrgT")
            tutorNames.append(tutor_name.text)
            PriceIndicatorValue = tutor.find_element(by=By.CLASS_NAME, value="styles_PriceIndicator__w2zeE")                
            priceIndicatorValue0=PriceIndicatorValue.text
            priceIndicatorValue=priceIndicatorValue0.replace("\nTRY\nper hour","")
            #tutor_price= tutor.find_element(by=By.CLASS_NAME, value ="styles_PriceIndicator__w2zeE")
            #tutor_price0=tutor_price.text 
            #tutor_price= tutor_price0.replace("\nTRY\nper hour","")
            if(tutor.find_elements_by_class_name("styles_StatsItem__9vB4s")):
                Stats = tutor.find_elements(by=By.CLASS_NAME, value="styles_StatsItem__9vB4s")
                for stat in Stats:
                    if(stat.text.find("student")>0):
                        activeStudents0=stat.text 
                    activeStudents=activeStudents0.replace(" active students","")
                    if(activeStudents.find("student")):
                        activeStudents=activeStudents.replace(" active student","")
                    if(activeStudents.find(",")):
                        activeStudents=activeStudents.replace(",","")
                    if(stat.text.find("lesson")>0):
                        totalLessons0=stat.text 
                    totalLessons=totalLessons0.replace(" lessons","")
                    if(totalLessons.find("lesson")):
                        totalLessons=totalLessons.replace(" lesson","")
                    if(totalLessons.find(",")):
                        totalLessons=totalLessons.replace(",","")
                    #strline=date_time0+","+str(itutor)+","+tutor_name+","+priceIndicatorValue+","+str(int(activeStudents))+","+str(int(totalLessons))
                strline=str(itutor)+","+tutor_name.text+","+str(int(activeStudents))+","+str(int(totalLessons))
                print(strline)
            
            

            
                






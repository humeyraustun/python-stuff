from selenium import webdriver
# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time
import datetime
#driver = webdriver.Chrome(executable_path=r'W:/chromedriver.exe')
driver = webdriver.Firefox(executable_path=r'W:/geckodriver.exe')
preplybase="https://preply.com/en/online/turkish-tutors?page="
i=1
prepurls=[]
while i<44:
    prepurls.append(preplybase+str(i))
    i=i+1
encoding='utf-8'
date_time_last=""
Once = True
keeplooping=True
while keeplooping:
    today = datetime.datetime.now()
    date_time = today.strftime("%Y%m%d")
    date_time0 = today.strftime("%d/%m/%Y")
    if(date_time!=date_time_last):
        filename = date_time+".csv"
        f = open(filename, "wb")
        print("Writing day:",date_time)
        itutor=0 
        strline="date_time,tutorRank,tutorName,tutorPrice,tutorStudents,tutorLessons"
        print(strline)
        f.write(strline.encode("utf-8"))
        f.write("\n".encode("utf-8"))
        for prepurl in prepurls:
            time.sleep(1)
            driver.get(prepurl)
            tutors=driver.find_elements_by_tag_name('li')
            for tutor in tutors:
                cls = tutor.get_attribute("class")
                if(cls=="styles_TutorCardWrapper__3hm5h"):
                    itutor=itutor+1
                    FullNameHeading = tutor.find_element_by_class_name("styles_FullNameHeading__31Hpy")
                    fullNameHeading=FullNameHeading.text
                    PriceIndicatorValue = tutor.find_element_by_class_name("styles_PriceIndicator__2dBvu")
                    priceIndicatorValue0=PriceIndicatorValue.text
                    priceIndicatorValue=priceIndicatorValue0.replace("\n£\nper hour","")
                    activeStudents0="0 active students"
                    if(tutor.find_elements_by_class_name("styles_ActiveStudents__1CXqQ")):
                        ActiveStudents = tutor.find_element_by_class_name("styles_ActiveStudents__1CXqQ")
                        activeStudents0=ActiveStudents.text 
                    activeStudents=activeStudents0.replace(" active students","")
                    if(activeStudents.find("student")):
                       activeStudents=activeStudents.replace(" active student","")
                    if(activeStudents.find(",")):
                       activeStudents=activeStudents.replace(",","")
                    totalLessons0="0 lessons"
                    if(tutor.find_elements_by_class_name("styles_TotalLessons__1f7II")):
                        TotalLessons = tutor.find_element_by_class_name("styles_TotalLessons__1f7II")
                        totalLessons0=TotalLessons.text 
                    totalLessons=totalLessons0.replace(" lessons","")
                    if(totalLessons.find("lesson")):
                       totalLessons=totalLessons.replace(" lesson","")
                    if(totalLessons.find(",")):
                       totalLessons=totalLessons.replace(",","")
                    strline=date_time0+","+str(itutor)+","+fullNameHeading+","+priceIndicatorValue+","+str(int(activeStudents))+","+str(int(totalLessons))
                    print(strline)
                    f.write(date_time0.encode("utf-8"))
                    f.write(",".encode("utf-8"))
                    f.write(str(itutor).encode("utf-8"))
                    f.write(",".encode("utf-8"))
                    f.write(fullNameHeading.encode("utf-8"))
                    f.write(",".encode("utf-8"))
                    f.write(priceIndicatorValue.encode("utf-8"))
                    f.write(",".encode("utf-8"))
                    f.write(str(int(activeStudents)).encode("utf-8"))
                    f.write(",".encode("utf-8"))
                    f.write(str(int(totalLessons)).encode("utf-8"))
                    f.write("\n".encode("utf-8"))
        date_time_last=date_time
        print("Finished writing day")
        f.close()
        if(Once):
           keeplooping=False
print("Finished all")
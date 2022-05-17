# -*- coding: utf-8 -*- 
import os
import pandas as pds
filelist = os.listdir()
first=True
dataFrames = []
namelist = []
filenames=[]
for filename in filelist:
    if(filename.find(".csv")>-1):
        filenames.append(filename)
filenames.sort(reverse=True)
for filename in filenames:
        if(filename!="rank.csv"):
            readframe=pds.read_csv(filename)
            names=readframe.tutorName.values.tolist()
            dataFrames.append(readframe)
dataFrame=pds.concat(dataFrames)
mostlessonnames=[]
mostlessonhours=[]
numlessons=0
print("\n")
#print("Classes taught yesterday")
for name in names:
    namelist.clear()
    namelist.append(name)
    df2=dataFrame[dataFrame.tutorName.isin(namelist)]
    lessons=df2.tutorLessons.values.tolist()
    prices=df2.tutorPrice.values.tolist()
    if(len(lessons)==len(dataFrames)):
        dates=df2.date_time.values.tolist()
        # Classes taught yesterday
        if(abs(lessons[0]-lessons[1])>0):
            numlessons+=lessons[0]-lessons[1]
            #print(name+" "+str(lessons[0]-lessons[1]))
            mostlessonnames.append(name)
            mostlessonhours.append(lessons[0]-lessons[1])
print("From "+dates[1]+" to "+dates[0]+", "+str(numlessons)+" Turkish lessons were taught in total, 10 most busy tutors:")
df3 = pds.DataFrame(list(zip(mostlessonnames, mostlessonhours)),
               columns =['tutorName', 'tutorLessons'])
df4=df3.sort_values(by=['tutorLessons'], ascending=False)
print(df4.head(10).to_string(index=False))


mostlessonnames.clear()
mostlessonhours.clear()
numlessons=0
print("\n")
#print("Classes taught ever")
for name in names:
    namelist.clear()
    namelist.append(name)
    df2=dataFrame[dataFrame.tutorName.isin(namelist)]
    lessons=df2.tutorLessons.values.tolist()
    prices=df2.tutorPrice.values.tolist()
    if(len(lessons)==len(dataFrames)):
        dates=df2.date_time.values.tolist()
        # Classes taught yesterday
        if(abs(lessons[0]-lessons[len(lessons)-1])>0):
            numlessons+=lessons[0]-lessons[len(lessons)-1]
            #print(name+" "+str(lessons[0]-lessons[1]))
            mostlessonnames.append(name)
            mostlessonhours.append(lessons[0]-lessons[len(lessons)-1])
            rangestr="From "+dates[len(dates)-1]+" to "+dates[0]+", "+str(numlessons)+" Turkish lessons were taught in total, 10 most busy tutors:"
df3 = pds.DataFrame(list(zip(mostlessonnames, mostlessonhours)),
               columns =['tutorName', 'tutorLessons'])
dfrange=df3.sort_values(by=['tutorLessons'], ascending=False)

topnames=dfrange.head(10).tutorName.values.tolist()


topname='Hümeyra Ü.'
namelist.clear()
namelist.append(topname)
print("\n")
print(topname)
df2=dataFrame[dataFrame.tutorName.isin(namelist)]
lessons=df2.tutorLessons.values.tolist()
rank=df2.tutorRank.values.tolist()
students=df2.tutorStudents.values.tolist()
iles=0
dailylesson=[]
for lesson in lessons:
    if (iles==len(lessons)-1):
       dailylesson.append(0)
    else:
       dailylesson.append(lesson-lessons[iles+1])
    iles=iles+1
dates=df2.date_time.values.tolist()
alldates=dates
df5 = pds.DataFrame(list(zip(dates,rank,students,dailylesson,lessons)),
               columns =['date', 'rank','students','daily lessons', 'totallessons'])
print(df5.head(10).to_string(index=False))


topname='Elif Büşra U.'
namelist.clear()
namelist.append(topname)
print("\n")
print(topname)
df2=dataFrame[dataFrame.tutorName.isin(namelist)]
lessons=df2.tutorLessons.values.tolist()
rank=df2.tutorRank.values.tolist()
students=df2.tutorStudents.values.tolist()
iles=0
dailylesson=[]
for lesson in lessons:
    if (iles==len(lessons)-1):
       dailylesson.append(0)
    else:
       dailylesson.append(lesson-lessons[iles+1])
    iles=iles+1
dates=df2.date_time.values.tolist()
df5 = pds.DataFrame(list(zip(dates,rank,students,dailylesson,lessons)),
               columns =['date', 'rank','students','daily lessons', 'totallessons'])
print(df5.head(10).to_string(index=False))

topname='Dünya Ç.'
topname='Betül M.'
namelist.clear()
namelist.append(topname)
print("\n")
print(topname)
df2=dataFrame[dataFrame.tutorName.isin(namelist)]
lessons=df2.tutorLessons.values.tolist()
rank=df2.tutorRank.values.tolist()
students=df2.tutorStudents.values.tolist()
iles=0
dailylesson=[]
for lesson in lessons:
    if (iles==len(lessons)-1):
       dailylesson.append(0)
    else:
       dailylesson.append(lesson-lessons[iles+1])
    iles=iles+1
dates=df2.date_time.values.tolist()
df5 = pds.DataFrame(list(zip(dates,rank,students,dailylesson,lessons)),
               columns =['date', 'rank','students','daily lessons', 'totallessons'])
print(df5.head(10).to_string(index=False))

for topname in topnames:
    namelist.clear()
    namelist.append(topname)
    print("\n")
    print(topname)
    df2=dataFrame[dataFrame.tutorName.isin(namelist)]
    lessons=df2.tutorLessons.values.tolist()
    rank=df2.tutorRank.values.tolist()
    students=df2.tutorStudents.values.tolist()
    iles=0
    dailylesson.clear()
    for lesson in lessons:
        if (iles==len(lessons)-1):
           dailylesson.append(0)
        else:
           dailylesson.append(lesson-lessons[iles+1])
        iles=iles+1
    dates=df2.date_time.values.tolist()
    df5 = pds.DataFrame(list(zip(dates,rank,students,dailylesson,lessons)),
               columns =['date', 'rank','students','daily lessons', 'totallessons'])
    print(df5.head(10).to_string(index=False))


print(rangestr)
print(dfrange.head(10).to_string(index=False))



today=alldates[0]
print("\n")
print("Classes taught ever")
namelist.clear()
namelist.append(today)
df2=dataFrame[dataFrame.date_time.isin(namelist)]
dfever=df2.sort_values(by=['tutorLessons'], ascending=False)
print(dfever.head(10).to_string(index=False))
allnames=df2.tutorName.values.tolist()

rankstrs=[]
rankstr=[]

filename = "rank.csv"
f = open(filename, "wb")
# header
rankstr.clear()
rankstr.append("name")
rankstr.append("students")
rankstr.append("lessons")
for date in alldates:
    rankstr.append(date)
#print(rankstr)
for rank in rankstr:
    f.write(rank.encode("utf-8")+",".encode("utf-8"))
f.write("\n".encode("utf-8"))
for topname in allnames:
    namelist.clear()
    namelist.append(topname)
    df2=dataFrame[dataFrame.tutorName.isin(namelist)]
    lessons=df2.tutorLessons.values.tolist()
    ranks=df2.tutorRank.values.tolist()
    students=df2.tutorStudents.values.tolist()
    dates=df2.date_time.values.tolist()
# ranks
    rankstr.clear()
    rankstr.append(topname)
    rankstr.append(str(students[0]))
    rankstr.append(str(lessons[0]))
    i=0
    while i<len(alldates):
        j=0
        found=False
        date=alldates[i]
        while j<len(dates):
            if(dates[j]==date):
                found=True
                break
            j=j+1
        if(found):
            rankstr.append(str(ranks[j]))
        else:
            rankstr.append("0")
        i=i+1
    #print(rankstr)
    for rank in rankstr:
        f.write(rank.encode("utf-8")+",".encode("utf-8"))
    f.write("\n".encode("utf-8"))

    


    
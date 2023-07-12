import matplotlib.pyplot as plt
import numpy as np
with open('pageviews-20201101-020000.txt') as file_object:
    contents=file_object.readlines()
language=[]
views=[]
for l in contents:
    language.append(l.split()[0])
    views.append(l.split()[-2])


countb=0
countd=0
countf=0
countm=0
countmw=0
countn=0
countq=0
counts=0
countv=0
countvoy=0
countw=0
countwd=0



for i in range(0,len(language)):
     if  language[i].endswith(".b")  :
         countb=countb+int(views[i])
     elif language[i].endswith(".d")  :
         countd = countd + int(views[i])
     elif language[i].endswith(".f")   :
         countf = countf + int(views[i])
     elif language[i].endswith(".m") :
         countm = countm + int(views[i])
     elif language[i].endswith(".mw") :
         countdmw = countmw + int(views[i])
     elif language[i].endswith(".n")   :
         countn = countn + int(views[i])
     elif language[i].endswith(".q")   :
         countq = countq + int(views[i])
     elif language[i].endswith(".s") :
         counts = counts + int(views[i])
     elif language[i].endswith(".v")   :
         countv = countv + int(views[i])
     elif language[i].endswith(".voy") :
         countvoy = countvoy+ int(views[i])
     elif language[i].endswith(".w") :
         countw = countw + int(views[i])
     elif language[i].endswith(".wd")   :
         countwd = countwd + int(views[i])

countnew=[countb,countd,countf,countm,countmw,countn,countq,counts,countv,countvoy,countw,countwd]
language1new=["wikibooks  ","  wiktionary  ","  wikimediafoundation  ","  wikimedia  ","  wikipedia mobile\n(mw)  ","  wikinews  ","  wikiquote  ","  wikisource  ","  wikiversity  ","  wikivoyage  ","  mediawiki  ","  wikidata  "]
fig, ax = plt.subplots()
ax.scatter(countnew,language1new,color='g')
ax.plot(countnew,language1new)
plt.title("The views of each Domain trailing part for All languages")
plt.xlabel("Views  (*10^7)")
plt.show()



ar=0
es=0
ja=0
tr=0
zh=0
de=0
it=0
ja=0

for i in range(0,len(language)):

    if language[i].startswith("ar"):
        ar=ar+int(views[i])
    elif language[i].startswith("es"):
        es = es + int(views[i])
    elif language[i].startswith("tr"):
        tr = tr + int(views[i])
    elif language[i].startswith("zh"):
        zh = zh + int(views[i])
    elif language[i].startswith("de"):
        de = de + int(views[i])
    elif language[i].startswith("it"):
        it = it + int(views[i])
    elif language[i].startswith("ja"):
        ja = ja + int(views[i])
lan=["Chinese","German","Italian","Japanese","Turkish","Spanish"]
vi=[zh,de,it,ja,tr,es]
plt.plot(lan,vi, 'ro')
plt.bar(lan, vi,color="g")
plt.xlabel("Language")
plt.ylabel("Views")
plt.title("Comparing the total number of views of all articles for different languages.")
plt.show()

plt.pie(vi,labels= lan,autopct= '%1.1f%%',startangle=90)
plt.title('The percentages of total number of views of all articles for different languages.')
plt.show()

print("****************************************************************")

with open('geoeditors-monthly-2018-04.txt') as file_object:
    content=file_object.readlines()
lan=[]
country_Breton=[]
lower=[]
upper=[]
edit=[]
edits=[]

for i in content:
    if i.split()[0]=="brwiki":
        lan.append(i)
        country_Breton.append(i.split()[1])
        upper.append(int(i.split()[-1]))
        lower.append(int(i.split()[-2]))
        edit=i.split()[-5:-2]
        edits.append(edit[0]+edit[1]+edit[2])
print("edits",edits)
country_Breton_new=[]
for i in country_Breton:
    if i not in country_Breton_new:
        country_Breton_new.append(i)
    else:
        for j in range(0,len(country_Breton_new)):
            if country_Breton_new[j]==i:
                for b in lan:
                    if b.split()[1]==country_Breton_new[j]:
                        x=country_Breton_new[j]
                        country_Breton_new[j]=x +"\n"+"("+b.split()[-5]+b.split()[-4]+b.split()[-3]+" edits"+")"

                    elif b.split()[1]==i:
                        i=i+"\n"+"("+b.split()[-5]+b.split()[-4]+b.split()[-3]+" edits"+")"

                        country_Breton_new.append(i)
print(country_Breton_new)

print(lower)
print(upper)
print(country_Breton)

labels =country_Breton_new
Lower_Bound=lower
Upper_Bound=upper


x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,Lower_Bound, width, label='LowerBound')
rects2 = ax.bar(x + width/2,Upper_Bound, width, label='UpperBound')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Lower and Upper number of editors')
ax.set_title('Lower and Upper number of editors of each country for Breton  Wiki database (brwiki)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()


count_edits1=0
count_edits2=0
for i in edits:
    if i=="100ormore":
        count_edits1=count_edits1+1
    else:
        count_edits2=count_edits2+1

plt.pie([count_edits1,count_edits2],  labels=["100 or more edits","5 to 99 edits"], autopct='%1.1f%%', shadow=True, startangle=90)
plt.legend(["France",["France,Netherlands, Spain, United, unknown"]],loc='lower left')

plt.title('The percentages of types range  for edits in Breton  Wiki database (brwiki)')
plt.show()

print("********************************************************************")

with open('unique_devices_per_project_family_daily-2021-05-08.txt') as file_object:
    cont=file_object.readlines()
ProjectFamily=[]
EstimateOfUniqueDevice=[]
for i in cont:
    ProjectFamily.append(i.split()[0])
    EstimateOfUniqueDevice.append(i.split()[-2])
ProjectFamilyNew=[]
EstimateOfUniqueDeviceNew=[]

for i in range(-1,-(len(ProjectFamily)+1),-1):
    ProjectFamilyNew.append(ProjectFamily[i])
    EstimateOfUniqueDeviceNew.append((EstimateOfUniqueDevice[i]))


plt.bar(ProjectFamilyNew,EstimateOfUniqueDeviceNew,color="m")
plt.ylabel("Estimate Of Unique Device")
plt.xlabel("Project Family Name")
plt.title("Estimate of unique devices per project family 2021-05-08")
plt.show()



with open('unique_devices_per_domain_daily-2021-05-08.txt') as file_object:
    cont1=file_object.readlines()

ProjectFamily_Armenian=['wikivoyage', 'wikinews', 'wikiversity', 'wikidata', 'mediawiki', 'wikiquote', 'wikibooks', 'wikisource', 'wiktionary', 'wikipedia']
EstimateOfUniqueDevice_Armenian=[]
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikivoyage' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikinews' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikiversity' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikidata' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'mediawiki' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikiquote' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikibooks' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikisource' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wiktionary' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
a=0
for i in cont1:
    if i.startswith("hy"):
        if 'wikipedia' in i:
            a=a+int(i.split()[-2])

EstimateOfUniqueDevice_Armenian.append(a)
print(EstimateOfUniqueDevice_Armenian)
print(ProjectFamily_Armenian)

fig, ax = plt.subplots()
ax.bar(ProjectFamily_Armenian, EstimateOfUniqueDevice_Armenian)
ax.bar(ProjectFamily_Armenian, EstimateOfUniqueDevice_Armenian)
ax.set_ylabel('Estimate')
ax.set_title('Estimate Of Unique Device for Armenian language (hy)')
plt.show()


EstimateOfUniqueDevice_Armenian1=EstimateOfUniqueDevice_Armenian[:]
ProjectFamily_Armenian1=ProjectFamily_Armenian[:]
for i in range(0,len(EstimateOfUniqueDevice_Armenian)):
    if EstimateOfUniqueDevice_Armenian[i]==0:
        EstimateOfUniqueDevice_Armenian1.remove(EstimateOfUniqueDevice_Armenian[i])
        ProjectFamily_Armenian1.remove(ProjectFamily_Armenian[i])
plt.pie(EstimateOfUniqueDevice_Armenian1,labels=ProjectFamily_Armenian1,autopct='%1.1f%%',startangle=90)
plt.legend()
plt.title('Estimate Of Unique Device for Armenian language (hy)')
plt.show()

with open('unique_devices_per_project_family_daily-2020-05-08.txt') as file_object:
    cont2=file_object.readlines()
ProjectFamily2=[]
EstimateOfUniqueDevice2=[]
for i in cont2:
    ProjectFamily2.append(i.split()[0])
    EstimateOfUniqueDevice2.append(i.split()[-2])
ProjectFamilyNew2=[]
EstimateOfUniqueDeviceNew2=[]

for i in range(-1,-(len(ProjectFamily2)+1),-1):
    ProjectFamilyNew2.append(ProjectFamily2[i])
    EstimateOfUniqueDeviceNew2.append((EstimateOfUniqueDevice2[i]))



with open('unique_devices_per_project_family_daily-2019-05-08.txt') as file_object:
    cont3=file_object.readlines()
ProjectFamily3=[]
EstimateOfUniqueDevice3=[]
for i in cont3:
    ProjectFamily3.append(i.split()[0])
    EstimateOfUniqueDevice3.append(i.split()[-2])
ProjectFamilyNew3=[]
EstimateOfUniqueDeviceNew3=[]

for i in range(-1,-(len(ProjectFamily3)+1),-1):
    ProjectFamilyNew3.append(ProjectFamily3[i])
    EstimateOfUniqueDeviceNew3.append((EstimateOfUniqueDevice3[i]))


plt.figure(figsize=(3,1))
plt.subplot(311)
plt.bar(ProjectFamilyNew3, EstimateOfUniqueDeviceNew3,color='r')
plt.ylabel("2019")
plt.subplot(312)
plt.bar(ProjectFamilyNew2, EstimateOfUniqueDeviceNew2,color='b')
plt.ylabel("2020")
plt.subplot(313)
plt.bar(ProjectFamilyNew, EstimateOfUniqueDeviceNew,color='g')
plt.ylabel("2021")
plt.suptitle('Estimate of unique devices per project family for the same day(8) and month(5) with different year(2019,2020,2021)')
plt.show()






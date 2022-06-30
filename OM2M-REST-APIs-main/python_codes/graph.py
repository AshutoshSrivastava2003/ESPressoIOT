import requests

# importing matplotlib module 
from matplotlib import pyplot as plt

ae="Final_Dt"
cnt="N1"
uriCse="http://127.0.0.1:8080/~/in-cse/in-name"
uriAe=uriCse+'/'+ae
uriCnt=uriAe+'/'+cnt

y=[]
x=[]

headers = { 'X-M2M-Origin': 'admin:admin', 'Content-type': 'application/json' } 

uri=uriCnt+"/?rcn=4"
getdata=requests.get(uri,headers=headers)

string = getdata.json()

# print(string)

for i in string['m2m:cnt']['m2m:cin']:
    # print(i['con'],i['ct'])
    y.append(i['con'])
    x.append(str(i['ct'][0:11][-2:])+":" + str(i['ct'][0:13][-2:])+":" + str(i['ct'][0:15][-2:]))

print(y)
print(x)



plt.plot(x,y)

plt.show()
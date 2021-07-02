import csv
data=[]
gravity=[]
with open("main2.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
stardata=data[1:]
data2=list(stardata)
for row in stardata:
    row[3]=float(row[3])* 1.989e+30
    row[4]=float(row[4])* 6.957e+8
for row in stardata:
    mass=float(row[3])
    radius=float(row[4])
    G=6.67*10^-11
    gravity_value=G*mass/radius^2
    gravity.append(gravity_value)
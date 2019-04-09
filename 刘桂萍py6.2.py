import pandas as pd
data = pd.read_csv('test.csv')
import csv


with open("test.csv","w") as csvfile: 
    writer = csv.writer(csvfile)

    writer.writerow(["No.","Name","Age","Score"])
  
    writer.writerows([[1,'mayi',18,99],[2,'jack',21,89],[3,'tom',25,95],[4,'rain',19,80],[5,'hanmeimei',23,81]])
import csv
with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    #这里不需要readlines
    for line in reader:
        print (line)

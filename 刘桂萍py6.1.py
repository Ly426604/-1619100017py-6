import random as r
a=[]
for i in range(50):
    x=int(r.random()*100)
    a.append(x)
print(a)
a.sort()
print(a)
with open(r'C:\Users\HUAWEI\Desktop\python\liuguiping.txt', 'w') as f:
    for i in range(50):
        f.write(str(a[i])+' ')
    f.write("\n")
    a.reverse()
    for i in range(50):
        f.write(str(a[i])+' ')
#     f.write("\n")
#     # print(f.read())

# # print(a)
# f=open(r'C:\Users\HUAWEI\Desktop\python\liu.txt','a')
# for i in range(50):
#     f.write(str(a[i])+' ')
# # f.close()
# f=open(r'C:\Users\HUAWEI\Desktop\python\liu.txt','r')
# # print(f.read())
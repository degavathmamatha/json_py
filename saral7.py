import json
n_dic={}
a_file=open("mammu.txt","r")
for line in a_file:
    key,value=line.strip().split(None,1)
    n_dic[key]=value.strip()
print(n_dic)
import json
dic={"chitti":5,"lucky":6}
print(json.dumps(dic))

#(list)
import json 
dict={"name":"mama","age":21,"num":[1,2,3,4,5],"bool":True,"s":4.67,"tuple":(1,8,6,5,9)}
data=json.dumps(dict)
print(data)
import json
dic={"chitti":5,"lucky":6}
print(json.dumps(dic))

#(list)
import json 
list1=[1,2,3,4,5,6]
print(json.dumps(list1))

#(tupal)
import json
a=("apple","banana","mango")
print(json.dumps(a))

#(string)
import json
s="mammu"
print(json.dumps(s))

#(int)
import json
b=2345
print(json.dumps(b))

#(float)
import json
x=123.56
print(json.dumps(x))

#(true)
import json
f=True
print(json.dumps(f))

#(false)
import json
g=False
print(json.dumps(g))

#(none)
f=None
print(json.dumps(f))
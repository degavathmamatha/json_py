import json
dic='{"a":  1,"a":  2,"a":  3, "a": 4,"b": 1, "b": 2}'
print(type(dic))
my_js=json.loads(dic)
print(type(my_js))
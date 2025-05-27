s_info={"Name":"Bob", "Age":15,"Major":False}
print(s_info)
s_info.update({"email":"bob@email.com"})
print(s_info)
s_info["Age"]=20
print(s_info)
del s_info["Major"]
print(s_info)
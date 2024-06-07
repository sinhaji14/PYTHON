info = {
    "name": "yash",
    "age" : 21,
    "cgpa" :{ 
        "first":7.55,
         "second":8.55,
         "third": 8.23,
    },
    "branch" : "chemical",

}
print(len(list(info.keys())))
print(list(info.values()))
print(list(info.items()))
print(list(info.get("branch")))
info.update({"city":"delhi"})
print(info)

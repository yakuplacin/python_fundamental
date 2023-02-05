# key - value    relationship is the dictionary
# 34 => Istanbul   38 => Kayseri

users = {
    "yakuplacin": {
        "age": 22,
        "email": "yakuplacin@agu.edu.tr",
        "address": "Kayseri",
        "roles" : ["admin","user"]
    },
    "seymalacin": {
        "age": 10,
        "email": "NAN",
        "address": "Kayseri",
        "roles" : ["user"]
    }
}

print(users["seymalacin"]["age"])
print(users["yakuplacin"])
print(users["yakuplacin"]["roles"][0])
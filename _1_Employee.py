import json

# # returns the data from json
# file1=open("D:\\DS291022B\\_6_assignment\\_1_load.json")
# data=json.load(file1)
# print(data)

# # dumps the data from into json 
# file1=open("D:\\DS291022B\\_6_assignment\\_1_load.json","w")
# json.dump(data,file1)




dictionary={
    "Andhra Pradesh":"Amaravati",
    "Arunachal Pradesh":"itanagar",
    "Assam":"Dispur",
    "Bihar":"Patna",
    "Tamil Nadu":"Chennai",
    "Karnataka":"Bangaore",
    "Kerala":"Tiruvananthapuram"
}

state=open("D:\\DS291022B\\_6_assignment\\_1_State.json","w")
json.dump(dictionary,state)

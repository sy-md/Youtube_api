# Youtube_api
Createing db with your faviote youtube playlist. with features


password is the connection str psw

youtube api is the the youtube goold cloud api key you make

late night programming had a really simple issues but becuase i was tired


api = [{"id" : "1","name" : "hello world"},{"id" : "2","name" : "mommy"},{"id" : "3","name" : "codind"}]  
db = [{"id" : "1","name" : "hello world"},{"id" : "2","name" : "mommy"}]

print("Before >>",db)
for x in api:
    for k in range(len(db)):
        if x["name"] == db[k]["name"]:
            print("[api]{} == [db]{} - found in db".format(x["name"],db[k]["name"]))
            break
        else:
            print("[api]{} != [db]{} - not found in db".format(x["name"],db[k]["name"]))
            if k == (len(db)-1): # if u went through the whole db then add new 
                db.append(x)
                break
print("After >>",db)
      

1.) so tired didnt realize break, broke out of a current loop

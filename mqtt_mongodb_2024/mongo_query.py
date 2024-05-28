
import pymongo

MONGODB_SERVER = "192.168.0.223" #Dell

myclient = pymongo.MongoClient("mongodb://"+MONGODB_SERVER+":27017/")
MYDB = myclient["Koti"]
MYCOL = MYDB["Parveke"]

myquery = { "Sensor": " SHT3X" }

#temp ="none"
#humid="none"

Tempdata = []
Humiddata = []
#timestamp1 = 0
#timestamp2 = 0

def mongodb_query():
    #mydocs = MYCOL.find(myquery).limit(10)

    mydocs = MYCOL.find().limit(5).sort({"date" :-1}); 

    #mydocs = MYCOL.find().skip(0).limit(10).sort("name")

    #mydocs = MYCOL.find({"$or":[{"Temperature":{"$gt":0.0}}, {"Humidity":{"$gt":0.0}}]}).limit(10).sort({"date":-1})          
    for doc in mydocs:
        #print(doc)
        temp ="none"
        humid="none"
        date = doc["date"]
        #print(y)
        if "Temperature" in doc:
            temp = doc["Temperature"]
        if "Humidity" in doc:    
            humid = doc["Humidity"]

        if"NodeInfo" in doc:
            pass  
            #print("Skip")
        else:
            if (temp != "none"):
                Tempdata.append((date, temp))
                #timestamp1 += 1
                print(date+ " Temp : "+str(temp)+ "°C")
            if (humid != "none"):
                Humiddata.append((date, humid))
                #timestamp2 += 1    
                print(date+ " Humid: "+str(humid)+"%")
 
    #print(Tempdata)
    #print(Humiddata)
    print("TempNow : " + str(Tempdata[0]))
    print("HumidNow: " + str(Humiddata[0]))

# EOF def monodb_query

mongodb_query()
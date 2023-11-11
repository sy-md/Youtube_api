import json,os,time
import logging as lg
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

yt_key = os.environ.get("API_KEY")
psw = os.environ.get("PSW")
file = "../output/cleaned.json"

con_str = (f"mongodb+srv://crazymartell:{psw}@cluster0.noggzpz.mongodb.net/youtube")
cli = MongoClient(con_str)
mydb = cli["youtube"]
collection = mydb["average_channels"]  # get/make a collection in the db

lg.basicConfig()
my_lg = lg.getLogger(__name__)
my_lg.setLevel(lg.INFO)

class update_db:
    def get_vids():
        my_lg.info("pulling data from my database")

        with open(file, "r") as read:
            cl_data = json.load(read)
            db_data = update_db.pull_data_from_db(mydb)
            
            seen = db_data
            new_vid = []
            song = "song_title"

            for api in cl_data:
                for db in range(len(db_data)):
                    if api[song] == db_data[db][song]:
                        #print("{} <> {} ... found in db".format(api[song],db_data[db][song]))
                        #time.sleep(0.1)
                        break
                    else:
                        #print("{} <> {} ... not found in db".format(api[song],db_data[db][song]))
                        #time.sleep(0.1)
                        if db == (len(db_data)-1):
                            new_vid.append(api)
                            break

            if len(new_vid) < 1:
                return

            if seen is None:
                push_new_videos(mydb , cl_data)
            else:
                for i in new_vid:
                    print("found new song {}".format(i[song]))
                    time.sleep(0.1)
                push_new_videos(mydb ,new_vid)                        
 
    def pull_data_from_db(db) -> list:
        coll = db["average_channels"]
        saved_data = []
        mycoll = coll.find()
        for data in mycoll:
            saved_data.append(data)
        return saved_data

def push_new_videos(mydb, nw_vid=None):
    collection = mydb["average_channels"]

    if nw_vid == "None":
        with open(file, 'r') as reading:
            data = json.load(reading)
            collection.insert_many(data)
    else:
        collection.insert_many(nw_vid)


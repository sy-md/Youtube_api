import json,os
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
            
            """
            check if cleaned data is not in the database
            if cleaned data is in database continue

            we only want whats not in the database
            """
            seen = db_data
            idx = 0
            cnt = 0

            #while idx < len(cl_data):
            for x in seen:
                for k,v in x.items():
                    if cl_data[idx]["song_title"] != v: 
                        seen.append(cl_data[idx])
                        print("not found in db")
                        print(idx)
                        print("sent" ,cl_data[idx])
                    else:
                        print("found in db")
                idx += 1
            #push_new_videos(mydb)


 
    def pull_data_from_db(db) -> list:
        coll = db["average_channels"]

        saved_data = []

        mycoll = coll.find()

        for data in mycoll:
            saved_data.append(data)

        return saved_data


def push_new_videos(mydb):
    """
    cleaned.json need a model

    yt :
        old : []
        new : []

    then this function onlt runs insertn_one() insead of many

    """
    
    collection = mydb["average_channels"]
    with open(file, 'r') as reading:
        data = json.load(reading)

        collection.insert_many(data)

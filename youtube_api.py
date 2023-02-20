from googleapiclient.discovery import build
import json, os
from mongo_db import pull_data_from_db
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file = "data.json"

api_service_name = "youtube"
api_version = "v3"
api_key = "AIzaSyDRR8QBp6QT44WjjOdHwu9l8sK-x0srM2w" # put youtbe_api key here
amt = 35  # 50
playlist = "PLUCV7KPLwz1FLrmI0JTIs1hOrSM8kvCaL"
psw = os.environ.get("MONGODB_PWD")
con_str = (f"mongodb+srv://crazymartell:{psw}@cluster0.noggzpz.mongodb.net/youtube")
cli = MongoClient(con_str)
mydb = cli["youtube"]
collection = mydb["average_channels"] # get/make a collection in the db

class get_raw_youtube_data():

    def send_request():
        youtube = build(
           api_service_name, api_version, developerKey=api_key
        )
        return youtube

    def get_update():
        get_raw_youtube_data.getplaylist() # get the api platlist
        get_sv_data = pull_data_from_db(mydb) # get datbase playlist

        with open(file, "r") as read:
            data = json.load(read)

            items = data["items"] # updated
            seen = []
            tmp = []
            
            cnt = 0
            cntt = 0

            for x in get_sv_data:
                seen.append(x["video"])
 
            while cntt < len(items):
                channel = items[cntt]["snippet"]["videoOwnerChannelTitle"]
                song_title = items[cntt]["snippet"]["title"]
                if song_title not in seen:
                    vid = {channel: song_title}
                    tmp.append(vid)
                cntt += 1
            print("found {} new song".format(len(tmp)))
            for x in tmp:
                print(x, end="\n")



    def getplaylist():
        pass
       #my_youtube = get_raw_youtube_data.send_request()

       #request = my_youtube.playlistItems().list(
       #    part="snippet,id",
       #    maxResults=amt,
       #    playlistId=playlist,
       #)
       #response = request.execute()

       #with open(file, "w") as send:
       #    json.dump(response, send, indent=3)

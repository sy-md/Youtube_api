from googleapiclient.discovery import build
import json, os
from mongo_db import pull_data_from_db, push_new_videos
from pymongo import MongoClient
from cleaning_data import clean_for_percetage
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file = "data.json"

api_service_name = "youtube"
yt_key = os.environ.get("API_KEY")
api_version = "v3"
api_key = yt_key # put youtbe_api key here
playlist = "PLUCV7KPLwz1FLrmI0JTIs1hOrSM8kvCaL"
psw = os.environ.get("PSW")
con_str = (f"mongodb+srv://crazymartell:{psw}@cluster0.noggzpz.mongodb.net/youtube")
cli = MongoClient(con_str)
mydb = cli["youtube"]
collection = mydb["average_channels"]  # get/make a collection in the db


class get_raw_youtube_data():
    amt= 50  # 50
    def send_request():
        youtube = build(
           api_service_name, api_version, developerKey=api_key
        )
        return youtube

    def get_update():
        get_sv_data = pull_data_from_db(mydb) # get datbase playlist

        with open(file, "r") as read:  # opeing the youtube api json / data.json
            data = json.load(read)

            items = data["items"] # updated videos from youtube api
            tmp = []
            tmp = []
            cntt = 0
            vid_amt = 1

            while cntt < len(items):
                channel = items[cntt]["snippet"]["videoOwnerChannelTitle"]
                song_title = items[cntt]["snippet"]["title"]
                if song_title not in seen:
                    vid = {channel: song_title}
                    tmp.append(vid)
                cntt += 1

            get_raw_youtube_data.amt = (cntt // 2)
            get_raw_youtube_data.getplaylist()  # get the api platlist / creates data.json
            clean_for_percetage()
            print("found {} new song".format(len(tmp))) # found 10 songs
            for x in tmp:
                print("{}:{} send to db".format(vid_amt, x))  # 20-40
                push_new_videos(mydb)
                vid_amt += 1
                print(vid_amt)
                print("{} > {}".format(get_raw_youtube_data.amt, cntt))
                if get_raw_youtube_data.amt > cntt:
                    exit()
                else:
                    print("cycleing")
                    get_raw_youtube_data.getplaylist()
                    get_raw_youtube_data.get_update()



    def getplaylist():
        # getting a youtube.com users playlist into memory
        my_youtube = get_raw_youtube_data.send_request() # helper function to get youtube api

        request = my_youtube.playlistItems().list(
            part="snippet,id",
            maxResults=10,
            playlistId=playlist,
        )
        response = request.execute()

        with open(file, "w") as send:  # dumps the youtube api data into data.json
            json.dump(response, send, indent=3)

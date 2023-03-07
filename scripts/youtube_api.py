from googleapiclient.discovery import build
import json
import os
import logging as lg 
from mongo_db import pull_data_from_db, push_new_videos
from pymongo import MongoClient
from cleaning_data import clean_raw_data
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file = "../data/data.json" # raw data

yt_key = os.environ.get("API_KEY")
psw = os.environ.get("PSW")

api_service_name = "youtube"
api_version = "v3"
api_key = yt_key # put youtbe_api key here
playlist = "PLUCV7KPLwz1FLrmI0JTIs1hOrSM8kvCaL"

con_str = (f"mongodb+srv://crazymartell:{psw}@cluster0.noggzpz.mongodb.net/youtube")
cli = MongoClient(con_str)
mydb = cli["youtube"]
collection = mydb["average_channels"]  # get/make a collection in the db

lg.basicConfig()
my_lg = lg.getLogger(__name__)
my_lg.setLevel(lg.INFO)

class get_raw_youtube_data():
    amt= 0

    def send_request():
        youtube = build(
           api_service_name, api_version, developerKey=api_key
        )
        my_lg.info("sending a requst to Youtube API ")

        return youtube

    def getplaylist():
        my_lg.info("getting youtube data")
        my_youtube = get_raw_youtube_data.send_request() # helper function to get youtube api
        

        request = my_youtube.playlistItems().list(
            part="snippet,id",
            maxResults=get_raw_youtube_data.amt,
            playlistId=playlist,
        )

        response = request.execute()
        new_amt = response["pageInfo"]["totalResults"]
        my_lg.info("{} videos left in Playlist".format(new_amt))
        get_raw_youtube_data.amt = new_amt

        request = my_youtube.playlistItems().list(
            part="snippet,id",
            maxResults=get_raw_youtube_data.amt,
            playlistId=playlist,
        )
        my_lg.info("grabbed the youtube playlist ")
        response = request.execute()
        clean_raw_data(response)

        with open(file, "w") as send:  # dumps the youtube api data into data.json
            json.dump(response, send, indent=3)
        my_lg.info("Storing user data")

        
###############################################

    def get_update():
        get_raw_youtube_data.getplaylist()  # get the api platlist / creates data.json

        my_lg.info("exiting")
        exit()





        get_sv_data = pull_data_from_db(mydb) # get datbase playlist
        my_lg.info("pulling data from my database")


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




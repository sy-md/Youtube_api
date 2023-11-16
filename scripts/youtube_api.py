from googleapiclient.discovery import build
import json
import os
import time
import logging as lg
#from pymongo import MongoClient
from cleaning_data import clean_raw_data
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file = "../data/data.json" # raw data

yt_key = os.environ.get("API_KEY")
#psw = os.environ.get("PSW")

api_service_name = "youtube"
api_version = "v3"
api_key = yt_key # put youtbe_api key here
playlist = "PLq3UZa7STrbpGCddK4y9ZOlNzrElTGzVl"

#con_str = (f"mongodb+srv://crazymartell:{psw}@cluster0.noggzpz.mongodb.net/youtube")
#cli = MongoClient(con_str)
#mydb = cli["youtube"]
#collection = mydb["average_channels"]  # get/make a collection in the db

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
        

        get_amt = my_youtube.playlistItems().list(
            part="snippet,id",
            maxResults=get_raw_youtube_data.amt,
            playlistId=playlist,
        )

        #response = get_amt.execute()
        print( get_amt.execute())
        exit()

        new_amt = response["pageInfo"]["totalResults"]
        get_raw_youtube_data.amt = new_amt
        my_lg.info("{} videos left in Playlist".format(new_amt))
        time.sleep(3)

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

        

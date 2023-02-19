from googleapiclient.discovery import build
import json

file = "data.json"


class get_raw_youtube_data():

    def __init__(self):
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.api_key = "AIzaSyDRR8QBp6QT44WjjOdHwu9l8sK-x0srM2w" # put youtbe_api key here
        self.amt =35  # 50
        self.playlist = "PLUCV7KPLwz1FLrmI0JTIs1hOrSM8kvCaL"

    def send_request(self):
        youtube = build(  # connection to youtube api
           self.api_service_name, self.api_version, eveloperKey=self.api_key
        )
        return youtube

    def get_update(self):
        get_raw_youtube_data.getplaylist()

        with open(file, "r") as read:
            data = json.load(read)

            items, seen = data["items"], {}

            cnt = 0
            for x in range(0, len(items)):
                song_title = items[x]["snippet"]["title"]
                channel = items[x]["snippet"]["videoOwnerChannelTitle"]
                vid = (song_title, channel)
                seen[cnt + 1] = vid
            self.amt = cnt # find the difference to tell user how many new vidsoes were there


    def getplaylist(self):
        my_youtube = get_raw_youtube_data.send_request()

        request = my_youtube.playlistItems().list(
            part="snippet,id",
            maxResults=self.amt,
            playlistId=self.playlist,
        )
        response = request.execute()

        with open(file, "w") as send:
            json.dump(response, send, indent=3)

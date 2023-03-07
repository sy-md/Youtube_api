import json
import logging as lg

cleaned = "cleaned.json"

lg.basicConfig()
my_log = lg.getLogger(__name__)
my_log.setLevel(lg.INFO)

def clean_raw_data(response):
    my_log.info("Cleaning data")

    cleaned_data = []
    tmp = {}
    data = response

    items = data["items"]  # the list of video snippets

    for k in range(0, len(items)):
        title = items[k]["snippet"]["title"]
        channel = items[k]["snippet"]["videoOwnerChannelTitle"]
        tmp["channle"] = channel
        tmp["video"] = title
        cleaned_data.append(tmp)
        tmp = {}

    with open(cleaned, "w") as send:
        json.dump(cleaned_data, send, indent=3)

    my_log.info("all done Cleaning user data ", cleaned_data)

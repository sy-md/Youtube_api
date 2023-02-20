import os
import json

file = "cleaned.json"

def pull_data_from_db(db) -> list:
    coll = db["average_channels"]

    saved_data = []

    mycoll = coll.find()

    for data in mycoll:
        saved_data.append(data)

    return saved_data


def push_new_videos():
    pass
   #my_db = self.cli.youtube  # get/make db in cluster of connection_string
   #with open(file, 'r') as read:
   #    data = json.load(read)
   #    """
   #    we want to update not push a huge new cluster of data
   #    """
   #    for x in data:
   #        inserted_ids = collection.insert_many(data).inserted_ids

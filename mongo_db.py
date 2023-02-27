import json
file = "cleaned.json"


def pull_data_from_db(db) -> list:
    coll = db["average_channels"]

    saved_data = []

    mycoll = coll.find()

    for data in mycoll:
        saved_data.append(data)

    return saved_data


def push_new_videos(mydb):
    collection = mydb["average_channels"]
    with open(file, 'r') as reading:
        data = json.load(reading)

        collection.insert_many(data)

import json
file = "data.json"
newfile = "cleaned.json"


def clean_for_percetage():  # new vids and putting into cleaned.json
    cleaned_data = []
    tmp = {}

    with open(file, "r") as read_it: # opening youtube api json
        data = json.load(read_it)

        items = data["items"]  # the list of video snippets

        for k in range(0, len(items)):
            title = items[k]["snippet"]["title"]
            channel = items[k]["snippet"]["videoOwnerChannelTitle"]
            tmp["channle"] = channel
            tmp["video"] = title
            cleaned_data.append(tmp)
            tmp = {}

        with open(newfile, "w") as send:
            json.dump(cleaned_data, send, indent=3)

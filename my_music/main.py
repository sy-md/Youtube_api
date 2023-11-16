from youtube_api import get_raw_youtube_data
#from mongo_db import update_db
import logging as lg

lg.basicConfig()
my_lg = lg.getLogger(__name__)
my_lg.setLevel(lg.INFO)

def main():
    ans = input("do you wanna update the database y/n" )
    if ans == "y":
        my_lg.info("getting user playlist data")
        get_raw_youtube_data.getplaylist()
        my_lg.info("sending user data to the database")
        update_db.get_vids()
        
    ans = input("do you want donwload to a playlist to a location y/n")
    if ans == "y":
        get_raw_youtube_data.getplaylist()
    else:
        update_db.get_vids()
        
if __name__ == "__main__":
    main()

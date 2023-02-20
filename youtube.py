from youtube_api import get_raw_youtube_data
from cleaning_data import clean_for_percetage


def main():
    ans = input("do you wanna update the database y/n")

    if ans == "y":
        get_raw_youtube_data.get_update()
        print("updating the playlist")
    else:
        pass


    get_raw_youtube_data.getplaylist()
    print("geting the playlist ready")
    clean_for_percetage()
    print("cleaning data")


if __name__ == "__main__":
    main()

from youtube_api import get_raw_youtube_data

def main():
    ans = input("do you wanna update the database y/n")
    if ans == "y":
        get_raw_youtube_data.getplaylist()
    else:
        exit()
if __name__ == "__main__":
    main()

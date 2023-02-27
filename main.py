from youtube_api import get_raw_youtube_data


def main():
    ans = input("do you wanna update the database y/n")

    if ans == "y":
        get_raw_youtube_data.get_update()
        print("updated db with new videos")
    else:
        exit()


if __name__ == "__main__":
    main()

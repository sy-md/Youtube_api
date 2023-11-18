import os
import json
import shutil
import logging as lg
import time

lg.basicConfig(filename="downloader.log", level=lg.INFO, format="%(asctime)s %(message)s")

# 1. get the url from the cleaned.
# 2. download the video from the url
# 3. convert the video to mp3 using ffmpeg
# 4. save the mp3 to the same folder as the video

links = "output/cleaned.json"
dst = "output/"


class video_converter:
    def __init__(self):
        self.links = links
        self.dst = dst

    def download(self):
        """
        this function will download the videos from the url in the cleaned.json file
        and save it to the output folder
        """
        with open(self.links, "r") as mylks:
            data = json.load(mylks)
            # url: +__++_+__+
            print(data[0]["url"])

            for k in data:
                url = k["url"]
                os.system("youtubedr download 'https://youtu.be/{}' ".format(url))
            lg.info("Downloaded the videos to the output folder")
        return self.convert()
    def convert(self):

        for video in self.dst:
            mp4 = video
            if video.endswith(".mp4") or video.endswith(".m4a"):
                """
                using os.system to convert the video to mp3
                in the format of ffmpeg -i input_file output_file
                """
                lg.info(f"Converting {video} to mp3 there are {len(video)} videos left")
                os.system(f"ffmpeg -i '{video}' '{video[:-4]}'.mp3")
                lg.info(f"removing {video}")
                os.remove(mp4)

    def test():
        """
        this function will test if the download function works
        and convert function works
        """
        def download():
            """
            download the video from the url
            """
            url_id = "AYKYvVkhIYo"
            lg.info("Testing the download function...")
            os.system(f"youtubedr download 'https://youtu.be/{url_id}'")
            lg.info("Downloaded the video")

        def convert():
            # convert the video to mp3
            for x in os.listdir():
                if x.endswith(".mp4"):
                    lg.info("Testing the convert function... data is {}".format(type(x)))
                    print(f"Converting {x} to mp3")
                    # ffmepeg seems to be receiving the wrong data type
                    os.system(f"ffmpeg -i '{x}' '{x[:-4]}.mp3' ")


        ans = input("[y]downlaod [n]convert:")
        if ans == "y":
            return download()
        else:
            return convert()


if __name__ == "__main__":
    #test the download function
    video_converter.test()
    #lg.info("Starting the download process")
    #video_converter.download()







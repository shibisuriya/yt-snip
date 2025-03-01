import os
import yt_dlp
from constants import YT_SNIPS, TEMPORARY_DOWNLOAD_DIRECTORY


def download_youtube_video(
    url,
    output_dir=os.path.join("./", TEMPORARY_DOWNLOAD_DIRECTORY),
    format="best",
):
    ydl_opts = {
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",  # Save with the video title
        "format": format,  # Video format
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"An error occurred: {e}")

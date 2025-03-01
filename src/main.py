import argparse
from helpers import download_youtube_video
from constants import YT_SNIPS, TEMPORARY_DOWNLOAD_DIRECTORY
import os


def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to download and cut YouTube videos."
    )
    parser.add_argument("url", type=str, help="URL of the YouTube video")
    parser.add_argument(
        "-s",
        "--start",
        type=str,
        required=False,
        help="Start time in hh:mm:ss format",
    )
    parser.add_argument(
        "-e",
        "--end",
        type=str,
        required=False,
        help="End time in hh:mm:ss format",
    )

    args = parser.parse_args()
    print(args)

    try:
        if not args.start and not args.end:
            download_youtube_video(args.url, os.path.join("./", YT_SNIPS))
        else:
            download_youtube_video(args.url, os.path.join("./", TEMPORARY_DOWNLOAD_DIRECTORY))
            if not args.start:
                # Assume 00:00:00 as the start time.
            else not args.end
                # Assume 00:00:00 as the start time.
            else not args.end

    except Exception:
        print("Downloading failed!")


if __name__ == "__main__":
    main()

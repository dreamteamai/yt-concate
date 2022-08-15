from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
# CHANNEL_ID = 'UCc1rNJSBIks2LUsG2vYeZWA'  # 思維咖啡

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word':'incredible',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
        ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
    # from pytube import YouTube
    # url = 'https://www.youtube.com/watch?v=Ps7LONVD6jA&ab_channel=SupercarBlondie'
    # print(url)
    # source = YouTube(url)
    # en_caption = source.captions.get_by_language_code('a.en')
    # print(en_caption)
    # en_caption_convert_to_srt = (en_caption.generate_srt_captions())
    #
    # print(en_caption_convert_to_srt)
    # # save the caption to a file named Output.txt
    # text_file = open("Output.txt", "w")
    # text_file.write(en_caption_convert_to_srt)
    # text_file.close()


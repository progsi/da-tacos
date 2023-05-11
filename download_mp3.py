from __future__ import unicode_literals
import yt_dlp
import os
import pandas as pd


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

def download_clip(url, outdir):

    filename = os.path.join(outdir, url.split("?v=")[-1])
    
    if not os.path.isfile(filename + '.mp3'):

        ydl_opts = {
            'ffmpeg_location': '../ffmpeg/ffmpeg',
            'format': 'bestaudio/best',
            'outtmpl': filename,
            'noplaylist': True,
            'continue_dl': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', }],
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.cache.remove()
                info_dict = ydl.extract_info(url, download=False)
                ydl.prepare_filename(info_dict)
                ydl.download([url])
                return True
        except Exception:
            return False


def main(df, outdir):

    for k, row in df.iterrows():
        print("{:d} de {:d} - {} - {}".format(k, len(df), row["perf_id"], row["yt_id"]))
        # name = "_".join((str(row["perf_id"]), str(row["yt_id"])))
        if type(row["yt_id"]) == str:
            download_clip("https://youtube.com/watch?v=" + row["yt_id"], outdir)


if __name__ == "__main__":
    
    input_file = 'data/yt_id_list.csv'
    output_dir = '../data/da-tacos/mp3/'
        
    df_list = pd.read_csv(input_file, sep=',')
    df_list.columns = ["index", "perf_id", "yt_id"]
    
    main(df_list, output_dir)

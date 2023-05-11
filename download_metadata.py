from youtubesearchpython import Video, ResultMode
import json
import os 
import pandas as pd


def main(df, outdir):

    for k, row in df.iterrows():
        print("{:d} de {:d} - {} - {}".format(k, len(df), row["perf_id"], row["yt_id"]))
        # name = "_".join((str(row["perf_id"]), str(row["yt_id"])))
        if type(row["yt_id"]) == str:
            
            target_file = output_dir + row["yt_id"] + '.json'
            if not os.path.isfile(target_file) and type(row["yt_id"]) == str:
                try:
                    response = Video.getInfo("https://youtube.com/watch?v=" + row["yt_id"], mode = ResultMode.json)
                    
                    with open(target_file, "w") as f:
                        json.dump(response, f)
                except TypeError:
                    continue
            

if __name__ == "__main__":
    
    input_file = 'data/yt_id_list.csv'
    output_dir = '../data/da-tacos/metadata/'
        
    df_list = pd.read_csv(input_file, sep=',')
    df_list.columns = ["index", "perf_id", "yt_id"]
    
    main(df_list, output_dir)
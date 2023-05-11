import h5py
import pandas as pd
import os


def main(df, output_dir):
    
    for root, dirs, files in os.walk(initial_feature_dir):
        
        for file in files:
            
            if file.endswith('.h5'):
            
                file_path = os.path.join(root, file)
                
                perf_id = file.split("_")[1]
                yt_id = df[df.perf_id == int(perf_id)].yt_id.values[0]
                
                if type(yt_id) == str:
                    f = h5py.File(file_path, 'r')
                    crema = f["crema"][:]
                    
                    f_out = h5py.File(output_dir + yt_id + '.h5', 'w')
                    
                    f_out.create_dataset("crema", data=crema, compression='gzip')
                    
                    f.close()
                    f_out.close()
        
        
    
    

if __name__ == "__main__":
    
    input_file = 'data/yt_id_list.csv'
    initial_feature_dir = 'data/da-tacos_benchmark_subset_crema/'
    output_dir = '../data/da-tacos/features/'
        
    df_list = pd.read_csv(input_file, sep=',')
    df_list.columns = ["index", "perf_id", "yt_id"]
    
    main(df_list, output_dir)

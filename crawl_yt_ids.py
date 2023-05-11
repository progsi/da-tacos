import requests
from lxml import html
import pandas as pd

# List of IDs

def main():
    # Iterate over the ID list
    
    df = pd.read_csv('data/da-tacos_benchmark.csv', sep=';')
    
    yt_id_list = []
    
    for perf_id in df.P_ID:
        # Construct the URL for the current ID
        url = f"http://www.secondhandsongs.com/performance/{perf_id}"

        # Send a GET request to the URL and retrieve the HTML content
        response = requests.get(url)
        html_content = response.content

        # Parse the HTML content into an lxml tree
        tree = html.fromstring(html_content)

        # Find the target element using the XPath and get the value of its "id" attribute
        target_element = tree.xpath('/html/body/section[4]/div/div[1]/div[2]/section[1]/div/div/div[1]/div/div[1]/div[1]/div/div[1]/a/img')
        
        try:
            yt_id_list.append({"P_ID": perf_id, "yt_id": target_element[0].get("src").split('/')[-2]})
        except:
            print(f"Error for {perf_id}")
            yt_id_list.append({"P_ID": perf_id, "yt_id": None})


    
    pd.DataFrame(yt_id_list).to_csv("data/yt_id_list.csv")

if __name__ == "__main__":
    
    main()
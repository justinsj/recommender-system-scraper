import argparse
import pandas as pd
from classes.clients import clients
import traceback
import json
import time
import requests
import os

from constants.data import data
min_i = 0
def main(output_path):
    amazon_client = clients.Amazon()

    results = data

    with open('tmp.' + output_path , 'a') as f:
        for key in results:
            if (int(key.replace('refrigerator','')) < min_i): continue
            result = results[key]
            link = result['link']
            node_data = amazon_client.GetNodeData(link)
            # result['storeText'] = node_data['storeText']
            result['imageSrcUrl'] = node_data['imageSrc']
            # result['details'] = node_data['details']
            # result['productId'] = node_data['productId']
            
            results[key] = result

            img_data = requests.get(node_data['imageSrc']).content

            img_name = key + '.jpg'
            with open(os.path.join('images',img_name), 'wb') as handler:
                handler.write(img_data)

            result['imageSrc'] = '[pre]' + img_name + '[post]'
            f.write(f'"{key}": {json.dumps(result, indent=2)},\n')

            
            time.sleep(3)
            #print("\n\n\nresults: ", results)
    # Output file if path is provided
    if (output_path):
        print("Saving to: ", output_path)
        # output_df = pd.read_json(
        #     json.dumps(results),
        #     orient='index'
        #     )
        # output_df.to_csv(output_path)

        with open(output_path, 'w+') as f:
            f.write('export const data = ' + json.dumps(results,indent=2))

    print("""
*******************
***  Completed  ***
*******************""")

if __name__ == '__main__':
    # Load command line arguments
    parser = argparse.ArgumentParser(description='Export leads from csv into Salesforce')

    parser.add_argument('-o','--out_path', type=str, default='outfile', help='if provided, writes output to the given path')
    parser.add_argument('--test', default=False, action='store_true')

    args = parser.parse_args()

    main(args.out_path)

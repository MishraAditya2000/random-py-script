import pandas as pd
import requests
import time
start=time.time()
# Read the CSV file
csv_file_path = './demo product.csv'
data = pd.read_csv(csv_file_path)

# ImgBB API key
imgbb_api_key = 'd89f4854e663f5ed6c680565d7800530'

for index, row in data.iterrows():
    filename = row['file_name']  # Replace with the actual column name
    # image_path = './product image/'+filename  # Adjust the image path accordingly
    print(filename);
    img_arr=[]
    new=filename.split('|');
    for file in new:
        image_path = './product image/'+file  # Adjust the image path accordingly
        print(image_path)
        with open(image_path, 'rb') as image_file:
            response = requests.post(
            'https://api.imgbb.com/1/upload?key=' + imgbb_api_key,
            files={'image': image_file})
            if response.status_code == 200:
                image_url = response.json()['data']['url']
                img_arr.append(image_url);
            else:
                exit()
    print(img_arr);
    data.at[index, 'image_url'] = str(img_arr) # Replace with the actual column name
    # Save the updated data back to the CSV file
    data.to_csv(csv_file_path, index=False)
end=time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
    #     print(response)
    #     if response.status_code == 200:
    #         image_url = response.json()['data']['url']
    #         print(image_url)


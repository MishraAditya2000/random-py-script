import pandas as pd
import requests

# Read the CSV file
csv_file_path = './demo product.csv'
data = pd.read_csv(csv_file_path)

# ImgBB API key
imgbb_api_key = ''

for index, row in data.iterrows():
    filename = row['file_name']  # Replace with the actual column name
    image_path = './product image/'+filename  # Adjust the image path accordingly
    print(filename);
    print(image_path);
    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://api.imgbb.com/1/upload?key=' + imgbb_api_key,
            files={'image': image_file}
        )
        print(response)
        if response.status_code == 200:
            image_url = response.json()['data']['url']
            print(image_url)
            data.at[index, 'image_url'] = image_url  # Replace with the actual column name

# Save the updated data back to the CSV file
data.to_csv(csv_file_path, index=False)

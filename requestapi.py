import requests, base64


import requests
import json 


url = "https://api.appetize.io/v1/apps"
apikey ="tok_qkkj7paq6wob2kms3zfck5ubnm"
user = ""
basic = f"{apikey}:"
basic = base64.b64encode(basic.encode()).decode()
headers = {
    "Authorization": f"Basic {basic}",
    "Content-Type": "application/json"
}



# Basic payload with only required fields
payload = {
    "url": "http://152.69.212.39:18398/20250322_205310_upload.apk",
    "platform": "android",
    "fileType": "apk"
}

response = requests.post(url, headers=headers, json=payload)
print("Status Code:", response.status_code)
print("Response Text:", response.text)
data = json.loads(response.text)
app_url = data["appURL"]
last_id = app_url.rstrip('/').split('/')[-1]
print(f"App URL: {app_url}")
print(f"Extracted ID: {last_id}")
print(f"Embeded url: https://appetize.io/embed/{last_id}")



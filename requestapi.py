import requests
import base64
import json

def get_basic_auth_header(apikey: str) -> dict:
    """
    Creates and returns the HTTP headers with Basic Authentication
    using the provided API key.
    """
    # Create the basic auth string (format: "apikey:")
    basic = f"{apikey}:"
    # Base64 encode the string
    basic_encoded = base64.b64encode(basic.encode()).decode()
    # Return the headers dictionary
    return {
        "Authorization": f"Basic {basic_encoded}",
        "Content-Type": "application/json"
    }

def post_app_to_appetize(apikey: str, apk_url: str, platform: str = "android", fileType: str = "apk") -> dict:
    """
    Sends a POST request to the Appetize API with the provided parameters.
    
    :param apikey: Your Appetize API key.
    :param apk_url: URL of the APK file to upload.
    :param platform: Platform type (default "android").
    :param fileType: Type of file (default "apk").
    :return: Parsed JSON response as a dictionary.
    """
    url = "https://api.appetize.io/v1/apps"
    headers = get_basic_auth_header(apikey)
    
    payload = {
        "url": apk_url,
        "platform": platform,
        "fileType": fileType
    }
    
    response = requests.post(url, headers=headers, json=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    # If the response is not successful, return an empty dictionary or handle accordingly
    if response.status_code != 200:
        print("Error: API call failed!")
        return {}
    
    return response.json()

def extract_app_data(response_data: dict) -> tuple:
    """
    Extracts the application URL, the last segment of the URL (as the ID),
    and constructs the embedded URL.
    
    :param response_data: Dictionary response from the Appetize API.
    :return: Tuple containing (app_url, extracted_id, embedded_url).
    :raises ValueError: If the response data is missing the "appURL" key.
    """
    if "appURL" not in response_data:
        raise ValueError("Invalid response data: 'appURL' key not found.")
    
    app_url = response_data["appURL"]
    # Extract the ID from the URL by splitting on '/'
    extracted_id = app_url.rstrip('/').split('/')[-1]
    embedded_url = f"https://appetize.io/embed/{extracted_id}"
    
    return app_url, extracted_id, embedded_url

def main():
    # Replace with your actual API key and APK URL
    apikey = "tok_qkkj7paq6wob2kms3zfck5ubnm"
    apk_url = "http://152.69.212.39:18398/20250322_205310_upload.apk"
    
    # Post the APK to Appetize API
    response_data = post_app_to_appetize(apikey, apk_url)
    
    if response_data:
        try:
            app_url, extracted_id, embedded_url = extract_app_data(response_data)
            print(f"App URL: {app_url}")
            print(f"Extracted ID: {extracted_id}")
            print(f"Embedded URL: {embedded_url}")
        except ValueError as ve:
            print("Error processing API response:", ve)

if __name__ == "__main__":
    main()

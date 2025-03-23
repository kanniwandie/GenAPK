import streamlit as st

from requestapi import extract_app_data, post_app_to_appetize
from uploadtonet import upload_file
import dotenv,os
dotenv.load_dotenv()

def main():
    st.title("Results")

    #Button to download the apk
    st.download_button(
        label="Download APK",
        data=open(st.session_state.apk, "rb").read(),
        file_name="app-debug.apk",
        mime="application/vnd.android.package-archive",
    )


    # Layout with columns for web browser and content
    # if 'initialized' not in st.session_state or not st.session_state.initialized:
    st.session_state.path = st.session_state.path
    apk = st.session_state.apk

    deploy(apk)



API_KEY = os.getenv("APPETIZE_APIKEY")
if API_KEY is None:
    st.error("API key not found. Please set the APPETIZE_APIKEY environment variable.")
    st.stop()
    API_KEY = ""
def deploy(apk_path):
    web_path = upload_file(apk_path)
    print(web_path)
    if API_KEY is not None:
        app_data=  post_app_to_appetize(apikey=API_KEY, apk_url=web_path)
        print("App data", app_data)

    else:
        # Handle the case where api_key is None
        # For example:
        raise ValueError("API key cannot be None")

    app_url, extracted_id, embedded_url = extract_app_data(app_data)

    # Button to open the embbeded app in a new tab
    st.write(f"View your app here: [{embedded_url}]({embedded_url})")



    return app_data

if __name__ == "__main__":
    main()

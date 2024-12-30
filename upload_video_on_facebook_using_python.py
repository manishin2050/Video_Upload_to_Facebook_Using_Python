# code starts here

import requests

# Access Token and Page ID
access_token = "Paste_Access_Token_Here" # make facebook developer account and create graph api for facebook page
page_id = "Paste_Facebook_Page_ID" #get from facebook settings
video_path = "Paste_Video_Path"  # Replace with the actual path to your video file
video_caption = "Best_Video_Ever" # replace with your caption

# Graph API for make request to connect facebook
url = f"https://graph-video.facebook.com/v21.0/{page_id}/videos"

# data upload to facebook
data = {
    "access_token": access_token,
    "title": f"upload by komal {video_caption}",
    "description": video_caption,
    "published": "true",
    "privacy": '{"value":"EVERYONE"}'
}

# converting video as binary
files = {
    "file": open(video_path, "rb"),  # Open the video file in binary mode
}
# print("file: ",files)

# uploading video to facebook
try:
    response = requests.post(url, data=data, files=files)
    response_json = response.json()

    if response.status_code == 200:
        print("Video uploaded successfully!")
        print("Video ID:", response_json.get("id"))
    else:
        print("Failed to upload video.")
        print("Error:", response_json)
except Exception as e:
    print(f"error aaya hai kyuki : {e}")

# code ends here
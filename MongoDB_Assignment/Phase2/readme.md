# Mongodb phase 2 Homework

This is the Mongodb homework for EC500. This project grabs images from a tweeter handler , analyze the images using Google Vision API to recognize products in the images and finally store in them a mongodb database.
Following python libraries are needed to run this project:-
- wget(pip install wget)
- Tweepy(pip install tweepy)
- FFMPEG(Command for Linux:- sudo apt install ffmpeg)
- Google Cloud Vision API(pip install --upgrade google-cloud-vision).
- Pymongo 

Now Tweety Google Cloud API will need your credentials to access information from your twitter account by following steps here[https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/].

For Tweety put your credential information into run.py.
 
Get your Google Vision API Credentials following steps here[https://cloud.google.com/vision/docs/auth]. Download the .json.  authentication file, Rename it as "google_key.json". and put it in the code folder.
 
# Command to run the code- 
  - python run.py --number_of_tweets --folder_name_where_you_want_images_and_Video_to_be_stored --frames_per_seconds     twitter_handle_name_with_@
 - Example:- python run.py --num 20 --output pictures/ --fps 25 @andresiniesta8 
 - Run "python run.py -h" for help with this program. 
 - This program will need username as a must input. All other inputs are optional, they will be used default if not provided by the user. Number of tweets will be assumed as 100 by default, outfolder folder will named as "pictures" and frame rate will be 20.
 
 This program will also generate a label.json file where all labels from images will be stored.

# APIs Homework

This is the API homework for EC500. This project grabs images from a tweeter handler and analyze the images using Google Vision API to recognize products in the images.
Following python libraries are needed to run this project:-
- wget(pip install wget)
- Tweepy(pip install tweepy)
- FFMPEG(Command for Linux:- sudo apt install ffmpeg)
- Google Cloud Vision API(pip install --upgrade google-cloud-vision).

Now Tweety Google Cloud API will need your credentials to access information from your twitter account by following steps here.

For Tweety put your credential information into run.py.
 
 Get your Google Vision API Credentials following steps here[https://cloud.google.com/vision/docs/auth]. Download the .json.  authentication file, Rename it as "google_key.json". and put it in the code folder.
 
 Get your tweeter API credential using this link:-https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/.

#To run the code:- python run.py --number_of_tweets --folder_name_where_you_want_images_and_Video_to_be_stored --frames_per_seconds twitter_handle_name_with_@
 - Example:- python run.py --num 20 --output pictures/ --fps 25 @andresiniesta8 

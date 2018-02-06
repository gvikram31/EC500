# APIs Homework

This is the API homework for EC500. This project grabs images from a tweeter handler and analyze the images using Google Vision API to recognize products in the images.
Some of the python libraries needed to run this project.
- wget(pip install wget)
- Tweepy(pip install tweepy)
- FFMPEG(Command for Linux:- sudo apt install ffmpeg)
- Google Cloud Vision API(pip install --upgrade google-cloud-vision).
Now Tweety Google Cloud API will need your credentials to access information from your twitter account by following steps here.

For Tweety put your credential information into run.py.
 
 Get your Google Vision API Credentials following steps here[https://cloud.google.com/vision/docs/auth]. Download the .json.  authentication file, Rename it as google_key.json. and put it in the code folder.
 
 Get your tweeter API credential using this link:-https://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/.

#To run the code:- Open terminal and write "chmod +x all.sh" then type "./all.sh twitterhandle_youwant". Which will get the 20 images from your mentioned twitter handle, create a video of them and analyze them. 

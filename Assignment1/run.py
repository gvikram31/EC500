import tweepy
import os
from tweepy import OAuthHandler
import json
import wget
import argparse
import configparser
import io
import glob
import google.cloud.vision
consumer_key = "GET THESE KEYS from Twitter"
consumer_secret = "GET THESE KEYS from Twitter"
access_key = "GET THESE KEYS from Twitter"
access_secret = "GET THESE KEYS from Twitter"
# export GOOGLE_APPLICATION_CREDENTIALS = "/home/mjhuria/Desktop/google_key.json"
Link = []
#TODO: Limit by number of tweets?
def parse_arguments():
  parser = argparse.ArgumentParser(description='Download pictures from a Twitter feed.')
  parser.add_argument('username', type=str, help='The twitter screen name from the account we want to retrieve all the pictures')
  parser.add_argument('--num', type=int, default=100, help='Maximum number of tweets to be returned.')
  parser.add_argument('--retweets', default=False, action='store_true', help='Include retweets')
  parser.add_argument('--replies', default=False, action='store_true', help='Include replies')
  parser.add_argument('--output', default='../pictures/', type=str, help='folder where the pictures will be stored')

  args = parser.parse_args()
  return args

def parse_config(config_file):
  config = configparser.ConfigParser()
  config.read(config_file)
  return config

@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status

def init_tweepy():
  # Status() is the data model for a tweet
  tweepy.models.Status.first_parse = tweepy.models.Status.parse
  tweepy.models.Status.parse = parse
  # User() is the data model for a user profil
  tweepy.models.User.first_parse = tweepy.models.User.parse
  tweepy.models.User.parse = parse

def authorise_twitter_api(config):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return auth

def download_images(api, username, retweets, replies, num_tweets, output_folder):
  tweets = api.user_timeline(screen_name=username, count=20, include_rts=retweets, exclude_replies=replies)
  if not os.path.exists(output_folder):
      os.makedirs(output_folder)

  downloaded = 0
  while (len(tweets) != 0):
    last_id = tweets[-1].id

    for status in tweets:
      media = status.entities.get('media', [])
      if(len(media) > 0 and downloaded < num_tweets):
        Link = media[0]['media_url']
        wget.download(media[0]['media_url'],out=output_folder+str(downloaded)+'.jpg')
        downloaded += 1

    tweets = api.user_timeline(screen_name=username, count=20, include_rts=retweets, exclude_replies=replies, max_id=last_id-1)

def doAnalysis(output):
    vision_client = google.cloud.vision.ImageAnnotatorClient()
    print(output+'*.jpg')
    for files in glob.glob(output+'*.jpg'):
        img1 = files
        with io.open(img1, 'rb') as image_file:
            content = image_file.read()
        image = google.cloud.vision.types.Image(content=content)
        response = vision_client.label_detection(image=image)
        web_detect = vision_client.web_detection(image=image).web_detection
        for entity in web_detect.web_entities:
            print('Description: {}'.format(entity.description))

def main():
  arguments = parse_arguments()
  username = arguments.username
  retweets = arguments.retweets
  replies = arguments.replies
  num_tweets = 20
  output_folder = arguments.output

  config = parse_config('../config.cfg')
  auth = authorise_twitter_api(config)
  api = tweepy.API(auth)

  download_images(api, username, retweets, replies, num_tweets, output_folder)
  print(Link)
  analysis = doAnalysis(output_folder)

if __name__=='__main__':
    main()

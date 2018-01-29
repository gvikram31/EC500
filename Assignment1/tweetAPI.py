#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


from __future__ import absolute_import, print_function
import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
consumer_key = "4nh1g0pVxZIfebASTXYL8Cf7E"
consumer_secret = "69wL6UDWA0nVmjyZCJjOjkza3HroLgWlgEAV4crnTA1tMSUpdd"
access_key = "217206877-wtmhPBHNL5FGKAgKsDUUAEwCjYvu9yjVYtZqIYID"
access_secret = "txWd16tYMusJM4Vugg5M6ZIqMVT3zkCuCRyw1ZSi5wJ5F"


def get_all_tweets(screen_name):

    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print ("...%s tweets downloaded so far" % (len(alltweets)))

    #write tweet objects to JSON
    file = open('tweet.json', 'w')
    print ("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)

    #close the file
    print ("Done")
    file.close()

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
    print(api.me().name)
#    api.update_status(status='Testing Tweepy!')
#    api.get_status('Testing Tweepy!')
    api.destroy_status(407458679404134401)
    #api.
    #pass in the username of the account you want to download
    get_all_tweets("@vikramgarhwal31")
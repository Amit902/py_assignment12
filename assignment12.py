#Q.1- What is an access token? Generate your access token for any API.
# (for example Twitter,Spotify etc).

#To Access Token
The Access Token is a credential type and  that can be used by an application to access an API and their features.



#To generate access token


1.>create  your own twitter account
2.>go to the link https://apps.twitter.com
3.>click on create new application icon.
4.>fill the form and create Account
5.>click on create new application
6.>Note the consumer_key,consumer_secrate,access_token,access_token_secrate



#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

#nslookup youtube.com
Address:  192.168.43.1
Name:    google.com
Addresses:  2404:6800:4002:805::200e
          216.58.196.206




#nslookup facebook.com

Address:  192.168.43.1
Name:    facebook.com
Addresses:  2a03:2880:f126:83:face:b00c:0:25de
          31.13.78.35



#Q.3- Using Tweepy library try to extract tweets from Twitter.

import tweepy

consumer_key='*******************'
consumer_secret='***************************'

access_token='**************************************'
access_Token_Secret='*************************************'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_Token_Secret)
api=tweepy.API(auth)
tweets=api.search("#angry",lang="en",count="10",tweet_mode="extended")
print('2525')
print(tweets)
for tweet in tweets:
    print("------------------")
    print(tweet.full_text)
    print("--------------------")



#Q.4- What is a difference between library and API . Figure it out with examples.

A library:
	A liablary is a collection of functions / objects that serves one particular purpose.
	 you could use a library in a variety of projects.
	(Various specialized services in our case)

	example: JQuery library, is a library of prewritten,
	 cross-browser Javascript animations and functions
	which you will need while making a website.


An API:
	An API is an interface for other programs to interact with your program or library
	 without having direct access.
	 ( giving specifications for our need to various vendors in our case)

	example: with Google Map APIs you can show maps for different places without
	writing/hosting the whole code on your server, and just use it,
	 usually this data transfer is in form of JSON i.e JavaScript Object Notation.
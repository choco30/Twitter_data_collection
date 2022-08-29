import os
import logging
import time
import twitter_class
import geocoder
from kafka import KafkaProducer
from json import dumps
import tweepy
from datetime import datetime


class Twitter_data:
	producer = KafkaProducer(bootstrap_servers=["localhost:9092"],value_serializer=lambda x:dumps(x).encode('utf-8'))
	topic_name = "twitter_api"

	def connection(self):
		bearer_token=str(os.environ.get("bearer_token_twitter"))
		Twitter_class = twitter_class.twitter_connection(bearer_token)
		Twitter_account_connection = Twitter_class.make_connection()
		return Twitter_account_connection

	def fetch_data(self,api,loc):
		geolocation=geocoder.osm(loc)
		tweet_response=api.closest_trends(geolocation.lat,geolocation.lng)
		tweets=api.get_place_trends(tweet_response[0]['woeid'])
		tweet_text=""
		dic=dict()
		trend_name=[]
		tweet_url=[]
		tweet_volume=[]
		for i in tweets:
			for j in i["trends"]:
				dic["trend_name"] = j['name']
				dic["twee_url"] =j['url']
				dic["tweet_volume"] =j['tweet_volume']
				print(dic)
				self.producer.send(self.topic_name, value=dic)

		'''for tweet in tweet_response.data:
			tweet_text+=tweet.text
		print(tweet_text)
		#self.producer.send(self.topic_name,value="ad")'''


if __name__ == "__main__":
	logging.info("applicationstatred")
	#loc=input("Enter the Location Country")
	try:
		data = Twitter_data()
		con = data.connection()
		logging.info("connection is made successfully")
		while True:
			data.fetch_data(con, "India")
			time.sleep(60)
			logging.info("data extraction is completed")
	except Exception as e:
		print(e)


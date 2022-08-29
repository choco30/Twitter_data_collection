import tweepy
import os

class twitter_connection:

    def __init__(self,bearer_token):
        self.bearer_token=bearer_token
        self.conn=None

    def make_connection(self):
        conn= tweepy.OAuth2BearerHandler(self.bearer_token)

        return tweepy.API(conn)


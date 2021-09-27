import tweepy
from connect import Connect
import config
from apscheduler.schedulers.blocking import BlockingScheduler

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)

api = tweepy.API(auth)

woeid = 23424768
trends = api.trends_place(woeid)

connection = Connect.get_connection()

db = connection.test4

db.inventory.insert_many(trends)


schedule = BlockingScheduler()

@schedule.scheduled_job('interval', seconds=60)
def timed_job():
    trends = api.trends_place(woeid)
    db.inventory.insert_many(trends)

schedule.start()
import tweepy
from connect import Connect
import config
from apscheduler.schedulers.blocking import BlockingScheduler

# Autentificação e coneção com API do twitter
auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.token_secret)
api = tweepy.API(auth)

# Woeid - Codigo para receber os trends referente a localização Brasil
woeid = 23424768

# Recebe a lista do API com 50 trends em formato Json
trends = api.trends_place(woeid)

# Conecta ao mongo e escreve no Database
connection = Connect.get_connection()
db = connection.test

# Escreve no banco de dados a lista com 50 trends a cada 30 minutos
schedule = BlockingScheduler()

@schedule.scheduled_job('interval', seconds=1800)
def timed_job():
    trends = api.trends_place(woeid)
    db.inventory.insert_many(trends)

schedule.start()
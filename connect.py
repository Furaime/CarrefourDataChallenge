from pymongo import MongoClient
import config

class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient(config.mongo_url)
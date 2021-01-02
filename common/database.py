import os
from typing import Dict

import pymongo


class Database:
    # URI = "mongodb://127.0.0.1:27017/pricing"
    URI = os.environ.get('MONGODB_URI')
    DATABASE = pymongo.MongoClient(URI, onnectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True,
                                   connect=False,
                                   maxPoolsize=1).get_database('pricing')

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].remove(query)

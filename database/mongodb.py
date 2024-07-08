from pymongo import MongoClient


class Database:
    
    def __init__(self, collection:str):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["robos"]
        self.collection = collection

    def insert(self, data: dict):
        """
        Faz uma inserção no banco.

        Argumentos:
        - data: Os dados desejados para fazer a inserção.
        """
        collection = self.db[self.collection]
        result = collection.insert_one(data)
        return result.inserted_id

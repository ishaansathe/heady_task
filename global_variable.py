import pymongo
import os
from dotenv import load_dotenv , find_dotenv

load_dotenv(verbose=True)
client = pymongo.MongoClient(os.getenv("CLIENT"))
mongo_db = client[os.getenv("MONGO_DB")]
secret_key = os.getenv("Secret_key")

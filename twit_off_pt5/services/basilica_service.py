import basilica, os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("basilica_key")

connection = basilica.Connection(key)


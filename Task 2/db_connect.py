from mongoengine import connect
import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__), '..', 'Task 1', 'config.ini')

config = configparser.ConfigParser()
config.read(config_file_path) 

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASS')
db_name = 'RabbitMQ'

def connection():
    connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{db_name}.bbyacvi.mongodb.net/{db_name}?retryWrites=true&w=majority&appName=hmweb8""", ssl=True)

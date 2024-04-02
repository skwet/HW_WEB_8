from mongoengine import connect
import configparser

config = configparser.ConfigParser()
config.read('Task 1/config.ini')

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASS')
db_name = config.get('DB', 'DB_NAME')

def connection():
    connect(host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{db_name}.bbyacvi.mongodb.net/{db_name}?retryWrites=true&w=majority&appName=hmweb8""", ssl=True)

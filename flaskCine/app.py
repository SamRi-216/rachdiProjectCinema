from flask import Flask
import pymysql

from config import Config
app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
        )
@app.route('/')
def index():
    return 'test'

from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
FB_EMAIL = os.getenv('FB_EMAIL')
FB_PASSWORD = os.getenv('FB_PASSWORD')
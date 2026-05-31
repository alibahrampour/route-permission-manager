import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

USERNAME = os.getenv("USERNAME")

PASSWORD = os.getenv("PASSWORD")

ROLE_ID = os.getenv("ROLE_ID")

RETRY_COUNT = int(
    os.getenv("RETRY_COUNT", 3)
)
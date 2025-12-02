import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get_database_uri():
        return f"mysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
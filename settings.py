import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path().resolve().joinpath('.env')
load_dotenv(dotenv_path)

SHEET_KEY = os.environ.get('SHEET_KEY')
API_TOKEN = os.environ.get('API_TOKEN')

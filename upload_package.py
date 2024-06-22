from dotenv import load_dotenv
import os

load_dotenv()

TWINE_USERNAME = os.getenv('TWINE_USERNAME')
TWINE_PASSWORD = os.getenv('TWINE_PASSWORD')

os.system(f'twine upload dist/* -u {TWINE_USERNAME} -p {TWINE_PASSWORD}')

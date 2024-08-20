import os

# postgresql connection
HUB_SERVER = os.environ['HUB_SERVER']
HUB_PORT = os.environ['HUB_PORT']
HUB_USER = os.environ['HUB_USER']
HUB_PASSWORD = os.environ['HUB_PASSWORD']

# datetime format
TIMEZONE = 'Asia/Ho_Chi_Minh'
DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

# path
PAGE_PATH = "./pages/"
IMAGE_PATH = "./images/"
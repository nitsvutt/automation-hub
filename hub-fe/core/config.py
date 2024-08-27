import os

class Environment():
    def __init__(self):
        self.TIMEZONE = 'Asia/Ho_Chi_Minh'
        self.DATE_FORMAT = '%Y-%m-%d'
        self.DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class DBConnection():
    def __init__(self):
        self.HUB_SERVER = os.environ['HUB_SERVER']
        self.HUB_PORT = os.environ['HUB_PORT']
        self.HUB_USER = os.environ['HUB_USER']
        self.HUB_PASSWORD = os.environ['HUB_PASSWORD']

class Path():
    def __init__(self):
        self.PAGE_PATH = "./pages/"
        self.ASSET_PATH = "./assets/"
        self.IMAGE_PATH = self.ASSET_PATH + "images/"
        self.CSS_PATH = self.ASSET_PATH + "css/"

env = Environment()
dbconnection = DBConnection()
path = Path()
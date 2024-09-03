from dataclasses import dataclass
import os

@dataclass
class DBConnection:
    DB_TYPE: str
    SERVER: str
    PORT: int
    USER: str
    PASSWORD: str
    DB: str
    @property
    def URL(self) -> str:
        return f'{self.DB_TYPE}://{self.SERVER}:{self.PORT}@{self.USER}:{self.PASSWORD}/{self.DB}'

@dataclass
class DatetimeFormat:
    TIMEZONE: str
    DATE_FORMAT: str
    DATETIME_FORMAT: str

hub_db = DBConnection(
    DB_TYPE='postgresql', SERVER=os.environ['HUB_SERVER'], PORT=os.environ['HUB_PORT'],
    USER=os.environ['HUB_USER'], PASSWORD=os.environ['HUB_PASSWORD'], DB=os.environ['HUB_DB']
)

dt_format = DatetimeFormat(
    TIMEZONE='Asia/Ho_Chi_Minh', DATE_FORMAT='%Y-%m-%d', DATETIME_FORMAT='%Y-%m-%d %H:%M:%S'
)

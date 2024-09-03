from dataclasses import dataclass
import os

@dataclass
class DatetimeFormat:
    TIMEZONE: str
    DATE_FORMAT: str
    DATETIME_FORMAT: str

@dataclass
class Path:
    PAGE_PATH: str
    ASSET_PATH: str
    @property
    def IMAGE_PATH(self) -> str:
        return self.ASSET_PATH + 'images/'
    @property
    def CSS_PATH(self) -> str:
        return self.ASSET_PATH + 'css/'

dt_format = DatetimeFormat(
    TIMEZONE='Asia/Ho_Chi_Minh', DATE_FORMAT='%Y-%m-%d', DATETIME_FORMAT='%Y-%m-%d %H:%M:%S'
)

path = Path(
    PAGE_PATH = "./pages/", ASSET_PATH = "./assets/"
)
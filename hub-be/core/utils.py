from datetime import datetime
import pytz

from core.config import dt_format

def current_sysdate():
    return datetime.now(pytz.timezone(dt_format.TIMEZONE)).strftime(dt_format.DATE_FORMAT)

def current_systime():
    return datetime.now(pytz.timezone(dt_format.TIMEZONE)).strftime(dt_format.DATETIME_FORMAT)
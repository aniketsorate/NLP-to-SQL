from time import time
from app.core.config import settings

request_log = {}

def check_rate_limit(user="default"):
    now = time()

    if user in request_log and now - request_log[user] < settings.RATE_LIMIT_SECONDS:
        return False

    request_log[user] = now
    return True
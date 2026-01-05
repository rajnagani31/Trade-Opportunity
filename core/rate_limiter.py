import threading
from time import time
from collections import defaultdict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RateLimiter")

RATE_LIMIT = 1      # requests
WINDOW = 60         # seconds

# Thread-safe request store
REQUEST_STORE = defaultdict(list)
LOCK = threading.Lock()

def is_rate_limited(key: str):
    if not key:
        logger.error("Rate limiter key is invalid or empty.")
        raise ValueError("Key must be a non-empty string.")

    now = time()

    with LOCK:  # Ensure thread safety
        # Remove expired timestamps
        REQUEST_STORE[key] = [
            t for t in REQUEST_STORE[key] if now - t < WINDOW
        ]

        if len(REQUEST_STORE[key]) >= RATE_LIMIT:
            logger.info(f"Rate limit exceeded for key: {key}")
            return True

        # Add the current timestamp
        REQUEST_STORE[key].append(now)

    logger.debug(f"Request allowed for key: {key}. Current window: {REQUEST_STORE[key]}")
    return False


IP_LIMIT = 1                 # max requests
WINDOW = 60 * 60 * 24        # 24 hours (1 day)

IP_REQUESTS = defaultdict(list)
LOCK = threading.Lock()

def is_ip_rate_limited(ip: str) -> bool:
    if not ip:
        logger.error("IP address missing for rate limiting")
        return True

    now = time()

    with LOCK:
        # remove old timestamps (older than 24 hours)
        IP_REQUESTS[ip] = [
            t for t in IP_REQUESTS[ip] if now - t < WINDOW
        ]

        if len(IP_REQUESTS[ip]) >= IP_LIMIT:
            logger.warning(f"Daily IP limit exceeded: {ip}")
            return True

        # record current request
        IP_REQUESTS[ip].append(now)

    logger.info(f"IP allowed: {ip}, count={len(IP_REQUESTS[ip])}")
    return False
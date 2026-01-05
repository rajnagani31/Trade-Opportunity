import uuid
from typing import Dict
from time import time
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SessionManager")

SESSIONS: Dict[str, float] = {}

SESSION_EXPIRY = 60 * 60 * 24  # 1 day
LOCK = threading.Lock()

def get_or_create_session(session_id: str | None):
    now = time()

    with LOCK:  
        if session_id and session_id in SESSIONS:
            if now - SESSIONS[session_id] < SESSION_EXPIRY:
                SESSIONS[session_id] = now  # refresh session
                logger.info(f"Session refreshed: {session_id}")
                return session_id
            else:
                logger.info(f"Session expired: {session_id}")
                del SESSIONS[session_id]  # expired

        new_session_id = str(uuid.uuid4())
        SESSIONS[new_session_id] = now
        logger.info(f"New session created: {new_session_id}")
        return new_session_id

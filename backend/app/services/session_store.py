from typing import Dict
from threading import Lock


class SessionStore:
    """
    In-memory session store.
    Later replaceable with Redis / DB without breaking code.
    """

    def __init__(self):
        self._sessions: Dict[str, Dict] = {}
        self._lock = Lock()

    def get(self, session_id: str) -> Dict:
        with self._lock:
            return self._sessions.get(session_id, {})

    def set(self, session_id: str, context: Dict):
        with self._lock:
            self._sessions[session_id] = context

    def exists(self, session_id: str) -> bool:
        with self._lock:
            return session_id in self._sessions

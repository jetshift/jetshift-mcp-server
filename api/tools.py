import requests
from api import config


def ping_server() -> str:
    """
    Ping the JetShift API server to check if it is alive.
    """
    try:
        resp = requests.get(f"{config.JETSHIFT_API_URL}/test/", timeout=5)
        resp.raise_for_status()
        return resp.text.strip()
    except Exception as e:
        return f"Ping failed: {e}"

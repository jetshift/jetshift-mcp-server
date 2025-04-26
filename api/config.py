import os
from dotenv import load_dotenv

# Automatically load .env from the root
load_dotenv()

# Read environment variables with defaults
JETSHIFT_API_URL = os.getenv("JETSHIFT_API_URL", "http://127.0.0.1:8000/api")

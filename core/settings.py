from pathlib import Path
from os import getenv

# DIRS
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "template"
STATIC_DIR = BASE_DIR / "static"
STATIC_URL = "/static/"

# DATABASE
DB_URL = getenv("DB_URL")

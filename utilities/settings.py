import os, logging
from dotenv import load_dotenv

log = logging.getLogger(__name__)
load_dotenv()

# ------------------------------------------------------------------ #
# Settings classes
# ------------------------------------------------------------------ #

class WebullSettings:
    APP_ID=os.environ.get('WEBULL_API_APP_ID')
    APP_KEY=os.environ.get('WEBULL_API_KEY')
    APP_SECRET=os.environ.get('WEBULL_API_SECRET')
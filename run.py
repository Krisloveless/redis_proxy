from src.main import app
from dotenv import dotenv_values

config = dotenv_values(".env")
# OrderedDict([('REDIS_HOST', ''), ('CACHE_EXPIRY', ''), ('CACHE_CAPACITY', ''), ('HOST', '')])

HOST = config["HOST"] or "0.0.0.0"
PORT = int(config["PORT"]) if config["PORT"] else 5000

app.run(port=PORT, host=HOST)

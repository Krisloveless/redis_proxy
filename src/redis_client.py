from dotenv import dotenv_values
import redis
import asyncio

config = dotenv_values(".env")

CACHE_EXPIRY = int(config['CACHE_EXPIRY']) if config['CACHE_EXPIRY'] else 600
CACHE_CAPACITY = int(config['CACHE_CAPACITY']) if config['CACHE_CAPACITY'] else 5
REDIS_HOST = config['REDIS_HOST'] or "0.0.0.0"


import os
import redis.asyncio as redis
from kombu.utils.url import safequote

# Read environment variables for Redis configuration
redis_host = safequote(os.environ.get('REDIS_HOST', 'localhost'))
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_db = int(os.environ.get('REDIS_DB', 0))
redis_username = os.environ.get('REDIS_USERNAME', None)
redis_password = os.environ.get('REDIS_PASSWORD', None)

# Initialize Redis client
redis_client = None

async def initialize_redis():
    global redis_client
    try:
        redis_client = redis.Redis(
            host=redis_host,
            port=redis_port,
            db=redis_db,
            decode_responses=True,
            username=redis_username,
            password=redis_password,
        )
        # Test the connection
        await redis_client.ping()
        print(f"Connected to Redis on port: {redis_port} !" )
    except Exception as e:
        print(f"Error initializing Redis client: {e}")
        redis_client = None

# Functions for Redis operations
async def add_key_value_redis(key, value, expire=None):
    try:
        if redis_client is None:
            raise redis.ConnectionError("Redis client is not initialized.")
        await redis_client.set(key, value)
        if expire:
            await redis_client.expire(key, expire)
    except Exception as e:
        print(f"Error adding key-value to Redis: {e}")
        raise

async def get_value_redis(key):
    try:
        if redis_client is None:
            raise redis.ConnectionError("Redis client is not initialized.")
        return await redis_client.get(key)
    except Exception as e:
        print(f"Error getting value from Redis: {e}")
        raise

async def delete_key_redis(key):
    try:
        if redis_client is None:
            raise redis.ConnectionError("Redis client is not initialized.")
        await redis_client.delete(key)
    except Exception as e:
        print(f"Error deleting key from Redis: {e}")
        raise
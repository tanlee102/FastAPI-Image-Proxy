from cachetools import TTLCache

# Cache with a maximum size of 100 entries and a TTL of 1800 seconds (30 minutes)
cache = TTLCache(maxsize=700, ttl=86400)
# redis_proxy

A proxy example for Redis.

### Test

```
make test
```

### Deploy

```
make deploy
```

#### Starting local Redis server

```
docker-compose up -d redis
# tear down with:   docker-compose down
```

#### Loading data to Redis

The current test data is placed at `/data/redis_data`.

```
docker exec local_redis bash -c "cat redis_data | redis-cli --pipe"
```

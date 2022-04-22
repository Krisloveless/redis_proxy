# redis_proxy

A proxy for Redis.

### Test

```
make test
```

### Deploy

```
make deploy
# tear down with:   docker-compose down
```

You can either use `make deploy` or follow the process below

##### 1. Starting local Redis server

```
docker-compose up -d redis
# tear down with:   docker-compose down
```

##### 2. Loading data to Redis

The current test data is placed at `/data/redis_data`.

```
docker exec local_redis bash -c "cat redis_data | redis-cli --pipe"
```

##### 3. Start web server

```
python3 run.py &
```

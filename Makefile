.PHONY: test

install:
	pip3 install -r requirements.txt
test:
	pytest test
deploy:
	docker-compose up -d redis
	docker exec local_redis bash -c "cat redis_data | redis-cli --pipe"
	python3 run.py &
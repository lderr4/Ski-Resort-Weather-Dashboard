build: 
	docker-compose build

down:
	docker-compose down --volumes

run:
	make down && docker-compose up -d

stop:
	docker-compose stop
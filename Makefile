init:
	docker-compose build
start:
	docker-compose up -d &&\
	watchman-make -p 'src/**/*.py' -s 1 --run 'touch src/uwsgi-reload'
stop:
	docker-compose stop	
logs:
	docker-compose logs --tail=50 -f flask
	
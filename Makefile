init:
	docker-compose build
install_dev_dependencies:
	docker-compose exec client npm i
start:
	docker-compose up -d &&\
	watchman-make -p 'src/**/*.py' -s 1 --run 'touch src/uwsgi-reload'
stop:
	docker-compose stop	
flask_logs:
	docker-compose logs --tail=50 -f flask
client_logs:
	docker-compose logs --tail=50 -f logs

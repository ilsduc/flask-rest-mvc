# Flask MVC server for Rest API

You fill find here

- A flask service for api
- A little MVC for Rest with Flask
- A PGSQL database
- A PGAdmin service

# Prequisites

You must have Docker and Docker Compose installed, if it's not done yet, please refer to those getting started guides

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

# Installation

1. Build containers:

```bash
$ make init
```

1. `(bis)` Install client dev dependencies

```bash
$ make install_dev_dependencies
```

2. Run apps

```bash
$ make start
```

3. Connect to PG Admin and create the demo table. You will find the creation script in create_table_demo.sql

Then ...

- Hits http://localhost:5000 for API endpoints
- Hits http://localhost:3000 for client part
- Hits http://localhost:8000 to connect to PG Admin

# Create the connection with PG admin

1. Browse `http://localhost:8000`
2. Connect with development credentials set in `docker-compose.yml` file at the `db` service section
3. Click on the 'Add new server' button in the 'Quick links' dashboard section
4. Choose the name your want for the new server
5. In the 'connection' tab, fill the host whith the database service name `db` and the others information as there are filled in `docker-compose.yml` (`POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`) and save.
6. In the new connection explore to Servers > `<your server name>` > Databases > `<your database>` > Schemas > public
7. Click right on Tables >> Query Tool
8. Paste the create demo table statment from `create_table_demo.sql` and execute it !

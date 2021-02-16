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

2. Run apps

```bash
$ make start
```

3. Connect to PG Admin and create the demo table. You will find the creation script in create_table_demo.sql

Then ...

- Hits http://localhost:5000/demos for get demos
- Hits http://localhost:8000 to connect to PG Admin

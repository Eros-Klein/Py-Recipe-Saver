# Recipe List

## Goals
- Creating a very basic __full-stack application__.
- Learning how to use __Flask__ to create a RESTful API.
- Leaning how to access a database from a Flask application using __psycopg2__.
- Learning how to use __React__ to create a frontend that consumes the API.
- Learning how to use __Docker__ to containerize the application.

## Requirements
- [Docker](https://docs.docker.com/get-docker/)
- [Conda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [Pip](https://pip.pypa.io/en/stable/installation/)
- [Node.js](https://nodejs.org/en/download/)

## Getting Started
- Run a local database thats not file based (Postgres recommended)
  ```
    docker pull postgres:latest
    docker run --name recipe-db \
    -e POSTGRES_DB=recipe_db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=recipe \
    -d -p 5432:5432 \
    postgres:latest
  ```
- Create a conda environment and install the required packages
  ```
    conda create -n recipe-app python=3.8
    conda activate recipe-app
    conda install -c conda-forge psycopg2 flask
  ```
- Install the required node packages
  ```
    npm install
  ```
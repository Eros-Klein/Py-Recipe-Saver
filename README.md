# FlavorSaver - Save your recipes!

![Happy People](./assets/happy-people.jpg)

## Goals
- Creating a very basic __full-stack application__.
- Learning how to use __Flask__ to create a RESTful API.
- Leaning how to access a database from a Flask application using __Psycopg2__.
- Learning how to use the __NextJs React framework__ to create a frontend that consumes the API.
- Learning how to style frontend applications via __Tailwind CSS__.
- Learning how to use __Docker__ to containerize the application.

## Requirements
- [Docker](https://docs.docker.com/get-docker/)
- [Conda/Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [Pip](https://pip.pypa.io/en/stable/installation/)
- [Node.js](https://nodejs.org/en/download/)

## Starter Code
The starter code contains a basic Flask API that provides a list of recipes, which gets inserted on every application restart. The recipes are stored in a Postgres database. Furthermore, a NextJs frontend is provided that consumes the API and displays the recipes in a simple list. The frontend is styled using Tailwind CSS.

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
    cd client
    npm install
  ```

## Running the Application
- If database is not already running, start it
  ```
    docker start recipe-db
  ```
- Start the Flask API
  ```
    conda activate recipe-app
    python app.py
  ```
- Start the NextJs frontend
  ```
    cd client
    npm run dev
  ```

## Necessary Improvements

### Server-Side
- In the current state of the application, it is only possible to obtain all recipes at once. Provide routes to obtain recipes by filters. Following filters should be applieable: _(Flask/Psycopg2 | Medium)_
  - Name
  - Ingredients (Pass one (_or more_) ingredients and get all recipes that contain it)
  - Id
- Use the constructor of the already existing class `recipe` to add another recipe to the database. This should be done via a POST request to the API. _(Flask | Medium)_
- Implement routes to query data of all ingredients and create its corresponding class and interface/dto (Hint: The `recipe_interface` and `recipe` class have already been done for you). _(Flask/Psycopg2 | Medium-Hard)_
- Implement a route to delete a recipe by its id.  _(Flask/Psycopg2 | Easy)_
- Solve the TODOs in the provided python files. _(Python | Easy-Medium)_
  
### Client-Side
- Implement light-mode styles for the application. _(Tailwind | Easy)_
- Implement a search bar that allows the user to search for recipes by name and add a dropdown to choose from existing ingredients, so the user can also search by ingredients (Hint: Use `<select>`). _(React/Tailwind | Medium)_
- After implementing the POST-Request on the Server-Side, create a form to add a new recipe. This form should be callable at `/store` and have the following fields: _(React | Hard)_
  - Name
  - Ingredients
  - Instructions

## Optional Improvements
- Add a image to the recipe. This image can either be stored as an byte array in the database or in a local folder (e.g: `~/FlavorSaver/pictures`). _(Flask/Psycopg2/React | Hard)_
- Implement a route to delete a ingredient by its id. You are probably going to encounter an error similar to `cannot delete referenced column`, which indicates that you also have to delete all recipes that contain this ingredient. I know it does not make to much sense to delete an ingredient => Educational Purpose Only _(Flask/Psycopg2 | Hard)_
- Add a route to update a recipe by its id. This route should be called via a PUT request and should update the recipe with the given id. _(Flask/Psycopg2 | Medium)_
- Implement a authentication system that allows users to create an account and store their own recipes. Mind that you must decrypt passwords before saving them (Use a library of your choice to do so). _(Flask/Psycopg2/React | The Hardest)_
- Create a Dockerfile for the Flask API and the NextJs frontend. _(Docker | Easy)_
- Create a Docker-Compose file that starts the Flask API, the NextJs frontend and the Postgres database, so they run simultaneously (Hint: DependsOn will be important). _(Docker | Medium)_

### Good Luck and Have Fun!
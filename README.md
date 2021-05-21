# artistry-codex

- A Python/Django API with a react client to store and list artist throughout the country

- To run local using docker:
  - create a .env file with
    - POSTGRES_USER=root
    - POSTGRES_PASSWORD=root
    - POSTGRES_DB=local
    - POSTGRES_HOST=db
  - Run `docker compose up --build`
    - This will create a bundle for the client, if you want to work on the react app follow the next step
  - Go to `/client`, intall the packages (yarn) and run `yarn start` to start dev server
    - the app will run both on the default port set by react and on url set to the designated template on /url.py file
  - For the following steps enter the container bash `docker-composer exec web bash`
    - run migrations `python manage.py migrate`
    - create a super user `python manage.py createsuperuser`
    - load the fixtures `python manage.py loaddata */fixtures/*`
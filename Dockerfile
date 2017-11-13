FROM tiangolo/uwsgi-nginx-flask:python3.6

# Make sure all dependencies needed for model fitting are included
COPY ./setup.py /app/dependencies/setup.py
COPY ./docker_deployment_example /app/dependencies/docker_deployment_example
RUN pip install /app/dependencies/

# Copy the builded model into this container
COPY ./build /app/model

# Copy the rest endpoints the app should expose
COPY ./app /app
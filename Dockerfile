FROM florishoogenboom/restfull-scikit:python3.6-v0.1-alpha

# Make sure all dependencies needed for model fitting are included
COPY ./setup.py /app/dependencies/setup.py
COPY ./docker_deployment_example /app/dependencies/docker_deployment_example
RUN pip install /app/dependencies/

# Copy the builded model into this container
COPY ./build/model /app/objects/model

# Copy the rest endpoints the app should expose
COPY ./schema.py /app/modules/schema.py
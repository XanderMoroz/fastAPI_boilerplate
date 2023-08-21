# pull the official docker image
FROM python:3.11.1-slim

ARG REQUIREMENTS_FILE

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY ./requirements/ ./requirements
RUN pip install -r ./requirements/${REQUIREMENTS_FILE}

# copy project
COPY . ./
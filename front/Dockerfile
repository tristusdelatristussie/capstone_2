# Base image:
FROM python:3.10-slim

LABEL maintainer="backend_flask"

ENV PYTHONUNBUFFERED=TRUE

RUN pip --no-cache-dir install pipenv

# -- Install Application into container:
RUN set -ex && mkdir /app
WORKDIR /app

# COPY Pipfile.lock Pipfile.lock
COPY ["Pipfile", "Pipfile.lock", "./"]

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system

# Copy files from host to the container
COPY ["*.py", "./"]

EXPOSE 8501

ENTRYPOINT ["pipenv", "run", "streamlit", "run", "front_streamlit.py","--server.port=8501", "--server.address=0.0.0.0"]

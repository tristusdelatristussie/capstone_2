# Base image:
FROM python:3.10-slim

LABEL maintainer="back-flask"

ENV PYTHONUNBUFFERED=TRUE

#RUN apt-get update && apt-get install -y python3-pip

#RUN apt-get update && apt-get install libgl1-mesa-dev -y && apt-get install libglib2.0-dev -y
RUN pip install pipenv

RUN set -ex && mkdir /app && mkdir /kih
WORKDIR /app

# COPY Pipfile.lock Pipfile.lock
COPY ["Pipfile", "Pipfile.lock", "./"]

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system

# Copy files from host to the container
COPY ["*.py", "./"]

COPY kih ./kih

# Port where the App will be Exposed
EXPOSE 9797

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:9797", "backend_flask:app"]


#ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9797", "back-flask:app"] 
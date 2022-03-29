FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update -y
RUN apt-get install poppler-utils -y
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
ENV FIREBASE_CONFIG echo $FIREBASE_CONFIG
ENV FIREBASE_CREDENTIALS_FILEPATH echo $FIREBASE_CREDENTIALS_FILEPATH
RUN echo $FIREBASE_CONFIG >> $FIREBASE_CREDENTIALS_FILEPATH

COPY . /code

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

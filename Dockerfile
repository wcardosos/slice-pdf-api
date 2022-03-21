FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update -y
RUN apt-get install poppler-utils -y
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

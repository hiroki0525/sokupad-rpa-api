FROM python:3.9.4-alpine

WORKDIR /usr/local/src

# TODO: Chromeのインストール

COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY server.py .
#COPY const/ ./const/
#COPY entity/ ./entity/
#COPY infra/ ./infra/
#COPY rpa/ ./rpa/

EXPOSE 8000
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
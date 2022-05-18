FROM docker.io/fnndsc/ubuntu-python3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3","app.py"]

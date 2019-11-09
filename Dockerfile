FROM python:3
RUN pip3 install flask
RUN pip3 install redis
COPY server.py /
EXPOSE 5000
ENTRYPOINT ["python3", "server.py"]
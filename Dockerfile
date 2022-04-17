FROM python:3.9.2-slim-buster
COPY . .
RUN pip3 install -r requirements.txt
CMD ["bash","run.sh"]
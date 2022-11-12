FROM python:slim

RUN useradd blogsite

WORKDIR /home/blogsite

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY blogsite.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP blogsite.py

RUN chown -R blogsite:blogsite ./
USER blogsite

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
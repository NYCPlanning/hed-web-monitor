FROM python:3

ADD scraper.py /

ADD messenger.py /

RUN pip install beautifulsoup4
RUN pip install requests

CMD [ "python", "./scraper.py"]
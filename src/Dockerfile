FROM python:3.6

RUN mkdir /src

WORKDIR /src

ARG FLASK_ENV
ARG FLASK_APP

ENV FLASK_ENV=development
ENV FLASK_APP=/src/app.py

EXPOSE 5000

# TA-Lib
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && \
    tar -xvzf ta-lib-0.4.0-src.tar.gz && \
    cd ta-lib/ && \
    ./configure --prefix=/usr && \
    make && \
    make install

RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "uwsgi", "--ini", "app.ini" ]
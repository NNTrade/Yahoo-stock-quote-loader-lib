FROM mcr.microsoft.com/devcontainers/python:3.11 as build

RUN python3 -m pip install --user virtualenv
RUN python3 -m venv /opt/venv
#RUN source env/bin/activate
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip3 install -U -r requirements.txt

FROM python:3.11 as work

WORKDIR /flask-srv

COPY --from=build /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./src ./src

CMD python3 -m src.app
#CMD flask run -p 80
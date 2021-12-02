FROM python:3.10.0-bullseye
WORKDIR /app
COPY  requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 500

COPY main.py .
COPY owid-covid-data.csv .

CMD [ "python", "main.py" ]

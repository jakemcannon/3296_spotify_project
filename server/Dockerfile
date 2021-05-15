FROM python:3.7-slim-buster


# layer caching for faster builds
COPY requirements.txt .
RUN pip3 install --quiet -r requirements.txt

COPY app.py .

ENTRYPOINT ["python", "app.py"]



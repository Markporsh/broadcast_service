FROM python:3.10-slim
RUN pip install --upgrade pip
WORKDIR /web
COPY requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python3", "manage.py", "runserver", "0:8000"]
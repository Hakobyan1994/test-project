FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Port für Heroku festlegen
ENV PORT=8000

# Port für Heroku freigeben
EXPOSE $PORT

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT"]
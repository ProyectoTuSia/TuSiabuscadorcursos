# For more information, please refer to https://aka.ms/vscode-docker-python

#FROM python:3.8-slim

#EXPOSE 8001

# Keeps Python from generating .pyc files in the container
#ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
#ENV PYTHONUNBUFFERED=1

# Install pip requirements
#COPY requirements.txt .
#RUN python -m pip install -r requirements.txt

#WORKDIR /app
#COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8001", "busquedorcursos.wsgi"]''''
FROM python:3.8
EXPOSE 4325
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ARG URL=0.0.0.0:4325

CMD ["sh", "-c", "python manage.py makemigrations Buscador && python manage.py migrate && python manage.py runserver $URL"]
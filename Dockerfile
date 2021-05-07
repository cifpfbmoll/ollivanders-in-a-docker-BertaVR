FROM mysql:latest

EXPOSE 3500
#Installing stuff
RUN sudo apt-get update
RUN sudo apt-get install python3.6
RUN sudo apt install python3-pip

#Installing requirements
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

#Setting workdirectory
WORKDIR /Ollivanders
COPY . /Ollivanders

#Setting user
RUN sudo adduser --home /Ollivanders -R someuser
RUN chown someuser:someuser /Ollivanders -R
USER someuser

CMD [ "gunicorn", "0.0.0.0:3500" ]
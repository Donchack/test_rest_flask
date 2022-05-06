FROM python:3.8.13
COPY ./Task_rest_flask/ /var/www/Task_rest_flask
RUN pip install -r /var/www/Task_rest_flask/requirements.txt
EXPOSE 5001
CMD ["python", "/var/www/Task_rest_flask/run.py"]

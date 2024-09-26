FROM python:3.12.6-alpine3.20

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org

COPY . .
ENV FLASK_APP=app.py
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

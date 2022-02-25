FROM python:3.8
ENV PYTHONBUFFERED 1
WORKDIR /APIs
COPY  req.txt /APIs/req.txt
RUN pip insatll -r req.txt
COPY . /APIs
CMD python manage.py runserver 0.0.0.0:8000
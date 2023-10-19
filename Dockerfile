# ====================== OK ====================

# FROM python:3.9.5

# # WORKDIR /simple_app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN mkdir logs


# COPY ./requirements.txt /app/requirements.txt

# RUN pip install -r /app/requirements.txt \
#     && rm -rf /root/.cache/pip

# COPY ./app ./app




# ====================== TEST ====================
FROM python:3.9.5

WORKDIR /simple_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir logs


COPY ./requirements.txt .

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./app ./app
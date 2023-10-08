FROM python:3.9.5
# FROM python:3.9.18
# RUN rm /bin/sh && ln -s /bin/bash /bin/sh


RUN apt-get update
WORKDIR /dask
# COPY requirements.txt .

# RUN groupadd -g 1000 dask_group

# RUN useradd -g dask_group --uid 1000 --disabled-password dask_user

# RUN chown -R dask_user:dask_group /dask

# USER dask_user

COPY requirements.txt .
RUN python -m venv env_dask
# RUN source venv/bin/activate
RUN . env_dask/bin/activate
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip freeze > requirements_freeze.txt
EXPOSE 8786 8787


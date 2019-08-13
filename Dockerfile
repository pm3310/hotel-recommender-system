FROM python:3.6-slim-stretch


RUN apt-get -y update && apt-get install -y --no-install-recommends \
         nginx \
         ca-certificates \
         g++ \
    && rm -rf /var/lib/apt/lists/*

# Set some environment variables. PYTHONUNBUFFERED keeps Python from buffering our standard
# output stream, which means that logs can be delivered to the user quickly. PYTHONDONTWRITEBYTECODE
# keeps Python from writing the .pyc files which are unnecessary in this case. We also update
# PATH so that the train and serve programs are found when the container is invoked.

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY requirements.txt /opt/program/requirements.txt
WORKDIR /opt/program/src

# Here we get all python packages.
RUN pip install flask gevent gunicorn future
RUN pip install -r ../requirements.txt && rm -rf /root/.cache

COPY src /opt/program/src/
COPY executor.sh /opt/program/executor.sh

ENTRYPOINT ["executor.sh"]

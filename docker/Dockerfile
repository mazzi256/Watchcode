FROM python:3.8.11 as base

FROM base

ENV PYTHONUNBUFFERED=1
ENV APP_HOST_SRC=.
ENV APP_CONTAINER_SRC=/watchcode

RUN apt-get -y update && \
    apt-get -y install \
    nmap \
    && apt-get -y clean


WORKDIR $APP_CONTAINER_SRC

#copy the requirements folder to image working directory
COPY ${APP_HOST_SRC}/requirements ${APP_CONTAINER_SRC}/requirements

RUN pip install -r requirements/base.txt


#copy the app code to image working directory
COPY $APP_HOST_SRC $APP_CONTAINER_SRC

EXPOSE 8002

RUN mv docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

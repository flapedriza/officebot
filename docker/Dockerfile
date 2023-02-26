FROM python:3.11-slim-bullseye

WORKDIR /code

RUN pip install --upgrade pip
ADD docker/requirements/ /build/
ARG DEV=''
RUN pip install --no-cache-dir -r /build/requirements.txt && \
    if [ "$DEV" = "true" ] ; then pip install --no-cache-dir -r /build/requirements_dev.txt ; else true ; fi

ADD bot/ /code/
ADD docker/scripts/ /scripts/

ENV TZ=Europe/Madrid

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["/bin/sh", "/scripts/bootstrap.sh"]

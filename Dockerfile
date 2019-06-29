FROM alpine
ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8
ENV PYTHON_VERSION 3.5
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN echo http://mirrors.ustc.edu.cn/alpine/v3.8/main > /etc/apk/repositories

RUN echo http://mirrors.ustc.edu.cn/alpine/v3.8/community >> /etc/apk/repositories

RUN apk add g++ jpeg-dev openjpeg-dev libressl-dev
RUN apk add --no-cache python3
RUN apk add --no-cache --virtual=build-dependencies g++ \
    build-base libffi-dev python3-dev \
    libffi openssl ca-certificates \
    zlib-dev freetype-dev lcms2-dev  tiff-dev tk-dev tcl-dev \
    linux-headers pcre-dev   
RUN pip3 install --no-cache-dir --default-timeout=100  -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com  


COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]


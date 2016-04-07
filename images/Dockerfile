FROM centos:7

RUN yum -y install httpd ; \
yum -y install mod_wsgi ; \
yum -y install yum-utils ; \
yum-builddep -y python ; \
yum -y install make ; \
cd ~/. ; \
curl -O https://www.python.org/ftp/python/3.5.0/Python-3.5.0.tgz ; \
tar xf Python-3.5.0.tgz ; \
cd Python-3.5.0 ; \
./configure ; \
make ; \
make install ; \
/usr/local/bin/pyvenv /var/sample-app-env

COPY ./mod_wsgi.conf /etc/httpd/conf.d/

COPY ./requirements.txt /var/sample-app-env/

COPY ./sample-app /var/sample-app-env/

RUN /var/sample-app-env/bin/pip install -r /var/sample-app-env/requirements.txt

RUN /var/sample-app-env/bin/pip install -e /var/sample-app-env/ 

COPY ./pyramid.wsgi /var/sample-app-env/

COPY ./production.ini /var/sample-app-env/

COPY httpd.vars /etc/sysconfig/httpd

# forward the Apache logs to the Docker logging collector
RUN ln -sf /dev/stdout /etc/httpd/logs/access_log
RUN ln -sf /dev/stderr /etc/httpd/logs/error_log


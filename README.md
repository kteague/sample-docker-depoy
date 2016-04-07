# sample-docker-deploy

Build the sample-app into a Docker image.


## Install and run

For development, to install use the buildout.cfg supplied:

    python3.5 bootstrap.py
    ./bin/buildout
    
This will generate the script at:

     ./bin/create_docker_image

Run this script to generate Docker images. The script takes an argument
that matches an existing tag in the sample-app git repo:

    ./bin/create_docker_image 1.0
    ./bin/create_docker_image 1.1

Run a generated Docker image with the following command:

    docker run -d -p 80:80 -t sample-app:1.1 /usr/sbin/apachectl -D FOREGROUND

Note that the -t switch refers to a Docker image in the <name>:<tag> format.

When an image is running, it will need to be stopped before a new image can be run.
To display a list of running Docker containers run 'docker ps':

    $ docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
    903653e5d6de        sample-app:1.1      "/usr/sbin/apachectl "   4 minutes ago       Up 4 minutes        0.0.0.0:80->80/tcp   awesome_carson

A running Docker container is given a name for convenience. Stop the container wtih the kill 
sub-command and the name:

    $ docker kill awesome_carson


##Additional Docker notes

To start a shell with an image run:

    docker run -i -t sample-app:1.1 /bin/bash

To build an image from the Dockerfile:

    cd files
    docker build -f ./Dockerfile .

To view the web application visit http://localhost:80 or if running on Docker Machine
on Mac OS X or Windows you first need to get the IP address of the virtual machine hosting
the docker containers:

    docker-machine ip

Then enter that IP address in your web browser.


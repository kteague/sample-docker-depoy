# sample-docker-deploy

Build the sample-app into a Docker image.


## Install and run

First, clone the git repo:

    git clone https://github.com/kteague/sample-docker-depoy.git sample-docker-deploy

You will need a copy of Python 3 installed (tested with 3.5.0). Then install using Buildout.
The Python bootsrap.py script will install a copy of the build tool Buildout in the local
bin directory:

    cd sample-docker-deploy
    python3.5 bootstrap.py
    ./bin/buildout

This will generate the script at:

     ./bin/create_docker_image

Run this script to generate Docker images. The script takes an argument
that matches an existing tag in the sample-app git repo:

    ./bin/create_docker_image 1.0
    ./bin/create_docker_image 1.1
    ./bin/create_docker_image 1.2

Run a generated Docker image with the following command:

    docker run -d -p 80:80 -t sample-app:1.1 /usr/sbin/apachectl -D FOREGROUND

To view the web application visit http://localhost:80/app or if running on Docker Machine
on Mac OS X or Windows you first need to get the IP address of the virtual machine hosting
the docker containers:

    docker-machine ip

Then enter that IP address in your web browser and append /app to the URL.

Note that the -t switch refers to a Docker image in the <name>:<tag> format.
When an container is running, it will need to be stopped before a new container can be run
(or multiple containers can run simultaneously by adjusting the network pots they bind to).

To display a list of running Docker containers run 'docker ps':

    $ docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                NAMES
    903653e5d6de        sample-app:1.1      "/usr/sbin/apachectl "   4 minutes ago       Up 4 minutes        0.0.0.0:80->80/tcp   awesome_carson

A running Docker container is given a name for convenience. Stop the container wtih the kill 
sub-command and the name:

    $ docker kill awesome_carson

##Using build ids

The `create_docker_image` takes a second optional argument, a build id. This can be used to 
reference different configurations built from the same release of the sample-app project.
For example, different versions of the underlying Pyramid web framework can be deployed.
The file at `images\requirements.txt` contains a list of the specific versions of every
library in the project. Edit this file to change the library versions, then run the command
with a build_id argument:

    ./bin/create_docker_image 1.2 extra_name_or_id

When a build id is used it will commit the changes to the config in the images directory
and create a tag of these changes.

##Additional Docker notes

To start a shell from an image run:

    docker run -i -t sample-app:1.1 /bin/bash



# Author: Michael McDowall
# Use the existing image as a base
FROM us-docker.pkg.dev/colab-images/public/runtime

# Install additional services or software
RUN sudo apt update
RUN sudo apt install software-properties-common
RUN sudo add-apt-repository --yes --update ppa:ansible/ansible
RUN sudo apt install ansible
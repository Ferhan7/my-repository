#! /bin/bash

# update the OS
yum update -y

# install Apache
yum install httpd -y

# copy content to
cd /var/www/html
FOLDER="https://raw.githubusercontent.com/Ferhan7/my-repository/main/101-kittens-carousel-static-website-ec2/static-web/"



wget ${FOLDER}/index.html
wget ${FOLDER}/cat0.jpg
wget ${FOLDER}/cat1.jpg
wget ${FOLDER}/cat2.jpg

systemctl start httpd
systemctl enable httpd


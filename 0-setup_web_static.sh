#!/usr/bin/env bash
# script that:
#   -installs and configures nginx if not present
#   -creates directories, files and symlinks
#   -changes ownership of directory /data/
if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo ufw allow 'Nginx HTTP'
    echo "Hello World!" | sudo tee /var/www/html/index.html
    echo "Page not Found" | sudo tee /var/www/html/custom_404.html
    sudo sed -i  "s/\s*server_name _;/&\n\trewrite ^\/redirect_me.*$ https:\/\/example.com permanent;\n\terror_page 404 \/custom_404.html;\n\tadd_header X-Served-By \"$(hostname)\";/" /etc/nginx/sites-available/default
    sudo service nginx start
fi
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Great School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/X-Served-By/a\
        location /hbnb_static {\
            alias /data/web_static/current/;\
        }' /etc/nginx/sites-available/default
sudo service nginx restart

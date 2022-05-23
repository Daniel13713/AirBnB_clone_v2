#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

# Install nginx if not already installed
pkg=nginx
status="$(dpkg-query -W --showformat='${db:Status-Status}' "$pkg" 2>&1)"
output=$?
if [ ! "$output" = 0 ] || [ ! "$status" = installed ];
then
    sudo apt install "$pkg" -y
fi

# create folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create index.html file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#create symbolic link and recreated if exits
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to user and group ubuntu
sudo chown -R ubuntu:ubuntu /data/

#create config file
echo "server {
        listen 80 default_server;
        index index.html;
        server_name _;
        root /var/www/riodu.tech/html;
        location /redirect_me {
      return 301 https://www.youtube.com/watch?v=hjpF8ukSrvk&ab_channel=PinkFloyd-Topic\$request_uri;
      }
        error_page 404 /du_404.html;
        location = /du_404.html {
                root /var/www/riodu.tech/html;
                internal;
        }
        location /hbnb_static {
                alias /data/web_static/current;
        }
        add_header X-Served-By 3811-web-01;
}
" > /etc/nginx/conf.d/riodu.tech.conf

#creates the index file
echo "Hello World from du.tech (server 1)" > /var/www/riodu.tech/html/index.html;

#error page 404
echo "Ceci n'est pas une page" > /var/www/riodu.tech/html/du_404.html;

#restart nginx
sudo service nginx restart

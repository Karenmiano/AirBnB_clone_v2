sudo sed '/error_page/a\
        location /hbtn_static/ {\
            alias /data/web_static/current/;\
        }' /etc/nginx/sites-available/default

echo "hello"
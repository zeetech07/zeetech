#!/bin/bash

# Exit on any error
set -e

echo "Starting Deployment for Zeetech..."

# 1. Variables
DOMAIN="zeetechacademy.in"
PUB_IP="3.109.124.219"
PROJECT_DIR=$(pwd)
PROJECT_NAME="zeetech"
USER=$(whoami)
VENV_DIR="$PROJECT_DIR/venv"

echo "Project Directory: $PROJECT_DIR"
echo "User: $USER"

# 2. Update System and Install System Dependencies
echo "Installing system dependencies..."
sudo apt update
sudo apt install -y python3-pip python3-venv python3-dev nginx curl

# 3. Create and Activate Virtual Environment
echo "Setting up Virtual Environment..."
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

# 4. Install Python Requirements
echo "Installing Python dependencies..."
$VENV_DIR/bin/pip install --upgrade pip
if [ -f "$PROJECT_DIR/req.txt" ]; then
    $VENV_DIR/bin/pip install -r "$PROJECT_DIR/req.txt"
else
    echo "req.txt not found!"
    exit 1
fi

# Make sure gunicorn is installed
$VENV_DIR/bin/pip install gunicorn

# 5. Django setup (Migrations and Static files)
echo "Running Django migrations and collectstatic..."
$VENV_DIR/bin/python "$PROJECT_DIR/manage.py" makemigrations
$VENV_DIR/bin/python "$PROJECT_DIR/manage.py" migrate
$VENV_DIR/bin/python "$PROJECT_DIR/manage.py" collectstatic --noinput

# 6. Setup Gunicorn Systemd Service
echo "Configuring Gunicorn..."
GUNICORN_SERVICE="/etc/systemd/system/gunicorn.service"
sudo bash -c "cat > $GUNICORN_SERVICE" <<EOF
[Unit]
Description=gunicorn daemon for $PROJECT_NAME
Requires=gunicorn.socket
After=network.target

[Service]
User=$USER
Group=www-data
WorkingDirectory=$PROJECT_DIR
ExecStart=$VENV_DIR/bin/gunicorn \\
          --access-logfile - \\
          --workers 3 \\
          --bind unix:/run/gunicorn.sock \\
          $PROJECT_NAME.wsgi:application

[Install]
WantedBy=multi-user.target
EOF

GUNICORN_SOCKET="/etc/systemd/system/gunicorn.socket"
sudo bash -c "cat > $GUNICORN_SOCKET" <<EOF
[Unit]
Description=gunicorn socket for $PROJECT_NAME

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
EOF

sudo systemctl daemon-reload
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
sudo systemctl restart gunicorn

# 7. Setup Nginx
echo "Configuring Nginx..."
NGINX_CONF="/etc/nginx/sites-available/$PROJECT_NAME"
sudo bash -c "cat > $NGINX_CONF" <<EOF
server {
    listen 80;
    server_name $DOMAIN www.$DOMAIN $PUB_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias $PROJECT_DIR/staticfiles/;
    }

    location /media/ {
        alias $PROJECT_DIR/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
EOF

# Enable Nginx site
sudo ln -sf /etc/nginx/sites-available/$PROJECT_NAME /etc/nginx/sites-enabled/
# Remove default nginx configuration if exists
sudo rm -f /etc/nginx/sites-enabled/default

sudo systemctl restart nginx
sudo systemctl enable nginx

echo "Deployment Successful!"
echo "You can now visit http://$DOMAIN or http://$PUB_IP"

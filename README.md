# captiveportalv1

* First installing apache server and cloning this repository
sudo apt-get install apache2
cd /var/www/html
git clone https://github.com/WellingtonCimentoOficial/captiveportalv1
chown -R www-data /var/www/html

* Second configure apache server to capative portal
sudo a2enmod rewrite
sudo nano /etc/apache2/apache2.conf (OBS: replace “AllowOverride None” with “AllowOverride all”)
sudo nano /var/www/html/.htaccess

RewriteEngine on
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule . index.html [L]
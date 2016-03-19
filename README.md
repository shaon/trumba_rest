# trumba_rest


## Setup for development
```
virtualenv env-trumba
cd env-trumba

git clone https://github.com/shaon/trumba_rest.git
cd trumba_rest

pip install -r requirements.txt

python run.py
```

## Setup with Apache on CentOS
```
yum install httpd mod_wsgi-python27

cd /var/www/html/

git clone https://github.com/shaon/trumba_rest.git
cd trumba_rest

for x in `cat requirements.txt`; do easy_install $x; done

vim /etc/httpd/conf/httpd.conf #(add the following lines at the end)

<VirtualHost *:80>
    ServerName <IP Address/Hostname>
    ServerAdmin webmaster@dummy-host.example.com
    WSGIScriptAlias / /var/www/html/trumba_rest/trumbarest.wsgi
    DocumentRoot /var/www/html/trumba_rest
    ErrorLog /var/log/httpd/trumba_error_log
    CustomLog /var/log/httpd/trumba_access_log common
</VirtualHost>
```

#!/bin/bash

if [ -n "${APP_LOG_FILE}" ]; then 
    mkdir -p $(dirname $APP_LOG_FILE)
    uwsgi --ini uwsgi.ini --logto $APP_LOG_FILE --logfile-chmod 644;
else 
    uwsgi --ini uwsgi.ini;
fi
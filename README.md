# drugml-app-backend

Backend Flask server for the drugML project. Currently hosted on AWS: https://drugmlapi-env.eba-f7kpi2dc.us-east-1.elasticbeanstalk.com/api/swagger

## Quick Start

In the drugML-app-backend folder:

Create virtual environment

Activate virtual environment
 - ```pip install -r requirements.txt```

Then, start the application with the following:

**Linux**
 - Run start bash file ```./start.sh```

**Windows**
 - Set ```FLASK_APP``` environment variable ```set FLASK_APP=application```
 - Set ```FLASK_ENV``` environment variable ```set FLASK_ENV=development```
 - Start flask application ```flask run```
## TLS Encryption

The directories .ebextensions and .platform provide HTTPS security for AWS Elastic Beanstalk Single Instance NGINX webservers. They are platform agnostic and can be cut and pasted.

Sources found here: 

 - https://github.com/HausCloud/AWS-EB-SSL
 - https://gist.github.com/tony-gutierrez/198988c34e020af0192bab543d35a62a

The following lines in **.platform/hooks/postdeploy/00_ssl_setup_certbot.sh** should be edited

```
# IMPORTANT: no whitespaces in CERTBOT_NAME, otherwise following error: "invalid number of arguments in "ssl_certificate" directive in /etc/nginx/nginx.conf:81"
CERTBOT_NAME='<bot_name>' # can be anything
CERTBOT_EMAIL='<email>' # can be anything
# Multiple domain example: CERTBOT_DOMAINS='bort.com,www.bort.com,bort-env.eba-2kg3gsq2.us-east-2.elasticbeanstalk.com'
CERTBOT_DOMAINS='<comma-separated domains> ' # list any domains, subdomains, elastic-beanstalk domains that should have certificates.
```

Note: Non-Elastic Beanstalk domains may not be needed, but not sure.
## Dependancies

```Python 3.6``` - ```Python 3.8```

Python module dependencies be found in ```requirements.txt```
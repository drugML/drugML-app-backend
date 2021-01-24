# drugml-app-backend

Backend Flask server for the drugML project. Currently hosted on AWS: https://drugmlapi-env.eba-f7kpi2dc.us-east-1.elasticbeanstalk.com/api/swagger

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
CERTBOT_DOMAINS='<comma-separated domains> ' # list any domains, subdomains, elastic-beanstalk domains that should have certificates
```

## Dependancies

Can be found in requirements.txt
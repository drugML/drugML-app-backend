# drug-ml-app

For SSL encryption
	openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 (note: on GitBash, winpty openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365)
		Password: drugML!01
		Country Name (2 letter code) [AU]:US
		State or Province Name (full name) [Some-State]:MA
		Locality Name (eg, city) []:Boston
		Organization Name (eg, company) [Internet Widgits Pty Ltd]:drugML
		Organizational Unit Name (eg, section) []:drugML
		Common Name (e.g. server FQDN or YOUR name) []:drugML
		Email Address []:.
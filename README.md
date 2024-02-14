# Secure Lock 

## Overview

> This project is a Django application that provides a simple way to control who is accessing your database information. With tools that track suspiscous login attempts a administrator would be able to secure the site and files to protect against losses.

## Table of Contents

+ [Introduction](#introduction)
+ [Motivation](#motivation)
+ [Features](#features)
+ [Installation](#installation)
+ [Related Work](#related-work)
+ [DATA](#data)
+ [Installation](#installation)

## Introduction

> This project is a Django application that provides a simple way to lock down a website to a specific IP address. It is intended to be used as a security measure for websites that are not intended to be accessed by the general public. Work in progress. The project is currently in the early stages of development. This project will secure databases and provide IP authentication for the user.

## Motivation

> This project was important for me to start because of the gap I saw in the industry while working an internship with a school and its system admins. They had a lot of issues with people trying to hack into their system and they had no way to stop it. I wanted to create a way to stop people from hacking into their systems and to make it easier for them to manage their systems. I saw how crucial IP authentication was for them and how much they needed it. I wanted to create a way to make it easier for them to manage their system and to make it more secure. Many of their attacks were coming from outside the US, this is why I wanted to create a project to secure systems from threats.

## Features

List and briefly describe the key features of your project. This can include:

+ **IP Honeypot tracker:** How users' IP addresses are used for authentication.
+ **Database Protection:** Measures taken to secure databases.
+ **IP Authentication:** Filtered IP specific access to the site.
+ **Uploading files to database** For usage of the site.
+ **Admin Dashboard:** For the admin to manage the site and users.
+ **Web Traffic Monitoring:**  To track suspicious login attempts and database views.

## DATA

IP2Location™ LITE IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE Database
<https://lite.ip2location.com/ip2location-lite>

## API 
IPSTACK

## Related Work

While developing this project, we reviewed existing solutions in the realm of IP authentication and database protection.

## Installation

To install the project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone ...
```

2. Once in the Peyton_Kelly_Artifact, start the virtual environment:

```bash
source venv/bin/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements.txt
```

4. Change Directory to Admin, Create a superuser:

```bash
cd Admin
python manage.py createsuperuser
```

5. Check for migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```


5. Run the project locally:

```bash
python manage.py runserver
```

6. Open your web browser and navigate to the following URL:

```bash
http://127.0.0.1:8000/
```

USING DOCKER:

1. Clone the repository to your local machine:

```bash
git clone ...
```

2. Once in the Peyton_Kelly_Artifact, start the virtual environment:

```bash
source venv/bin/activate
```

3. Where the Dockerfile is located, build the docker image:

```bash
docker-compose build
```

4. Run the docker image:

```bash
docker-compose up
```

5. Open your web browser and navigate to the following URL:

```bash
http://0.0.0.0:8000
or localhost:8000
```

## Conclusion









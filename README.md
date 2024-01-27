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

> This project is a Django application that provides a simple way to lock down a website to a specific IP address. It is intended to be used as a security measure for websites that are not intended to be accessed by the general public. Work in progress. The project is currently in the early stages of development. IP Lock will secure databases and provide IP authentication for the user.

## Motivation

> This project was important for me to start because of the gap I saw in the industry while working an internship with a school and its system admins. They had a lot of issues with people trying to hack into their system and they had no way to stop it. I wanted to create a way to stop people from hacking into their systems and to make it easier for them to manage their systems. I saw how crucial IP authentication was for them and how much they needed it. I wanted to create a way to make it easier for them to manage their system and to make it more secure. Many of their attacks were coming from outside the US, this is why I wanted to create a project to secure systems from threats.

## Features

List and briefly describe the key features of your project. This can include:

+ **IP Honeypot tracker:** How users' IP addresses are used for authentication.
+ **Database Protection:** Measures taken to secure databases.
+ **RSA Encryption logic**
+ **Uploading files to database**

## DATA

IP2Location™ LITE IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE Database
<https://lite.ip2location.com/ip2location-lite>

## Related Work

While developing this project, we reviewed existing solutions in the realm of IP authentication and database protection.

## Installation

MySQL and MYSQL workbench are used in this project. Once those are downloaded properly. Find the local instance and connect to the server. From there create a new database called 'incominguser' with the password that is set in the Settings.py file of the project repository. Once the database is created, open the terminal, Cd to the projects directory. Outside of the virt folder run 'source virt/Scripts/activate'
Once in the repository, be in the Admin folder which has manage.py in the directory. Run 'python manage.py makemigrations' then 'python manage.py migrate' this should create the local instances of the schemas used, if no errors run 'python manage.py runserver'. This will start the local server for the site to be displayed. 


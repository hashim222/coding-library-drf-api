# Coding Library DRF-API - Backend

## Introduction

Coding Library Drf-Api is a back-end API created using Django Rest Framework that handles all backend functionality including user profiles, posts, comments, likes, post bookmarks, followers, authentication, authorization and more.

## Preview
* ### [Coding Library DRF-API ](https://coding-library-drf-api.herokuapp.com/) 

## Contents
* [Database Scheme](#database-scheme)

* [Testings](#testings)

* [Bugs](#bugs)
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)

* [Technologies Used](#technologies-used)

    * [Language](#language)
    * [Framework](#frameworks)
    * [Libraries/Module Installed](#librariesmodule-installed)
    * [Other Technologies](#other-technologies)

* [Deployments](#deployments)

    * [Heroku](#heroku)
    * [Github](#github)

* [Credits](#credits)


## Database Scheme
![Database schema for the website](static/readme-images/database-schema.png)

## Testings

## Bugs

* ### Fixed Bugs
    * In posts serializers, I encountered an issue where I was getting `PostSerializer object has no attribute get_is_owner` error, which turned out to be an indentation for the `get_is_owner` method.  

        ![get_is_owner bug image 1](static/readme-images/get_is_owner-bug-1.png)
        ![get_is_owner bug image 2](static/readme-images/get_is_owner-bug-2.png)  

    * During deployment on Heroku, I encountered another issue. Every time I ran my deployed site, I received a `Bad Request` error, which was caused by the unnecessary `https://` I added to the allowed host. After I removed it, the site worked fine.

        ![get_is_owner bug image 1](static/readme-images/bad-request-deployed-error-1.png)
        ![get_is_owner bug image 2](static/readme-images/bad-request-deployed-error-2.png) 

        
* ### Unfixed Bugs

## Technologies Used

* ### Language
    * [Python](https://www.python.org/) 
* ### Frameworks
    * [Django REST framework](https://www.django-rest-framework.org/)
    * [Django](https://docs.djangoproject.com/en/4.1/)

* ### Libraries/Module Installed
    * asgiref==3.5.2
    * cloudinary==1.30.0
    * dj-database-url==0.5.0
    * dj-rest-auth==2.2.5
    * Django==3.2.16
    * django-allauth==0.50.0
    * django-cloudinary-storage==0.3.0
    * django-cors-headers==3.13.0
    * django-filter==22.1
    * djangorestframework==3.14.0
    * djangorestframework-simplejwt==5.2.2
    * gunicorn==20.1.0
    * oauthlib==3.2.2
    * Pillow==9.3.0
    * psycopg2==2.9.5
    * PyJWT==2.6.0
    * python3-openid==3.2.0
    * pytz==2022.6
    * requests-oauthlib==1.3.1
    * sqlparse==0.4.3

* ### Other Technologies
    * [Git](https://git-scm.com/)
    * [Github](https://github.com/)
    * [Gitpod](https://gitpod.io/workspaces)
    * [Heroku](https://dashboard.heroku.com/apps)
    * [Cloudinary](https://cloudinary.com/)
    * [Lucidchart](https://lucid.app/documents#/dashboard)

## Deployments
* ### Heroku
* ### Github

## Credits
* ### Media
* ### Content





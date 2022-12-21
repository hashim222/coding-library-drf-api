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
* You can check what testing has been performed for the website by clicking [Testings.md](Testings.md)

## Bugs

* ### Fixed Bugs
    * In posts serializers, I encountered an issue where I was getting `PostSerializer object has no attribute get_is_owner` error, which turned out to be an indentation for the `get_is_owner` method.  

        ![get_is_owner bug image 1](static/readme-images/get_is_owner-bug-1.png)
        ![get_is_owner bug image 2](static/readme-images/get_is_owner-bug-2.png)  

    * During deployment on Heroku, I encountered another issue. Every time I ran my deployed site, I received a `Bad Request` error, which was caused by the unnecessary `https://` I added inside the `ALLOWED_HOSTS`. After I removed it, the site worked fine.

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
    * [CI Python Linter](https://pep8ci.herokuapp.com/)

## Deployments
* ### Project Setup
    * Navigate the CI provided template repo on github and click `use this template` button and then press `create a new repository`.
    * Add your project name and then select `create a repository from template`.
    * After successfully creating a repo, you will see the green `gitpod` button, which by clicking creates a workspace for your project.
    * In the workspace using terminal add `pip3 install 'django<4'` to install django and also install Cloudinray storage and Pillow using `pip install django-cloudinary-storage`, `pip install Pillow`.
    * create your project name by using `django-admin startproject my_proj_name .`
    * Make sure to add these on the settings.py file too,  
        ``` json
        INSTALLED_APPS = [
        "cloudinary_storage",
        'django.contrib.staticfiles',
        "cloudinary",
        "my_proj_name"
        ] 
        ```
    * Visit the [cloudinary](https://cloudinary.com/) website and create an account with them.
    * In the gitpod workspace create a new `env.py` file on the top level directory and `import os`.
    * Visit the Cloudinary website and click dashboard then copy the URL for `your API Environment variable`.
    * Set the CLOUDINARY_URL in `env.py`,
        ```
        os.environ['CLOUDINARY_URL'] = 'cloudinary://<API Environment variable from cloudinary>'
        ```
    * In the `settings.py` file `import os` and below add
        ```
        if os.path.exists('env.py'):
            import env
        ```
    * Set `CLOUDINARY_STORAGE` variable equals to the `CLOUDINARY_URL` variable,
        ```
        CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
        }
        ```
    * Define Media Storage URL
        `MEDIA_URL = '/media/'`
    * Define Default File Storage to Cloudinary
        ```
        DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        ```
    * Use these commands to save everything on Github
        ```
        git add .  

        git commit -m "created my project and setup with cloudinary"

        git push
        ```



* ### JWT Tokens
* ### ElephantSQL
* ### Heroku
* ### Github

## Credits
* ### Media
* ### Content





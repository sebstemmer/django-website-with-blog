# Website with Blog Based on Django, Wagtail CMS and Bootstrap

[![Django Version](https://img.shields.io/badge/Django-2.1.5-brightgreen.svg)](https://www.djangoproject.com/)
[![Wagtail Version](https://img.shields.io/badge/Wagtail-2.4-brightgreen.svg)](https://wagtail.io/)
[![Bootstrap Version](https://img.shields.io/badge/Bootstrap-4.2.1-brightgreen.svg)](https://getbootstrap.com/)
[![gulp.js Version](https://img.shields.io/badge/gulp.js-4.0.0-brightgreen.svg)](https://gulpjs.com/) 
[![jQuery Version](https://img.shields.io/badge/jQuery-3.3.1-brightgreen.svg)](https://jquery.com/) 

Live-Demo: [sebastian-stemmer.com](https://sebastian-stemmer.com/)

## Features

- Based on Django framework
- Fully functional blog using Wagtail CMS
- Fully responsive using Bootstrap
- gulp.js ready (minifies JS and CSS)
- Contact form (considering GDPR)
- Google Analytics (considering GDPR)
- Easy color theme changes

### Blog with Wagtail CMS

The blog is a separated app and includes the following functionalities using [Wagtail CMS](https://wagtail.io/):

- blog posts
- categories
- tags
- ability to perform a search  
- list posts by categories and tags
- admin interface with raw html editor

### Fully Responsive Design with Bootstrap

The design is fully responsive. While the main page is implemented by a modified version of

[Agency Bootstrap Theme](https://startbootstrap.com/themes/agency/),

the blog is constructed by a modified version of the

[Blog Home Bootstrap Theme](https://startbootstrap.com/templates/blog-home/)

and the

[Blog Post Bootstrap Theme](https://startbootstrap.com/templates/blog-post/).

The responsive CV is implemented by adapting

[https://codyhouse.co/gem/vertical-timeline/](https://codyhouse.co/gem/vertical-timeline/).

### Easy Development with gulp.js

There is a ``gulpfile.js``. Its purpose is to minify all ``.js`` and ``.css`` files. While the command

```bash
gulp
```

executes the default task, which does the minification,

```bash
gulp watchAll
```

will do the minification when some of the considered files change.

### Contact Form

The contact form was designed with considering the GDPR. Required fields are indicated by a star. There is a checkbox with privacy information and a general statement in ``mywebsite/mainpage/templates/mainpage/privacy_en.py`` (English) and ``mywebsite/mainpage/templates/mainpage/privacy_de.py`` (German).

### Google Analytics

For respecting the GDPR, IP anonymization in ``gtag.js`` is activated. Furthermore, there is an opt-out cookie functionality and a general statement in ``mywebsite/mainpage/templates/mainpage/privacy_en.py`` (English) and ``mywebsite/mainpage/templates/mainpage/privacy_de.py`` (German).

### Easy color theme changes

To change the color theme open ``mywebsite/mainpage/static/mainpage/css/variables.css`` and change the css variables accordingly.

## Installation and Configuration

### Development

First, clone this git repository

```bash
git clone git@github.com:sebastianstemmer/django-website-with-blog.git
```

Then, create and activate a virtual environment as described in [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html). Install the development requirements

```bash
pip install -r requirements_dev.txt
```

<br>

Next, we configure ``mywebsite/mywebsite/settings.py``. In development, set

```python
IN_DEVELOPMENT = True
```

For private, environment specific settings like paths or the secret key a file called ``env_settings.py`` is used. There is an example file ``env_settings_example_dev.py``. Adapt this file to your environment. Especially, set the constant ``DEV_DIR`` to the directory you want Django to save your media files and development database in. Also, add your Django secret key to ``SECRET_KEY``. Do not forget to rename the file to ``env_settings.py``. Add the path where your modified environment settings file ist stored to

```python
ENV_SETTINGS_PATH_DEV = 'path/to/folder/which/contains/env_settings/'
```

in ``mywebsite/mywebsite/settings.py``.

<br>

Now, use the command

```bash
npm install
```

on the root of this repository to install gulp.js. With the command

```bash
gulp
```

gulp.js will minify all ``.js`` and ``.css`` files. Furthermore, the command

```bash
gulp watchAll
```

will tell gulp.js to watch all ``.css`` and ``.js`` files and to minify them when they are updated.

<br>

Run the development server with

```bash
python ./mywebsite/manage.py runserver
```

Make sure your virtual environment is running, when executing this command.

### Production

For the production case, the procedure of installation and configuration is similar to the development case. First, clone the repository, create and activate a virtual environment and then

```bash
pip install -r requirements_prod.txt
```

<br>

In ``mywebsite/mywebsite/settings.py`` set

```python
IN_DEVELOPMENT = False
```

Again, we need an environment settings file. There is an example file ``env_settings_example_prod.py``. Adapt it to your environment including the credentials for your database and the constant ``PROD_DIR``. This constant defines the path for the static, media and log files. Rename the file to ``env_settings.py`` and set its path to

```python
ENV_SETTINGS_PATH_PROD = 'path/to/folder/which/contains/env_settings/'
```

in ``mywebsite/mywebsite/settings.py``.

<br>

That's it! All other settings, like the setup of your production database, the choice of webserver, etc. are platform dependent and not further discussed here.

## Changelog

### 1.0.0

- Initial version

### 1.0.1

- some changes in README.md
- fixed package in requirements_prod.txt

## License

Copyright © 2019 Sebastian Stemmer

Take a look at the license file [LICENSE](https://github.com/sebastianstemmer/django-website-with-blog/blob/master/LICENSE).
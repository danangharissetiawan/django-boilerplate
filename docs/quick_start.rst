Quick Start Guide
=================

Download Django Boilerplate
----------------------------------------------

First, you need to download the django-boilerplate from `GitHub`_. 

.. _Github: https://github.com/danangharissetiawan/django-boilerplate

Secret Django Key
-----------------

This boilerplate has the **DJANGO_KEY** setting variable hidden.
You can generate your DJANGO_KEY `django key generator`_.

.. _django key generator: https://miniwebtool.com/django-secret-key-generator/


This project is named *django-boilerplate*, so if you are using this
Boilerplate to create your own project, you'll have to change
the name in a few places:

- *django-boilerplate* **folders** (your top project container)
- *django-boilerplate/apps* **folder** (name of your core project)
- *apps/config* **folder** (folder for project configuration)
- *apps/main* **folder** (name of your main project)
- virtual environment name: **djangoboilerplate** and **djangoboilerplate-test** (name whatever you want)
- In the virtual environment of the **postactivate** file (see section below), you must add:

.. code-block:: bash

  export DJANGO_SECRET_KEY="<DJANGO KEY>"
  export DJANGO_SETTINGS_MODULE="config.settings.development"
  export DJANGO_DEVELOPMENT_MODE="DEVELOPMENT"

do the same in the test environment

.. code-block:: bash

  export DJANGO_SECRET_KEY="<DJANGO KEY>"
  export DJANGO_SETTINGS_MODULE="config.settings.testing"


Virtual environments and Settings Files
---------------------------------------

First, you must know your Python 3

.. code-block:: bash

  $ which python3

which is something similar to /usr/local/bin/python3.

Next, create a Development virtual environment with Python 3 installed

.. code-block:: bash

  $ mkvirtualenv --python=/usr/local/bin/python3 djangoboilerplate

where you might need to change it with your python path.

Go to the virtual environment folder with

.. code-block:: bash

  $ cd $VIRTUAL_ENV/bin

and edit the postactivate file.

.. code-block:: bash

  $ vim postactivate

You must add the lines: 

.. code-block:: bash

  export DJANGO_SECRET_KEY="<DJANGO KEY>"
  export DJANGO_SETTINGS_MODULE="config.settings.development"
  export DJANGO_DEVELOPMENT_MODE="DEVELOPMENT"

with your project name and your own secret key.

Next, edit the **predeactivate** file and add the line

.. code-block:: bash

  unset DJANGO_SECRET_KEY

Repeat the last steps for your testing environment

.. code-block:: bash

  $ mkvirtualenv --python=/usr/local/bin/python3 djangoboilerplate-test
  $ cd $VIRTUAL_ENV/bin
  $ vim postactivate

where you have to add the lines

.. code-block:: bash

  export DJANGO_SECRET_KEY="<DJANGO KEY>"
  export DJANGO_SETTINGS_MODULE="config.settings.testing"

Next, install the packages in each environment

.. code-block:: bash

  $ workon djangoboilerplate
  $ pip install -r requirements/development.txt
  $ workon djangoboilerplate-test
  $ pip install -r requirements/testing.txt


Internationalization and Localization
-------------------------------------

Settings
********

The default language for this Project is **English**, and we use internatinalization to translate the text into Indonesia.

If you want to change the translation language, or include a new one, you just need to modify the **LANGUAGES** variable in the file *settings/base.py*. The language codes that define each language can be found `codes_link`_.

.. _codes_link: http://msdn.microsoft.com/en-us/library/ms533052(v=vs.85).aspx

For example, if you want to use German you should include

.. code-block:: python

    LANGUAGES = (
        ...
        'de', _("German"),
        ...
    )

You can also specify a dialect, like Luxembourg's German with

.. code-block:: python

    LANGUAGES = (
        ...
        'de-lu', _("Luxemburg's German"),
        ...
    )

Note: the name inside the translation function _("") is the language name in the default language (English).

More information on the `internationalization`_. 

.. _internationalization: https://docs.djangoproject.com/en/3.2/topics/i18n/

Translation
***********

Go to the terminal, inside the *django-boilerplate/apps* folder and create the files to translate with

.. code-block:: bash

  $ python manage.py makemessages -l id

change the language "id" for your selected language.

Next, go to the locale folder of your language

.. code-block:: bash

  $ cd local/id/LC_MESSAGES

You have to edit the file *django.po* and translate the strings. You can find more information about how to translate the strings `translation_strings_post`_.

.. _translation_strings_post: https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#translate-template-tag

Once the translation is done, compile your messages with

.. code-block:: bash

  $ python manage.py compilemessages -l id

Tests
*****

We need to update the languages in our Tests to make sure the translation works correclty. Open the file *functional_tests/test_all_users.py*:

- In **test_internationalization**, update your languages with the translation of title text, here "Hello World!".
- In **test_localization**, update your languages.

Useful commands
---------------

A list of all the commands used to run this template

.. code-block:: bash

    $ workon djangoboilerplate
    $ workon djangoboilerplate-test

    $ python manage.py makemessages -l ca
    $ python manage.py compilemessages -l ca
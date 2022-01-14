
# About the Bookr Website

This website is a showcase website, made for my portfolio only.
This isn't a fully working website, some features does not work due to a reasonable cause(e.g. Reset Passwords, Sending emails for confirmation codes | stuff that require some third party services).

### In the "About" page I will describe the functionality of the site alongside with the backend code for it.

#### The entire source code for the website you can find on [github.com](https://github.com/3h04m1), also you can visit [my portfolio](https://3h04m1.github.io), see for more html templates, python scripts and my other work.
***

## Framework

### Backend
The framework/library used for this code is Django, a backend python library.
The website is hosted on my personal home-server which I will describe in my last chapter of the about page.
For the database I used in development SQLite3 and in production moved on PostgreSQL.
Libraries used alongside Django were :
```
asgiref==3.4.1
backports.entry-points-selectable==1.1.1
cffi==1.15.0
cryptography==36.0.1
distlib==0.3.4
dj-database-url==0.5.0
Django==3.2.9
django-configurations==2.3.1
django-crispy-forms==1.13.0
django-debug-toolbar==3.2.4
djangorestframework==3.12.4
filelock==3.4.2
greenlet==1.1.2
gunicorn==20.1.0
msgpack==1.0.3
neovim==0.3.1
Pillow==8.4.0
platformdirs==2.4.1
plotly==5.4.0
psycopg2==2.9.3
pycparser==2.21
Pygments==2.11.1
pynvim==0.4.3
pyOpenSSL==21.0.0
pytz==2021.3
six==1.16.0
sqlparse==0.4.2
tenacity==8.0.1
virtualenv==20.9.0
zipp==3.6.0
```
### Frontend

#### For the frontend part I used mainly :
-  HTML
-  DjangoHTML
-  CSS
#### Also for some other tasks used:
- JS
- ReactJS
- Babel
- zero-md
- prisma.js

## Project

### The project structure:
```shell
.
├── bookr
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   ├── utils.cpython-38.pyc
│   │   ├── views.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── wsgi.py
├── bookr_admin
│   ├── admin.py
│   ├── app_admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── app_admin.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   └── models.cpython-38.pyc
│   ├── tests.py
│   └── views.py
├── config
│   └── gunicorn
│       ├── dev.py
│       └── __pycache__
│           └── dev.cpython-38.pyc
├── db.sqlite3
├── manage.py
├── media
│   ├── book_covers
│   │   ├── 1984.jpg
│   │   ├── 71OFqSRFDgL.jpg
│   │   ├── Advanced_Deep_Learning_with_Keras.jpg
│   │   ├── Animal_Farm_A_Fairy_Story.jpg
│   │   ├── Architects_of_Intelligence.jpg
│   │   ├── Brave_New_World.jpg
│   │   ├── Deep_Reinforcement_Learning_Hands-On.jpg
│   │   ├── For_Whom_The_Bell_Tolls.jpg
│   │   ├── Hands-On_Reinforcement_Learning_with_Python.jpg
│   │   ├── machine-learning-for-algorithmic-trading.png
│   │   ├── Natural_Language_Processing_with_TensorFlow.jpg
│   │   ├── Paul_Clifford.jpg
│   │   ├── Pride_and_Prejudice.jpg
│   │   ├── The_Catcher_in_the_Rye.jpg
│   │   ├── The_Grapes_of_Wrath.jpg
│   │   ├── The_Great_Gatsby.jpg
│   │   ├── The_Talisman.jpg
│   │   └── To_Kill_A_Mocking_Bird.jpg
│   └── book_samples
│       └── machine-learning-for-trading.pdf
├── production.conf
├── react_test_app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── apps.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── static
│   │   └── react
│   │       └── index.js
│   ├── templates
│   │   └── react
│   │       ├── db.sqlite3
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── reviews
│   ├── admin.py
│   ├── api_views.py
│   ├── apps_admin.py
│   ├── forms.py
│   ├── __init__.py
│   ├── management
│   │   └── commands
│   │       ├── __init__.py
│   │       ├── loadcsv.py
│   │       └── WebDevWithDjangoData.csv
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_book_contributor.py
│   │   ├── 0003_auto_20211111_0058.py
│   │   ├── 0004_alter_book_publisher.py
│   │   ├── 0005_auto_20211130_1239.py
│   │   ├── 0006_auto_20220105_1237.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       ├── 0002_book_contributor.cpython-38.pyc
│   │       ├── 0003_auto_20211111_0058.cpython-38.pyc
│   │       ├── 0004_alter_book_publisher.cpython-38.pyc
│   │       ├── 0005_auto_20211130_1239.cpython-38.pyc
│   │       ├── 0006_auto_20220105_1237.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-38.pyc
│   │   ├── api_views.cpython-38.pyc
│   │   ├── forms.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── serializers.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   ├── utils.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── serializers.py
│   ├── static
│   │   └── reviews
│   │       ├── about.md
│   │       ├── book.details.css
│   │       └── logo.png
│   ├── templates
│   │   └── reviews
│   │       ├── about.html
│   │       ├── book_details.html
│   │       ├── book_list.html
│   │       ├── books_list.html
│   │       ├── example-form.html
│   │       ├── index.html
│   │       ├── instance-form.html
│   │       └── search-results.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── profile_tags.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-38.pyc
│   │       └── profile_tags.cpython-38.pyc
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── urls.py
│   ├── utils.py
│   └── views.py
├── service-conf
├── static
│   ├── icon.png
│   ├── logo.png
│   ├── main.css
│   ├── prism.css
│   ├── prism.js
│   └── recent-reviews.js
└── templates
    ├── admin
    │   ├── admin_profile.html
    │   └── logout.html
    ├── base.html
    ├── profile.html
    └── registration
        ├── logged_out.html
        ├── login.html
        ├── password_change_done.html
        ├── password_change_form.html
        ├── password_reset_complete.html
        ├── password_reset_confirm.html
        ├── password_reset_done.html
        ├── password_reset_email.html
        └── password_reset_form.html
```

### The Django's settings.py :

```python
class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent
    PROJ_ROOT = '/home/bookr/Bookr-django-project/'
    SECRET_KEY = 'django-insecure--)2beo8kr9maxs#gj#gx=2m446+)4$i0!1lk+zd*@-q@qwxdst'
    DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = ['192.168.0.7', '127.0.0.1', '192.168.0.5', 'www.baiters.ml']
    # Application definition

    INSTALLED_APPS = [
        'bookr_admin.app_admin.BookrAdminConfig',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'reviews',
        'bookr_admin',
        'rest_framework',
        'rest_framework.authtoken',
        'crispy_forms',
        'react_test_app',

    ]

    MIDDLEWARE = [
  #      'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'bookr.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'bookr.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = values.DatabaseURLValue(f'sqlite:///{BASE_DIR}/db.sqlite3', environ_prefix='DJANGO')

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'
    STATIC_ROOT = '/home/bookr/Bookr-django-project/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = '/home/bookr/Bookr-django-project/media/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
   # INTERNAL_IPS = ['127.0.0.1', '192.168.0.7', '0.0.0.0']
    CRISPY_TEMPLATE_PACK = 'bootstrap4'


class Prod(Dev):
    DEBUG = True
    SECRET_KEY = environ['DJANGO_SECRET_KEY']
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',

                'NAME': 'db.sqlite3',

                #'USERNAME': 'bookr',

                #'PASSWORD': 'bargain23',

                #'HOST':  'localhost',

                #'PORT': '',
                }
            }
```

## Database & models.py
So for the develpment part of the website I used the **sqlite3** database, it's the one that django is shiping from, but in production I changed it to **PostreSQL**.
Because this websites is about books I populated the database with books.
### The SQL table for the project is:
```sql
CREATE TABLE IF NOT EXISTS "django_migrations" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app" varchar(255) NOT NULL,
    "name" varchar(255) NOT NULL,
    "applied" datetime NOT NULL
);
CREATE TABLE sqlite_sequence(name, seq);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE TABLE IF NOT EXISTS "django_admin_log" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "action_time" datetime NOT NULL,
    "object_id" text NULL,
    "object_repr" varchar(200) NOT NULL,
    "change_message" text NOT NULL,
    "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0)
);
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE TABLE IF NOT EXISTS "django_content_type" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL
);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE TABLE IF NOT EXISTS "auth_permission" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "codename" varchar(100) NOT NULL,
    "name" varchar(255) NOT NULL
);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE TABLE IF NOT EXISTS "auth_group" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_user" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "password" varchar(128) NOT NULL,
    "last_login" datetime NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(150) NOT NULL UNIQUE,
    "last_name" varchar(150) NOT NULL,
    "email" varchar(254) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" datetime NOT NULL,
    "first_name" varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" datetime NOT NULL
);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE TABLE IF NOT EXISTS "book_management_app_book" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(255) NOT NULL,
    "author" varchar(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS "authtoken_token" (
    "key" varchar(40) NOT NULL PRIMARY KEY,
    "created" datetime NOT NULL,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "bookr_test_publisher" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(50) NOT NULL,
    "website" varchar(200) NOT NULL,
    "email" varchar(254) NOT NULL
);
CREATE TABLE IF NOT EXISTS "reviews_book" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "title" varchar(70) NOT NULL,
    "publication_date" date NOT NULL,
    "isbn" varchar(20) NOT NULL,
    "publisher_id" bigint NOT NULL REFERENCES "reviews_publisher" ("id") DEFERRABLE INITIALLY DEFERRED,
    "cover" varchar(100) NULL,
    "sample" varchar(100) NULL
);
CREATE INDEX "reviews_book_publisher_id_a3cbe35c" ON "reviews_book" ("publisher_id");
CREATE TABLE IF NOT EXISTS "reviews_bookcontributor" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "role" varchar(20) NOT NULL,
    "book_id" integer NOT NULL REFERENCES "reviews_book" ("id") DEFERRABLE INITIALLY DEFERRED,
    "contributor_id" bigint NOT NULL REFERENCES "reviews_contributor" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX "reviews_bookcontributor_book_id_e7bfc5b2" ON "reviews_bookcontributor" ("book_id");
CREATE INDEX "reviews_bookcontributor_contributor_id_e3ee3341" ON "reviews_bookcontributor" ("contributor_id");
CREATE TABLE IF NOT EXISTS "reviews_contributor" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "first_names" varchar(50) NOT NULL,
    "last_names" varchar(50) NOT NULL,
    "email" varchar(254) NOT NULL
);
CREATE TABLE IF NOT EXISTS "reviews_publisher" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(50) NOT NULL,
    "website" varchar(200) NOT NULL,
    "email" varchar(254) NOT NULL
);
CREATE TABLE IF NOT EXISTS "reviews_review" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "content" text NOT NULL,
    "rating" integer NOT NULL,
    "date_created" datetime NOT NULL,
    "date_edited" datetime NULL,
    "book_id" integer NOT NULL REFERENCES "reviews_book" ("id") DEFERRABLE INITIALLY DEFERRED,
    "creator_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX "reviews_review_book_id_9a657eea" ON "reviews_review" ("book_id");
CREATE INDEX "reviews_review_creator_id_46914a15" ON "reviews_review" ("creator_id");
```

## API
For the api part I used Django REST Api. The api url is /api and current it has 2 Api calls:
- <em>/api/books</em> which gives all the information about the books example 

	```json
	[
	{
	    "title": "Advanced Deep Learning with Keras",
	    "publication_date": "2018-10-31",
	    "isbn": "9781788629416",
	    "cover": "http://www.baiters.ml/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg",
	    "publisher": {
	        "name": "Packt Publishing",
	        "website": "https://www.packtpub.com/",
	        "email": "info@packtpub.com"
	    },
	    "rating": 4,
	    "reviews": [
	        {
	            "pk": 1,
	            "content": "A must read for all",
	            "date_created": "2021-11-12T22:46:06.452473Z",
	            "date_edited": "2020-01-04T16:31:40.376237Z",
	            "rating": 5,
	            "creator": {
	                "username": "peterjones@test.com",
	                "email": "peterjones@test.com"
	            },
	            "book": {
	                "pk": 1,
	                "title": "Advanced Deep Learning with Keras",
	                "publisher": 1,
	                "contributors": [
	                    1
	                ],
	                "cover": "/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
	            }
	        },
	        {
	            "pk": 2,
	            "content": "An ok read",
	            "date_created": "2021-11-12T22:46:06.475012Z",
	            "date_edited": "2020-01-04T16:31:40.376237Z",
	            "rating": 3,
	            "creator": {
	                "username": "marksandler@test.com",
	                "email": "marksandler@test.com"
	            },
	            "book": {
	                "pk": 1,
	                "title": "Advanced Deep Learning with Keras",
	                "publisher": 1,
	                "contributors": [
	                    1
	                ],
	                "cover": "/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
	            }
	        },
	        {
	            "pk": 3,
	            "content": "this book is great",
	            "date_created": "2021-12-01T14:30:06.198023Z",
	            "date_edited": null,
	            "rating": 5,
	            "creator": {
	                "username": "alice",
	                "email": "alice@example.com"
	            },
	            "book": {
	                "pk": 1,
	                "title": "Advanced Deep Learning with Keras",
	                "publisher": 1,
	                "contributors": [
	                    1
	                ],
	                "cover": "/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
	            }
	        },
	        {
	            "pk": 4,
	            "content": "this book is great",
	            "date_created": "2021-12-01T14:30:57.317000Z",
	            "date_edited": null,
	            "rating": 5,
	            "creator": {
	                "username": "alice",
	                "email": "alice@example.com"
	            },
	            "book": {
	                "pk": 1,
	                "title": "Advanced Deep Learning with Keras",
	                "publisher": 1,
	                "contributors": [
	                    1
	                ],
	                "cover": "/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
	            }
	        }
	    ]
	},
	{
	    "title": "Hands-On Machine Learning for Algorithmic Trading",
	    "publication_date": "2018-12-31",
	    "isbn": "9781789346411",
	    "cover": "http://www.baiters.ml/media/book_covers/machine-learning-for-algorithmic-trading.png",
	    "publisher": {
	        "name": "Packt Publishing",
	        "website": "https://www.packtpub.com/",
	        "email": "info@packtpub.com"
	    },
	    "rating": 5,
	    "reviews": [
	        {
	            "pk": 5,
	            "content": "Test review for books read section in profile page",
	            "date_created": "2021-12-08T15:53:08.623742Z",
	            "date_edited": null,
	            "rating": 5,
	            "creator": {
	                "username": "max",
	                "email": "maxv0itc0v@gmail.com"
	            },
	            "book": {
	                "pk": 2,
	                "title": "Hands-On Machine Learning for Algorithmic Trading",
	                "publisher": 1,
	                "contributors": [
	                    4
	                ],
	                "cover": "/media/book_covers/machine-learning-for-algorithmic-trading.png"
	            }
	        }
	    ]
	},
	{
	    "title": "Architects of Intelligence",
	    "publication_date": "2018-11-23",
	    "isbn": "9781789954531",
	    "cover": "http://www.baiters.ml/media/book_covers/Architects_of_Intelligence.jpg",
	    "publisher": {
	        "name": "Packt Publishing",
	        "website": "https://www.packtpub.com/",
	        "email": "info@packtpub.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Deep Reinforcement Learning Hands-On",
	    "publication_date": "2018-06-20",
	    "isbn": "9781788834247",
	    "cover": "http://www.baiters.ml/media/book_covers/Deep_Reinforcement_Learning_Hands-On.jpg",
	    "publisher": {
	        "name": "Packt Publishing",
	        "website": "https://www.packtpub.com/",
	        "email": "info@packtpub.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Natural Language Processing with TensorFlow",
	    "publication_date": "2018-05-30",
	    "isbn": "9781788478311",
	    "cover": "http://www.baiters.ml/media/book_covers/Natural_Language_Processing_with_TensorFlow.jpg",
	    "publisher": {
	        "name": "Packt Publishing",
	        "website": "https://www.packtpub.com/",
	        "email": "info@packtpub.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Hands-On Reinforcement Learning with Python",
	    "publication_date": "2018-06-27",
	    "isbn": "9781788836524",
	    "cover": "http://www.baiters.ml/media/book_covers/Hands-On_Reinforcement_Learning_with_Python.jpg",
	    "publisher": {
	        "name": "Packt Publishing",
	        "website": "https://www.packtpub.com/",
	        "email": "info@packtpub.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Brave New World",
	    "publication_date": "2006-10-18",
	    "isbn": "9780060850524",
	    "cover": "http://www.baiters.ml/media/book_covers/Brave_New_World.jpg",
	    "publisher": {
	        "name": "Harper Collins",
	        "website": "https://www.harpercollins.com",
	        "email": "feedback@harpercollins.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "The Grapes of Wrath",
	    "publication_date": "2006-03-28",
	    "isbn": "9780143039433",
	    "cover": "http://www.baiters.ml/media/book_covers/The_Grapes_of_Wrath.jpg",
	    "publisher": {
	        "name": "Penguin Classics",
	        "website": "http://www.penguinclassics.com",
	        "email": "contact@penguinclassics.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "For Whom The Bell Tolls",
	    "publication_date": "2019-07-16",
	    "isbn": "9781476787770",
	    "cover": "http://www.baiters.ml/media/book_covers/For_Whom_The_Bell_Tolls.jpg",
	    "publisher": {
	        "name": "Scribner",
	        "website": "https://www.simonandschusterpublishing.com/scribner/",
	        "email": "ScribnerPublicity@SimonandSchuster.com."
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "To Kill A Mocking Bird",
	    "publication_date": "2002-01-01",
	    "isbn": "9780060935467",
	    "cover": "http://www.baiters.ml/media/book_covers/To_Kill_A_Mocking_Bird.jpg",
	    "publisher": {
	        "name": "Harper Collins",
	        "website": "https://www.harpercollins.com",
	        "email": "feedback@harpercollins.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "The Great Gatsby",
	    "publication_date": "2004-09-30",
	    "isbn": "9780743273565",
	    "cover": "http://www.baiters.ml/media/book_covers/The_Great_Gatsby.jpg",
	    "publisher": {
	        "name": "Scribner",
	        "website": "https://www.simonandschusterpublishing.com/scribner/",
	        "email": "ScribnerPublicity@SimonandSchuster.com."
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "The Catcher in the Rye",
	    "publication_date": "2001-01-30",
	    "isbn": "9780316769174",
	    "cover": "http://www.baiters.ml/media/book_covers/The_Catcher_in_the_Rye.jpg",
	    "publisher": {
	        "name": "Bay Back Books",
	        "website": "https://www.hachettebookgroup.com/imprint/little-brown-and-company/back-bay-books/",
	        "email": "customer.service@hbgusa.com."
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Farenheit 451",
	    "publication_date": "2012-01-10",
	    "isbn": "9781451673319",
	    "cover": "http://www.baiters.ml/media/book_covers/71OFqSRFDgL.jpg",
	    "publisher": {
	        "name": "Simon and Schuster",
	        "website": "https://www.simonandschuster.com",
	        "email": "contact@simonandschuster.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Pride and Prejudice",
	    "publication_date": "2002-12-31",
	    "isbn": "9780141439518",
	    "cover": "http://www.baiters.ml/media/book_covers/Pride_and_Prejudice.jpg",
	    "publisher": {
	        "name": "Penguin Classics",
	        "website": "http://www.penguinclassics.com",
	        "email": "contact@penguinclassics.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "1984",
	    "publication_date": "2017-04-04",
	    "isbn": "9781328869333",
	    "cover": "http://www.baiters.ml/media/book_covers/1984.jpg",
	    "publisher": {
	        "name": "Houghton Mifflin Harcourt",
	        "website": "https://www.hmhco.com",
	        "email": "techsupport@hmhco.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Animal Farm: A Fairy Story",
	    "publication_date": "1996-04-18",
	    "isbn": "9780151002177",
	    "cover": "http://www.baiters.ml/media/book_covers/Animal_Farm_A_Fairy_Story.jpg",
	    "publisher": {
	        "name": "Houghton Mifflin Harcourt",
	        "website": "https://www.hmhco.com",
	        "email": "techsupport@hmhco.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "Paul Clifford",
	    "publication_date": "2018-05-12",
	    "isbn": "9781719053167",
	    "cover": "http://www.baiters.ml/media/book_covers/Paul_Clifford.jpg",
	    "publisher": {
	        "name": "CreateSpace Independent Publishing Platform",
	        "website": "https://www.createspace.com",
	        "email": "info@createspace.com"
	    },
	    "rating": null,
	    "reviews": null
	},
	{
	    "title": "The Talisman",
	    "publication_date": "2012-09-25",
	    "isbn": "9781451697216",
	    "cover": "http://www.baiters.ml/media/book_covers/The_Talisman.jpg",
	    "publisher": {
	        "name": "Pocket Books",
	        "website": "https://pocketbookssampleurl.com",
	        "email": "pocketbook@example.com"
	    },
	    "rating": null,
	    "reviews": null
	}
	]
	```
- <em>/api/reviews/</em> wich gives all the information about the reviews in the database

```json
[
{
    "pk": 1,
    "content": "A must read for all",
    "date_created": "2021-11-12T22:46:06.452473Z",
    "date_edited": "2020-01-04T16:31:40.376237Z",
    "rating": 5,
    "creator": {
        "username": "peterjones@test.com",
        "email": "peterjones@test.com"
    },
    "book": {
        "pk": 1,
        "title": "Advanced Deep Learning with Keras",
        "publisher": 1,
        "contributors": [
            1
        ],
        "cover": "http://www.baiters.ml/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
    }
},
{
    "pk": 2,
    "content": "An ok read",
    "date_created": "2021-11-12T22:46:06.475012Z",
    "date_edited": "2020-01-04T16:31:40.376237Z",
    "rating": 3,
    "creator": {
        "username": "marksandler@test.com",
        "email": "marksandler@test.com"
    },
    "book": {
        "pk": 1,
        "title": "Advanced Deep Learning with Keras",
        "publisher": 1,
        "contributors": [
            1
        ],
        "cover": "http://www.baiters.ml/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
    }
},
{
    "pk": 3,
    "content": "this book is great",
    "date_created": "2021-12-01T14:30:06.198023Z",
    "date_edited": null,
    "rating": 5,
    "creator": {
        "username": "alice",
        "email": "alice@example.com"
    },
    "book": {
        "pk": 1,
        "title": "Advanced Deep Learning with Keras",
        "publisher": 1,
        "contributors": [
            1
        ],
        "cover": "http://www.baiters.ml/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
    }
},
{
    "pk": 4,
    "content": "this book is great",
    "date_created": "2021-12-01T14:30:57.317000Z",
    "date_edited": null,
    "rating": 5,
    "creator": {
        "username": "alice",
        "email": "alice@example.com"
    },
    "book": {
        "pk": 1,
        "title": "Advanced Deep Learning with Keras",
        "publisher": 1,
        "contributors": [
            1
        ],
        "cover": "http://www.baiters.ml/media/book_covers/Advanced_Deep_Learning_with_Keras.jpg"
    }
},
{
    "pk": 5,
    "content": "Test review for books read section in profile page",
    "date_created": "2021-12-08T15:53:08.623742Z",
    "date_edited": null,
    "rating": 5,
    "creator": {
        "username": "max",
        "email": "maxv0itc0v@gmail.com"
    },
    "book": {
        "pk": 2,
        "title": "Hands-On Machine Learning for Algorithmic Trading",
        "publisher": 1,
        "contributors": [
            4
        ],
        "cover": "http://www.baiters.ml/media/book_covers/machine-learning-for-algorithmic-trading.png"
    }
}
]
```
I used both Apis for creating front end with React an Babel. 


## Aditional python modules

In the developement of the site I included a list of aditiional modules for more functionability

### The list of the python modules used alongside Django:
- Csv
- Plotly
- Crispy Forms
- Django All_auth
- Django Debug Toolbar

### CSV
 I Used Csv for the profile page, the history for the books read or better to say the history of books you reviewed is stored and you can download it in a .csv format.
 This feature is for integration only, it is not a main feature, and it does not have a purpose the same reading history is displayed on the profile page.

 The backend for the reading history is written in bookr.bookr.views.reading_history
 ```python
 @login_required
def reading_history(request):
    user = request.user.username
    books_read = get_books_read(user)

    temp_file = BytesIO()

    workbook = Workbook(temp_file)
    worksheet = workbook.add_worksheet()

    data = []
    for book_read in books_read:
        data.append([book_read['title'],str(book_read['completed_on'])])

    for row in range(len(data)):
        for col in range(len(data[row])):
            worksheet.write(row, col, data[row][col])

    workbook.close()
    data_to_download = temp_file.getvalue()

    response = HttpResponse(content_type='aplication/vnd.ms-excel')
    response['Content-Disposition'] = 'atachement; filename=reading_history.xlsx'
    response.write(data_to_download)
    return response
 ```
 
### Plotly
I used plotly also on the user/profile page. The library creates a graph for the number of books read/reviewed in the past year.
The backend for the plot is also stored in bookr.bookr.views.
```python
@login_required
def profile(request):
    user = request.user
    permissions = user.get_all_permissions()
    books_read_by_month = get_books_read_by_month(user.username)
    months = [i+1 for i in range(12)]
    books_read = [0 for _ in range(12)]

    for num_books_read in books_read_by_month:
        list_index = num_books_read['date_created__month'] - 1
        books_read[list_index] = num_books_read['book_count']

    figure = graphs.Figure()
    scatter = graphs.Scatter(x=months, y=books_read)
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Month", yaxis_title="No. of books read")
    plot_html = plot(figure, output_type="div")

    context = {
        "user": user,
        "permissions": permissions,
        "books_read_plot": plot_html
    }
    return render(request, 'profile.html', context=context)
```

### Django ALL-AUTH
I installed and used Django All-Auth, but since this is a portfolio website, I did not planned to collect any data so it was removed in the production phase.

## Javascript
Like I said, JS was used only for frontend development and the libraries used were:
- React
- Babel

I am not fluent in JS, but with a little of Google and stackoverflow I can manage it.

I used Javascript only for the index page(https://www.baiters.ml/) in a div with the class="recent_reviews" and it's purpose for the page is to list the latest reviews written on the website.

```js
class ReviewDisplay extends React.Component {
    constructor(props) {
        super(props);
        this.state = { review: props.review };
    }

    render () {
      const review = this.state.review;

      return <div className="col mb-4">
            <div className="card">
                <div className="card-body">
		    <div>
		    <img className="card_img_top" src={ review.book.cover } alt={review.book.title}/>
                    <h5 className="card-title">{ review.book.title }
                    </h5>
		    </div>
                    <h6 className="card-subtitle mb-2 text-muted">{ review.creator.email }</h6>
                    <p className="card-text"><span className="badge badge-primary badge-pill">{ review.rating }</span> { review.content }</p>
                </div>
                <div className="card-footer">
                    <a href={'/book/' + review.book.pk + '/' } className="card-link">View Book</a>
                </div>
            </div>
        </div>;
    }

}

class RecentReviews extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            reviews: [],
            currentUrl: props.url,
            nextUrl: null,
            previousUrl: null,
            loading: false
        };
    }

    fetchReviews() {
        if (this.state.loading)
            return;
        this.setState( {loading: true} );

        fetch(this.state.currentUrl, {
          method: 'GET',
          headers: {
              Accept: 'application/json'
          }
        }).then((response) => {
          return response.json();
        }).then((data) => {
        this.setState({
                loading: false,
                reviews: data.results,
                nextUrl: data.next,
                previousUrl: data.previous
          })
		console.log(data.results)
        })
         //console.log(data.results)
    }

    componentDidMount() {
        this.fetchReviews()
    }

    loadNext() {
      if (this.state.nextUrl == null)
          return;

        this.state.currentUrl = this.state.nextUrl;
        this.fetchReviews();
    }

    loadPrevious() {
        if (this.state.previousUrl == null)
            return;

        this.state.currentUrl = this.state.previousUrl;
        this.fetchReviews();
    }

    render() {
        if (this.state.loading) {
            return <h5>Loading...</h5>;
        }

        const previousButton = <button
            className="btn btn-secondary"
            onClick={ () => { this.loadPrevious() } }
            disabled={ this.state.previousUrl == null }>
                Previous
        </button>;

        const nextButton = <button
            className="btn btn-secondary float-right"
            onClick={ () => { this.loadNext() } }
            disabled={ this.state.nextUrl == null }>
                Next
        </button>;

        let reviewItems;

        if (this.state.reviews.length === 0) {
            reviewItems = <h5>No reviews to display.</h5>
        } else {
            reviewItems = this.state.reviews.map((review) => {
                return <ReviewDisplay key={review.pk} review={review}/>
            })
        }

        return <div>
            <div className="row row-cols-1 row-cols-sm-2 row-cols-md-3">
                { reviewItems }
            </div>
            <div>
                { previousButton }
                { nextButton }
            </div>
        </div>;
    }
}
```

## Deployment
### For the deployment, since this is a portfolio project I choosed to deploy it on a self hostet server.
On an old laptop I installed Ubuntu Server 20.04 LTS and configured it for web hosting: installed ssh,nginx, gunicorn, python3, pip3, psycopg2(for integration with PostgreSQL), postgresql, SQLite3 etc. 

The website runs on another User, and this User is not sudoer, and cannot login with a Password, the only way to connect with the server is with ssh and ssh-keys only.
Configuration files can be found in bookr/service-conf/

### Nginx

The Nginx configuration in /etc/nginx/sites-avaible/bookr
```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    client_max_body_size 16M;
    root /home/bookr/Bookr-django-project;

    index intex.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
	    proxy_set_header Host $host;
            proxy_pass http://127.0.0.1:8001;
            proxy_set_header X-Forwarded-Host $server_name;
            proxy_set_header X-Real-IP $remote_addr;
            add_header p3p 'CP="ALL DSP COR PSAa OUR NOR ONL UNI COM NAV"';
            add_header Access-Control-Allow-Origin *;
    }
    location /static/ {
    	alias /home/bookr/Bookr-django-project/static/;
    }

    location /media/ {
    	alias /home/bookr/Bookr-django-project/media/;
	}
}
```
For SSL certificate I used Let's encrypt and Certbot so the final configuration file for Nginx looks like:
```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    client_max_body_size 16M;
    root /home/bookr/Bookr-django-project;

    index intex.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
	    proxy_set_header Host $host;
            proxy_pass http://127.0.0.1:8001;
            proxy_set_header X-Forwarded-Host $server_name;
            proxy_set_header X-Real-IP $remote_addr;
            add_header p3p 'CP="ALL DSP COR PSAa OUR NOR ONL UNI COM NAV"';
            add_header Access-Control-Allow-Origin *;
    }
    location /static/ {
    	alias /home/bookr/Bookr-django-project/static/;
    }

    location /media/ {
    	alias /home/bookr/Bookr-django-project/media/;
	}
}


server {

    root /home/bookr/Bookr-django-project;
    client_max_body_size 16M;

    index intex.html index.htm index.nginx-debian.html;
    server_name www.baiters.ml; # managed by Certbot


    location / {
	    proxy_set_header Host $host;
            proxy_pass http://127.0.0.1:8001;
            proxy_set_header X-Forwarded-Host $server_name;
            proxy_set_header X-Real-IP $remote_addr;
            add_header p3p 'CP="ALL DSP COR PSAa OUR NOR ONL UNI COM NAV"';
            add_header Access-Control-Allow-Origin *;
    }
    location /static/ {
    	alias /home/bookr/Bookr-django-project/static/;
    }

    location /media/ {
    	alias /home/bookr/Bookr-django-project/media/;
	}


    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.baiters.ml/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.baiters.ml/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}server {
    if ($host = www.baiters.ml) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80 ;
    listen [::]:80 ;
    server_name www.baiters.ml;
    return 404; # managed by Certbot


}
```

### Gunicorn

The configuration files fore gunicorn are stored in `bookr/config/gunicorn/dev.py`:
```python
command = '/home/bookr/Bookr-django-project/venv/bin/gunicorn'
pythonpath = '/home/bookr/Bookr-django-project/bookr/'
bind = '127.0.0.1:8001'
workers = 3
user = 'bookr'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=bookr.settings'
daemon = True
```

And the command that runs Gunicorn is `gunicorn -c config/gunicorn/dev.py bookr.wsgi:application:`



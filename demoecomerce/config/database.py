DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
    'data': {
        'NAME': 'bsale_test',
        'ENGINE': 'django.db.backends.mysql',
        'HOST' : 'mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com',
        'USER': 'bsale_test',
        'PASSWORD': 'bsale_test',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}

DATABASE_ROUTERS = ['apps.products.routers.RouterSql']
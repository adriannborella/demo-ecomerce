DATABASES = {
    'default': {
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

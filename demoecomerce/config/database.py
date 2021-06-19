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

# DATABASES = {
#     'default': {
#         'NAME': 'db_test',
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST' : '127.0.0.1',
#         'PORT' : 13306,
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'OPTIONS': {
#           'autocommit': True,
#         },
#     }
# }
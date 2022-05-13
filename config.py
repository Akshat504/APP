'''
    a config file, where we can remove or assign the new value according the code.
'''
import os

# class Config(object):
#     DEBUG = False
#     TESTING = False

# class ProductionConfig(Config):
#     pass

# class DevelopmentConfig(Config):
#     DEBUG = True

# class TestingConfig(Config):
#     TESTING = True



# class Config(object):        
#     DEBUG = False
#     TESTING = False
#     SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"

#     DB_NAME = "production-db"
#     DB_USERNAME = "admin"
#     DB_PASSWORD = "example"

#     IMAGE_UPLOADS = "/home/username/app/app/static/images/uploads"

#     SESSION_COOKIE_SECURE = True

# class ProductionConfig(Config):                                         #   config class we'll use for running in production
#     pass

# class DevelopmentConfig(Config):                                        #   Is the config class we'll use for development
#     DEBUG = True

#     DB_NAME = "development-db"
#     DB_USERNAME = "admin"
#     DB_PASSWORD = "example"

#     IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"

#     SESSION_COOKIE_SECURE = False

# class TestingConfig(Config):                                            #    class we'll use for testing
#     TESTING = True

# # assigning new values to configuration variables

#     DB_NAME = "development-db"
#     DB_USERNAME = "admin"
#     DB_PASSWORD = "example"

#     SESSION_COOKIE_SECURE = False
    


class Config(object):
    # ...
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
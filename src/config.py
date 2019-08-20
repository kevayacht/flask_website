import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # the above key is used cryptographic key, used to generate signatures or tokens

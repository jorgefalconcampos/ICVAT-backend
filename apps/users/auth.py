# https://tinyurl.com/bdevujx7

from rest_framework import authentication

class BearerAuth(authentication.TokenAuthentication):
    keyword = "Bearer"
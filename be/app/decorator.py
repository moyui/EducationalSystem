from functools import wraps
from flask import request

def is_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        userid = request.cookies.get('userid')
        return f(userid = userid, *args, **kwargs)
    return decorated_function

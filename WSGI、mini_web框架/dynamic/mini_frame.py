import time


def log_in():
    return '>>>>>>>>这是登陆页面<<<<<<<<<%s' % time.ctime()


def register():
    return '>>>>>>>>这是注册页面<<<<<<<<<%s' % time.ctime()


def profile():
    return '>>>>>>>>这是个人主面<<<<<<<<<%s' % time.ctime()


def index():
    with open('./static/test') as file:
        content = file.read()
        return content


def application(environ, set_header):
    set_header('200 ok', [('content-Type', 'Text.html; charset=utf-8')])
    file_name = environ['PATH_INFO']
    if file_name == '/login.py ':
        return log_in()
    elif file_name == '/index.py ':
        return index()
    elif file_name == '/register.py ':
        return register()
    elif file_name == '/profile.py ':
        return profile()
    else:
        return 'NOT FILE FOUND'

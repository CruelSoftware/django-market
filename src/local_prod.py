import environ


def local_or_prod():
    env = environ.Env()
    environ.Env.read_env('.env')
    if env.bool('DEBUG') == True:
        return True, 'config.local'
    else:
        return False, 'config.production'
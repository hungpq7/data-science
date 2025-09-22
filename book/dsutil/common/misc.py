def config_timezone():
    import os
    import time
    os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
    time.tzset()

def chronometer(inner):
    import functools
    import datetime as dt
    @functools.wraps(inner)
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()
        output = inner(*args, **kwargs)
        end = dt.datetime.now()
        duration = end - start
        msg = f'Function {inner.__name__} - elapsed time {duration}'
        print(msg)
        return output
    return wrapper
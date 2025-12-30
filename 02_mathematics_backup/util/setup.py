def setup_timezone():
    import os
    import time
    os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
    time.tzset()

def setup_reload():
    get_ipython().run_line_magic("reload_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")
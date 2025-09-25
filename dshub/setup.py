class NBConfig:
    @classmethod
    def set_warnings(cls):
        import warnings
        warnings.filterwarnings('ignore')

    @classmethod
    def set_timezone(cls):
        import os
        import time
        os.environ['TZ'] = 'Asia/Ho_Chi_Minh'
        time.tzset()

    @classmethod
    def set_reload(cls):
        get_ipython().run_line_magic("reload_ext", "autoreload")
        get_ipython().run_line_magic("autoreload", "2")
    
    @classmethod
    def setup(cls):
        cls.set_warnings()
        cls.set_timezone()
        cls.set_reload()
# Copyright 2019- Hiroki.H

class Config(object):
    """
    設定を取得するクラス。
    デフォルトではカレントディレクトリの config.ini を読み込む。
    """
    __instance = None
    __slots__ = ("__cfg")

    def __init__(self):
        super(Config, self).__init__()
        from configparser import ConfigParser
        self.__cfg = ConfigParser()
        import os
        self.__cfg.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        pass
    
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Config, cls).__new__(cls)
            pass
        return cls.__instance

    @property
    def consumer_key(self):
        return self.__cfg["CONSUMER"]["API_KEY"]
    
    @property
    def consumer_secret_key(self):
        return self.__cfg["CONSUMER"]["API_SECRET_KEY"]
    
    @property
    def access_token(self):
        return self.__cfg["ACCESS"]["TOKEN"]
    
    @property
    def access_token_secret(self):
        return self.__cfg["ACCESS"]["TOKEN_SECRET"]
    pass

class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    OPENAI_KEY = "your_secret_api_key_will_come_here"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

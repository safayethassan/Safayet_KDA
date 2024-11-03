class Config:
    DEV = {
        'base_url': 'https://www.facebook.com/',
        'timeout': 10,
    }

    STAGE = {
        'base_url': 'https://www.facebook.com/',
        'timeout': 15,
    }

    @staticmethod
    def get_config(env):
        return getattr(Config, env.upper(), None)
import logging

config = {
    "development": "app.config.DevelopmentConfig",
    "staging": "app.config.StagingConfig",
    "testing": "app.config.TestingConfig",
    "default": "app.config.DevelopmentConfig"
}

log = logging.getLogger()
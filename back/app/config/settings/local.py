from .base import *

#####################
# Security settings #
#####################

SECRET_KEY = '<fake-secret-key>'

DEBUG = True

ALLOWED_HOSTS = ['*']

################
# Static files #
################

STATIC_ROOT = BASE_DIR / 'static'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = BASE_DIR / 'media'

############
# Database #
############

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.get_value('MYSQL_DB_NAME'),
        'USER': env.get_value('MYSQL_USER_NAME'),
        'PASSWORD': env.get_value('MYSQL_PASSWORD'),
        'HOST': env.get_value('MYSQL_HOST_LOCAL'),
        'PORT': env.get_value('MYSQL_PORT'),
    }
}
DATABASES['default']['TIME_ZONE'] = 'Asia/Tokyo'
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['sql_mode'] = 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO'
# DATABASES['default']['init_command'] = 'STRICT_TRANS_TABLES'

###########
# Logging #
###########

LOGGING = {
    # スキーマバージョンは「1」固定
    'version': 1,
    # すでに作成されているロガーを無効化しないための設定
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # 開発用
        'development': {
            'format': '[{name}] {asctime} [{levelname}] {pathname}:{lineno:d} '
                      '{message}',
            'style': '{',
        },
    },
    # ハンドラ
    'handlers': {
        # コンソール出力用ハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'development',
        },
    },
    # ルートロガー
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    # その他のロガー
    'loggers': {
        # 自作アプリケーションごとにロガーを定義することも可能
        'ctf': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django本体が出力するログ全般を扱うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 発行されるSQL文を出力するためのロガー
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
    },
}

########################
# Django Debug Toolbar #
########################

if DEBUG:
    def show_toolbar(request):
        return True


    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

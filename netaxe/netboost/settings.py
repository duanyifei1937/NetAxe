"""
Django settings for netboost project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
import sys
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 自建APP
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# 初始化plugins插件路径到环境变量中
# PLUGINS_PATH = os.path.join(BASE_DIR, "apps")
# sys.path.insert(0, os.path.join(PLUGINS_PATH))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-57w6rkqxn1-)ry+sdc@3fmcd2)opcr^2a)zs^&#&-x)=fp(vb_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'channels',
    'guardian',
    'captcha',
    'django_filters',
    'multi_captcha_admin',
    'django_celery_results.apps.CeleryResultConfig',
    'rest_framework.apps.RestFrameworkConfig',
    'rest_framework.authtoken',
    'rest_framework_tracking',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',

    'apps.asset.apps.AssetConfig',
    'apps.api.apps.ApiConfig',
    'apps.config_center.apps.ConfigCenterConfig',
    'apps.route_backend.apps.RouteBackendConfig',
    'apps.users.apps.UsersConfig',
    'apps.automation.apps.AutomationConfig',
    'apps.int_utilization.apps.IntUtilizationConfig',
    'apps.system.apps.SystemConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# REST_FRAMEWORK = {
#     # # 全局配置异常模块
#     # 'EXCEPTION_HANDLER': 'apps.api.exception.custom_exception_handler',
#     # # 修改默认返回JSON的renderer的类
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'apps.api.rendererresponse.customrenderer',
#     # ),
#     'DEFAULT_FILTER_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackend'
#     ],
#     'DEFAULT_PERMISSION_CLASSES': (
#         # 'rest_framework.permissions.DjangoModelPermissions',
#         'rest_framework.permissions.IsAuthenticated',
#         # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ),
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         # 'apps.api.authentication.ExpiringTokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ),
#
# }
ROOT_URLCONF = 'netboost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Channels settings
ASGI_APPLICATION = "netboost.routing.application"

WSGI_APPLICATION = 'netboost.wsgi.application'

# 用户自定义配置
if os.path.exists("{}/{}/{}".format(BASE_DIR, "netboost", "conf.py")):
    from .conf import *
else:
    raise RuntimeError("没有找到conf.py的配置信息")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netboost.settings')
os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.UserProfile'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# channel配置
CHANNEL_LAYERS = {
    "default": {
        # This example app uses the Redis channel layer implementation channels_redis
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["{}0".format(REDIS_URL)],
        },
    },
}
CELERY_ONCE_URL = "{}1".format(REDIS_URL)
CELERY_RESULT_BACKEND = 'django-db'  # 使用django数据库
# CELERY_BROKER_URL = 'redis://10.254.0.111:6379/8'
CELERY_BROKER_URL = "{}8".format(REDIS_URL)
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERY_RESULT_BACKEND = 'redis://10.254.0.110:6379/9' #结果存储，我配置的是存储到数据库
# CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_ACCEPT_CONTENT = ['json', 'application/text']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_CONCURRENCY = 40  # celery worker的并发数
CELERY_MAX_TASKS_PER_CHILD = 20
CELERYD_MAX_TASKS_PER_CHILD = 20
# 这个表示每个工作的进程／线程／绿程 在执行 n 次任务后，主动销毁，之后会起一个新的。主要解决一些资源释放的问题。
CELERY_RESULT_EXPIRES = 7200  # celery任务执行结果的超时时间，
CELERY_TASK_RESULT_EXPIRES = 7200
# 这个表示保存任务结果的时长，这个时间会被设置到 redis 里面（假设 backend 是 redis ），如果抓取数据量大的话，是可以缩短保存的时间，
# 节省 backend 的资源（ redis 主要是内存）消耗，默认是 24 小时（ 86400 ），单位是秒。
CELERY_TASK_TIME_LIMIT = 7200
# 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'UTC'
CELERY_WORKER_CONCURRENCY = 40  # celery worker的并发数
# 也是命令行-c指定的数目,事实上实践发现并不是worker也多越好,保证任务不堆积,加上一定新增任务的预留就可
# 官方用来修复CELERY_ENABLE_UTC=False and USE_TZ = False 时时间比较错误的问题；
# 详情见：https://github.com/celery/django-celery-beat/pull/216/files
DJANGO_CELERY_BEAT_TZ_AWARE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
# STATIC_ROOT = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  # causes verbose duplicate notifications in django 1.9
)
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# simple jwt 设置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  # access token 有效期 30分钟
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),  # refresh token 有效期 2 天
    'ROTATE_REFRESH_TOKENS': True,
}

# restful api 配置
REST_FRAMEWORK = {
    # # 全局配置异常模块
    # 'EXCEPTION_HANDLER': 'apps.api.exception.custom_exception_handler',
    # # 修改默认返回JSON的renderer的类
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'apps.api.rendererresponse.customrenderer',
    # ),
    # 'DEFAULT_FILTER_BACKENDS': [
    #     'django_filters.rest_framework.DjangoFilterBackend'
    # ],
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissions',
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'apps.api.authentication.ExpiringTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 下面控制分页
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'apps.api.tools.custom_pagination.LargeResultsSetPagination',
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'apps.api.tools.custom_exception.custom_exception_handler',
    # 'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema'

}
# Restful token 有效时间60分钟
REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES = 60 * 8

DATA_UPLOAD_MAX_MEMORY_SIZE = 30485760
# api 缓存配置
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 60,
    'DEFAULT_USE_CACHE': 'api_cache',
    'DEFAULT_OBJECT_CACHE_KEY_FUNC': 'rest_framework_extensions.utils.default_object_cache_key_func',
    'DEFAULT_LIST_CACHE_KEY_FUNC': 'rest_framework_extensions.utils.default_list_cache_key_func',
}
# REST API REDIS缓存配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "{}2".format(REDIS_URL),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100},
        }
    },
    "api_cache": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "{}3".format(REDIS_URL),
        # "TIMEOUT": 7 * 24 * 60 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "guardian.backends.ObjectPermissionBackend",  # 这是guardian的
)

# ================================================= #
# **************** 验证码配置  ******************* #
# ================================================= #
# 验证码配置
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}
# CAPTCHA_IMAGE_SIZE = (160, 60)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
CAPTCHA_OUTPUT_FORMAT = "%(image)s %(text_field)s %(hidden_field)s "
CAPTCHA_FONT_SIZE = 40  # 字体大小
CAPTCHA_FOREGROUND_COLOR = "#64DAAA"  # 前景色
CAPTCHA_BACKGROUND_COLOR = "#F5F7F4"  # 背景色
CAPTCHA_NOISE_FUNCTIONS = (
    "captcha.helpers.noise_arcs",  # 线
    # "captcha.helpers.noise_dots",  # 点
)
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #字母验证码
CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"  # 加减乘除验证码

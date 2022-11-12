# -*- coding: utf-8 -*-
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'

    CKEDITOR_CONFIGS = {
        # django-ckeditor 默认使用default配置，
        'default': {
            # 编辑器宽度自适应
            'width': 'auto',
            'height': '600px',
            # tab键转换空格数
            'tabSpaces': 4,
            # 工具栏风格
            'toolbar': 'Custom',
            # 工具栏按钮
            'toolbar_Custom': [
                # 源代码
                ['Source'],
                # 格式、字体、大小
                ['Format', 'Font', 'FontSize'],
                # 字体颜色
                ['TextColor', 'BGColor'],
                # 字体风格
                ['Bold', 'Italic', 'Underline', 'RemoveFormat', 'Blockquote'],
                # 预览、表情
                ['Preview', 'Smiley'],
                # 链接
                ['Link', 'Unlink'],
                # 列表
                ['Image', 'NumberedList', 'BulletedList', 'HorizontalRule'],
                # 居左，居中，居右
                ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                ['CodeSnippet', 'Markdown'],  # 这个markdown插件默认没有，得额外下载。
                # 最大化
                ['Maximize'],

            ],
            # 加入代码块插件
            'extraPlugins': ','.join(['codesnippet', 'markdown', 'image2', 'filebrowser', 'widget', 'lineutils']),
        },
        # 评论用的，可以定义多个分别应用的不同的场景
        'comment': {
            # 编辑器宽度自适应
            # tab键转换空格数
            'tabSpaces': 4,
            # 工具栏风格
            'toolbar': 'Custom',
            # 工具栏按钮
            'toolbar_Custom': [
                # 表情 代码块
                ['Smiley', 'CodeSnippet'],
                # 字体风格
                ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat', 'Blockquote'],
                # 字体颜色
                ['TextColor', 'BGColor'],
                # 链接
                ['Link', 'Unlink'],
                # 列表
                ['NumberedList', 'BulletedList'],
            ],
            # 加入代码块插件
            'extraPlugins': ','.join(['codesnippet']),
        }
    }

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)

    BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')
    BLUELOG_POST_PER_PAGE = 10
    BLUELOG_MANAGE_POST_PER_PAGE = 15
    BLUELOG_COMMENT_PER_PAGE = 15
    # ('theme name', 'display name')
    BLUELOG_THEMES = {'perfect_blue': '经典蓝', 'black_swan': '黑夜模式'}
    BLUELOG_SLOW_QUERY_THRESHOLD = 1

    BLUELOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    BLUELOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

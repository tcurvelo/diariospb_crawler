# Scrapy settings for diarios project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'diarios'

SPIDER_MODULES = ['diarios.spiders']
NEWSPIDER_MODULE = 'diarios.spiders'

DOWNLOAD_DELAY = 2

USER_AGENT = 'diarios_pb crawler'

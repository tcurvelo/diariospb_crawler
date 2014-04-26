BOT_NAME = 'diarios'

SPIDER_MODULES = ['diarios.spiders']
NEWSPIDER_MODULE = 'diarios.spiders'

DOWNLOAD_DELAY = 2

USER_AGENT = 'diarios_pb crawler'

ITEM_PIPELINES = {
    'scrapy.contrib.pipeline.files.FilesPipeline': 500,
}

FILES_STORE = "/tmp/"
FILES_URLS_FIELD = "url"
FILES_RESULT_FIELD = "files"

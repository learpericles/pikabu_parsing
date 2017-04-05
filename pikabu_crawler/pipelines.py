import json
import codecs

class PikabuCrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open('stories.json', 'w', encoding='utf-8') #a for addition a new data

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

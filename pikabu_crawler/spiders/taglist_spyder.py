from scrapy.spiders import CrawlSpider
from pikabu_crawler.items import StoryItem

class TaglistSpyder(CrawlSpider):
    name = "taglist"
    allowed_domains = ["pikabu.ru"]
    start_urls = [
        "http://pikabu.ru/new",
    ]

    def parse(self, response):
        EMPTY_STORY_ID = u"_"

        for story in response.css('div.story'):
            story_id = story.css('*::attr(data-story-id)').extract_first()

            if story_id == EMPTY_STORY_ID:
                continue

            item = StoryItem()
            item["date"] = story.css('div.story__date::attr(title)').extract()
            item["tags"] = story.css("div.story__tags a::text").extract()

            for i in range(len(item["tags"])):
                tag = item["tags"][i]
                tag = tag[8:-7]
                item["tags"][i] = tag

            yield item

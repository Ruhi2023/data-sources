from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings  # Import the spider
from scrapy_test import PdfSpider
# Initialize the Scrapy crawler process
process = CrawlerProcess(get_project_settings())

# Configure the spider to run
process.crawl(PdfSpider)

# Start the crawling process
process.start()


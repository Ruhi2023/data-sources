
# w-flow trying scrapy
import scrapy
import json

class PdfSpider(scrapy.Spider):
    name = 'pdf_spider'
    
    # List of websites you want to scrape
    start_urls = [
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC11706671/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC11706667/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC11706642/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC11706636/",
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC11706634/"
    ]
    def give_urls(self, url_list):
        self.start_urls = url_list

    def parse(self, response):
        # Find the <a> tag with the specific class
        pdf_link_tag = response.css('a.usa-button.usa-button--outline.width-24.display-inline-flex.flex-align-center.flex-justify-start.padding-left-1::attr(href)').get()
        
        if pdf_link_tag:
            # Handle relative URLs (if necessary)
            if pdf_link_tag.startswith('pdf'):
                pdf_link_tag = response.urljoin(pdf_link_tag)  # Convert relative URL to absolute
            
            # Yield the result (or you can save it directly)
            data = {
                'url': response.url,
                'pdf_link': pdf_link_tag
            }
            yield data
            with open('scraped_data.json', 'a') as file:
                json.dump(data, file)
                file.write(',\n')
        else:
            self.log(f"No PDF link found on {response.url}")
    
    # seg-expl: called when execution is finished for crawler, to save links in a json file
    def closed(self, reason):
        
        self.log('Saved pdf links to pdf_links.json')


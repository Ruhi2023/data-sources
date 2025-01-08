from pymedx import PubMed as pm1
from pymedx import PubMedCentral as pmc
from pymed import PubMed as pm2
import time
import requests
import json
import aiohttp

# w-flow 1.first check how long it takes to get the id and article from pubmed 
# w-flow 1.1. implement pubmedx first
# w-flow 1.2. implement pubmed then
# w-flow 1.3. implement aiohttp 
# w-flow 1.4. implement requests
# w-flow 2. compare and contracst best results


# w-flow 1.first check how long it takes to get the id and article from pubmed 

# seg-expl This is initialization
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
fl = open("apikey.txt", "r")
PMX = pm1(api_key=fl.readline())
PMC1 = pmc(api_key=fl.readline())
PM = pm2()
query = "fibrosis"

# w-flow 1.1. implement pubmedx first
pmx_start = time.time()
art_id = PMC1._getArticleIds(query,max_results=7)
print(art_id)
    # use this id to get the article
res_dat= PMC1._getArticles(art_id)
for articles in res_dat:
    print(articles.toJSON())
    print(articles.pmc_id)
    
    # full_text_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{article.pmc}/"
    # print(f"Full Text Available at: {full_text_url}")

pmx_end = time.time()
print(pmx_end-pmx_start)

# w-flow 1.2. implement pubmed then
# w-flow 1.3. implement aiohttp 
# w-flow 1.4. implement requests
# w-flow 2. compare and contracst best results
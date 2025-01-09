
from pymedx import PubMed as pm1
from pymedx import PubMedCentral as pmc
from pymed import PubMed as pm2
import time
import re
import doi2pdf
import requests
import json
import aiohttp
from concurrent.futures import ThreadPoolExecutor as myexe
import timeit
from functools import partial

# w-flow 1.first check how long it takes to get the id and article from pubmed 
# w-flow 1.1. implement pubmedx first
# * will not implement it 1.2. implement pubmed then
# w-flow 1.3. implement aiohttp 
# w-flow 1.4. implement requests
# w-flow 2. compare and contracst best results


# w-flow 1.first check how long it takes to get the id and article from pubmed 

# seg-expl This is initialization and utility functions
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
fl = open("apikey.txt", "r")
PMX = pm1(api_key=fl.readline())
PMC1 = pmc(api_key=fl.readline())
PM = pm2()
query = "cancer"

# utility function valid file name


def sanitize_filename(filename: str) -> str:
# Define a regular expression pattern to match any invalid characters
    invalid_chars = r'[<>:"/\\|?*]'

    # Replace invalid characters with an underscore (_)
    sanitized_filename = re.sub(invalid_chars, '_', filename)

    return sanitized_filename

# w-flow 1.1. implement pubmedx first
pmx_start = time.time()
art_id = PMC1._getArticleIds(query,max_results=5)
print(art_id)
    # use this id to get the article
res_dat= PMC1._getArticles(art_id)
art_dat =[]
for articles in res_dat:

    art_dat.append((articles.doi, articles.title, articles.pmc_id))
print(art_dat)

    
    # full_text_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{article.pmc}/"
    # print(f"Full Text Available at: {full_text_url}")

pmx_end = time.time()
print(pmx_end-pmx_start)

# * does not work
#// def download_pdf(doi, name):
#//     name =sanitize_filename(name)
#//     try:
#//         doi2pdf.doi2pdf(doi,output=f"docs/{name}.pdf")
#//     except Exception as e:
#//         print(f"Unable to download {name}")
#//         print(e)
#//         try:
#//             doi2pdf.doi2pdf(name=name,output=f"docs/{name}.pdf")
#//         except Exception as e:
#//             print(f"Unable to download {name}")
#//             print(e)

# seg-expl: since we have the doi and names now we just use threadpoolexecuter
# *does not work
#// def concurrent_download(tuple_list):
#//     with myexe(max_workers=10) as executor:
#//         # it's a batch job the doi and name will be tuples
#//         for doi, name in tuple_list:
#//             executor.submit(download_pdf, doi, name)

#// concurrent_download_par = partial(concurrent_download, tuple_list=art_dat)
# seg-expl: this is the main function
# *does not work
#// def main():
#//     # using timeit to time the concurrent download function
#//     tt =timeit.timeit(concurrent_download_par, number=1, globals=globals(),)
#//     print(tt)

# seg-expl: trying to check working with normal values
# * downoads html as it is
# time_start = time.time()
# for  doi, name in art_dat:
#     print("Downloading: ", name)
#     print("DOI: ", doi)
#     download_pdf(doi, name)
#     print("Done")
# time_end = time.time()
# time_to_download = time_end - time_start
# print(time_to_download)


# w-flow 1.3. implement aiohttp 
# w-flow 1.4. implement requests
# w-flow 2. compare and contracst best results
from pymed import PubMed
import time

# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed()

# Create a GraphQL query in plain text
query = "liver function"

# time now
now = time.time()
# Execute the query against the API
# seg-expl this is just testing
results = pubmed.query(query, max_results=5)
art = []
after = time.time()
# Loop over the retrieved articles
for article in results:

    # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle)
    print(type(article))

    # Print a JSON representation of the object
    temp = article.toJSON()
    art.append(temp)
    print(temp)
# seg-expl creating a text file output 50 to telll the Query result of 50 articles

with open("500_arts.txt", "w") as f:
    f.write(str(art))
    f.write("time taken =" + str(after - now))

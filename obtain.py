def get_URI(query: str, API_KEY: str) -> str:
    # append query to uri
    URI = f'https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}'

    # add page_num and date parameters
    # URI = URI + f'&page{page_num}&begin_date={date}&end_date={date}'

    # add API key
    URI = URI + f'&api-key={API_KEY}'

    # return the new URI
    return URI

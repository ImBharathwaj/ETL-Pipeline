import time
import datetime
import pandas as pd
import requests
from pandas import json_normalize
from obtain import *


# ---------------------------------------------
# ------------------ Extract ------------------
# ---------------------------------------------
def run():
    # create a dataframe that will store all articles
    df = pd.DataFrame()

    # get current date
    current_date = datetime.datetime.now().strftime('%Y%m%d')

    # collect data from all available pages
    page_num = 1
    api = "Ssl1xKId80aKG4IikUM20zitycF478OL"

    while True:
        # get the URI needed for the articles related to Winter Olympics from newest to oldest
        URI = get_URI(query='Artificial Intelligence', API_KEY=api)

        # make a request with the url
        response = requests.get(URI)

        # collect the data from the response in JSON format
        data = response.json()

        # convert data to a data frame
        df_request = json_normalize(data['response'], record_path=['docs'])

        # end loop if no new articles are available
        if df_request.empty:
            break

        # append df_request to the dataframe
        df = pd.concat([df, df_request])

        # pause to stay within the limit of number of requests
        time.sleep(6)

        # got to the next page
        page_num += 1

        return df
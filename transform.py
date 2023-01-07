from extract import *


# ---------------------------------------------
# ----------------- Transform -----------------
# ---------------------------------------------
def transform():
    df = run()
    df = df.drop_duplicates('_id', keep='first')
    # df = df[df['headline.main'].isnull() is False]
    df = df[df['type_of_material'] != 'op-ed']
    df = df[['headline.main', 'pub_date', 'byline.original', 'web_url']]
    df.columns = ['headline', 'date', 'author', 'url']
    return df

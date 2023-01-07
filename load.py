from transform import *
from sqlalchemy import create_engine


# ---------------------------------------------
# -------------------- Load -------------------
# ---------------------------------------------
def load():
    username = 'postgres'
    password = 'root'
    database = 'test'
    database_uri = f'postgresql://{username}:{password}@localhost:5432/{database}'

    engine = create_engine(database_uri)
    # con = engine.connect()
    df_test = transform()

    # Add data to database
    df_test.to_sql(
        'news_articles',
        con=engine,
        if_exists='append'
    )

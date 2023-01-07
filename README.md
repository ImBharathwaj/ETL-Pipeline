# ETL-Pipeline
Building ETL pipeline using NewYork Times article API with Pandas and PostgreSQL


# Extract
Fetching article data from NewYork times 
by passing some query string article API
using python


# Transform
Transforming extracted data from the API
is cleansed & re-formatted into a useful schema
and stored into a dataframe using Pandas dataframe


# Load
Cleansed and re-formatted data is getting loaded in PostgreSQL
using sqlalchemy and loaded data is fetched using the same 
sqlalchemy as we required using python

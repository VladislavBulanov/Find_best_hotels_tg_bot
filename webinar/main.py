from database.core import crud
from database.models.models import History, db
from site_api.core import siteapi, url, headers, params

db_write = crud.create()
db_read = crud.retrieve()

fact_by_number = siteapi.get_math_fact()
fact_by_date = siteapi.get_date_fact()

response = fact_by_number("GET", url, headers, params, 5, 3)
response = response.json()
data = [
    {
        "number": response.get("number"),
        "message": response.get("text"),
    }
]
db_write(db, History, data)

response = fact_by_date("GET", url, headers, params, "6", "21", 3)
response = response.json()
data = [
    {
        "number": response.get("year"),
        "message": response.get("text"),
    }
]
db_write(db, History, data)

retrieved = db_read(db, History, History.number, History.message)

for element in retrieved:
    print(element.number, element.message)

from sqlalchemy.orm import Session
from sqlalchemy import Date, cast
from database import SessionLocal, engine, Base
from models import Entry

# Створення бази даних і таблиць
Base.metadata.create_all(bind=engine)

# Створення сесії
db = SessionLocal()

def goOutside():
    for row in db.query(Entry):
        row.go_outside=True
        if row.wind_kph > 50: row.go_outside=False
        if row.air_quality_Carbon_Monoxide > 1000: row.go_outside=False
        if row.air_quality_Ozone > 100: row.go_outside=False
        if row.air_quality_Nitrogen_dioxide > 50: row.go_outside=False
        if row.air_quality_Sulphur_dioxide > 50: row.go_outside=False
        if row.air_quality_PM2_5 > 35.5: row.go_outside=False
        if row.air_quality_PM10 > 155: row.go_outside=False
        if row.air_quality_us_epa_index > 2: row.go_outside=False
        if row.air_quality_gb_defra_index > 4: row.go_outside=False
        db.commit()
        db.refresh(row)

goOutside()
# Закриття сесії
db.close()

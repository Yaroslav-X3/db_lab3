from sqlalchemy import Column, Integer, String, Boolean, Float, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Entry(Base):
    __tablename__ = 'weather'

    go_outside = Column(Boolean, index=True)
    country = Column(String, primary_key=True, index=True)
    location_name = Column(String, primary_key=True, index=True)
    timezone = Column(String, index=True)
    wind_degree = Column(String, index=True)
    last_updated_epoch = Column(String, index=True)
    moon_illumination = Column(String, index=True)
    wind_kph = Column(Float, index=True)
    latitude = Column(Float, index=True)
    wind_kph = Column(Float, index=True)
    longitude = Column(Float, index=True)
    last_updated = Column(Date, primary_key=True, index=True)
    sunrise = Column(Time, index=True)
    sunset = Column(Time, index=True)
    air_quality_Carbon_Monoxide = Column(Float, index=True)
    air_quality_Ozone = Column(Float, index=True)
    air_quality_Nitrogen_dioxide = Column(Float, index=True)
    air_quality_Sulphur_dioxide = Column(Float, index=True)
    air_quality_PM2_5 = Column(Float, index=True)
    air_quality_PM10 = Column(Float, index=True)
    air_quality_us_epa_index = Column(Float, index=True)
    air_quality_gb_defra_index = Column(Float, index=True)

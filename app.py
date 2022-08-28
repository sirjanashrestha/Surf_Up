#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,func

from flask import Flask,jsonify

#set up database
engine=create_engine("sqlite:///hawaii.sqlite")

#reflect database into classes
Base=automap_base()

#reflect database
Base.prepare(engine,reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station
session=Session(engine)

#set up Flask
app=Flask(__name__)

#define the route
@app.route("/")
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /apo/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        '''
    )


#Precipitation route
@app.route("/api/v1.0/precipitation")

#create precipitation function
def precipitation():
    # Calculate the date one year from the last date in data set.
    prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
    precipitation=session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date>=prev_year).all()
    precip={date:prcp for date,prcp in precipitation}
    return jsonify(precip)

#Station route
@app.route("/api/v1.0/stations")

#create stations function
def stations():
    result=session.query(Station.station).all()
    stations=list(np.ravel(result))
    return jsonify(stations=stations)
  

#Temperature route
@app.route("/api/v1.0/tobs")

#create temperature function
def temp_monthly():
    prev_year=dt.date(2017,8,23)-dt.timedelta(days=365)
    results=session.query(Measurement.tobs).\
    filter(Measurement.station=='USC00519281').\
    filter(Measurement.date>=prev_year).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)


#Create route for statistical analysis
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create a function
def stats(start=None, end=None):
    sel=[func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]

    if not end:
        results=session.query(*sel).\
            filter(Measurement.date>=start).all()
        temps=list(np.ravel(results))
        return jsonify(temps=temps)

    results=session.query(*sel).\
            filter(Measurement.date>=start).\
             filter(Measurement.date<=start).all()
    temps=list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == "__main__":
    app.run()
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates
from mpld3 import plugins, utils
from datetime import datetime, timedelta
import custom_plugins as mplm

#Pull in the data created by get_data.py
harris_data = pd.read_excel("Harris_Data.xlsx")
harris_data["Date"] = harris_data["Date"].astype('datetime64[ns]')
harris_dates = harris_data["Date"].tolist()
harris_datetimes = [date.to_pydatetime() for date in harris_dates]

maricopa_data = pd.read_excel("Maricopa_Data.xlsx")
maricopa_data["Date"] = maricopa_data["Date"].astype('datetime64[ns]')
maricopa_dates = maricopa_data["Date"].tolist()
maricopa_datetimes = [date.to_pydatetime() for date in maricopa_dates]

san_diego_data = pd.read_excel("San_Diego_Data.xlsx")
san_diego_data["Date"] = san_diego_data["Date"].astype('datetime64[ns]')
san_diego_dates = san_diego_data["Date"].tolist()

salt_lake_data = pd.read_excel("Salt_Lake_Data.xlsx")
salt_lake_data["Date"] = salt_lake_data["Date"].astype('datetime64[ns]')
salt_lake_dates = salt_lake_data["Date"].tolist()

utah_data = pd.read_excel("Utah_Data.xlsx")
utah_data["Date"] = utah_data["Date"].astype('datetime64[ns]')
utah_dates = utah_data["Date"].tolist()

clark_data = pd.read_excel("Clark_Data.xlsx")
clark_data["Date"] = clark_data["Date"].astype('datetime64[ns]')
clark_dates = clark_data["Date"].tolist()

travis_data = pd.read_excel("Travis_Data.xlsx")
travis_data["Date"] = travis_data["Date"].astype('datetime64[ns]')
travis_dates = travis_data["Date"].tolist()

westchester_data = pd.read_excel("Westchester_Data.xlsx")
westchester_data["Date"] = westchester_data["Date"].astype('datetime64[ns]')
westchester_dates = westchester_data["Date"].tolist()

los_angeles_data = pd.read_excel("Los_Angeles_Data.xlsx")
los_angeles_data["Date"] = los_angeles_data["Date"].astype('datetime64[ns]')
los_angeles_dates = los_angeles_data["Date"].tolist()

county_dict = {'harris': harris_data, 'maricopa': maricopa_data, 'san_diego': san_diego_data, 
		       'salt_lake': salt_lake_data, 'utah': utah_data, 'clark': clark_data,
		       'travis': travis_data, 'westchester': westchester_data, 'los_angeles': los_angeles_data}

"""
Population Source
https://covid19-uscensus.hub.arcgis.com/
2014-2018 ACS Total Population

The American Community Survey (ACS) period estimates are based on a rolling sample survey spanning a 60-month period. A Margin of Error (MOE) measures the variability of the estimate due to sampling error.

Source: American Community Survey (ACS)
"""
population_dict = {'harris': 4602523, 'maricopa': 4253913, 'san_diego': 3302833, 
				   'salt_lake': 1120805, 'utah': 590440, 'clark': 2141574,
				   'travis': 1203166, 'westchester': 968815, 'los_angeles': 10098052}

#Calculate cumulative totals as a percentage of the total population
for county, data in county_dict.items():
	confirmed_data = data["Confirmed"].tolist()
	percapita_data = [round(100* confirmed / population_dict[county],2) for confirmed in confirmed_data]
	data["PerCapita"] = percapita_data

#DO SOME EPLOTTING
fig, ax = plt.subplots(1, figsize=(10,5))
harris_line = ax.plot(harris_datetimes, harris_data["PerCapita"], '-', marker='o', label="Harris County, TX")
maricopa_line = ax.plot(maricopa_datetimes, maricopa_data["PerCapita"], '-', marker='o', label="Maricopa County, AZ")
travis_line = ax.plot(travis_dates, travis_data["PerCapita"], '-', marker='o', label="Travis County, TX")
san_diego_line = ax.plot(san_diego_dates, san_diego_data["PerCapita"], '-', marker='o', label="San Diego County, CA")
los_angeles_line = ax.plot(los_angeles_dates, los_angeles_data["PerCapita"], '-', marker='o', label="Los Angeles County, CA")
clark_line = ax.plot(clark_dates, clark_data["PerCapita"], '-', marker='o', label="Clark County, NV")
salt_lake_line = ax.plot(salt_lake_dates, salt_lake_data["PerCapita"], '-', marker='o', label="Salt Lake County, UT")
utah_line = ax.plot(utah_dates, utah_data["PerCapita"], '-', marker='o', label="Utah County, UT")
westchester_line = ax.plot(westchester_dates, westchester_data["PerCapita"], '-', marker='o', label="Westchester County, NY")

ax.set_xlabel('Date')
ax.set_ylabel('Cumulative COVID-19 Cases Per 100 People')
ax.set_title('Cumulative Percentage of Population Infected With COVID-19')
ax.legend()


mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(harris_line[0],labels=harris_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(maricopa_line[0],labels=maricopa_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(san_diego_line[0],labels=san_diego_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(salt_lake_line[0],labels=salt_lake_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(utah_line[0],labels=utah_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(clark_line[0],labels=clark_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(travis_line[0],labels=travis_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(westchester_line[0],labels=westchester_data["PerCapita"].tolist()))
mpld3.plugins.connect(fig, mpld3.plugins.PointLabelTooltip(los_angeles_line[0],labels=los_angeles_data["PerCapita"].tolist()))

mpld3.save_html(fig, "uploads/core/templates/core/plotpercapita.html")





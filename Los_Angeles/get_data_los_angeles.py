import pandas as pd
import io
import requests
from datetime import datetime

#Import data file if it already exists
try:
	past_data = pd.read_excel("Los_Angeles_Data.xlsx")
	past_dates = past_data["Date"].tolist()
except:
	past_data = pd.DataFrame({})
	past_dates = []

#Get today's date and then generate a list of dates starting 01-22-2020 and ending today
todays_date = datetime.today().strftime('%m-%d-%Y')
datetimerange = pd.date_range(start='03/01/2020', end=datetime.today()).to_pydatetime().tolist()
daterange = []
for date in datetimerange:
	daterange.append(date.strftime('%m-%d-%Y'))

#Make empty lists to fill in later
confirmed = []
deaths = []
recovered = []
active = []
good_dates = []
daily_confirmed = [0]

#iterate over the list of dates
#grab each file
#grab only los_angeles county data
#get specific data from each date and append to a list
for date in daterange:
	if date in past_dates:
		pass

	else:
		url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
				+ date + ".csv")
		try:
			s = requests.get(url).content
			full_csv = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col="Combined_Key")
			los_angeles = pd.DataFrame(full_csv.loc["Los Angeles, California, US"])

			los_angeles = los_angeles.transpose()
			try:
				confirmed.append(los_angeles.iloc[0]["Confirmed"])
			except:
				confirmed.append(0)
			try:
				deaths.append(los_angeles.iloc[0]["Deaths"])
			except:
				deaths.append(0)
			try:
				recovered.append(los_angeles.iloc[0]["Recovered"])
			except:
				recovered.append(0)
			try:
				active.append(los_angeles.iloc[0]["Active"])
			except:
				active.append(0)
			good_dates.append(date)
			print("Getting info for " + str(date))
		except:
			pass

		try:
			s = requests.get(url).content
			full_csv = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col="Province/State")
			los_angeles = pd.DataFrame(full_csv.loc["Los Angeles County, CA"])

			los_angeles = los_angeles.transpose()
			try:
				confirmed.append(los_angeles.iloc[0]["Confirmed"])
			except:
				confirmed.append(0)
			try:
				deaths.append(los_angeles.iloc[0]["Deaths"])
			except:
				deaths.append(0)
			try:
				recovered.append(los_angeles.iloc[0]["Recovered"])
			except:
				recovered.append(0)
			try:
				active.append(los_angeles.iloc[0]["Active"])
			except:
				active.append(0)
			good_dates.append(date)
			print("Getting info for " + str(date))
		except:
			pass

#Append newly grabbed data to the existing data
los_angeles_data = past_data.copy()
for i in range(len(good_dates)):
	los_angeles_data = los_angeles_data.append({"Date": good_dates[i], "Confirmed": confirmed[i],
									  "Deaths": deaths[i], "Recovered": recovered[i],
									  "Active": active[i]}, ignore_index=True)

#Drop duplicates or it messes up plotting
los_angeles_data = los_angeles_data.drop_duplicates(subset="Date", ignore_index=True)

with pd.ExcelWriter("Los_Angeles_Data.xlsx") as writer:
	los_angeles_data.to_excel(writer, 'Los Angeles Co., CA')

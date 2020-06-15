import pandas as pd
import io
import requests
from datetime import datetime

#Import data file if it already exists
try:
	past_data = pd.read_excel("Travis_Data.xlsx")
	past_dates = past_data["Date"].tolist()
except:
	past_dates = []

#Get today's date and then generate a list of dates starting 01-22-2020 and ending today
todays_date = datetime.today().strftime('%m-%d-%Y')
datetimerange = pd.date_range(start='03/05/2020', end=datetime.today()).to_pydatetime().tolist()
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
#grab only travis county data
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
			travis = pd.DataFrame(full_csv.loc["Travis, Texas, US"])

			travis = travis.transpose()
			try:
				confirmed.append(travis.iloc[0]["Confirmed"])
			except:
				confirmed.append(0)
			try:
				deaths.append(travis.iloc[0]["Deaths"])
			except:
				deaths.append(0)
			try:
				recovered.append(travis.iloc[0]["Recovered"])
			except:
				recovered.append(0)
			try:
				active.append(travis.iloc[0]["Active"])
			except:
				active.append(0)
			good_dates.append(date)
			print("Getting info for " + str(date))
		except:
			pass

		try:
			s = requests.get(url).content
			full_csv = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col="Province/State")
			travis = pd.DataFrame(full_csv.loc["Travis County, TX"])

			travis = travis.transpose()
			try:
				confirmed.append(travis.iloc[0]["Confirmed"])
			except:
				confirmed.append(0)
			try:
				deaths.append(travis.iloc[0]["Deaths"])
			except:
				deaths.append(0)
			try:
				recovered.append(travis.iloc[0]["Recovered"])
			except:
				recovered.append(0)
			try:
				active.append(travis.iloc[0]["Active"])
			except:
				active.append(0)
			good_dates.append(date)
			print("Getting info for " + str(date))
		except:
			pass

#Append newly grabbed data to the existing data
try:
	travis_data = past_data.copy()
except:
	travis_data = pd.DataFrame({})
for i in range(len(good_dates)):
	travis_data = travis_data.append({"Date": good_dates[i], "Confirmed": confirmed[i],
									  "Deaths": deaths[i], "Recovered": recovered[i],
									  "Active": active[i]}, ignore_index=True)

#Drop duplicates or it messes up plotting
travis_data = travis_data.drop_duplicates(subset="Date", ignore_index=True)

with pd.ExcelWriter("Travis_Data.xlsx") as writer:
	travis_data.to_excel(writer, 'Travis Co., TX')

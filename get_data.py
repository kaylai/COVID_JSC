import pandas as pd
import io
import requests
from datetime import datetime

#Get today's date and then generate a list of dates starting 01-22-2020 and ending today
todays_date = datetime.today().strftime('%m-%d-%Y')
datetimerange = pd.date_range(start='03/22/2020', end=datetime.today()).to_pydatetime().tolist()
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
#grab only Harris county data
#get specific data from each date and append to a list
for date in daterange:
	print("Getting info for " + str(date))
	url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
			+ date + ".csv")
	try:
		s = requests.get(url).content
		full_csv = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col="Combined_Key")
		harris = pd.DataFrame(full_csv.loc["Harris, Texas, US"])

		harris = harris.transpose()
		try:
			confirmed.append(harris.iloc[0]["Confirmed"])
		except:
			confirmed.append(0)
		try:
			deaths.append(harris.iloc[0]["Deaths"])
		except:
			deaths.append(0)
		try:
			recovered.append(harris.iloc[0]["Recovered"])
		except:
			recovered.append(0)
		try:
			active.append(harris.iloc[0]["Active"])
		except:
			active.append(0)
		good_dates.append(date)
	except:
		pass

	try:
		s = requests.get(url).content
		full_csv = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col="Combined_Key")
		harris = pd.DataFrame(full_csv.loc["Harris,Texas,US"])

		harris = harris.transpose()
		try:
			confirmed.append(harris.iloc[0]["Confirmed"])
		except:
			confirmed.append(0)
		try:
			deaths.append(harris.iloc[0]["Deaths"])
		except:
			deaths.append(0)
		try:
			recovered.append(harris.iloc[0]["Recovered"])
		except:
			recovered.append(0)
		try:
			active.append(harris.iloc[0]["Active"])
		except:
			active.append(0)
		good_dates.append(date)
	except:
		pass
		

#Make a new dataframe and turn your lists of data into columns
harris_data = pd.DataFrame()
harris_data["Date"] = good_dates
harris_data["Confirmed"] = confirmed
harris_data["Deaths"] = deaths
harris_data["Recovered"] = recovered
harris_data["Active"] = active

with pd.ExcelWriter("Harris_Data.xlsx") as writer:
	harris_data.to_excel(writer, 'Harris Co., Texas')


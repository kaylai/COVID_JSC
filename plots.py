import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

#define function to calculate a 5-day moving average
def moving_average(a, n=5) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

#Pull in the data created by get_data.py
harris_data = pd.read_excel("Harris_Data.xlsx")
harris_data["Date"] = harris_data["Date"].astype('datetime64[ns]')

#Calculate daily totals instead of cumulative
confirmed_data = harris_data["Confirmed"].tolist()
daily_confirmed = [0]
for i in range(len(confirmed_data)):
	if i==8:
		daily_confirmed.append(0)
	elif i>0:
		daily_confirmed.append(confirmed_data[i]-confirmed_data[i-1])
harris_data["Daily_Confirmed"] = daily_confirmed

#Calculate whether negative or postive trend in last 14 days
date_list = harris_data["Date"].tolist()

datetime_list = [] #convert dates from pandas timestamp to python datetimes
for date in date_list:
	datetime_list.append(date.to_pydatetime())

most_recent_date = datetime_list[-1]
fourteen_days_ago = most_recent_date - timedelta(days=14) #get date 14 days before most recent date in date list
closest_date_with_data = min(datetime_list, key=lambda d: abs(d - fourteen_days_ago)) #get date in list of dates that is closest to our 14 days ago datetime

fourteen_days_index = datetime_list.index(closest_date_with_data) #get index of our "14 days ago" date

last_14_days = daily_confirmed[(fourteen_days_index - len(daily_confirmed)):]
trend = [0]
for i in range(len(last_14_days)):
	if i>0:
		trend.append(last_14_days[i] - last_14_days[i-1])

if sum(last_14_days) > 0:
	trend_color = 'red'
elif sum(last_14_days) <= 0:
	trend_color = 'green'


#calculate the simple moving average with a window size of 5
#DAILY CASES
daily_confirmed = np.array(daily_confirmed)
confirmed_moving = list(moving_average(daily_confirmed))
leading_zeroes = [0,0,0,0]
confirmed_moving = leading_zeroes + confirmed_moving
harris_data["Confirmed_Moving"] = confirmed_moving

#CUMULATIVE CASES
confirmed_data = np.array(confirmed_data)
confirmed_cum_moving = list(moving_average(confirmed_data))
confirmed_cum_moving = leading_zeroes + confirmed_cum_moving
harris_data["Confirmed_Cum_Moving"] = confirmed_cum_moving


fig, ax = plt.subplots(2, sharex=True)
ax[0].bar(datetime_list, harris_data["Daily_Confirmed"], color='papayawhip', label="Daily Confirmed Cases")
ax[0].plot(datetime_list, harris_data["Confirmed_Moving"], '-', color='darkorange', label="5-day moving average")
ax[0].axvspan(closest_date_with_data, datetime_list[-1], alpha=0.25, color=trend_color)
ax[1].bar(datetime_list, harris_data["Confirmed"], color='lightblue', label="Cumulative Confirmed Cases")
ax[1].plot(datetime_list, harris_data["Confirmed_Cum_Moving"], '-', color='darkblue', label="5-day moving average")
fig.autofmt_xdate()
ax[1].fmt_xdata = mdates.DateFormatter('%m-%d-%Y')
ax[1].xaxis.set_major_locator(mdates.AutoDateLocator())
ax[0].legend()
ax[1].legend()
plt.show()
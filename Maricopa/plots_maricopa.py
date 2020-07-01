import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates
from mpld3 import plugins, utils
from datetime import datetime, timedelta
import custom_plugins as mplm
from scipy.stats import linregress

#define function to calculate a 5-day moving average
def moving_average(a, n=5) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

#Pull in the data created by get_data.py
maricopa_data = pd.read_excel("Maricopa_Data.xlsx")
maricopa_data["Date"] = maricopa_data["Date"].astype('datetime64[ns]')

#Calculate daily totals instead of cumulative
confirmed_data = maricopa_data["Confirmed"].tolist()
daily_confirmed = [0]
for i in range(len(confirmed_data)):
	if i==8:
		daily_confirmed.append(0)
	elif i>0:
		daily_confirmed.append(confirmed_data[i]-confirmed_data[i-1])
maricopa_data["Daily_Confirmed"] = daily_confirmed

#Calculate whether negative or postive trend in last 14 days
date_list = maricopa_data["Date"].tolist()

datetime_list = [] #convert dates from pandas timestamp to python datetimes
for date in date_list:
	datetime_list.append(date.to_pydatetime())

most_recent_date = datetime_list[-1]
fourteen_days_ago = most_recent_date - timedelta(days=14) #get date 14 days before most recent date in date list
closest_date_with_data = min(datetime_list, key=lambda d: abs(d - fourteen_days_ago)) #get date in list of dates that is closest to our 14 days ago datetime

fourteen_days_index = datetime_list.index(closest_date_with_data) #get index of our "14 days ago" date

last_14_days = daily_confirmed[(fourteen_days_index - len(daily_confirmed)):]
last_14_days_datetimes = datetime_list[(fourteen_days_index - len(daily_confirmed)):]
trend = [0]
for i in range(len(last_14_days)):
	if i>0:
		if last_14_days[i] == 0:
			pass
		else:
			trend.append(last_14_days[i] - last_14_days[i-1])

x_vals = [i for i in range(len(last_14_days))]
slope, intercept, r_value, p_value, std_err = linregress(x_vals, last_14_days)

if slope > 0:
	trend_color = '#faafaf'
elif slope <= 0:
	trend_color = '#affaaf'


#calculate the simple moving average with a window size of 5
#DAILY CASES
daily_confirmed = np.array(daily_confirmed)
confirmed_moving = list(moving_average(daily_confirmed))
leading_zeroes = [0,0,0,0]
confirmed_moving = leading_zeroes + confirmed_moving
maricopa_data["Confirmed_Moving"] = confirmed_moving

#CUMULATIVE CASES
confirmed_data = np.array(confirmed_data)
confirmed_cum_moving = list(moving_average(confirmed_data))
confirmed_cum_moving = leading_zeroes + confirmed_cum_moving
maricopa_data["Confirmed_Cum_Moving"] = confirmed_cum_moving

#DO SOME EPLOTTING
fig, ax = plt.subplots(2, figsize=(10,10))
barpoints = ax[0].bar(datetime_list, maricopa_data["Daily_Confirmed"], color='papayawhip', label="Daily Confirmed Cases")
trend_barpoints = ax[0].bar(last_14_days_datetimes, last_14_days, color=trend_color, label="Last 14 Days")
confirmed_line = ax[0].plot(datetime_list, maricopa_data["Confirmed_Moving"], '-', linewidth=3, color='darkorange', label="5-day moving average")
ax[0].axvspan(closest_date_with_data, datetime_list[-1], alpha=0.25, color=trend_color)
cum_barpoints = ax[1].bar(datetime_list, maricopa_data["Confirmed"], color='lightblue', label="Cumulative Confirmed Cases")
ax[1].plot(datetime_list, maricopa_data["Confirmed_Cum_Moving"], '-', linewidth=3, color='darkblue', label="5-day moving average")
fig.autofmt_xdate()
ax[1].fmt_xdata = mdates.DateFormatter('%m-%d-%Y')
ax[1].xaxis.set_major_locator(mdates.AutoDateLocator())
ax[1].set_xlabel('Date')
ax[0].set_ylabel('Daily Confirmed Cases')
ax[1].set_ylabel('Cumulative Confirmed Cases')
ax[0].set_title('COVID-19 Cases in Maricopa County, AZ')
ax[0].legend()
ax[1].legend()

#MAKE LABELS FOR PLOTTED VALUES
daily_bar_labels = []
cum_bar_labels = []
for i in range(len(daily_confirmed)):
	daily_bar_labels.append(datetime_list[i].strftime('%m-%d-%Y') + ": " + str(daily_confirmed[i]))
	cum_bar_labels.append(datetime_list[i].strftime('%m-%d-%Y') + ": " + str(confirmed_data[i]))

last_14_bar_labels = []
for i in range(len(last_14_days)):
	last_14_bar_labels.append(last_14_days_datetimes[i].strftime('%m-%d-%Y') + ": " + str(last_14_days[i]))


mpld3.plugins.connect(fig, mplm.MousePositionDatePlugin())
mpld3.plugins.connect(fig, mplm.BarLabelToolTip([utils.get_id(bar) for bar in barpoints], daily_bar_labels))
mpld3.plugins.connect(fig, mplm.BarLabelToolTip([utils.get_id(bar) for bar in trend_barpoints], last_14_bar_labels))
mpld3.plugins.connect(fig, mplm.BarLabelToolTip([utils.get_id(bar) for bar in cum_barpoints], cum_bar_labels))
mpld3.save_html(fig, "uploads/core/templates/core/plotmaricopa.html")

#mpld3.show()








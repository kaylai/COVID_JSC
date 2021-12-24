import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates
from mpld3 import plugins, utils
from datetime import datetime, timedelta
import custom_plugins as mplm

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
	if i>0:
		daily_confirmed.append(confirmed_data[i]-confirmed_data[i-1])
harris_data["Daily_Confirmed"] = daily_confirmed

# determine outliers
q_low = harris_data["Daily_Confirmed"].quantile(0.01)
q_hi  = harris_data["Daily_Confirmed"].quantile(0.99)
df_filtered = harris_data[(harris_data["Daily_Confirmed"] < q_hi) & (harris_data["Daily_Confirmed"] > q_low)]

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
last_14_days_datetimes = datetime_list[(fourteen_days_index - len(daily_confirmed)):]
trend = [0]
for i in range(len(last_14_days)):
	if i>0:
		trend.append(last_14_days[i] - last_14_days[i-1])

if sum(last_14_days) > 0:
	trend_color = '#faafaf'
elif sum(last_14_days) <= 0:
	trend_color = 'mediumseagreen'


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

#DO SOME EPLOTTING
fig, ax = plt.subplots(2, figsize=(10,10))
barpoints = ax[0].bar(datetime_list, harris_data["Daily_Confirmed"], color='papayawhip', label="Daily Confirmed Cases")
trend_barpoints = ax[0].bar(last_14_days_datetimes, last_14_days, color=trend_color, label="Last 14 Days")
confirmed_line = ax[0].plot(datetime_list, harris_data["Confirmed_Moving"], '-', linewidth=3, color='darkorange', label="5-day moving average")
ax[0].axvspan(closest_date_with_data, datetime_list[-1], alpha=0.25, color=trend_color)
cum_barpoints = ax[1].bar(datetime_list, harris_data["Confirmed"], color='lightblue', label="Cumulative Confirmed Cases")
ax[1].plot(datetime_list, harris_data["Confirmed_Cum_Moving"], '-', linewidth=3, color='darkblue', label="5-day moving average")
fig.autofmt_xdate()
ax[1].fmt_xdata = mdates.DateFormatter('%m-%d-%Y')
ax[1].xaxis.set_major_locator(mdates.AutoDateLocator())
# use filtered dataset to get y max (no outliers)
if df_filtered.Daily_Confirmed.max() > harris_data.Confirmed_Moving.max():
	my_y_max = df_filtered.Daily_Confirmed.max()
else:
	my_y_max = harris_data.Confirmed_Moving.max() + 100
ax[0].set_ylim(0,my_y_max)
ax[1].set_xlabel('Date')
ax[0].set_ylabel('Daily Confirmed Cases')
ax[1].set_ylabel('Cumulative Confirmed Cases')
ax[0].set_title('COVID-19 Cases in Harris County, TX')
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
mpld3.save_html(fig, "./uploads/core/templates/core/plotfile.html")

#mpld3.show()








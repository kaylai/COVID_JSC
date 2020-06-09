COVID_JSC
=========

A couple of quick scripts to plot up COVID-19 data in Harris County, Texas.

These plots are designed to emulate some of the data being used by Johnson Space Center to determine when more employees can return to work onsite. Two plots are generated: Daily confirmed cases and Cumulative confirmed cases. In both plots, bars represent daily values and lines represent a 5-day moving average. In the Daily confirmed cases plot, a red or green shaded box covering the previous 14 days of data indicates whether the trend of daily cases is positive (red) or negative (green).

Eventually, these plots will be generated daily and pushed to a website.

Data Source
-----------
All data used here are from the Johns Hopkins Whiting School of Engineering Center for Systems Science and Engineering. https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
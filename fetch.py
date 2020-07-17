#!/usr/bin/env python

"""
This is our chron job file. This is what needs to auto-run to
create new plots each day. 
"""
from datetime import datetime
todays_date = datetime.today().strftime('%m-%d-%Y %H:%M:%S')
print(todays_date)

#import harris modules
print("Harris Co., TX")
import get_data
import plots

#import maricopa modules
import sys
sys.path.append('Maricopa/')
print("Maricopa Co., AZ")
import get_data_maricopa
import plots_maricopa

#import utah modules
sys.path.append('Utah/')
print("Utah Co., UT")
import get_data_utah
import plots_utah

#import salt_lake modules
sys.path.append('Salt_Lake/')
print("Salt Lake Co., UT")
import get_data_salt_lake
import plots_salt_lake

#import san_diego modules
sys.path.append('San_Diego/')
print("San Diego Co., CA")
import get_data_san_diego
import plots_san_diego

#import clark modules
sys.path.append('Clark/')
print("Clark Co., NV")
import get_data_clark
import plots_clark

#import travis modules
sys.path.append('Travis/')
print("Travis Co., TX")
import get_data_travis
import plots_travis

#import westchester modules
sys.path.append('Westchester/')
print("Westchester Co., NY")
import get_data_westchester
import plots_westchester

#import los_angeles modules
sys.path.append('Los_Angeles/')
print("Los Angeles Co., CA")
import get_data_los_angeles
import plots_los_angeles

#import miamidade modules
sys.path.append('MiamiDade/')
print("Miami-Dade Co., FL")
import get_data_miamidade
import plots_miamidade

#import per capita modeul
import percapita


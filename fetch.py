#!/usr/bin/env python

"""
This is our chron job file. This is what needs to auto-run to
create new plots each day. 
"""

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


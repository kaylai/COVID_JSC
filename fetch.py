#!/usr/bin/env python

"""
This is our chron job file. This is what needs to auto-run to
create new plots each day. 
"""

#import harris modules
import get_data
import plots

#import maricopa modules
import sys
sys.path.append('Maricopa/')
import get_data_maricopa
import plots_maricopa


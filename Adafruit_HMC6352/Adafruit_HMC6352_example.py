#!/usr/bin/python

import time
from Adafruit_HMC6352 import HMC6352

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the HMC6352
hmc = HMC6352()

heading = hmc.readData()
print "Compass Heading: %.1f" % heading

time.sleep(0.1)

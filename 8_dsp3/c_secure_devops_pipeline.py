'Secure Devops Pipeline'

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from sejam_python_bootcamp import config
from dsp3.models.manager import Manager

dsm = Manager(username=config.DSAS_USER, password=config.DSAS_PASSWORD, tenant=config.DSAS_TENANT)


# Step 1: Initiate ansible development pipeline: 
	# Opens App Control maintenance window
	# pull git repo to server
	# shuts down exisiting docker container
	# rebuilds new container
	# closes app control maintenance window.


# Step 2: Use DSP3 to put Fernando's Donuts webserver in detect only mode.
#dsm.security_profile_assign_to_host(6122, 33603)

# Step 3: lauch sql injection attacks against fernando donuts then run

#dsm.host_getevents_now([33603]) 
#events = dsm.dpi_event_retreive(host_id=33603)['DPIEvents']['item']
#print(events[0])

# Step 4: use DSP3 to put Fernando's Donuts webserver in prevent mode.
#dsm.security_profile_assign_to_host(6123, 33603)

# Step 5: lauch sql injection attacks against fernando donuts then run

#events = dsm.dpi_event_retreive(host_id=33603)['DPIEvents']['item']
#print(events[1])


dsm.end_session()

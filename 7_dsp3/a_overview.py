'Deep Security Python 3 SDK -> DSP3'

'''
Goals
* To provide a simple to use interface written in Python 3 that provides and abstraction layer over
  both the DS REST and SOAP API calls
* Simple to use for folks with litte or now programmig experience

Installation
pip install -i https://testpypi.python.org/pypi dsp3
'''
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))


from python_bootcamp import config
from dsp3.models.manager import Manager       #step one import base Manager class

dsm = Manager(username=config.DSAS_USER, password=config.DSAS_PASSWORD, tenant=config.DSAS_TENANT)

#lets check the api version
print(dsm.get_api_version())


#lets get Malware events over last 24 hours
events = dsm.antimalware_event_retreive(time_type="LAST_7_DAYS")

if events['antiMalwareEvents']:
	for event in events['antiMalwareEvents'][0]:
		print('Malware name:', event['malwareName'])    



#make sure to end connections as they are limited.	
dsm.end_session()

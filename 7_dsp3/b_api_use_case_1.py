'DS API Use Case 1: Add 300 AWS accounts in DS'

'''
path: /rest/cloudaccounts/aws      methods=[POST]

Adds a new AWS cloud account into Deep Security

Input:
AddAwsAccountRequest - AddAwsAccountRequest object describing the Amazon account.

Output:
AddAwsAccountResponse - A response with status 200 OK and a body containing AddAwsAccountResponse object when addition was successful If there is an authentication issue with the session cookie it will return a 403 Forbidden If there is a permission issue with the give AWS credentials, or the account has already been imported it will return a 400 Bad Request If there is an error adding the account it will return a 500 Internal Server Error

Cookie parameters:
sID - a session ID returned by the Authentication API.

Produces:
application/json

Consumes:
application/json



Name: AddAwsAccountRequest
Request object for the AWS Account API.

JSON Example:
{"AddAwsAccountRequest":
 {
   "awsCredentials": awsCredentials,
   "crossAccountRole": crossAccountRole,
   "seedRegion": String,
   "useInstanceRole": Boolean,
 }
}



Name: awsCredentials
Credentials object
{"awsCredentials":
 {
   "accessKeyId": String,
   "secretKey": String,
 }
}


Name: crossAccountRole
Cross Account Role object

JSON Example:
{"crossAccountRole":
 {
   "externalId": String,
   "roleArn": String,
 }
}


'''
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from python_bootcamp import config

from dsp3.models.manager import Manager

dsm = Manager(username=config.DSAS_USER, password=config.DSAS_PASSWORD, tenant=config.DSAS_TENANT)
#print(dsm.add_aws_cloud_account_with_keys('access_key', 'secret_key'))

# or
print(dsm.get_api_version())

# How to set up cross account role - https://help.deepsecurity.trendmicro.com/Add-Computers/add-aws.html
print( dsm.add_aws_cloud_account_with_cross_account_role(config.EXTERNAL_ID, config.ARN)) 
# View DSPS Implentation -> https://github.com/jeffthorne/DSP3/blob/master/dsp3/utilities/cloudacct_utils.py


dsm.end_session()			# don' forget to end sessions. They can run out!






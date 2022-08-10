from venv import create
import requests
import json
import urllib3

def createSession():
    uri = 'https://102.164.112.135/api/session'
    sessionRequest = requests.post(uri,verify=False, auth=('stage@vsphere.local', 'djZ82L-28+qZKJJ'))
    return(str(sessionRequest.text).strip('\"'))


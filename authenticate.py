from venv import create
import requests
import json
import urllib3

def createSession():
    uri = 'https://102.165.112.135/api/session'
    sessionRequest = requests.post(uri,verify=False, auth=('xd@vsphere.local', 'password'))
    return(str(sessionRequest.text).strip('\"'))


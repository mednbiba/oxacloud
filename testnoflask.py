from venv import create
import requests
import json
import urllib3






#Create Session
def createSession():
    uri = 'https://102.164.112.135/api/session'
    sessionRequest = requests.post(uri,verify=False, auth=('stage@vsphere.local', 'djZ82L-28+qZKJJ'))
    return(str(sessionRequest.text).strip('\"'))

sessionID=createSession()
#Get Hosts   
def getHosts(sessionID):
    urihosts='https://102.164.112.135/api/vcenter/host/'
    headers = {'vmware-api-session-id': ''+sessionID+''}
    hosts = requests.get(urihosts,verify=False,headers=headers)
    hostArray=json.loads(hosts.content)
    status = hosts.status_code
    print(status)
    return hostArray


#Get VMs
def getVMs(sessionID):
    urivms='https://102.164.112.135/api/vcenter/vm'
    headers = {'vmware-api-session-id': ''+sessionID+''}
    hosts = requests.get(urivms,verify=False,headers=headers).content
    vmArray=json.loads(hosts)
    return vmArray


#Create VM Function Basic
#TO-DO :
#Change function to parse JSON file as a parameter
#Modify API Call in Flask Server
def createVM(sessionID,NameVM):
    uricreatevm='https://102.164.112.135/api/vcenter/vm'
    headers = {'vmware-api-session-id': ''+sessionID+''}
    json_data = {
    'cpu': {
        'cores_per_socket': 1,
        'count': 1,
        'hot_add_enabled': False,
        'hot_remove_enabled': False,
    },
    
    'guest_OS': 'DOS',
    'memory': {
        'hot_add_enabled': False,
        'size_MiB': 500,
    },


    'name': NameVM,

    
    'placement': {
        'host': 'host-1008',
        'datastore': 'datastore-1009',
        'folder': 'group-v1002',

    },

                    }
    response = requests.post('https://102.164.112.135/api/vcenter/vm', headers=headers, json=json_data,verify=False).content
    vmcreate=json.loads(response)
    return vmcreate

#Delete VM Function
#Takes NameVM = VM ID i.e : "vm-1046"
def deleteVM(sessionID,NameVM):
    uridelete='https://102.164.112.135/api/vcenter/vm/'+NameVM
    headers = {'vmware-api-session-id': ''+sessionID+''}
    delete = requests.delete(uridelete,verify=False,headers=headers).content
    print(delete)

print(getHosts(sessionID))









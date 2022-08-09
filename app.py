import requests
import json
import urllib3
from flask import Flask,jsonify,redirect, url_for, request
#TO-DO : Separate modules & functions
#

sessionID='7b1652d0cb161c9d54d9a1ea80a9c5cd'



#sessionRequest = requests.post(uri,verify=False, auth=('', ''))
#print(sessionRequest.content)


#Get Hosts   
def getHosts(sessionID):
    urihosts='https://102.164.112.135/api/vcenter/host/'
    headers = {'vmware-api-session-id': ''+sessionID+''}
    hosts = requests.get(urihosts,verify=False,headers=headers).content
    hostArray=json.loads(hosts)
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

#how to run flask application/api:
#>pip install Flask
#>flask run


app = Flask(__name__)
#Lists VMS : GET request ==>http://127.0.0.1:5000/vm
@app.route('/vms', methods = ['GET'])
def vms():
    return jsonify(getVMs(sessionID))

#Lists Hosts : GET request ==>http://127.0.0.1:5000/vm
@app.route('/hosts', methods = ['GET'])
def hosts():
    return jsonify(getHosts(sessionID))

#CREATE VM : POST 
#Add query parameter in request url i.e : http://127.0.0.1:5000/vm?Name=Testing
@app.route('/vm', methods = ['POST'])
def vm():
    name=request.args.get('Name')
    return jsonify(createVM(sessionID,name))
#DELETE VM : DELETE
#Add query parameter in request url i.e : http://127.0.0.1:5000/delete?ID=Testing
@app.route('/delete', methods = ['DELETE'])
def delete():
    name=request.args.get('ID')
    return jsonify(deleteVM(sessionID,name))










import requests
import json
import urllib3
from flask import Flask,jsonify,redirect, url_for, request
import os
import dotenv 
#TO-DO : Separate modules & functions


#.env config
requests.packages.urllib3.disable_warnings()


#Create Session
def authenticate():
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file,override=True)
    uri = 'https://102.164.112.135/api/session'
    user = os.environ["VCENTER_USER"]
    password = os.environ["VCENTER_PASS"]
    sessionRequest = requests.post(uri,verify=False, auth=(user, password))
    id = str(sessionRequest.text).strip('\"')
    os.environ["VCENTER_CURRENT_SESSION"] = id
    dotenv.set_key(dotenv_file, "VCENTER_CURRENT_SESSION", os.environ["VCENTER_CURRENT_SESSION"])
    return(id)



def execute_getquery(uri,headers):
    query = requests.get(uri,verify=False,headers=headers)
    querycontent=json.loads(query.content)
    return querycontent

def get_statuscode_test(APIKEY):
    uritest='https://102.164.112.135/api/vcenter/host/'
    headers = {'vmware-api-session-id': ''+APIKEY+''}
    query = requests.get(uritest,verify=False,headers=headers)
    querycode=query.status_code
    return querycode


#Get Hosts   
def getHosts(APIKEY):
    urihosts='https://102.164.112.135/api/vcenter/host/'
    headers = {'vmware-api-session-id': ''+APIKEY+''}
    return(execute_getquery(urihosts,headers))
    


#Get VMs
def getVMs(APIKEY):
    urivms='https://102.164.112.135/api/vcenter/vm'
    headers = {'vmware-api-session-id': ''+APIKEY+''}
    return(execute_getquery(urivms,headers))


#Create VM Function Basic
#TO-DO :
#Change function to parse JSON file as a parameter
#Modify API Call in Flask Server
def createVM(APIKEY,NameVM):
    uricreatevm='https://102.164.112.135/api/vcenter/vm'
    headers = {'vmware-api-session-id': ''+APIKEY+''}
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
    response = requests.post(uricreatevm, headers=headers, json=json_data,verify=False)
    vmcreate=json.loads(response.content)
    return vmcreate

#Delete VM Function
#Takes NameVM = VM ID i.e : "vm-1046"
def deleteVM(APIKEY,NameVM):
    uridelete='https://102.164.112.135/api/vcenter/vm/'+NameVM
    headers = {'vmware-api-session-id': ''+APIKEY+''}
    delete = requests.delete(uridelete,verify=False,headers=headers)
    print(delete.content)
    return(delete.status_code)

def generate_token(old_token):
    #Clean up old token, Unecessary for now, token deletion is automatic upon creation of new token
    #uridelete='https://102.164.112.135/api/session'
    #headers = {'vmware-api-session-id': ''+old_token+''}
    #delete = requests.delete(uridelete,verify=False,headers=headers)
    #print(delete.status_code)
    authenticate()

#how to run flask application/api:
#>pip install Flask
#>flask run

#Initial Authentication
session=authenticate()
#print(getVM(os.environ['VCENTER_CURRENT_SESSION']))
app = Flask(__name__)
#Lists VMS : GET request ==>http://127.0.0.1:5000/vm
@app.route('/vms', methods = ['GET'])
def vms():
    #print(get_statuscode_test(sessionID))
    #print(sessionID)
    if(get_statuscode_test(os.environ['VCENTER_CURRENT_SESSION'])==401):
        print ("InvalidORExpired Session Token, Generating New Token")
        generate_token(os.environ['VCENTER_CURRENT_SESSION'])
        return jsonify(getVMs(os.environ['VCENTER_CURRENT_SESSION']))
    else:
        return jsonify(getVMs(os.environ['VCENTER_CURRENT_SESSION']))

#Lists Hosts : GET request ==>http://127.0.0.1:5000/vm
@app.route('/hosts', methods = ['GET'])
def hosts():
    return jsonify(getHosts(os.environ['VCENTER_CURRENT_SESSION']))

#CREATE VM : POST 
#Add query parameter in request url i.e : http://127.0.0.1:5000/vm?Name=Testing
@app.route('/vm', methods = ['POST'])
def vm():
    name=request.args.get('Name')
    return jsonify(createVM(os.environ['VCENTER_CURRENT_SESSION'],name))
#DELETE VM : DELETE
#Add query parameter in request url i.e : http://127.0.0.1:5000/delete?ID=Testing
@app.route('/delete', methods = ['DELETE'])
def delete():
    name=request.args.get('ID')
    return jsonify(deleteVM(os.environ['VCENTER_CURRENT_SESSION'],name))










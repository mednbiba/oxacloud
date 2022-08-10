import os
import dotenv 

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

print(os.environ["VCENTER_USER"])
print(os.environ["VCENTER_CURRENT_SESSION"])  # outputs "value"
os.environ["VCENTER_CURRENT_SESSION"] = 'test'
print(os.environ['VCENTER_CURRENT_SESSION'])  # outputs 'newvalue'

# Write changes to .env file.
dotenv.set_key(dotenv_file, "VCENTER_CURRENT_SESSION", os.environ["VCENTER_CURRENT_SESSION"])
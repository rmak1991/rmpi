import requests
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
response = requests.get("https://holidays.abstractapi.com/v1/?api_key=2a131c942c514b05963593cd93d4a7ce&country=US&year=2020&month=12&day=25")
print(response.status_code)
print(response.content)

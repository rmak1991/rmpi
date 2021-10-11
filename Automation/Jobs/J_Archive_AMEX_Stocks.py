
# importing the requests library
import requests,json,sys,os
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
import Lib.T_FileHandler as fw
import Lib.T_DateTime as dt
from Lib.T_Global import PATHS as _P

def archive_amex_stocks():
    if fw.FILE_EXISTS_PATTERN(_P.DATA_PATH,starts_with="amex_stocks_"):  
        FILENAME = fw.FILE_NAME_PATTERN(_P.DATA_PATH,starts_with="amex_stocks_")
        FILEPATH = _P.DATA_PATH
        ARCHIVEPATH =_P.DATA_ARCHIVE_PATH
        fw.FILE_ARCHIVE(FILEPATH,ARCHIVEPATH,FILENAME)
archive_amex_stocks()

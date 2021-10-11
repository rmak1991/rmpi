#!/usr/bin/python
from pathlib import Path
import os, sys,shutil
CHANGE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(CHANGE_PATH)
from Lib.T_Global import PATHS as _P
from Lib.T_Logs import LOG as l
SCRIPT = __file__.split(".")[0]
def FILE_READ(filename,path):
    '''returns all he data in a file'''
    l(SCRIPT,FILE_READ.__name__,"function called")
    _PATH= path+"/"+filename
    l(SCRIPT,FILE_READ.__name__,"PATH :"+str(_PATH))
    _FILE = Path(_PATH)
    _FILE_CONTENTS= open(_FILE, "r")
    CONTENTS = _FILE_CONTENTS.read()
    l(SCRIPT,FILE_READ.__name__,"Read contents: "+str(CONTENTS))
    return CONTENTS

def FILE_WRITE_OVERWRITE(filename,path,data):
    '''creates a file if not exist and overwrites it's contents'''
    l(SCRIPT,FILE_WRITE_OVERWRITE.__name__,"function called")
    _PATH= path+"/"+filename
    l(SCRIPT,FILE_WRITE_OVERWRITE.__name__,"PATH :"+str(_PATH))
    _FILE = Path(_PATH)
    _FILE_WRITE= open(_FILE, "w")
    l(SCRIPT,FILE_WRITE_OVERWRITE.__name__,"FILE_WRITE contents: "+str(data))
    _FILE_WRITE.write(str(data))
    l(SCRIPT,FILE_WRITE_OVERWRITE.__name__,"Contents was written successfully")
    _FILE_WRITE.close()
    if FILE_CONTENT_CHECK(filename,path,data):
        l(SCRIPT,FILE_WRITE_OVERWRITE.__name__,"Contents check was successful")
        return True
    else:
        l(SCRIPT,FILE_WRITE_OVERWRITE.__name__,"Contents check was unsuccessful")
        return False
def FILE_WRITE_APPEND(filename,path,data):
    '''creates a file if not exist and append data to it's contents'''
    l(SCRIPT,FILE_WRITE_APPEND.__name__,"function called")
    _PATH= path+"/"+filename
    l(SCRIPT,FILE_WRITE_APPEND.__name__,"PATH :"+str(_PATH))
    _FILE = Path(_PATH)
    _FILE_WRITE= open(_FILE, "a")
    l(SCRIPT,FILE_WRITE_APPEND.__name__,"FILE_WRITE contents: "+str(data))
    _FILE_WRITE.write(str(data))
    l(SCRIPT,FILE_WRITE_APPEND.__name__,"Contents was written successfully")
    _FILE_WRITE.close()
   
    
def FILE_EXISTS(filename,path):
    '''check if file exists'''
    l(SCRIPT,FILE_EXISTS.__name__,"function called")
    _PATH= path+"/"+filename
    l(SCRIPT,FILE_EXISTS.__name__,"PATH :"+str(_PATH))
    _FILE = Path(_PATH)
    return _FILE.is_file()
def FILE_EXISTS_PATTERN(path,**kwargs):
    '''check if file exists with pattern'''
    starts_with = kwargs.get('starts_with', "")
    ends_with = kwargs.get('ends_with', "")
    contains = kwargs.get('contains', "")
    for entry in os.scandir(path):
        if entry.name.endswith(ends_with) and entry.name.startswith(starts_with) and (contains in entry.name) and entry.is_file():
            return True
    return False;
def FILE_NAME_PATTERN(path,**kwargs):
    '''check if file exists with pattern'''
    starts_with = kwargs.get('starts_with', "")
    ends_with = kwargs.get('ends_with', "")
    contains = kwargs.get('contains', "")
    for entry in os.scandir(path):
        if entry.name.endswith(ends_with) and entry.name.startswith(starts_with) and (contains in entry.name) and entry.is_file():
            return entry.name
    return "";
def FILE_ARCHIVE(current_path,archive_path,file):
    '''archives file'''
    _PATH = current_path+"/"+file
    _NEWPATH = archive_path+"/"+file
    shutil.move(_PATH, _NEWPATH)
def FILE_CONTENT_CHECK(filename,path,content_to_check):
    '''check file contents'''
    l(SCRIPT,FILE_CONTENT_CHECK.__name__,"function called")
    l(SCRIPT,FILE_CONTENT_CHECK.__name__,"contents matched:"+str(FILE_READ(filename,path)==str(content_to_check)))
    return FILE_READ(filename,path)==str(content_to_check)
def FILE_DELETE(filename,path):
    '''Delete file'''
    l(SCRIPT,FILE_CONTENT_CHECK.__name__,"function called")
    _PATH= path+"/"+filename
    os.remove(_PATH)
def FILE_SIZE(filename,path):
    '''file size'''
    l(SCRIPT,FILE_CONTENT_CHECK.__name__,"function called")
    _PATH= path+"/"+filename
    return os.path.getsize(_PATH)
def FILES_NAME_PATTERN(path,**kwargs):
    '''check if file exists with pattern'''
    starts_with = kwargs.get('starts_with', "")
    ends_with = kwargs.get('ends_with', "")
    contains = kwargs.get('contains', "")
    filelist = []
    for entry in os.scandir(path):
        if entry.name.endswith(ends_with) and entry.name.startswith(starts_with) and (contains in entry.name) and entry.is_file():
            filelist.append(entry.name)
    return filelist;
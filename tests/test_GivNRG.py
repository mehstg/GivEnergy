import pytest, os
from GivNRG.GivNRG import GivNRG

# Get environment variables
username = os.environ.get('PYTEST_GIVNRG_USER')
password = os.environ.get('PYTEST_GIVNRG_PWD')

def test_login():
  nrg = GivNRG()
  status_code = nrg.login(username,password)
  assert status_code == 200  

def test_getPlantList():
  nrg = GivNRG()
  nrg.login(username,password)
  returned_json = nrg.getPlantList()["rows"][0]
  assert dictionaryContains(returned_json,"energyTotal")

def dictionaryContains(dictionary,search_string):
    if search_string in dictionary:
        return True
    else:
        return False
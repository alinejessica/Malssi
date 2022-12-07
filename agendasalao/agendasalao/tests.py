import requests
import pytest

urls = ['login/', 'cadastro/', 'agendamento/']


@pytest.mark.matrize("path", ['login/', 'cadastro/', 'agendamento/'])
def test_200(path):
    resp = requests.get('http://localhost:8000/'+ path)
    print (path)
    assert resp.status_code == 200







#for u in urls:
    #resp = requests.get('http://localhost:8000/'+u)
    #print ("tentativa"+u + str(resp))

#def test_1():
    #i = 1+1
    #assert i == 3
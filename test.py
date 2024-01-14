import requests
import unittest
from app import categoria

http = "http://127.0.0.1:5000"

class Test(unittest.TestCase):

    def test_conexion(self):
        response = requests.get(http)
        self.assertEqual(response.status_code, 200, "Algo salio mal")


    def test_can_get_user(self):
        response = requests.get(http + '/categorias')
        self.assertEqual(response.status_code, 200, "No trajo a los users")

    def test_can_get_user_by_id(self):
        id = 10
        nombre = 'juan'
        trabajo = 'obrero'
        
        user = {'id':id,
                'nombre': nombre,
                'trabajo': trabajo}
        
        reponse = requests.get(http + f'/categoria/{id}')
        self.assertEqual(reponse.json(), user, "No coinciden")
    

    def test_can_post_user(self):   
        nombre = 'juli'
        trabajo = 'tenista'
        
        user = {
                'nombre': nombre,
                'trabajo': trabajo}


        response = requests.post(http + '/categoria', json=user)
        self.assertEqual(response.status_code, 200, "no se agrego user")


    def test_can_update_user(self):
        id = 4
        nombre = 'actualizado test'
        trabajo = 'tester'
        
        update_user = {
                'nombre': nombre,
                'trabajo': trabajo}

        response = requests.put(http + f'/categoria/{id}', json=update_user)
        self.assertEqual(response.status_code, 200, "No se actualizo correctamente")


    def test_can_delete_user(self):
        id = 3

        response = requests.delete(http + f'/categoria/{id}')
        self.assertEqual(response.status_code, 200, "No se borro el user")

if __name__ == '__main__':
    unittest.main()



import requests

class User: #"receita de objetos"
    def list(self):
        response = requests.get("https://697b4b380e6ff62c3c5b9ac0.mockapi.io/api/v1/users")
        return response.json()

    def get(self):
        raise NotImplementedError
    
    def save(self):
        raise NotImplementedError

user = User() #instanciar uma classe, deixa de ser uma classe e passa a ser um objeto

print(user.list())

import requests

def list_users():
    response = requests.get("https://697b4b380e6ff62c3c5b9ac0.mockapi.io/api/v1/users")
    return response.json()

print(list_users())

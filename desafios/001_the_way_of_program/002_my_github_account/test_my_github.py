from my_github import my_github_username_is
import inspect
import requests

def test_not_none():
  assert my_github_username_is() is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(my_github_username_is()) == str and len(my_github_username_is()) > 3, "Esperado string com mais de 3 caracteres"

def test_parameters():
  assert len(inspect.getfullargspec(my_github_username_is).args) == 0, "Assinatura da função não poderá receber nenhum parâmetro"

def test_valid_account_my_github_username_is():
  user = my_github_username_is()
  github_user_api_url = 'https://api.github.com/users'
  response = requests.get(f'{github_user_api_url}/{user}')
  assert response.status_code == 200 and response.json()['login'] == user, "Esperado usuário github válido"

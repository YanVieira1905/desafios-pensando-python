from hello_world import hello_world
import inspect
import pytest

def test_not_none():
  assert hello_world() is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(hello_world()) == str and len(hello_world()) == 9, "Esperado string com 9 caracteres"

def test_parameters():
  assert len(inspect.getfullargspec(hello_world).args) == 0, "Assinatura da função não poderá receber nenhum parâmetro"

def test_options_hello_world():
  possible_anwsers = [
                      "Olá Mundo",
                      "Ola Mundo",
                      "olá mundo",
                      "ola mundo",
                      "OLÁ MUNDO",
                      "OLA MUNDO",
                     ]
  assert hello_world() in possible_anwsers , f"Esperado {possible_anwsers}"

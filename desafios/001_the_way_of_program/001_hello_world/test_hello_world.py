from hello_world import my_first_program
import inspect
import pytest

def test_not_none():
  assert my_first_program() is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(my_first_program()) == str and len(my_first_program()) == 9, "Esperado string com 9 caracteres"

def test_parameters():
  assert len(inspect.getfullargspec(my_first_program).args) == 0, "Assinatura da função não poderá receber nenhum parâmetro"

def test_options_my_first_program():
  possible_anwsers = [
                      "Olá Mundo",
                      "Ola Mundo",
                      "olá mundo",
                      "ola mundo",
                      "OLÁ MUNDO",
                      "OLA MUNDO",
                     ]
  assert my_first_program() in possible_anwsers , f"Esperado {possible_anwsers}"

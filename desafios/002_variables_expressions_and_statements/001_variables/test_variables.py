from variables import (
                        quoti_remai,
                        )
import inspect
import pytest

def test_not_none():
  assert quoti_remai(1, 1) is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(quoti_remai(1, 1)[0]) == int or type(quoti_remai(1, 1)[0]) == float, "Esperado valor numérico (int ou float)"
  assert type(quoti_remai(1, 1)[1]) == int or type(quoti_remai(1, 1)[1]) == float, "Esperado valor numérico (int ou float)"

def test_parameters():
  assert len(inspect.getfullargspec(quoti_remai).args) == 2, "Assinatura da função deverá receber dodois parâmetros"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (3, 1, (3, 0)),
    (2, 2, (1, 0)),
    (10, 1, (10, 0)),
    (10, 16, (0, 10)),
])
def test_quoti_remai(first_number, second_number, expected_result):
  assert quoti_remai(first_number, second_number) == expected_result, f"O quociente da divisão de {first_number} por {second_number} é {expected_result[0]} e o resto é {expected_result[1]}"

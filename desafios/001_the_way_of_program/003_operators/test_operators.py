from operators import (
                        add,
                        sub,
                        mult,
                        div,
                        expo,
                        remai,
                        quoti_remai,
                        )
import inspect
import pytest

def test_not_none():
  assert add(1, 1) is not None, "Esperado valor diferente de 'None'"
  assert sub(1, 1) is not None, "Esperado valor diferente de 'None'"
  assert mult(1, 1) is not None, "Esperado valor diferente de 'None'"
  assert div(1, 1) is not None, "Esperado valor diferente de 'None'"
  assert expo(1, 1) is not None, "Esperado valor diferente de 'None'"
  assert remai(1, 1) is not None, "Esperado valor diferente de 'None'"
  assert quoti_remai(1, 1) is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(add(1, 1)) == int or type(add(1, 1)) == float, "Esperado valor numérico (int ou float)"
  assert type(sub(1, 1)) == int or type(sub(1, 1)) == float, "Esperado valor numérico (int ou float)"
  assert type(mult(1, 1)) == int or type(mult(1, 1)) == float, "Esperado valor numérico (int ou float)"
  assert type(div(1, 1)) == int or type(div(1, 1)) == float, "Esperado valor numérico (int ou float)"
  assert type(expo(1, 1)) == int or type(expo(1, 1)) == float, "Esperado valor numérico (int ou float)"
  assert type(remai(1, 1)) == int or type(remai(1, 1)) == float, "Esperado valor numérico (int ou float)"
  assert type(quoti_remai(1, 1)[0]) == int or type(quoti_remai(1, 1)[0]) == float, "Esperado valor numérico (int ou float)"
  assert type(quoti_remai(1, 1)[1]) == int or type(quoti_remai(1, 1)[1]) == float, "Esperado valor numérico (int ou float)"

def test_parameters():
  assert len(inspect.getfullargspec(add).args) == 2, "Assinatura da função deverá receber dois parâmetros"
  assert len(inspect.getfullargspec(sub).args) == 2, "Assinatura da função deverá receber dois parâmetros"
  assert len(inspect.getfullargspec(mult).args) == 2, "Assinatura da função deverá receber dodois parâmetros"
  assert len(inspect.getfullargspec(div).args) == 2, "Assinatura da função deverá receber dois parâmetros"
  assert len(inspect.getfullargspec(expo).args) == 2, "Assinatura da função deverá receber dois parâmetros"
  assert len(inspect.getfullargspec(remai).args) == 2, "Assinatura da função deverá receber dois parâmetros"
  assert len(inspect.getfullargspec(quoti_remai).args) == 2, "Assinatura da função deverá receber dodois parâmetros"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (1, 1, 2),
    (1, 2, 3),
    (10, 1, 11),
    (10, 16, 26),
])
def test_add(first_number, second_number, expected_result):
  assert add(first_number, second_number) == expected_result, f"{first_number} + {second_number} = {expected_result}"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (1, 1, 0),
    (1, 2, -1),
    (10, 1, 9),
    (10, 16, -6),
])
def test_sub(first_number, second_number, expected_result):
  assert sub(first_number, second_number) == expected_result, f"{first_number} - {second_number} = {expected_result}"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (1, 1, 1),
    (1, 2, 2),
    (10, 1, 10),
    (10, 16, 160),
])
def test_mult(first_number, second_number, expected_result):
  assert mult(first_number, second_number) == expected_result, f"{first_number} x {second_number} = {expected_result}"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (1, 1, 1),
    (1, 2, 0.5),
    (10, 1, 10),
    (10, 16, 0.625),
])
def test_div(first_number, second_number, expected_result):
  assert div(first_number, second_number) == expected_result, f"{first_number} / {second_number} = {expected_result}"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (1, 1, 1),
    (1, 2, 1),
    (10, 1, 10),
    (10, 16, 10000000000000000),
])
def test_expo(first_number, second_number, expected_result):
  assert expo(first_number, second_number) == expected_result, f"{first_number} elevado a {second_number} = {expected_result}"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (1, 1, 0),
    (1, 2, 1),
    (10, 1, 0),
    (10, 16, 10),
])
def test_remai(first_number, second_number, expected_result):
  assert remai(first_number, second_number) == expected_result, f"Resto da divisão de {first_number} por {second_number} = {expected_result}"

@pytest.mark.parametrize("first_number, second_number, expected_result", [
    (3, 1, (3, 0)),
    (2, 2, (1, 0)),
    (10, 1, (10, 0)),
    (10, 16, (0, 10)),
])
def test_quoti_remai(first_number, second_number, expected_result):
  assert quoti_remai(first_number, second_number) == expected_result, f"O quociente da divisão de {first_number} por {second_number} é {expected_result[0]} e o resto é {expected_result[1]}"

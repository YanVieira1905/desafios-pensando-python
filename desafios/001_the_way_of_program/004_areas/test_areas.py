from areas import (
                    circle_area,
                    square_area,
                    rectangle_area,
                  )

import inspect
import pytest

def test_not_none():
  assert circle_area(1) is not None, "Esperado valor diferente de 'None'"
  assert square_area(1) is not None, "Esperado valor diferente de 'None'"
  assert rectangle_area(1, 1) is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(circle_area(1)) == float, "Esperado valor decimal (float)"
  assert type(square_area(1)) == int or type(square_area(1)) == float, "Esperado valor numérico"
  assert type(rectangle_area(1, 1)) == int or type(rectangle_area(1, 1)) == float, "Esperado valor numérico"

def test_parameters():
  assert len(inspect.getfullargspec(circle_area).args) == 1, "Assinatura da função deverá receber um parâmetros"
  assert len(inspect.getfullargspec(square_area).args) == 1, "Assinatura da função deverá receber um parâmetros"
  assert len(inspect.getfullargspec(rectangle_area).args) == 2, "Assinatura da função deverá receber dois parâmetros"

@pytest.mark.parametrize("radius, expected_result", [
    (1, 3.14),
    (2, 12.56),
    (12, 452.16),
    (16, 803.84),
])
def test_circle_area(radius, expected_result):
  assert circle_area(radius) == expected_result, f"A área de um círculo de raio {radius} é igual a {expected_result}"

@pytest.mark.parametrize("side, expected_result", [
    (1, 1),
    (2, 4),
    (3, 9),
    (9, 81),
])
def test_square_area(side, expected_result):
  assert square_area(side) == expected_result, f"A área de um quadrade de lado {side} é igual a {expected_result}"

@pytest.mark.parametrize("side, base, expected_result", [
    (1, 2, 2),
    (2, 4, 8),
    (3, 9, 27),
    (9, 5, 45),
])
def test_rectangle_area(side, base, expected_result):
  assert rectangle_area(side, base) == expected_result, f"A área de um retângulo de lado {side} e base {base} é igual a {expected_result}"

import pytest

from pytemplate.domain.models import Operands


def test_operands_initialization():
    op = Operands(3, 4)
    assert op.first_operand == 3
    assert op.second_operand == 4


def test_operands_equality():
    op1 = Operands(5, 6)
    op2 = Operands(5, 6)
    op3 = Operands(7, 8)
    assert op1 == op2
    assert op1 != op3


@pytest.mark.parametrize("first_operand, second_operand", [(1, 2), (10, 20), (-1, -2)])
def test_operands_parametrized(first_operand, second_operand):
    op = Operands(first_operand, second_operand)
    assert op.first_operand == first_operand
    assert op.second_operand == second_operand

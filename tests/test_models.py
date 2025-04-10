from pytemplate.domain.models import Operands


def test_if_operands_is_created():

    obj = Operands(12, 22)
    assert obj.first_operand == 12
    assert obj.second_operand == 22
    assert isinstance(obj, Operands)

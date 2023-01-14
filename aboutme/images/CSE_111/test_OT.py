import pytest
from OT import doing_work


def test_input():
    assert doing_work(3) == 15
    

def test_input2():
    assert doing_work(3.1)  == -1
    
pytest.main(["-v", "--tb=line", "-rN", __file__])
from ex11 import identity
from hypothesis import given, strategies as st

# Identity matrix must include only ones and zeroes
@given(st.integers(min_value=1,max_value=10))
def test_identity_1(i) :
    matrix = identity(i)
    for row in matrix:
        for element in row:
            assert element in [0,1]

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.integers(min_value=1,max_value=100))
def test_identity_2(i) :
    pass

from ex11 import identity
from hypothesis import given, strategies as st

# identity must only includes ones and zeroes
@given(st.integers(min_value=1,max_value=100))
def test_identity_1(i) :
    if i==1:
        assert identity(i) == [1]
    else:
        for row in identity(i):
            for element in row:
                assert element in [0,1]

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.integers(min_value=1,max_value=100))
def test_identity_2(i) :
    pass

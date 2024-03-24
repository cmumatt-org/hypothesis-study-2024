from ex14 import modinv
from hypothesis import given, strategies as st

# modinv must always return >= 0
@given(st.integers(min_value=0),st.integers(min_value=0))
def test_modinv_1(a: int, b: int) :
    assert modinv(a,b) >= 0

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.integers(min_value=0),st.integers(min_value=0))
def test_modinv_2(a: int, b: int) :
    pass
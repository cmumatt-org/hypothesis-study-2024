from tutorial import gcd
from hypothesis import given, strategies as st

# gcd(u,v) should equal gcd(v,u)
@given(st.integers(min_value=0,max_value=100),st.integers(min_value=0,max_value=100))
def test_gcd_1(u: int, v: int) :
    assert gcd(u,v) == gcd(v,u)
    assert gcd(u,(gcd(u,v))) == gcd(v,u)
    assert gcd(u,u) == u
    assert gcd(5*u, 5*v) == 5*gcd(u, v)

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.integers(min_value=0,max_value=100),st.integers(min_value=0,max_value=100))
def test_gcd_2(u: int, v: int) :
    pass

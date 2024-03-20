from ex12 import levenshteinDistance
from hypothesis import given, strategies as st

# levenshteinDistance must always return >= 0
@given(st.text(min_size=1),st.text())
def test_levenshteinDistance_1(s1: str, s2: str) :
    assert levenshteinDistance(s1,s2) >= 0

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.text(),st.text())
def test_levenshteinDistance_2(s1: str, s2: str) :
    pass

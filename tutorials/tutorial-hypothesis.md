# Tutorial: Hypothesis

Hypothesis is a useful tool for quickly unit testing Python programs.

## How to use Hypothesis:

1. Write a Hypothesis test:
   1. Generate inputs for the function you want to test
   2. Call the function using the generated input
   3. Validate the function's output using the `assert` statement
2. Run Hypothesis by calling `pytest` in the terminal
3. If Hypothesis finds an input where your `assert` fails, Hypothesis will show that example in the terminal output. Otherwise, it will tell you that the test passed.

We will walk through each step in the tutorial below.

## How to Read a Hypothesis test

Please examine the Hypothesis test file below:

```Python
1  from tutorial import gcd
2  from hypothesis import given, strategies as st
3
4  # gcd(u,v) should equal gcd(v,u)
5  @given(st.integers(min_value=0,max_value=100),st.integers(min_value=0,max_value=100))
6  def test_gcd_1(u: int, v: int) :
7      assert gcd(u,v) == gcd(v,u)
```

Can you find the key parts of the Hypothesis test?

* `Line 1`: Import the function to test (`gcd` from the `tutorial` package)
* `Line 2`: Import Hypothesis (here we are importing Hypothesis' `given` and `strategies`)
* `Line 5`: Use Hypothesis to generate two inputs:
   1. An integer in the range of [-100,100]
   2. Another integer in the range of [100,100]
* `Line 6`: Define our test function, which Hypothesis will call with the inputs it generated above.
* `Line 7`: Assert that ordering `gcd`'s parameters should not result in different outputs. If this assertion is not true, then Hypothesis will fail the test. Note that we are calling `gcd` twice here. 

> **Note**: It's important to note that in the above Hypothesis test, we never refer to specific inputs our outputs. This is because Hypothesis will execute the same test function over and over with a large number of inputs that Hypothesis pseudo-randomly generates. This means the `assert` should also be general and apply across all the inputs you specify that Hypothesis should generate.

## How Hypothesis works

Hypothesis generates the inputs specified on line 5 and calls the test function defined on line 6 at least once for each input that it generates. Hypothesis uses a specific strategy to generate these inputs, but you can kind of think of the inputs as being pseudo-randomly generated. 

The test function calls the function under test (here, `gcd`) and checks the `assert`ion made on line 7 about the function's output. If the assertion is true, Hypothesis considers the test `passed`. If the assertion is false, Hypothesis considers the test `failed`. 

When Hypothesis encounters a failed test, Hypothesis displays the inputs that caused the failured in the terminal and stops testing. It's important to note that Hypothesis will stop after it finds the first failure. Hypothesis calls this failing input the **falsification example**, meaning the example proves that the `assert`ion in the test is false in at least this one instance (and possibly in others).

Hypothesis can check many different complex inputs and check many different properties of a function. Hypothesis is quite powerful, and by using Hypothesis you can often avoid the tedium of writing a lot of unit tests.

## The function we are testing

The source code for `gcd` may be found in `tutorial.py` within the same `tutorials` folder. It looks like this:

```Python
def gcd(u:int, v:int):
    return gcd(v, u % v) if v else abs(u)
```

## Exercise 1

Open the `tutorial.py` file in this tutorial folder.

Open the `tutorial_test.py` file in this tutorials folder. Notice there are two test functions, but only one has an `assert` statement: you will fill in the second test later.

In your terminal:
* `cd tutorials`
* `pytest`

The test results are shown below. Remember if a test passes, Hypothesis does not provide a lot of information.

```
========================= test session starts =========================
platform darwin -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: [...]/tutorials
plugins: dash-2.8.1, anyio-4.3.0, hypothesis-6.68.2
collected 2 items                                                     

tutorial_test.py ..

========================== 2 passed in 0.24s ==========================
```

Review the results above. Did any tests fail?

> **Tip**: If Hypothesis only says `passed`, then no tests failed.

## Exercise 2

Inside `tutorial.py` on line 11, comment out the if statement such that the program look like this:

```Python
def gcd(u:int, v:int):
    return gcd(v, u % v) #if v else abs(u)
```

Save your changes to `tutorial.py`. 

Run `pytest` in the terminal. The output will look similar to the below:

```
========================= test session starts =========================
platform darwin -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: [...]/tutorials
plugins: dash-2.8.1, anyio-4.3.0, hypothesis-6.68.2
collected 2 items                                                     

tutorial_test.py F.

============================== FAILURES ===============================
_____________________________ test_gcd_1 ______________________________

    @given(st.integers(min_value=-100,max_value=100),st.integers(min_value=-100,max_value=100))
>   def test_gcd_1(u: int, v: int) :

tutorial_test.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
tutorial_test.py:7: in test_gcd_1
    assert gcd(u,v) == gcd(v,u)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

u = 0, v = 0

    def gcd(u:int, v:int):
>       return gcd(v, u % v) #if v else abs(u)
E       ZeroDivisionError: integer modulo by zero
E       Falsifying example: test_gcd_1(
E           u=0,
E           v=0,
E       )

tutorial.py:11: ZeroDivisionError
======================= short test summary info =======================
FAILED tutorial_test.py::test_gcd_1 - ZeroDivisionError: integer modulo by zero
===================== 1 failed, 1 passed in 0.26s =====================
```

Hypothesis provides a lot more information when a test fails! We can see at the top and bottom of the error report that there were failures. Let's start at the bottom of this report and work our way upwards.

### Falsification example

Can you find the falsification example near the bottom of the report?

The falsification example is the input that caused the test to fail. In the report above, calling `gcd()` with `u=0, v=0` caused the failure.

```
E       Falsifying example: test_gcd_1(
E           u=0,
E           v=0,
E       )
```

### Getting more details about the test failure

Scrolling up from the falsification example, you may see that Hypothesis provided more details about the failure. Keep in mind the information here can vary based on what the failure was. In this example, the report shows that `u % v` (with `u=0, v=0` from the above falsification example) caused a `ZeroDivisionError` that halted execution. Oops!

```
    def gcd(u:int, v:int):
>       return gcd(v, u % v) #if v else abs(u)
E       ZeroDivisionError: integer modulo by zero
```

Now revert `tutorial.py` back to its original state (remove the `#` character on line 11) and save. Run `pytest` again to make sure all tests pass.

## Exercise 3

In `tutorial_test.py` copy line 7 over line 13. There should only be one `assert` in the second test. 

Now change the `==` on line 13 to `!=`, save the file, and run `pytest`. 

Does the test pass or fail?

```
========================= test session starts =========================
platform darwin -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0
rootdir: [...]/tutorials
plugins: dash-2.8.1, anyio-4.3.0, hypothesis-6.68.2
collected 2 items                                                     

tutorial_test.py F.

============================== FAILURES ===============================
_____________________________ test_gcd_2 ______________________________

    @given(st.integers(min_value=-100,max_value=100),st.integers(min_value=-100,max_value=100))
>   def test_gcd_2(u: int, v: int) :

tutorial_test.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

u = 0, v = 0

    @given(st.integers(min_value=-100,max_value=100),st.integers(min_value=-100,max_value=100))
    def test_gcd_2(u: int, v: int) :
>       assert gcd(u,v) != gcd(v,u)
E       assert 0 != 0
E        +  where 0 = gcd(0, 0)
E        +  and   0 = gcd(0, 0)
E       Falsifying example: test_gcd_1(
E           u=0,
E           v=0,
E       )

tutorial_test.py:13: AssertionError
======================= short test summary info =======================
FAILED tutorial_test.py::test_gcd_2 - assert 0 != 0
===================== 1 failed, 1 passed in 0.25s =====================
```

Can you find the falsificarion example in the report above? What inputs caused the test to fail?

> **Tip**: Hypothesis pseudo-randomly generates inputs, so if multiple falsification examples are possible, you might see different falsifiction examples each time you run Hypothesis.

Look above the falsification example for more information about why the test failed. Can you see why the `assert`ion in the test failed since you made the change?

> **Tip**: The report shows that both calls to `gcd(u,v)` in the `assert` returned 0, which makes `assert gcd(u,v) != gcd(v,u)` fail.

## Exercise 4

An important part of using tools like Hypothesis is thinking carefully about the `assert`. Because the `assert` is checking a wide variety of pseudo-random inputs and outputs, it's helpful to creatively think about general properties of the function being tested as well as its inputs and output.

In the above example, we checked that `gcd(u,v) == gcd(v,u)`. What are some other `assert`s that should always be true of `gcd`'s inputs and outputs? 

Some ideas we could `assert` include:
* `gcd(u,gcd(u,v)) == gcd(v,u)`
* `gcd(u,v)` equals the result of a different implementation of `gcd`
* `gcd(u, u) == u`
* given positive integer `m`, `gcd(m⋅u, m⋅v) == m⋅gcd(u, v)`
* and so on...

Choose any of these, add it to one of the tests, and run `pytest` to check the property.

## Tips and tricks

**Show print statements.** Pytest by defailt does not show `print()`ed output during testing. If you want to see `print()`ed output, run `pytest -s` instead of `pytest`.

**Show all the inputs generatd.** Hypothesis by default does not show the inputs it generated for testing. If you want to see these inputs, run `pytest -s --hypothesis-verbosity=debug` instead of `pytest`.

**Narrow the inputs generated.** If you want Hypothesis to focus on a narrow range of inputs, you can use the `min_value` and `max_value` parameters when you specify the inputs Hypothesis should generate.

## Conclusion

Testing with Hypothesis is as simple as telling Hypothesis how to generate inputs, calling the function under test with those inputs, and then `assert`ing what should be true about the function's output relative to its input.

> **Tip**: When testing with Hypothesis, you can write as many test functions or asserts as you like. You can also write essentially any type of code you would like inside your test function, including `if` and `switch` statements. 

There are many advanced Hypothesis features you may explore in the documentation after this study, but what you have just learned is all you need for the tasks you will be performing today.

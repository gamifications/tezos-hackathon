import smartpy as sp

@sp.add_test(name='My First')
def test():
    scenario=sp.test_scenario()
    scenario.p('first output')

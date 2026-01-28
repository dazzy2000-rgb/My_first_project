import unittest


class TestPytestExample ():

    def test_summery(self):
        print("test_summery")
        a=2
        b=3
        assert a+b==5, "The sum of two numbers is not expected"
    def test_qu(self):
        print("test_qu")
        a=2
        b=3
        assert a*b==6, "The q of two numbers is not expected"
    def test_minus(self):
        print("test_minus")
        a=2
        b=3
        assert b-a==1, "The different of two numbers is not expected"
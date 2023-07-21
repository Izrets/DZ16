import argparse
import pytest

parser = argparse.ArgumentParser(description="Start test(s)")
parser.add_argument("-a", "--all", action="store_true", help="Start all tests in framework")
parser.add_argument("-t1", "--test1", action="store_true", help="Start test signup")
parser.add_argument("-t2", "--test2", action="store_true", help="Start test signin")

args = parser.parse_args()
if args.all:
    pytest.main(args=["-v", "test_signup_page.py", "test_signin_page.py"])
elif args.test1:
    pytest.main(args=["-v", "test_signup_page.py"])
elif args.test2:
    pytest.main(args=["-v", "test_signin_page.py"])
elif args.test3:
    pytest.main(args=["-v", "test.py::TestSignUpPage::test_3"])
elif args.test4:
    pytest.main(args=["-v", "test.py::TestSignUpPage::test_signup"])
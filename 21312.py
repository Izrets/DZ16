import argparse
import pytest

parser = argparse.ArgumentParser(description="Start test(s)")


args = parser.parse_args()

pytest.main(args=["-v", "test_signup_page.py", "test_signin_page.py"])

from modelproject.wordplay import is_palindrome
from modelproject.wordplay import mirror


class TestWordplay:
    def testMirror(self):
        assert mirror('abcd') == 'dcba'

    def testIsPalindromeOK(self):
        assert is_palindrome('kayak') is True

    def testIsPalindromeKO(self):
        assert is_palindrome('canoe') is False

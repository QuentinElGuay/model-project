from modelproject.wordplay import mirror, is_palindrome


class TestWordplay:
    def testMirror(self):
        assert mirror('abcd') == 'dcba'

    def testIsPalindromeOK(self):
        assert is_palindrome('kayak') == True

    def testIsPalindromeKO(self):
        assert is_palindrome('canoe') == False

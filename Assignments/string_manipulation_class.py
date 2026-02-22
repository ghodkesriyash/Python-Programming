# =============================================================================
# IITM BSc Degree - Python Programming
# Topic   : Object Oriented Programming - Classes & Methods
# File    : string_manipulation_class.py
# =============================================================================

# -----------------------------------------------------------------------------
# QUESTION - String Manipulation Class
#
# Create a StringManipulation class that operates on a list of lowercase strings.
#
#   __init__(self, words: list)
#       Initialise with a list of lowercase strings.
#
#   total_words(self) -> int
#       Return the total number of words in the list.
#
#   count(self, some_word: str) -> int
#       Return how many times some_word appears in the list.
#
#   words_of_length(self, length: int) -> list
#       Return all words of exactly the given length (preserving order).
#
#   words_start_with(self, char: str) -> list
#       Return all words starting with char (preserving order).
#
#   longest_word(self) -> str
#       Return the first longest word in the list (first on tie).
#
#   palindromes(self) -> list
#       Return all words that read the same forwards and backwards.
# -----------------------------------------------------------------------------


class StringManipulation:
    """A class to perform various manipulations on a list of strings."""

    def __init__(self, words: list):
        """Initialise with a list of lowercase strings."""
        self.words = words

    def total_words(self) -> int:
        """Return total number of words in the list."""
        return len(self.words)

    def count(self, some_word: str) -> int:
        """Return number of occurrences of some_word in the list."""
        return self.words.count(some_word)

    def words_of_length(self, length: int) -> list:
        """Return all words whose length equals the given length."""
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char: str) -> list:
        """Return all words that start with the given character."""
        return [word for word in self.words if word.startswith(char)]

    def longest_word(self) -> str:
        """Return the first longest word (first occurrence on tie)."""
        return max(self.words, key=len)

    def palindromes(self) -> list:
        """Return all words that are palindromes (word == reverse)."""
        return [word for word in self.words if word == word[::-1]]


# --- driver code ---
if __name__ == "__main__":
    words = input("enter words (space-separated): ").split()
    sm    = StringManipulation(words)

    print("total_words      :", sm.total_words())

    some_word = input("enter a word to count: ")
    print("count            :", sm.count(some_word))

    length = int(input("enter word length to filter: "))
    print("words_of_length  :", sm.words_of_length(length))

    char = input("enter starting character to filter: ")
    print("words_start_with :", sm.words_start_with(char))

    print("longest_word     :", sm.longest_word())
    print("palindromes      :", sm.palindromes())
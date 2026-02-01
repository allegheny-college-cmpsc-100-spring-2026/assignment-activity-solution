from WordList import List

def is_dbl(word: str = "", limit: int = 1) -> bool:
    """ 
    Return True if a word contains a given number of
    consecutively repeated word clusters, else False

    :param word: Description
    :type word: str
    :param limit: Description
    :type limit: int
    :return: Description
    :rtype: bool
    """
    # If there are no more words, bail immediately
    if not word: 
        return False
    # Setup our count for words with double letter clusters
    num_of_dbls = 0
    prev, next = None, None
    # Iterate through each word one letter at a time
    for letter in word:
        # Inch down the word letter by letter
        prev = letter
        if prev == next:
            # Add one if the previous and next letter are the same
            num_of_dbls +=1
        next = letter
    # Return the boolean outcome of our trial
    return num_of_dbls == limit

def main(words: list = []):
    """
    Driver function

    :param words: Description
    :type words: list
    """
    # While there's another word in our list of words...
    limit = int(input("Clusters to look for: "))
    while next(words, None):
        word = next(words, None)
        if is_dbl(word = word, limit = limit):
            print(word)

if __name__ == "__main__":
    main(List.load())
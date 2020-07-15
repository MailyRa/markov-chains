"""Generate Markov text from text files."""
import sys

from random import choice

#hello my name is Maily my name jon hi
#(hello, my) =  [name]
#(my, name) = [is, jon]
#(name, is) = [Maily]
#(is, Maily) = [my]
#(Maily, my) = [name]
#(my, name) = we have it as a key already then append it to the key 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text = file.read()
    file.close()


    return text 


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    #we made it a dictionary because we want to call it back but we are using 
    chains = {}

    
    #Splitting my text into a list by each word
    each_word = text_string.split()

#['Would', 'you', 'could', 'you', 'in', 'a', 'house?', 'Would', 'you', 'could', 'you', 'with', 'a',
#[''mouse?', 'Would', 'you', 'could', 'you', 'in', 'a', 'box?', 'Would', 'you', 'could', 'you',
#[''with', 'a', 'fox?', 'Would', 'you', 'like', 'green', 'eggs', 'and', 'ham?', 'Would', 'you',
#[''like', 'them,', 'Sam', 'I', 'am?']

    
    #Loop through your list and It will stop at 'Sam' (-2) since we want to look in pairs
    for i in range(len(each_word) -2):
    #key = ('Would', 'you') since we want a pair
        key = (each_word[i], each_word[i+1])
        #word = 'could' which is a string
        word = each_word[i + 2]
        #if key is not in my dictionary then:
        if key not in chains:
        #we want to append the value key thats in my dictionary ['Would', 'you'] to new list 
        #we want to create a new list everytime we dont have the key 
            chains[key] = []
            #this will add a value to key 
            # ('would', 'you') -> []

        #since the value is now a list we can append the string from variable word
        chains[key].append(word)
        #'could'
    return chains
   

def make_text(chains):
    """Return text from chains."""

    #choice = random pair 
    #chains.key() = access all my keys in my dictionary which are tuples
    #list() =turns my tuples into lists
    # ex = ['Would', 'you']
    key = choice(list(chains.keys()))
    #getting the first two indeces from my previous list
    words = [key[0], key[1]]
    

    while True:
        #We want to start with the last set of keys 
        #key = ('would, 'you') 
        key = (words[-2], words[-1])

        if key not in chains:
            break 
        #Acessing the value, randomly     
        value= choice(chains[key])

        words.append(value)
        #('would','you','like')


    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

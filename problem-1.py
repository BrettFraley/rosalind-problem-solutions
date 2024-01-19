"""
Problem

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s

of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
"""
# Note: Each time the Download dataset on Rosalind is pressed the dataset changes!
data = """
    CCCCTGACAGAATAGGGACTAGTAATCAGCTAAGAAAGGACTCGCACAGAATAGGTAACGTGACTTTGATGACTACTAGCGTAGAACGAGCCACCACTCCCCGCATAA
    TCTTCCGGAGTTACTGAGACACTGGTTCGGAGAGACCCAATTCTCCCTGGCCTGTGCTACGCAGAGCAAGCGACTGGAGATACCTCTTTGTTAATACTTACACACCAT
    CTCTTAGTGGTTTTAAATGGGAACGGAGTTCATGTCCGATGTGGGCGAAGACATGCTAATGACACACAATCAATTGCGAGAGTAACGTTCCATTCCATGCACACTAGA
    CGGTGTAAGGAACCATAGGGGTACCAGTAGATACCTCTTCCGGATGTAATATCAATCGTTCTGTTGGCGGTTGTGCAGCCCGTGGGCAGTTCCGCGCAGGAACTAACC
    CCCTAAAGCCGAAACAGGCACGCCGGGTTCGCTCGCCCATGTTTGCCCAACGTTCGAAGACATCTACCTAGAAGGAGGACTTTGGAAGTTAGCTCGAAAAGATGAATG
    CGCGTGGTCTTGAGCCAGTGACCTGTAAATTACTGTTGCCCTATGACCGGGTGAGCTTACCTCACTTAGTTTACTGGAGTTTCTACTAATACTCGTTCAAAAATTCGC
    GGGTGCTGTAACAGGACGGATTTTTTGTAAGGCCCCCTGGCGTGGTGAGTCGTTCTAGTATTTTGGGATAAGATACTGGCAGAGTAATGAACATGTATTCGACTACGA
    ATTAATCCTAGTTTTGGGCAGTGACACCAGAGGTCGTGCCCATTCTGTTGTGGCTCCAAGCCATGGCAGGAAGT
    """

# Approach using the `count` method
A, C, G, T = data.count("A"), data.count("C"), data.count("G"), data.count("T")
print(f"{A} {C} {G} {T}")

# Approach with a function `countAndPrintCharCount` that uses a loop and `count` method
# The name 'bases' is used instead of something like 'chars', because we're talking DNA base types here
bases = ["A", "C", "G", "T"]

def countAndPrintCharCount(chars, dataString):
    resultString = ""

    for char in chars:
        resultString += f"{ dataString.count(char) } "

    return resultString

test = countAndPrintCharCount(bases, data)
print(test)

# Approach using an object and property assignment. Note: normally, this should have an __init__ constructor, etc.
class charCounts:
    A
    C
    G
    T

counts = charCounts()
charCounts.A = data.count("A")

# Unrelated to this Rosalind problem is that I realized a Python class can be declared like this,
# which is weird and could potentially be useful, but don't do this!
class weirdClass: A, C, G, T

classWeirdClassTest = weirdClass()
classWeirdClassTest.A = "Weird how this is okay"
print(classWeirdClassTest.A)

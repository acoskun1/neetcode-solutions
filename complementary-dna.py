
"""
Given a DNA strand, return the complementary DNA string.

Example:
"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

"""

def DNA_strand(dna):

    pairs = {"A":"T","T":"A","G":"C","C":"G"}

    return ''.join(pairs[x] for x in dna)

if __name__ == "__main__":

    ans = DNA_strand("ATTGC")
    print(ans)

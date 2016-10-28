# Rabin karp pattern search using string hashing
#
# Hashing :
# Every alpahbet letter is given a unique number, say a=1, b=2 .... z=26
# to calculate hash of a pattern
# 1. Prepare unique value of each chars as explaied above
#    j = 10, u = 21, n = 14, k = 11, i = 9  or  simply ord(char) % 96
#
# 2. Choose a favorite prime number

#
# Eg: Suppose given a string -> ijunks
#     And search for junk pattern
#
# 1. Create hash for search pattern.
#
#   hash =  value_j * (prime ** j_index) +
#           value_u * (prime ** u_index) +
#           value_n * (prime ** n_index) +
#           value_k * (prime ** k_index)
#
#  hash = (10 * (3**0)) + (21 * (3**1)) + (14 * (3**2)) + (11 * (3**3)) = 496
#    Can be written as as 3**0 -> 1
#
#  hash = 10 + (21 * (3**1)) + (14 * (3**2)) + (11 * (3**3)) = 496
#
# 2. Next search for the hash in the given string progressively.
#   a. Calculate hash for ijun
#   b. Reuse previosuly calculated hash of ijun to calculate hash for junk
#   c. Every time when hash is calculated match against pattern's hash value.
#   d. Repeate the steps until end of string
#
# 3. How to reuse previously calculated hash to generate new hash ?
#    Eg:
#       hash for "junk" is calculated by formula
#       hash = 10 + (21 * (3**1)) + (14 * (3**2)) + (11 * (3**3)) = 496
#
#       So how to calculate hash for "unki" using "junk" pattern's hash ?
#       Remove j's hash camponent and add i's to previous hash
#
#       junk hash -> 496
#
#       j hash(remember j is at position 0) ->  10 * 3**0  or 10
#
#       incomplete hash = 496 - 10 = 486
#       divide by primenumber to remove shit powers = 486/3 = 162
#       ie to turn hash =  (14 * (3**2)) + (11 * (3**3)) = 486 to
#       (14 * (3**1)) + (11 * (3**2)) = 486 / 3 = 162
#
#       Now add i's hash component ie -> 9 * (3**3) = 243
#       (note: power is three as i is at 3rd position)
#
#       new hash = 162 + 243 = 405
#
# 4. Match newly calculated hash with pattern's hash to know substring is same
# as pattern or not.
#


inp = 'this is a bigandjununkjuuunnkkjunkkheloobigwordend iunk funk junk '
inp_length = len(inp)

pattern = 'junk'
patter_length = len(pattern)

PRIME = 3

def get_char_val(char):
    # return 1 for a, 2 for b, ....... 26 for z
    if char == ' ':
        return 27

    return ord(char) % 96

def get_nth_hash(char, char_index):
    char_value = get_char_val(char)
    return char_value * (3 ** char_index)


def get_progressive_hash(prev_hash, prev_char, char):
    semi_hash = (prev_hash - get_char_val(prev_char))/PRIME
    return semi_hash + get_nth_hash(char, patter_length-1)


def get_pattern_hash(pattern):
    # use only for initial purpose
    # Eg: To generate first time hash/ patterns's hash
    return sum([get_nth_hash(char, i) for i, char in enumerate(pattern)])


counter = patter_length
prev_pattern = inp[0: patter_length]
pattern_hash = get_pattern_hash(pattern)
prev_pattern_hash = get_pattern_hash(prev_pattern)


while counter < inp_length:
    char = inp[counter]
    curr_hash = get_progressive_hash(prev_pattern_hash, prev_pattern[0], char)
    prev_pattern = prev_pattern[1:] + char
    prev_pattern_hash = curr_hash

    counter += 1

    if curr_hash == pattern_hash:
        print "Found at: ", counter - patter_length


import re

# Sample text
text = """
abc

defabc

abc123

def

a.b

a\nb

word

sword

password

wordy

a_word

_word_

Word

word

@example

contact@domain.org

@mention

nonmention

mixed@mention

Here are some email addresses:
user1@example.com, contact@domain.org, and a username without an @ sign.

Another line: @mention, nonmention, and mixed@mention.

abb ab abbb aaa aaaa aaaaa aa a

bbb
aaab
aab
a b

(abc

ABC

AbC

1abc

xyz

pqr
"""

# 1. Using (?m)^abc: Extract all lines that start with 'abc'
lines_starting_with_abc = re.findall(r'(?m)^abc', text)
print("Lines starting with 'abc':", lines_starting_with_abc)

# 2. Using (?s)a.b: Extract all occurrences of 'a' followed by any single character (including newline), followed by 'b'
occurrences_a_b = re.findall(r'(?s)a.b', text)
print("Occurrences of 'a' followed by any single character and 'b':", occurrences_a_b)

# 3. Using \bword\b: Extract all occurrences of the whole word 'word'
whole_word_occurrences = re.findall(r'\bword\b', text)
print("Occurrences of the whole word 'word':", whole_word_occurrences)

# 4. Using \Bword\B: Extract all occurrences of 'word' when it is part of a larger word
part_of_larger_word = re.findall(r'\Bword\B', text)
print("Occurrences of 'word' as part of a larger word:", part_of_larger_word)

# 5. Using (?<=@)\w+: Extract all sequences of word characters that are immediately preceded by an @
sequences_after_at = re.findall(r'(?<=@)\w+', text)
print("Sequences of word characters immediately preceded by '@':", sequences_after_at)

# 6. Using (?<!@)\w+: Extract all sequences of word characters that are not immediately preceded by an @
sequences_not_after_at = re.findall(r'(?<!@)\w+', text)
print("Sequences of word characters not immediately preceded by '@':", sequences_not_after_at)

# 7. Using a?b: Extract all matches of the pattern a?b
matches_a_b = re.findall(r'a?b', text)
print("Matches of the pattern 'a?b':", matches_a_b)

# 8. Using a{3}: Extract all matches of the pattern a{3}
matches_a3 = re.findall(r'a{3}', text)
print("Matches of the pattern 'a{3}':", matches_a3)

# 9. Using a{2,4}: Extract all matches of the pattern a{2,4}
matches_a2_4 = re.findall(r'a{2,4}', text)
print("Matches of the pattern 'a{2,4}':", matches_a2_4)

# 10. Using [abc]: Extract all single characters that are either 'a', 'b', or 'c'
characters_abc = re.findall(r'[abc]', text)
print("Single characters 'a', 'b', or 'c':", characters_abc)

# 11. Using [^abc]: Extract all single characters that are not 'a', 'b', or 'c'
characters_not_abc = re.findall(r'[^abc]', text)
print("Single characters not 'a', 'b', or 'c':", characters_not_abc)

# 12. Using \(abc: Extract all occurrences of the literal string (abc
literal_string = re.findall(r'\(abc', text)
print("Occurrences of the literal string '(abc':", literal_string)

# 13. Using (?i)abc: Extract all occurrences of the string 'abc' in a case-insensitive manner
case_insensitive_abc = re.findall(r'(?i)abc', text)
print("Occurrences of 'abc' in a case-insensitive manner:", case_insensitive_abc)

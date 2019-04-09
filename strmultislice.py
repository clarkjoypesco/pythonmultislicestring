# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:2]
print substring1
substring2 = sentence[6:30]
print substring2
substring3 = sentence[34:]
print substring3

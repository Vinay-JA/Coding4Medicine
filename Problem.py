#Write a Python function to sort a list of nucleotide sequences based on their lengths. When two sequences have the same length, sort them alphabetically.

# Note: For this specific question, you cannot use built-in functions in Python apart from “len” and “range”.
# Example
# Input:
#l2= ["ATGGCCGTGG", "ATGG", "TACC", "AATTGG", "A", "GCTGGGGG", "ATCG"]
# Output:
#["A", "ATCG", "ATGG", "TACC",  "AATTGG", "GCTGGGGG", "ATGGCCGTGG"]

l2= ["ATGGCCGTGG", "ATGG", "TACC", "AATTGG", "A", "GCTGGGGG", "ATCG"]
def nucleotide_Sequence(seq):
    n = len(seq)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(seq[j])>len(seq[j+1]):
                seq[j],seq[j+1]=seq[j+1],seq[j]
            elif len(seq[j]) == len(seq[j+1]) and seq[j]>seq[j+1]:
                seq[j],seq[j+1]=seq[j+1],seq[j]
    return seq
result = nucleotide_Sequence(l2)
print("Sorted List is:", result)
"""


A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

The answers to these M = 3 queries are as follows:

        The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 respectively, so the answer is 2.
        The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
        The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

    def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:
    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6

the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        M is an integer within the range [1..50,000];
        each element of arrays P, Q is an integer within the range [0..N − 1];
        P[K] ≤ Q[K], where 0 ≤ K < M;
        string S consists only of upper-case English letters A, C, G, T.

"""

# 100
def solution(S, P, Q):
    # write your code in Python 3.6

    # dobra smieszki, plan jest prosty - temat to prefix sums wiec trzeba je wykorzystac

    # 1) Zrobić 3 prefix sumsy zliczajace wystepowanie danego nukleotydu w danym zakresie, czwarty - T, bedzie wypadkowy
    # jakos tak to bylo z wymiarem tego ...
    prefs_A = [0] * (len(S) + 1)
    prefs_C = [0] * (len(S) + 1)
    prefs_G = [0] * (len(S) + 1)
    # teraz czeba zrobic tego summ -> chyba suma w p[1] to p[0] + s[0]?!?! :(
    # no to siup
    for i in range(1, len(S) + 1):
        prefs_A[i] = prefs_A[i - 1] + ((dejNukleo(S[i - 1]) % 4) % 3) % 2
        prefs_C[i] = prefs_C[i - 1] + ((dejNukleo(S[i - 1]) % 4) % 3) // 2
        prefs_G[i] = prefs_G[i - 1] + (dejNukleo(S[i - 1]) % 4) // 3

    # resulty
    results = [0] * len(P)
    # kolejna petelka bedzie dla kolegow P i Q, wiec zlozonosc bedzie O(N + M), a P i Q takie same wiec po dlugosci P
    for i in range(len(P)):
        # literka A
        if prefs_A[Q[i] + 1] - prefs_A[P[i]] > 0:
            results[i] = 1
        # literka C
        elif prefs_C[Q[i] + 1] - prefs_C[P[i]] > 0:
            results[i] = 2
        # literka G
        elif prefs_G[Q[i] + 1] - prefs_G[P[i]] > 0:
            results[i] = 3
        # literka T jak TOK
        else:
            results[i] = 4

    return results


# dodatkowa funkcja zwracajaca cyferka za literka
def dejNukleo(s):
    if s == "A":
        return 1
    elif s == "C":
        return 2
    elif s == "G":
        return 3
    else:
        return 4
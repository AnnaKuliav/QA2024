from typing import List


def custom_zip(*sequences, full=False, default=None) -> List[List]:
    if full:
        max_length = max(len(seq) for seq in sequences)
    else:
        max_length = min(len(seq) for seq in sequences)

    zipped = []
    for i in range(max_length):
        if full:
            zipped.append(tuple(seq[i] if i < len(seq) else default for seq in sequences))
        else:
            zipped.append(tuple(seq[i] for seq in sequences))

    return zipped


# Examples
seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
print(custom_zip(seq1, seq2))  # [(1, 9), (2, 8), (3, 7)]
print(custom_zip(seq1, seq2, full=True, default="Q"))  # [(1, 9), (2, 8), (3, 7), (4, 'Q')], (5, 'Q')]




def create_fib_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-2] + sequence[i-1])
    return sequence

def find_n_in_fib(sequence, n):
    if n in sequence:
        return f"The number - {n} is at index {sequence.index(n)}"
    else:
        return f"The number {n} is not in the sequence"

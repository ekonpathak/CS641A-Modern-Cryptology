import collections

def frequency_analysis(text):
    # Remove any non-alphabetic characters and convert to lowercase
    text = ''.join(c for c in text if c.isalpha()).lower()

    # Count the frequency of each letter in the text
    freq = collections.Counter(text)

    # Sort the letters by frequency (most frequent first)
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Print the results
    for letter, count in sorted_freq:
        print(letter, count)

text = "qmnjvsanvwewcflctvprjtjtvvplvlfvxjavqildhcxmlnvcnacyclpafcgytvfvwfvwgqyppqqpqcsywsqrxqmnjvafycgvtlvhfcwtylaeuqfvxjatkbvcqnsqslhfavawnccveasfuqbqvqtcyllrqrxxwacfypsdcuqfavrqcgefqpyattracxwvtaawwddveasflcbqvdtrawmvupqquwxdecgqcwtyqyaflvlqsyqklhqsnafqvmllhvqpawrnqgvfusrecwawyqpfnwgawdgf"
frequency_analysis(text)		
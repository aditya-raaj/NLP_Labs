# Morphological Analysis is the process of systematically breaking down a word into these morphemes,
# to identify their meaning and grammatical properties clearly.

# Define known prefixes, suffixes, and roots (simple morphological rules)
prefixes = {
    'un': 'not',
    're': 'again',
    'dis': 'opposite of',
    'pre': 'before'
}

suffixes = {
    'ing': 'present participle form of verb',
    'ed': 'past tense form of verb',
    'ness': 'state of',
    'able': 'capable of',
    'er': 'one who does'
}

roots = ['play', 'do', 'write', 'kind', 'read', 'comfort', 'happy']

# Sample words for Morphological Analysis
words = ['uncomfortable', 'redoing', 'kindness', 'player', 'readable', 'disliked', 'happiness']

# Function to analyze morphology
def morphological_analysis(word):
    analysis = {'Prefix': '', 'Root': '', 'Suffix': '', 'Meaning': []}

    # Check for prefix
    for pre in prefixes:
        if word.startswith(pre):
            analysis['Prefix'] = pre
            analysis['Meaning'].append(f"Prefix '{pre}' meaning '{prefixes[pre]}'")
            word = word[len(pre):]
            break  # Only one prefix assumed

    # Check for suffix
    for suf in suffixes:
        if word.endswith(suf):
            analysis['Suffix'] = suf
            analysis['Meaning'].append(f"Suffix '{suf}' indicating '{suffixes[suf]}'")
            word = word[:-len(suf)]
            break  # Only one suffix assumed

    # Check for root
    if word in roots:
        analysis['Root'] = word
        analysis['Meaning'].append(f"Root '{word}' (main meaning of the word)")
    else:
        analysis['Root'] = word
        analysis['Meaning'].append(f"Root '{word}' (root not found in dictionary)")

    return analysis

# Perform analysis and display detailed output
print("Practical Demonstration of Morphological Analysis\n")
for word in words:
    print(f"Analyzing Word: '{word}'")
    result = morphological_analysis(word)
    print(f"Prefix: {result['Prefix'] or 'None'}")
    print(f"Root: {result['Root']}")
    print(f"Suffix: {result['Suffix'] or 'None'}")
    print("Morpheme Contributions:")
    for meaning in result['Meaning']:
        print(f" - {meaning}")
    print("-" * 50)

import re
from collections import Counter

class Analyzer:
    def count_words(text):
        words = text.split()
        return f'Liczba słów użytych w artykule: {len(words)}'

    def count_letters(text):
        return f'Liczba liter użytych w artykule: {sum(char.isalpha() for char in text)}'

    def most_common_phrases(text, top=5):
        words = re.findall(r'\w+', text.lower())

        phrases = []
        
        for i in range(len(words)):
            phrases.append(words[i])
            if i < len(words) - 1:
                phrases.append(f'{words[i]} {words[i+1]}')
            if i < len(words) - 2:
                phrases.append(f'{words[i]} {words[i+1]} {words[i+2]}')

        phrase_counts = Counter(phrases)
        top_phrases = phrase_counts.most_common(top)

        result = []
        
        for phrase, count in top_phrases:
            result.append(f'{phrase}: {count}')

        return  f'Pięć najczęściej używanych fraz: {result}'
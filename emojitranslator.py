# Emoji Translator
emoji_dict = {
    "love": "❤️",
    "pizza": "🍕",
    "happy": "😊",
    "sad": "😢",
    "dog": "🐶",
    "cat": "🐱",
}

sentence = input("Enter a sentence: ").lower().split()
translated = ""

for word in sentence:
    translated += emoji_dict.get(word, word) + " "

print("Emoji Translation:", translated)

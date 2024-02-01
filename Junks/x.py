from gensim.models import KeyedVectors

# Path to the downloaded FastText model file
model_path = "wiki-news-300d-1M-subword.vec"

# Load the FastText model using gensim
model = KeyedVectors.load_word2vec_format(model_path, binary=False)

# Words to compare
word1 = "programming"
word2 = "coding"

# Check if both words are in the vocabulary
if word1 in model.vocab and word2 in model.vocab:
    # Calculate cosine similarity between the word vectors
    similarity = model.similarity(word1, word2)
    print(f"Similarity between '{word1}' and '{word2}': {similarity}")
else:
    print("One or both words are not in the vocabulary.")

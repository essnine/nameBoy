from enum import unique
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Embedding, LSTM, Dropout
from keras.utils import to_categorical
from random import randint
import re
from nltk import word_tokenize
from nltk.corpus import gutenberg as gut
from keras.preprocessing.text import Tokenizer


def preprocess_text(sen):
    # remove punc marks and numbers
    sentence = re.sub("[^a-zA-Z]", " ", sen)

    # remove single chars
    sentence = re.sub(r"\s+[a-zA-z]\s+", " ", sentence)

    # removing multiple spaces
    sentence = re.sub(r"\s+", " ", sentence)

    return sentence.lower()


def tokenizer(raw_text):
    raw_text_words = word_tokenize(raw_text)
    n_words = len(raw_text_words)
    unique_words = len(set(raw_text_words))

    print("total n_words:", n_words)
    print("total unique_words:", unique_words)

    # begin keras tokenizer section
    # we use the initialized tokenizer object directly, as it contains
    # a dict indexing the words to their occurence frequency values.
    k_tokenizer = Tokenizer(num_words=3437)
    k_tokenizer.fit_on_texts(raw_text_words)

    vocab_size = len(k_tokenizer.word_index)
    word_2_index = k_tokenizer.word_index

    print("Vocab size is", vocab_size)

    input_seq = []
    output_words = []
    input_seq_len = 100

    for i in range(0, n_words - input_seq_len, 1):
        in_seq = raw_text_words[i : i + input_seq_len]
        out_seq = raw_text_words[i + input_seq_len]
        input_seq.append([word_2_index[word] for word in in_seq])
        output_words.append(word_2_index[out_seq])

    print(input_seq[0])

    X = np.reshape(input_seq, (len(input_seq), input_seq_len, 1))
    X = X / float(vocab_size)

    y = to_categorical(output_words)

    print("X shape:", X.shape)
    print("y shape:", y.shape)

    model = Sequential()
    model.add(LSTM(800, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(LSTM(800, return_sequences=True))
    model.add(LSTM(800))
    model.add(Dense(y.shape[1], activation="softmax"))

    model.summary()

    model.compile(loss="categorical_crossentropy", optimizer="adam")
    model.fit(X, y, batch_size=64, epochs=10, verbose=1)

    return n_words


def main():
    # setting the gutenberg text fetched here as a variable
    training_text_raw_stream = gut.raw("shakespeare-macbeth.txt")
    processed_text_stream = preprocess_text(training_text_raw_stream)
    tokenized_text = tokenizer(processed_text_stream)
    print(tokenized_text)
    breakpoint()


if __name__ == "__main__":
    main()

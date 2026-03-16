def word_separator(sentence):

    new_sentence = ""

    for i in range(1, len(sentence)):
        new_sentence = new_sentence + sentence[i-1]

        if sentence[i].isupper():
            new_sentence = new_sentence + " "

    return new_sentence.strip()

if __name__=="__main__":
    sentence = "StopAndSmellTheRoses"

    new_sentence = word_separator(sentence)

    print(new_sentence)

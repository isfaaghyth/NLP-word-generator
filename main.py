import random

text = [None, None]

sentence_finished = False

while not sentence_finished:
    r = random.random()
    accumulator = .0

    for word in bigram_fd[tuple(text[-2:])].keys():
        accumulator += bigram_fd[tuple(text[-2:])][word]

        if accumulator >= r:
            text.append(word)
            break
    
    if text[-2:] == [None, None]:
        sentence_finished = True

print(' '.join([t for t in text if t]))
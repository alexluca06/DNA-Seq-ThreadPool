import random


SEED = 64
DNA_SAMPLE_LENGTH = 10000
SAMPLES = 100
CHOICE_SEQ = "ATGC"
EMPTY = ""


def seq_generator():
    dna = {}
    random.seed(SEED)
    # "".join() elimina separatorul dintre elementele listei!
    for i in range(SAMPLES):
        dna[i] = EMPTY.join([random.choice(CHOICE_SEQ) for i in range(DNA_SAMPLE_LENGTH)])

    return dna




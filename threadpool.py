from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from threading import current_thread
import samplesDNA

SEQ_TO_FIND = "CCCGATATT"
WORKER_NUM = 30
SAMPLES = 100



def find_seq(dna, seq_to_find, index):
    if dna[index].find(seq_to_find) != -1:
        return f"DNA sequence found in sample {index}"
    return None


def main():
    dna = samplesDNA.seq_generator()

    with ThreadPoolExecutor(WORKER_NUM) as executor:
        results = [executor.submit(find_seq, dna, SEQ_TO_FIND, index) for index in range(SAMPLES)]

        for r in as_completed(results):
            res = r.result()

            if res != None:
                print(res)


if __name__ == '__main__':
    main()

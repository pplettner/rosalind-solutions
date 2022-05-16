from itertools import groupby

def read_fasta(handle):
    fasta_iter = groupby(handle, lambda line: line[0] == ">")

    for (is_header, val) in fasta_iter:
        val = [x.strip('\n') for x in val]

        if is_header:
            [name] = val
            # Return name without ">" prefix
            name = name[1:]
        else:
            seq = ''.join(val)
            yield (name, seq)
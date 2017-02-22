import numpy as np


# query_vectorss:   curv mats representing a qr encounter
# database_vectors: curv mats representing a db individual
def dtw_alignment_cost(query_vectors, database_vectors, simfunc):
    S = np.zeros((len(query_vectors), len(database_vectors)), dtype=np.float32)
    for i, qcurv in enumerate(query_vectors):
        for j, dcurv in enumerate(database_vectors):
            S[i, j] = simfunc(qcurv, dcurv)

    return S

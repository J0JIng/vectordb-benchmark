import faiss
import pandas as pd
import numpy as np
from numpy import ndarray
from typing import Tuple

from utils.timer import timer

@timer
def get_data() -> tuple[ndarray,ndarray]:
    df = pd.read_csv("../data/sample.csv")
    np_arr = df.to_numpy()
    query_embeddings = df.iloc[0].to_numpy().astype('float32').reshape(1, -1)
    return np_arr, query_embeddings

@timer
def store_data(index) -> None:
    faiss.write_index(index, "../data/faiss_index.index")

@timer
def query_data(index, query_embeddings) -> None:
    index = faiss.read_index("../data/faiss_index.index")
    distances, indices = index.search(query_embeddings, k=5)
    print(distances, indices)


if __name__ == "__main__":
    np_arr, query_embeddings = get_data()
    # print(np_arr)
    # print("\n")
    # print(query_embeddings)

    M = len(np_arr[0])
    index = faiss.IndexFlatL2(M)    
    index.add(np_arr)
    store_data(index)
    query_data(index, query_embeddings)
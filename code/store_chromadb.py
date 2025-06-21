import faiss
import pandas as pd
import numpy as np
from numpy import ndarray
from typing import Tuple
import math
import chromadb
from chromadb import Collection
from chromadb import PersistentClient

from utils.timer import timer

@timer
def initDB() -> Collection:
    client = chromadb.PersistentClient("../data/chromaDB")
    collection = client.get_or_create_collection(name="sample")
    return collection

@timer
def get_data() -> tuple[list,list,list]:
    df = pd.read_csv("../data/sample.csv")
    py_arr = df.values.tolist()
    query_embeddings = df.iloc[0].tolist()
    ids = [str(idx) for idx in range(len(py_arr))]
    return ids, py_arr, query_embeddings

@timer
def store_data(collection: Collection, ids: list[str], py_arr: list[list[float]]) -> None:
    max_batch_size = 5461
    N, M = len(py_arr), len(py_arr[0])
    batches = math.ceil(N/max_batch_size)
    
    for batch in range(batches):
        print(f"Batch {batch+1} storing in process")
        start = batch * max_batch_size
        end = min((batch + 1) * max_batch_size, N)
        collection.add(
            embeddings=py_arr[start:end],
            ids=ids[start:end],
        )

@timer
def query_data(collection: Collection, embeddings: list[float]) -> None:
    result = collection.query(
            query_embeddings=embeddings,
            include=["embeddings"],
            n_results=1,
        )
    print(result)

if __name__ == "__main__":
    collection = initDB()
    ids, py_arr, query_embeddings = get_data()
    # print(ids, py_arr, query_embeddings)
    # print("\n")
    # print(query_embeddings)
    store_data(collection, ids, py_arr)
    query_data(collection, query_embeddings)
    
import os
import numpy as np
import pandas as pd

from utils.timer import timer

@timer
def create_data(n: int = 100000, m: int = 3072) -> None:
    "Creates a N X M sized matrix, saved as csv"

    np_arr = np.random.rand(n, m).astype(np.float32)
    df = pd.DataFrame(np_arr)
    df.to_csv('../data/test.csv',index=False)


if __name__ == "__main__":
    create_data(100,100)
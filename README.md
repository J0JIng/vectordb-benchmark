# benchmark-db

--- Start: func create_data execution ---
    End:   func create_data execution
--- Elapsed: 240.5822446346283 seconds ---

Run store_faiss.py

--- Start: func get_data execution ---
    End:   func get_data execution
--- Elapsed: 32.465811252593994 seconds ---
--- Start: func store_data execution ---
    End:   func store_data execution
--- Elapsed: 1.3994996547698975 seconds ---
--- Start: func query_data execution ---
[[  0.      469.37582 470.68057 470.86102 471.19617]] [[    0 27005 57245 51769 72620]]
    End:   func query_data execution
--- Elapsed: 0.6919302940368652 seconds ---

Run store_chromadb.py

--- Start: func initDB execution ---
    End:   func initDB execution
--- Elapsed: 0.6167559623718262 seconds ---
--- Start: func get_data execution ---
    End:   func get_data execution
--- Elapsed: 179.50069165229797 seconds ---
--- Start: func store_data execution ---
Batch 1 storing in process
Batch 2 storing in process
Batch 3 storing in process
Batch 4 storing in process
Batch 5 storing in process
Batch 6 storing in process
Batch 7 storing in process
Batch 8 storing in process
Batch 9 storing in process
Batch 10 storing in process
Batch 11 storing in process
Batch 12 storing in process
Batch 13 storing in process
Batch 14 storing in process
Batch 15 storing in process
Batch 16 storing in process
Batch 17 storing in process
Batch 18 storing in process
Batch 19 storing in process
    End:   func store_data execution
--- Elapsed: 324.61070132255554 seconds ---
--- Start: func query_data execution ---
{'ids': [['56946']], 'embeddings': [array([[0.92807174, 0.5682435 , 0.82433957, ..., 0.62318033, 0.46224821,
        0.07426658]], shape=(1, 3072))], 'documents': None, 'uris': None, 'included': ['embeddings'], 'data': None, 'metadatas': None, 'distances': None}
    End:   func query_data execution
--- Elapsed: 0.3595297336578369 seconds ---
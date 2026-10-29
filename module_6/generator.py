lst = [x for x in range (500)]
def data_load(chunk_size,lst):
    for i in range(0,len(lst),chunk_size):
        yield lst[i:i+chunk_size]

x = data_load(5,lst)
print(next(x))
print(next(x))
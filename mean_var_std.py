import numpy as np

def calculate(list):
       if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    dic={}
    arr=np.array(list)
    arr1=arr.reshape(3,3)


    dic['mean']=[
                arr1.mean(axis=0).tolist(),
                arr1.mean(axis=1).tolist(),
                arr1.mean().tolist()
            ]
    dic['variance']=[
                arr1.var(axis=0).tolist(),
                arr1.var(axis=1).tolist(),
                arr1.var().tolist()
    ]
    dic['standard deviation']=[
                arr1.std(axis=0).tolist(),
                arr1.std(axis=1).tolist(),
                arr1.std().tolist()
    ]
    dic['max']=[
                arr1.max(axis=0).tolist(),
                arr1.max(axis=1).tolist(),
                arr1.max().tolist()
    ]
    dic['min']=[
                arr1.min(axis=0).tolist(),
                arr1.min(axis=1).tolist(),
                arr1.min().tolist()
    ]
    dic['sum']=[
                arr1.sum(axis=0).tolist(),
                arr1.sum(axis=1).tolist(),
                arr1.sum().tolist()
    ]

    return calculations

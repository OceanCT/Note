import numpy as np



def read_data():
    data_read = np.loadtxt(fname='./train.csv', dtype=str, skiprows=1, delimiter=',')
    n = len(data_read)
    y_data = data_read[:, 80]
    y_data = y_data.astype(float)
    x_data = data_read[0:8]
    # for j in range(n):
    #     data_read[j][0] = np.int(data_read[j][0])
    #     print(data_read[j][0])
    #     print(type(data_read[j][0]))
    return data_read


data = read_data()

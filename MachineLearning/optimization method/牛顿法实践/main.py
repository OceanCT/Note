import numpy as np


def h_theta(theta_in: np.ndarray, x: np.ndarray):
    tmp = np.dot(theta_in.T, x)
    if tmp > 0:
        tmp = np.exp(-1 * tmp)
        tmp = 1 / (1 + tmp)
    else:
        tmp = np.exp(tmp)
        tmp = tmp / (1 + tmp)
    return tmp


def hessian(theta_in: np.ndarray, x: np.ndarray):
    n1 = len(x[0])
    ans = np.matrix(np.zeros((n1, n1)))
    for j in range(n):
        tmp_x = x[j]
        tmp_h = h_theta(theta_in, tmp_x)
        tmp = np.dot(np.matrix(tmp_x).T, np.matrix(tmp_x))
        ans += tmp_h * (1 - tmp_h) * tmp
    return 1 / n * ans


def gradient(theta_in: np.ndarray, x: np.ndarray, y: np.ndarray):
    n1 = len(x[0])
    ans = np.zeros((1, n1))
    for j in range(n):
        tmp_x = x[j]
        tmp_h = h_theta(theta_in, tmp_x)
        tmp = (tmp_h - y[j]) * tmp_x
        ans += tmp
    return 1 / n * ans


def teller(net: np.matrix, now: np.matrix):
    tmp = net - now
    ans1 = 0
    for tmp1 in tmp:
        ans1 += tmp1 * tmp1
    return ans1 < ending_flag


def iter_once(theta_in: np.ndarray, x: np.ndarray, y: np.ndarray):
    tmp_hess = hessian(theta_in, x)
    tmp = np.dot(np.linalg.inv(tmp_hess), gradient(theta_in, x, y).T).T.A[0]
    return theta_in - tmp


def test(theta_in: np.ndarray, x: np.ndarray):
    print("第一次成绩为%s,第二次成绩为%s的同学大概率" % (x[1], x[2]), end='')
    if h_theta(theta_in, x) < 0.5:
        print("不", end='')
    print("能及格")


if __name__ == '__main__':
    x_data = np.loadtxt('data2x.csv')
    y_data = np.loadtxt('data2y.csv')
    n = len(x_data)
    ending_flag = 1e-8
    x0 = [1 for i in range(n)]
    x_data = np.column_stack((x0, x_data))
    theta = np.array([0 for i in range(len(x_data[0]))])
    theta_next = iter_once(theta, x_data, y_data)
    print(theta_next)
    cnt = 1
    while not teller(theta_next, theta):
        cnt += 1
        theta = theta_next
        theta_next = iter_once(theta, x_data, y_data)
    theta = theta_next
    print("共迭代%s次" % cnt)
    print("最优theta为:", theta)
    test(theta, np.array([1, 20, 80]))

import numpy
import numpy as np
import matplotlib.pyplot as plt


def data_init():
    for j in range(2):
        tmp_mu = float(numpy.mean(x_data[j]))
        tmp_sigma = float(numpy.std(x_data[j]))
        mu.append(tmp_mu)
        sigma.append(tmp_sigma)
        x_data[j] = [(k - tmp_mu) / tmp_sigma for k in x_data[j]]


def h_theta():
    return numpy.dot(theta, x_data)


def grad(tar: np.ndarray, step: float):
    tmp = []
    for j in range(len(tar)):
        ans = 0
        for k in (h_theta() - y_data) * x_data[j]:
            ans += k
        tmp.append(float(tar[j] - step * ans / n))
    return np.array(tmp)


def iter_once():
    a, b = 0.001, 10
    while b - a > 0.001:
        a1 = a + 0.382 * (b - a)
        b1 = a + 0.618 * (b - a)
        theta1 = grad(theta, a1)
        theta2 = grad(theta, b1)
        if j_theta(theta1) < j_theta(theta2):
            b = b1
        else:
            a = a1
    return grad(theta, (a + b) / 2)


def teller(net: np.ndarray, now: np.ndarray):
    tmp = net - now
    ans1 = 0
    for tmp1 in tmp:
        ans1 += tmp1 * tmp1
    return ans1 < ending_flag


def j_theta(tar: np.ndarray):
    tmp = np.dot(tar, x_data) - y_data
    return np.dot(tmp, tmp.T) / 2 / n


def test(ques: list):
    room = ques[0]
    num = ques[1]
    for j in range(2):
        ques[j] = (ques[j] - mu[j]) / sigma[j]
    ques = np.array([1] + ques)
    ans = np.dot(theta, ques)
    print("面积为%s有%s间卧室的房价预计值为:%s" % (room, num, ans))


def picture_draw():
    plt.plot(np.array(training_loss))
    plt.show()


if __name__ == '__main__':
    # read task2
    x_data = numpy.loadtxt('./data2_x.csv').T
    y_data = numpy.loadtxt('./data2_y.csv').T
    training_loss = []
    mu = []
    sigma = []
    data_init()
    # add x_{0}
    n = len(x_data[0])
    x0 = [1 for i in range(n)]
    x_data = numpy.row_stack((x0, x_data))

    # def theta and step
    theta = np.array([0, 0, 0])
    ending_flag = 1e-8

    # iter_once
    theta_next = iter_once()
    print(theta_next)
    # record iter times
    cnt = 1
    while not teller(theta_next, theta):
        training_loss.append(j_theta(theta))
        theta = theta_next
        theta_next = iter_once()
        cnt += 1
    print("总共迭代%s次" % cnt)
    theta = theta_next
    print("theta最终等于: ", theta)
    print("损失函数值为: ", j_theta(theta))
    training_loss.append(j_theta(theta))
    test([1650, 3])

    picture_draw()

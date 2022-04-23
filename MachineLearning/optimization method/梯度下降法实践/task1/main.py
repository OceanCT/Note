import numpy
import numpy as np
import matplotlib.pyplot as plt


def h_theta():
    return numpy.dot(theta, x_data)


def iter_once(tar: np.ndarray):
    tmp = []
    for j in range(len(tar)):
        ans = 0
        for k in (h_theta() - y_data) * x_data[j]:
            ans += k
        tmp.append(float(tar[j] - step * ans / n))
    return np.array(tmp)


def teller(net: np.ndarray, now: np.ndarray):
    tmp = net - now
    ans1 = 0
    for tmp1 in tmp:
        ans1 += tmp1 * tmp1
    return ans1 < ending_flag


def j_theta():
    tmp = h_theta() - y_data
    ans = 0
    for tmp1 in tmp:
        ans += tmp1 * tmp1
    training_loss.append(ans / 2 / n)
    return ans / 2 / n


def test(age: float):
    ans = theta[0] * age + theta[1] * 1
    print("年龄为%s的小孩其身高的预测值为%s" % (age, ans))


def picture_draw():
    plt.plot(np.array(training_loss))
    plt.show()


if __name__ == '__main__':
    # read task1
    x_data = numpy.loadtxt('./data1_x.csv')
    y_data = numpy.loadtxt('./data1_y.csv')
    training_loss = []
    # add x_{0}
    n = len(x_data)
    x0 = [1 for i in x_data]
    x_data = numpy.row_stack((x_data, x0))
    # def theta and step
    theta = np.array([0, 0])
    step = 0.01
    ending_flag = 1e-8
    # print(ending_flag)
    # iter_once
    theta_next = iter_once(theta)
    print(theta_next)
    # record iter times
    cnt = 1
    while not teller(theta_next, theta):
        j_theta()
        theta = theta_next
        theta_next = iter_once(theta)
        cnt += 1
    print("总共迭代%s次" % cnt)
    theta = theta_next
    print("theta最终等于: ", theta)
    print("损失函数值为: ", j_theta())
    test(3.5)
    test(7)

    picture_draw()

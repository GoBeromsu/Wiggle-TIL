import numpy as np  # numpy 라이브러리를 임포트합니다. 이 라이브러리는 배열, 행렬 계산 등 수치 연산을 위한 기능을 제공합니다.
import matplotlib.pyplot as plt  # 데이터를 시각화하기 위해 matplotlib의 pyplot를 임포트합니다.

x_data = [1.0, 2.0, 3.0]  # x 값을 담은 리스트
y_data = [2.0, 4.0, 6.0]  # y 값을 담은 리스트

w = 1.0
def forward(x):  # 주어진 x 값에 대해 예측값을 계산하는 함수
    return x * w

def loss(x, y):  # 예측값과 실제값 사이의 오차(loss)를 계산하는 함수
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

def gradient(x,y):
    return 2*x*(x*x-y)

w_list = []  # 각 단계에서의 가중치 값(w)를 저장할 리스트
mse_list = []  # 각 단계에서의 평균 제곱 오차(MSE) 값을 저장할 리스트

print("Predict (before training) ", 4,forward(4))

for epoch in range(100):
    for x_val,y_val in zip(x_data,y_data):
        grad = gradient(x_val,y_val)
        w = w- 0.0.1

plt.plot(w_list,mse_list)  # w 값에 따른 평균 제곱 오차를 그래프로 그립니다.
plt.ylabel("Loss")  # y축의 라벨을 설정합니다.
plt.xlabel('w')  # x축의 라벨을 설정합니다.

plt.show()  # 그래프를 화면에 표시합니다.

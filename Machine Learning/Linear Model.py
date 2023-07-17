당신이 요청한대로 코드 블럭 옆에 주석을 달아봤습니다.

```python
import numpy as np  # numpy 라이브러리를 임포트합니다. 이 라이브러리는 배열, 행렬 계산 등 수치 연산을 위한 기능을 제공합니다.
import matplotlib.pyplot as plt  # 데이터를 시각화하기 위해 matplotlib의 pyplot를 임포트합니다.

x_data = [1.0, 2.0, 3.0]  # x 값을 담은 리스트
y_data = [2.0, 4.0, 6.0]  # y 값을 담은 리스트


def forward(x):  # 주어진 x 값에 대해 예측값을 계산하는 함수
    return x * w

def loss(x, y):  # 예측값과 실제값 사이의 오차(loss)를 계산하는 함수
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

w_list = []  # 각 단계에서의 가중치 값(w)를 저장할 리스트
mse_list = []  # 각 단계에서의 평균 제곱 오차(MSE) 값을 저장할 리스트

for w in np.arange(0.0, 4.1, 0.1):  # 가중치 값을 0.0에서 4.1까지 0.1씩 증가시키며
    print("w = ", w)
    l_sum = 0
    for x_val, y_val in zip(x_data,y_data):  # 각 x,y 데이터 쌍에 대해
        y_pred_val = forward(x_val)  # y 예측값을 계산하고
        l = loss(x_val,y_val)  # 오차를 계산한 후
        l_sum += l  # 전체 오차에 더합니다.
        print("\t", x_val, y_val, y_pred_val, 1)
    print("MSE = ",l_sum/3)  # 전체 오차를 데이터 개수로 나누어 평균 제곱 오차를 구합니다.
    w_list.append(w)  # 현재의 w 값을 리스트에 추가합니다.
    mse_list.append(l_sum/3)  # 현재의 평균 제곱 오차를 리스트에 추가합니다.

plt.plot(w_list,mse_list)  # w 값에 따른 평균 제곱 오차를 그래프로 그립니다.
plt.ylabel("Loss")  # y축의 라벨을 설정합니다.
plt.xlabel('w')  # x축의 라벨을 설정합니다.

plt.show()  # 그래프를 화면에 표시합니다.

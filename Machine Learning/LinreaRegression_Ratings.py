import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # 데이터 처리를 위해 pandas 라이브러리를 불러옵니다.

# csv 파일을 읽어서 데이터프레임으로 변환합니다.
df = pd.read_csv('/Users/gobeomsu/Documents/GitHub/Wiggle-TIL/Machine Learning/ratings.csv')

# 'userid' column을 x_data로 사용합니다.
x_data = df['userId'].values.tolist()

# 'rating' column을 y_data로 사용합니다.
y_data = df['rating'].values.tolist()

def forward(x): 
    return x * w

def loss(x, y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

w_list = []
mse_list = []

for w in np.arange(0.0, 4.1, 0.1):
    print("w = ", w)
    l_sum = 0
    for x_val, y_val in zip(x_data,y_data):
        y_pred_val = forward(x_val)
        l = loss(x_val,y_val)
        l_sum += l
    print("MSE = ",l_sum/len(x_data))  # len(x_data)를 사용해 x_data의 개수에 맞게 MSE를 계산합니다.
    w_list.append(w)
    mse_list.append(l_sum/len(x_data))
plt.plot(w_list,mse_list)
plt.ylabel("userId")
plt.xlabel('rating')
plt.show()

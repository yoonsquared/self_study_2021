# 대학원 합격 예측 프로그램
# conda가 필요하기 때문에 anaconda prompt를 사용.
'''
conda activate tf
cd  Documents\python_analysis\Jocoding
python tensor_lecture3.py
'''


import pandas as pd
# 엑셀데이터 다룰떄 가장 많이 쓰이는 pandas library

data = pd.read_csv('gpascore.csv')

# NA 찾기
print(data.isnull().sum())

# NA 열 지우기
data = data.dropna()
print(data.isnull().sum())

# gpa column (열) 만 print
print(data['gpa'])
# 그 열의 최소값
print(data['gpa'].min())
# 그 열의 최대값
print(data['gpa'].max())
# 그 열의 row 갯수
print(data['gpa'].count())

# admit column list 저장.
yData = data['admit'].values
xData = []

# iterrows() 한 행씩
## i 에 행번호
## rows 에 나머지 데이터들이 들어감
for i, rows in data.iterrows():

    xData.append( [ rows['gre'], rows['gpa'], rows['rank'] ] )

import tensorflow as tf
# keras 의 sequential은 자동으로 노드와 엣지로 딥러닝 모델을 만들어줌.
# 64 node -> 128 node -> 1 node
# Activation Function : sigmoid, tanh, relu, softmax, leakyRelu
## sigmoid는 모든 결과를 0~1 사이의 값으로 줄여주는 function.

# optimizer function : adam, adagrad, adadelta, rmsprop, sgd, 등등
# loss function : mse, binary_crossentropy, 등등
## 0과 1 사이 확률 예측에선 binary_crossentropy 가 좋다고 알려져있음.
model = tf.keras.models.Sequential( [      
tf.keras.layers.Dense( 64, activation = 'tanh' ),
tf.keras.layers.Dense( 128, activation = 'tanh' ),
tf.keras.layers.Dense( 1,activation = 'sigmoid' ), #마지막 레이어
] )

model.compile( optimizer = 'adam',loss = 'binary_crossentropy', metrics = ['accuracy']  )

# model.fit( x_data, y_data, epochs = 300)
## epochs = 몇번 돌릴건지.

import numpy as np
# 그냥 list를 받을 순 없어서 numpy_array 또는 tensor 형으로.
model.fit( np.array(xData), np.array(yData), epochs=300 )


# 이 gre, gpa, rank 값을 던졌을떄 과연 합격될 확률은?
predictedRez = model.predict( [ [750, 3.70, 3], [400, 2.2, 1] ] )

# Print predicted
print( predictedRez )
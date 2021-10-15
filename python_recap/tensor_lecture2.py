import tensorflow as tf

키 = [170, 180, 175, 160]
신발 = [260,270,265,255]

# y=ax+b

키2 = 170
신발2 = 260

# 신발 = (키 * a) + b
a = tf.Variable(0.1)
b = tf.Variable(0.2)

# 경사하강법에 의해 변수 optmize하는 function, ADAM 사용.
# gradient 를 알아서 해주는 고마운 것. 전반적으로 성능이 좋음.
opt = tf.keras.optimizers.Adam(learning_rate=0.1)

def loss_function():
    예측값 = 키2 * a + b
    return tf.square(260 - 예측값)

# loss_function = 손실함수

for i in range(300):
    opt.minimize(loss_function, var_list=[a,b])

print (a.numpy(),b.numpy())


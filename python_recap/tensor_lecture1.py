import tensorflow as tf
tensor = tf.constant([3,4,5])
tensor2 = tf.constant ([6,7,8])

tensor3 = tf.constant([ [1,2],
                        [3,4] ])

tensor4 = tf.zeros(10)
tensor5 = tf.zeros(2,2)
tensor6 = tf.zeros(2,2,3)

w = tf.Variable(1.0)


print(tensor)
print(tensor+tensor2)
print(tensor3)
print(tensor4)
print(tensor5)
print(tensor6)

print(tensor6.shape)

print(w.numpy)
w.assign(2)
print(w.assign)
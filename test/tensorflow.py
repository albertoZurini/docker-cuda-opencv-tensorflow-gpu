import tensorflow as tf

print(tf.__version__)

a = tf.constant(3)
b = tf.constant(4)
c = tf.Sum(a, b)

with tf.Session() as sess:
    print(sess.run(c))
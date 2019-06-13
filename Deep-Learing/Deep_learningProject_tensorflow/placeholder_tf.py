import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add_node = a+b

sess=tf.Session()
print(sess.run(add_node,{a: [1,3],b: [3,6]}))
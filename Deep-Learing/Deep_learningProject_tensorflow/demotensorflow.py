import tensorflow as tf

node1=tf.constant(3.0,tf.float32)

node2 = tf.constant(4.0)
# Build a session to run the computational Graph sess.run pass the node

sess=tf.Session()

print(sess.run([node1,node2]))
import  tensorflow as tf

w = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)
c = tf.placeholder(tf.float32)

linear_progam = w * c + b

#initializer Variable using global function and run session
init = tf.global_variables_initializer()

sess=tf.Session()

sess.run(init)

print(sess.run(linear_progam,{c:[1,2,3,4]}))

y=tf.Variable(tf.float32)

sqare_delta=tf.square(linear_progam - y)

loss=tf.reduce_sum(sqare_delta)

sess.run(init)

print(sess.run(loss,{x:[1,2,3,4],y:[0,1,2,3]}))
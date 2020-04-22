import tensorflow

hello = tensorflow.constant('hel')
sess = tensorflow.Session()
print(sess.run(hello))
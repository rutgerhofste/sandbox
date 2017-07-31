
# coding: utf-8

# In[1]:


from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)


# In[2]:


import tensorflow as tf


# In[3]:


x = tf.placeholder(tf.float32, [None, 784])


# In[4]:


W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))


# In[5]:


y = tf.nn.softmax(tf.matmul(x, W) + b)


# In[6]:


y_ = tf.placeholder(tf.float32, [None, 10])


# In[7]:


cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))


# In[8]:


train_step = tf.train.GradientDescentOptimizer(0.05).minimize(cross_entropy)


# In[9]:


sess = tf.InteractiveSession()


# In[10]:


tf.global_variables_initializer().run()


# In[11]:


for _ in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


# In[12]:


correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))


# In[13]:


accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


# In[14]:


print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


# In[ ]:





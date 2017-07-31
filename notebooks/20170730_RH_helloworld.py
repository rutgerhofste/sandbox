
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


node1 = tf.constant(3.0, dtype=tf.float32)


# In[3]:


node2 = tf.constant(4.0) # also tf.float32 implicitly


# In[4]:


print(node1, node2)


# In[5]:


sess = tf.Session()


# In[6]:


print(sess.run([node1, node2]))


# In[7]:


node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ",sess.run(node3))


# In[8]:


a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)


# In[9]:


print(sess.run(adder_node, {a: 3, b:4.5}))
print(sess.run(adder_node, {a: [1,3], b: [2, 4]}))


# Linear regression model

# In[10]:


W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b


# In[11]:


init = tf.global_variables_initializer()
sess.run(init)


# In[13]:


print(sess.run(linear_model, {x:[1,2,3,4]}))


# In[14]:


y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


# In[15]:


fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))


# In[16]:


optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


# In[31]:


sess.run(init) # reset values to incorrect defaults.


# In[32]:


x_train = [1,2,3,4]
y_train = [0,-1,-2,3]


# In[ ]:





# In[33]:


sess.run(init) # reset values to incorrect defaults.
for i in range(1000):
  sess.run(train, {x:x_train, y:y_train})

print(sess.run([W, b]))


# In[34]:


curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))


# In[ ]:





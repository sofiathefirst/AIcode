import tensorflow as tf
 


state = tf.Variable(0, name="counter")

#创建一个常量
one = tf.constant(1)

#对常量与变量进行简单的加法操作，这点需要说明的是： 在TensoorFlow中，
#所有的操作op和变量都视为节点，tf.add() 的意思就是在tf的默认图中添加一个op，这个op是用来做加法操作的。
new_value = tf.add(state,one)

#赋值操作。将new_value的值赋值给update变量
update = tf.assign(state,new_value)

#此处用于初始化变量。但是这句话仍然不会立即执行。需要通过sess来将数据流动起来 。如果有Variable，一定需要写这句话
init = tf.initialize_all_variables()

#切记：所有的运算都应该在session中进行，即 with tf.Session() as sess
with tf.Session() as sess:
    #对变量进行初始化，执行（run）init语句
    sess.run(init)
    #循环3次，并且打印输出。
    for _ in range(3):
        sess.run(update)
        # 打印变量时也需要用sess.run
        print(sess.run(state))
    writer = tf.summary.FileWriter("TensorBoard/test",sess.graph)
writer.close()



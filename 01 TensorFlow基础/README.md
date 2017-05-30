
作者邮箱：
	
	p995637308@gmail.com
	995637308@qq.com

ps 主要是issue，邮箱不怎么用。

##环境安装

[安装pathon和TensorFlow的方法，直通车	](http://blog.csdn.net/u013814964/article/details/72457235)




##源码解释

	
	01.py //矩阵相乘，启动图运算
	02.py //取代sess,加法
	03.py //循环加法，计数变量















##其他

如果机器上有超过一个可用的 GPU, 除第一个外的其它 GPU 默认是不参与计算的. 为了让 TensorFlow 使用这些 GPU, 你必须将 op 明确指派给它们执行. with...Device 语句用来指派特定的 CPU 或 GPU 执行操作:

	with tf.Session() as sess:
	  with tf.device("/gpu:1"):
	    matrix1 = tf.constant([[3., 3.]])
	    matrix2 = tf.constant([[2.],[2.]])
	    product = tf.matmul(matrix1, matrix2)
	    ...
设备用字符串进行标识. 目前支持的设备包括:

"/cpu:0": 机器的 CPU.
"/gpu:0": 机器的第一个 GPU, 如果有的话.
"/gpu:1": 机器的第二个 GPU, 以此类推. 
# 批量归一化

为了使神经网络收敛的更快，使用批量归一化。批量归一化会固定均值和标准差。其中 $\mu_B = \frac{1}{\abs{B}} \sum_{i \in B}x_i$ 和 $\sigma^2_B = \frac{1}{\abs{B}} \sum_{i \in B}(x_i - \mu_B)^2 + \epsilon$

接下来进行批量归一化
$$
x_{i+1} = \gamma \frac{x_{i} - \hat{\mu}_B}{\hat{\sigma}_B} + \beta
$$
对于全连接层，我们将在特征维进行批量归一化，考虑一个二维矩阵。
$$
\begin{pmatrix}
x_{11} & \cdots & x_{1n} \\
\vdots & \cdots & \vdots \\
x_{m1} & \cdots & x_{mn} \\
\end{pmatrix}
$$
其中每一行代表一个样本，每一列代表一个特征，现在对其进行批量归一化，就是对列套用公式 $(1)$ 。对于卷积层，则是在通道维进行批量归一化。批量归一化的本质是在每一个小批量加入噪音。

**总结：批量归一化可以加速收敛（可以用更大的学习率），但不改变模型的精度。**

# Res-Net(一个重要的网络)

Res-Net的核心思想就是 $f(x) = x + g(x)$ ，其中 $x$ 表示上一层的输出，$g(x)$ 表示本层需要学习到的额外的函数，残差块可以保证至少能够学习到小模型，并且在小模型的基础上学到更广阔的模型，使网络达到上千层，残差块可以看成是运用了**泰勒展开的思想**。

Res-Net的核心思想是使得模型一层层得叠加，并且是嵌套的叠加。

import clipboard

s = """Fixed distribution of inputs to a sub-network would
have positive consequences for the layers outside the subnetwork, as well. Consider a layer with a sigmoid activation function z = g(Wu + b) where u is the layer input,
the weight matrix W and bias vector b are the layer parameters to be learned, and g(x) = 1
1+exp(−x)
. As |x|
increases, g
′
(x) tends to zero. This means that for all dimensions of x = Wu+b except those with small absolute
values, the gradient flowing down to u will vanish and the
model will train slowly. However, since x is affected by
W, b and the parameters of all the layers below, changes
to those parameters during training will likely move many
dimensions of x into the saturated regime of the nonlinearity and slow down the convergence. This effect is
amplified as the network depth increases. In practice,
the saturation problem and the resulting vanishing gradients are usually addressed by using Rectified Linear Units
(Nair & Hinton, 2010) ReLU(x) = max(x, 0), careful
initialization (Bengio & Glorot, 2010; Saxe et al., 2013),
and small learning rates. If, however, we could ensure
that the distribution of nonlinearity inputs remains more
stable as the network trains, then the optimizer would be
less likely to get stuck in the saturated regime, and the
training would accelerate."""

s = s.replace("\n", " ")
clipboard.copy(s)

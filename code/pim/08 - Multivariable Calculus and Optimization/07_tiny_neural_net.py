# uv run --with numpy python "code/pim/08 - Multivariable Calculus and Optimization/07_tiny_neural_net.py"
#
# Section 14.9 in miniature: a from-scratch neural network trained by
# hand-rolled backpropagation (the chain rule + gradient descent), just
# like Kun's MNIST net but small enough to run instantly.  One hidden
# layer of sigmoids, an L2 loss, and stochastic gradient descent.  Task:
# learn XOR -- a problem no single linear threshold can solve, which is
# exactly why we need the nonlinear hidden layer.
import numpy as np

rng = np.random.default_rng(0)


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def sigmoid_prime(a):           # derivative in terms of the output a
    return a * (1.0 - a)


# XOR dataset: (x, label).  Not linearly separable.
X = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
y = np.array([0.0, 1.0, 1.0, 0.0])

# One hidden layer with 4 sigmoid neurons; one sigmoid output.
W1 = rng.uniform(-1, 1, size=(2, 4))
b1 = np.zeros(4)
W2 = rng.uniform(-1, 1, size=(4, 1))
b2 = np.zeros(1)
eta = 0.5

for step in range(40_000):
    i = rng.integers(len(X))          # stochastic: one random example
    x, target = X[i], y[i]

    # Forward pass (cache activations for the backward pass).
    h_in = x @ W1 + b1
    h = sigmoid(h_in)
    o_in = h @ W2 + b2
    o = sigmoid(o_in)[0]

    # Backward pass: dE/d* via the chain rule.  E = (o - target)^2.
    dE_do = 2.0 * (o - target)
    d_oin = dE_do * sigmoid_prime(o)              # through output sigmoid
    dW2 = np.outer(h, d_oin)
    db2 = np.array([d_oin])
    d_h = d_oin * W2[:, 0]                         # back into hidden layer
    d_hin = d_h * sigmoid_prime(h)                 # through hidden sigmoids
    dW1 = np.outer(x, d_hin)
    db1 = d_hin

    # Gradient descent step: move against the gradient.
    W2 -= eta * dW2
    b2 -= eta * db2
    W1 -= eta * dW1
    b1 -= eta * db1


def predict(x):
    h = sigmoid(x @ W1 + b1)
    return sigmoid(h @ W2 + b2)[0]


print("XOR predictions after training:")
correct = 0
for x, t in zip(X, y):
    p = predict(x)
    label = int(p >= 0.5)
    correct += (label == t)
    print(f"  {x.astype(int)} -> {p:.3f}  (label {label}, target {int(t)})")

# A backprop-trained net with a hidden layer solves XOR perfectly.
assert correct == 4, f"only {correct}/4 correct"
print("All 4 XOR cases correct: hand-rolled backprop learned a "
      "nonlinear function.")

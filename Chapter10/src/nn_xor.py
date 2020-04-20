from nn.neuralnetwork import NeuralNetwork
import numpy as np

# Testing the neural network that is using backpropagating algorithm over XOR dataset
# to prove that nonlinear activation functions and multiple hidden layers
# are suitable for seprating nonlinear datasets
X = np.array([[0,0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

nn = NeuralNetwork([2, 2, 1], alpha=0.5)
nn.fit(X, y, epochs=20000)

for (x, target) in zip(X, y):
    pred = nn.predict(x)[0][0]
    step = 1 if pred > 0.5 else 0
    print("[INFO] data={}, ground-truth={}, pred={:.4f}, step={}".format(
        x, target[0], pred, step
    ))
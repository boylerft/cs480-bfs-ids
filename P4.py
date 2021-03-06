from numpy import exp, array, random, dot

class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1


class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Pass the training set through our neural network
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calculate the error for layer 2 (The difference between the desired output
            # and the predicted output).
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            # Calculate the error for layer 1 (By looking at the weights in layer 1,
            # we can determine by how much layer 1 contributed to the error in layer 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            # Calculate how much to adjust the weights by
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Adjust the weights.
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    # The neural network thinks.
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    # The neural network prints its weights
    def print_weights(self):
        print "    Layer 1 (4 neurons, each with 3 inputs): "
        print self.layer1.synaptic_weights
        print "    Layer 2 (1 neuron, with 4 inputs):"
        print self.layer2.synaptic_weights
        
def binaryToDecimal(binary):   
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal   
'''
def add_correct(combs):
    new_array = []
    for i in range(len(combs)):
        if (binaryToDecimal(int(str(combs[i][0]) + str(combs[i][1]) + str(combs[i][2]))) >= 
           binaryToDecimal(int(str(combs[i][3]) + str(combs[i][4]) + str(combs[i][5])))):
            c = [combs[i]]
            c.append([1])
            new_array.append(c)
        else:
            c = [combs[i]]
            c.append([0])
            new_array.append(c)
    return new_array
'''

def add_correct(combs):
    new_array = []
    for i in range(len(combs)):
        if (binaryToDecimal(int(str(combs[i][0]) + str(combs[i][1]) + str(combs[i][2]))) >= 
           binaryToDecimal(int(str(combs[i][3]) + str(combs[i][4]) + str(combs[i][5])))):
            new_array.append(1)
        else:
            new_array.append(0)
    return new_array
            
def add_bias(combs):
    for i in range(len(combs)):
        combs[i].insert(0, -1)
def main():
    combs = [[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0],[0,0,0,0,1,1],[0,0,0,1,0,0],[0,0,0,1,0,1],[0,0,0,1,1,0],[0,0,0,1,1,1],[0,0,1,0,0,0],[0,0,1,0,0,1],[0,0,1,0,1,0],[0,0,1,0,1,1],[0,0,1,1,0,0],[0,0,1,1,0,1],[0,0,1,1,1,0],[0,0,1,1,1,1],[0,1,0,0,0,0],[0,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,0,1,1],[0,1,0,1,0,0],[0,1,0,1,0,1],[0,1,0,1,1,0],[0,1,0,1,1,1],[0,1,1,0,0,0],[0,1,1,0,0,1],[0,1,1,0,1,0],[0,1,1,0,1,1],[0,1,1,1,0,0],[0,1,1,1,0,1],[0,1,1,1,1,0],[0,1,1,1,1,1],[1,0,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,0,0,1,1],[1,0,0,1,0,0],[1,0,0,1,0,1],[1,0,0,1,1,0],[1,0,0,1,1,1],[1,0,1,0,0,0],[1,0,1,0,0,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,0,1,1,0,0],[1,0,1,1,0,1],[1,0,1,1,1,0],[1,0,1,1,1,1],[1,1,0,0,0,0],[1,1,0,0,0,1],[1,1,0,0,1,0],[1,1,0,0,1,1],[1,1,0,1,0,0],[1,1,0,1,0,1],[1,1,0,1,1,0],[1,1,0,1,1,1],[1,1,1,0,0,0],[1,1,1,0,0,1],[1,1,1,0,1,0],[1,1,1,0,1,1],[1,1,1,1,0,0],[1,1,1,1,0,1],[1,1,1,1,1,0],[1,1,1,1,1,1]]
    add_bias(combs)
    print(combs)
    #print(int(str(combs[16][0]) + str(combs[16][1]) + str(combs[16][2])))
    #print(binaryToDecimal(int(str(combs[16][0]) + str(combs[16][1]) + str(combs[16][2]))))
    
    #print(len(add_correct(combs)))
    #print(len(training_set_inputs))
    
    #tOutput = [add_correct(combs)]
    
    #print(combs)
    #training_set_outputs = array(add_correct(combs)).T
    #training_set_inputs = array([[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0],[0,0,0,0,1,1],[0,0,0,1,0,0],[0,0,0,1,0,1],[0,0,0,1,1,0],[0,0,0,1,1,1],[0,0,1,0,0,0],[0,0,1,0,0,1],[0,0,1,0,1,0],[0,0,1,0,1,1],[0,0,1,1,0,0],[0,0,1,1,0,1],[0,0,1,1,1,0],[0,0,1,1,1,1],[0,1,0,0,0,0],[0,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,0,1,1],[0,1,0,1,0,0],[0,1,0,1,0,1],[0,1,0,1,1,0],[0,1,0,1,1,1],[0,1,1,0,0,0],[0,1,1,0,0,1],[0,1,1,0,1,0],[0,1,1,0,1,1],[0,1,1,1,0,0],[0,1,1,1,0,1],[0,1,1,1,1,0],[0,1,1,1,1,1],[1,0,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,0,0,1,1],[1,0,0,1,0,0],[1,0,0,1,0,1],[1,0,0,1,1,0],[1,0,0,1,1,1],[1,0,1,0,0,0],[1,0,1,0,0,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,0,1,1,0,0],[1,0,1,1,0,1],[1,0,1,1,1,0],[1,0,1,1,1,1],[1,1,0,0,0,0],[1,1,0,0,0,1],[1,1,0,0,1,0],[1,1,0,0,1,1],[1,1,0,1,0,0],[1,1,0,1,0,1],[1,1,0,1,1,0],[1,1,0,1,1,1],[1,1,1,0,0,0],[1,1,1,0,0,1],[1,1,1,0,1,0],[1,1,1,0,1,1],[1,1,1,1,0,0],[1,1,1,1,0,1],[1,1,1,1,1,0],[1,1,1,1,1,1]])
    #print(len(training_set_inputs))
    #print (len(training_set_outputs))
    
    
    #Seed the random number generator
    random.seed(1)

    # Create layer 1 (2 neurons, each with 6 inputs)
    layer1 = NeuronLayer(2, 6)

    # Create layer 2 (a single neuron with 2 inputs)
    layer2 = NeuronLayer(1,2)

    # Combine the layers to create a neural network
    neural_network = NeuralNetwork(layer1, layer2)

    print "Stage 1) Random starting synaptic weights: "
    neural_network.print_weights()

    # The training set. We have 7 examples, each consisting of 3 input values
    # and 1 output value.
    #training_set_inputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    #training_set_outputs = array([[0, 1, 1, 1, 1, 0, 0]]).T
    
    training_set_inputs = array([[0,0,0,0,0,0],[0,0,0,0,0,1],[0,0,0,0,1,0],[0,0,0,0,1,1],[0,0,0,1,0,0],[0,0,0,1,0,1],[0,0,0,1,1,0],[0,0,0,1,1,1],[0,0,1,0,0,0],[0,0,1,0,0,1],[0,0,1,0,1,0],[0,0,1,0,1,1],[0,0,1,1,0,0],[0,0,1,1,0,1],[0,0,1,1,1,0],[0,0,1,1,1,1],[0,1,0,0,0,0],[0,1,0,0,0,1],[0,1,0,0,1,0],[0,1,0,0,1,1],[0,1,0,1,0,0],[0,1,0,1,0,1],[0,1,0,1,1,0],[0,1,0,1,1,1],[0,1,1,0,0,0],[0,1,1,0,0,1],[0,1,1,0,1,0],[0,1,1,0,1,1],[0,1,1,1,0,0],[0,1,1,1,0,1],[0,1,1,1,1,0],[0,1,1,1,1,1],[1,0,0,0,0,0],[1,0,0,0,0,1],[1,0,0,0,1,0],[1,0,0,0,1,1],[1,0,0,1,0,0],[1,0,0,1,0,1],[1,0,0,1,1,0],[1,0,0,1,1,1],[1,0,1,0,0,0],[1,0,1,0,0,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,0,1,1,0,0],[1,0,1,1,0,1],[1,0,1,1,1,0],[1,0,1,1,1,1],[1,1,0,0,0,0],[1,1,0,0,0,1],[1,1,0,0,1,0],[1,1,0,0,1,1],[1,1,0,1,0,0],[1,1,0,1,0,1],[1,1,0,1,1,0],[1,1,0,1,1,1],[1,1,1,0,0,0],[1,1,1,0,0,1],[1,1,1,0,1,0],[1,1,1,0,1,1],[1,1,1,1,0,0],[1,1,1,1,0,1],[1,1,1,1,1,0], [1,1,1,1,1,1]])
    #training_set_outputs = array(tOutput).T
    #training_set_inputs = array([[-1,0,0,0,0,0,0],[-1,0,0,0,0,0,1],[-1,0,0,0,0,1,0],[-1,0,0,0,0,1,1],[-1,0,0,0,1,0,0],[-1,0,0,0,1,0,1],[-1,0,0,0,1,1,0],[-1,0,0,0,1,1,1],[-1,0,0,1,0,0,0],[-1,0,0,1,0,0,1],[-1,0,0,1,0,1,0],[-1,0,0,1,0,1,1],[-1,0,0,1,1,0,0],[-1,0,0,1,1,0,1],[-1,0,0,1,1,1,0],[-1,0,0,1,1,1,1],[-1,0,1,0,0,0,0],[-1,0,1,0,0,0,1],[-1,0,1,0,0,1,0],[-1,0,1,0,0,1,1],[-1,0,1,0,1,0,0],[-1,0,1,0,1,0,1],[-1,0,1,0,1,1,0],[-1,0,1,0,1,1,1],[-1,0,1,1,0,0,0],[-1,0,1,1,0,0,1],[-1,0,1,1,0,1,0],[-1,0,1,1,0,1,1],[-1,0,1,1,1,0,0],[-1,0,1,1,1,0,1],[-1,0,1,1,1,1,0],[-1,0,1,1,1,1,1],[-1,1,0,0,0,0,0],[-1,1,0,0,0,0,1],[-1,1,0,0,0,1,0],[-1,1,0,0,0,1,1],[-1,1,0,0,1,0,0],[-1,1,0,0,1,0,1],[-1,1,0,0,1,1,0],[-1,1,0,0,1,1,1],[-1,1,0,1,0,0,0],[-1,1,0,1,0,0,1],[-1,1,0,1,0,1,0],[-1,1,0,1,0,1,1],[-1,1,0,1,1,0,0],[-1,1,0,1,1,0,1],[-1,1,0,1,1,1,0],[-1,1,0,1,1,1,1],[-1,1,1,0,0,0,0],[-1,1,1,0,0,0,1],[-1,1,1,0,0,1,0],[-1,1,1,0,0,1,1],[-1,1,1,0,1,0,0],[-1,1,1,0,1,0,1],[-1,1,1,0,1,1,0],[-1,1,1,0,1,1,1],[-1,1,1,1,0,0,0],[-1,1,1,1,0,0,1],[-1,1,1,1,0,1,0],[-1,1,1,1,0,1,1],[-1,1,1,1,1,0,0],[-1,1,1,1,1,0,1],[-1,1,1,1,1,1,0],[-1,1,1,1,1,1,1]])
    training_set_outputs =array([[1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1]]).T
    #print(training_set_outputs)
    #print(training_set_inputs)

    # Train the neural network using the training set.
    # Do it 60,000 times and make small adjustments each time.
    neural_network.train(training_set_inputs, training_set_outputs, 3)

    print "Stage 2) New synaptic weights after training: "
    neural_network.print_weights()

    # Test the neural network with a new situation.
    print "Stage 3) Considering a new situation [0,0,0,0,1,0] -> ?: "
    #hidden_state, output = neural_network.think(array([0,0,0,0,1,0]))
    result = 0.0
    for i in range(len(training_set_inputs)):
        #print(training_set_inputs[i])
        hidden_state, output = neural_network.think(training_set_inputs[i])
        x = round(output)
        #print(x)
        if x == training_set_outputs[i]:
            result += 1
    print ("result #", result)
    print ("ratio", float(result/64.0))
    
    
main()
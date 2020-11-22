import torch
import torch.nn as nn

#This is a feed forward neural network with 2 hidden layers
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        #Need to create 3 linear layers here
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        #activation function
        self.relu = nn.ReLU()
    
    def forward(self, x):
        #first linear layer
        out = self.l1(x)
        #activation function inbetween
        out = self.relu(out)
        #second linear layer
        out = self.l2(out)
        #activation function inbetween
        out = self.relu(out)
        #third linear layer
        out = self.l3(out)
        # no activation and no softmax at the end because later we apply the cross entorpy loss, and this 
        #will already apply this for us. Simply need to return the output instead.
        return out

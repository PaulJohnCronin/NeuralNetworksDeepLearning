# kuzu.py
# ZZEN9444, CSE, UNSW

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F

class NetLin(nn.Module):
    # linear function followed by log_softmax

    def __init__(self):
        super(NetLin, self).__init__()
        self.fc1   = nn.Linear(784, 10)

    def forward(self, x):
        out = x.view(x.size(0), -1)
        out = F.log_softmax(self.fc1(out),1)
        return out


class NetFull(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFull, self).__init__()
        self.fc1   = nn.Linear(784, 240)
        self.fc2   = nn.Linear(240, 10)

    def forward(self, x):
        out = x.view(x.size(0), -1)
        out = torch.tanh(self.fc1(out))
        out = F.log_softmax(self.fc2(out),1)
        return out

class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax

    def __init__(self):
        super(NetConv, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5, padding=2)
        self.conv2 = nn.Conv2d(6, 16, 5, padding=2)
        self.fc1   = nn.Linear(7*7*16, 240)
        self.fc2   = nn.Linear(240, 10)

    def forward(self, x):
        out = F.relu(self.conv1(x))
        out = F.max_pool2d(out, 2)
        out = F.relu(self.conv2(out))
        out = F.max_pool2d(out, 2)
        out = out.view(out.size(0), -1)
        out = F.relu(self.fc1(out))
        out = F.log_softmax(self.fc2(out),1)
        return out

class NetFullRes(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFullRes, self).__init__()
        self.fc1   = nn.Linear(784, 240)
        self.fc2   = nn.Linear(240+784, 10)

    def forward(self, x):
        out0 = x.view(x.size(0), -1)
        out1 = torch.tanh(self.fc1(out0))
        out2 = torch.cat((out0,out1),1)
        out = F.log_softmax(self.fc2(out2),1)
        return out
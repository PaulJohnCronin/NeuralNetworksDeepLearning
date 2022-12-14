# spiral.py
# ZZEN9444, CSE, UNSW
# python3 spiral_main.py --net polar --hid 6 --epochs 20000

import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt

class PolarNet(torch.nn.Module):
    def __init__(self, num_hid):
        super(PolarNet, self).__init__()
        self.fc1   = nn.Linear(2, num_hid)
        self.fc2   = nn.Linear(num_hid, 1)

    def forward(self, input):
        x = input[:,0:1]
        y = input[:,1:2]

        out = torch.cat((torch.sqrt(x * x + y * y),torch.atan2(y, x)),dim=1)
        out = torch.tanh(self.fc1(out))
        self.layer1=out
        out = torch.sigmoid(self.fc2(out))
        return out

class RawNet(torch.nn.Module):
    # python3 spiral_main.py --net raw --epochs 20000 --hid 9 --lr 0.025 --init 0.1 (2400)

    def __init__(self, num_hid):
        super(RawNet, self).__init__()
        self.fc1   = nn.Linear(2, num_hid)
        self.fc2   = nn.Linear(num_hid, num_hid)
        self.fc3   = nn.Linear(num_hid, 1)

    def forward(self, input):
        out = torch.tanh(self.fc1(input))
        self.layer1=out
        out = torch.tanh(self.fc2(out))
        self.layer2=out
        out = torch.sigmoid(self.fc3(out))
        return out

def graph_hidden(net, layer, node):
    xrange = torch.arange(start=-7,end=7.1,step=0.01,dtype=torch.float32)
    yrange = torch.arange(start=-6.6,end=6.7,step=0.01,dtype=torch.float32)
    xcoord = xrange.repeat(yrange.size()[0])
    ycoord = torch.repeat_interleave(yrange, xrange.size()[0], dim=0)
    grid = torch.cat((xcoord.unsqueeze(1),ycoord.unsqueeze(1)),1)

    with torch.no_grad(): # suppress updating of gradients
        net.eval()        # toggle batch norm, dropout
        output = net(grid)
        # net.train() # toggle batch norm, dropout back again

        if layer ==1:
            pred = (net.layer1[:,node] >= 0.5).float()
        if layer ==2:
            pred = (net.layer2[:,node] >= 0.5).float()


        # plot function computed by model
        plt.clf()
        plt.pcolormesh(xrange,yrange,pred.cpu().view(yrange.size()[0],xrange.size()[0]), cmap='Wistia')


1. def forward(self, x):
2.         alpha = torch.randn(1,requires_grad= True).to(device = 'cuda')
3.         beta = torch.randn(1,requires_grad= True).to(device = 'cuda')
4.         out = F.relu(self.bn1(self.conv1(x)))
5.         out = self.bn2(self.conv2(out))
6.         num = torch.atan(torch.div((alpha*x),torch.sqrt((beta**2)+1)))
7.         num = num.to(device = 'cuda')
8.         den = alpha * torch.sqrt((beta**2)+1)
9.         den = den.to(device = 'cuda')
10.       x_tan = torch.div(num ,den).to(device = 'cuda')
11.       out = F.relu(out)
12.         return out


class BasicBlock(nn.Module):
2.     expansion = 1
3.     def __init__(self, in_planes, planes, stride=1):
4.         super(BasicBlock, self).__init__()
5.         self.conv1 = nn.Conv2d(
6.             in_planes, planes, kernel_size=3, stride=stride, padding=1, bias=False)
7.         self.bn1 = nn.BatchNorm2d(planes)
8.         self.conv2 = nn.Conv2d(planes, planes, kernel_size=3,
9.                                stride=1, padding=1, bias=False)
10.         self.bn2 = nn.BatchNorm2d(planes)
11.         self.shortcut = nn.Sequential()
12.         if stride != 1 or in_planes != self.expansion*planes:
13.             self.shortcut = nn.Sequential(
14.                 nn.Conv2d(in_planes, self.expansion*planes,
15.                           kernel_size=1, stride=stride, bias=False),
16.                 nn.BatchNorm2d(self.expansion*planes)
17.             )
18.         self.alpha = nn.Parameter(torch.rand(1))
19.         self.beta = nn.Parameter(torch.rand(1))

20.     def forward(self, x):
21.         #alpha = torch.randn(1,requires_grad= True).to(device = 'cuda')
22.         #beta = torch.randn(1,requires_grad= True).to(device = 'cuda')
23.
24.         out = F.relu(self.bn1(self.conv1(x)))
25.         out = self.bn2(self.conv2(out))
26.         # num = torch.atan(torch.div((alpha*x),torch.sqrt((beta**2)+1)))
27.         # num = num.to(device = 'cuda')
28.         # den = alpha * torch.sqrt((beta**2)+1)
29.         # den = den.to(device = 'cuda')
30.         x_tan = torch.div(torch.atan(torch.div((self.alpha*x),torch.sqrt((self.beta**2)+1))) ,self.alpha * torch.sqrt((self.beta**2)+1))
31.         out += self.shortcut(x_tan)
32.         out = F.relu(out)
33.         return out
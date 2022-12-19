# n = 90 is the number of tokens,
# the 270 corresponds to 3n
# the 50 is the wordvector size

tensor1 = torch.randn(10, 3, 4)
>>> tensor2 = torch.randn(10, 4, 5)
>>> torch.matmul(tensor1, tensor2).size()
torch.Size([10, 3, 5])



B = torch.randn(90,270)
A = torch.randn(32,90,50)
C=torch.matmul(B,A)
Traceback (most recent call las
cd("/Users/user/PycharmProjects/NN_Assess_3")
dir


fname = 'train.json'; 
fid = fopen(fname); 
raw = fread(fid,inf); 
str = char(raw'); 
fclose(fid);

data = JSON.parse(str)

%value = {'businessCategory'; 'rating'; 'reviewText'};

%val = jsondecode(str); 
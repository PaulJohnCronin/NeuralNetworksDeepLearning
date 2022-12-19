% this programs determine which ngrams are most useful

% load each review as a set of ngrams
no_words = 19915;
fileID = fopen('reviews_ngrams.txt','r');
load_data = uint8(fread(fileID,[no_words,50000],'uint8'));
fclose(fileID)
raw_data = load_data';
clear load_data

% loads the business category data and codes it
fileID = fopen('bus_cat.txt','r');
B = fread(fileID,'uint8')';
fclose(fileID);

% loads the ratings category data and codes it
fileID = fopen('rat_cat.txt','r');
R = fread(fileID,'uint8')';
fclose(fileID);

% forms the results matrix
bMatrix = zeros(50000,7);
for i = 1:50000
    bMatrix(i,B(i)+1)=1;
    bMatrix(i,R(i)+6)=1;
end

% normalizes the review and results data
normalized_data = normalize(single(raw_data));
bMatrix = normalize(bMatrix,2);
clear raw_data

% computes the weights for each ngram
weights = lsqminnorm(normalized_data,bMatrix);

% computes the most import ngrams in order
norm_data = vecnorm(weights,2,2);
optimal_ngams = sort(norm_data,'descend');
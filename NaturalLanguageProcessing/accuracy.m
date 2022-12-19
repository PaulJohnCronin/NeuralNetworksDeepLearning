% using all the data, the accuracy is 88.43 percent accurate
% using the 100 most common words is 48.40 percenta accurate

%temp = 1:no_words;
%norm_data = vecnorm(weights,2,2);
%[dummy, best_seq] = sort(norm_data,'descend');
%[dummy, worst_seq] = sort(norm_data,'ascend');
%rand_seq = temp(randperm(no_words));

best_data=normalized_data(:,best_seq(1));
worst_data = normalized_data(:,worst_seq(1));
rand_data = normalized_data(:,rand_seq(1));
best_weights=weights(best_seq(1),:);
worst_weights = weights(worst_seq(1),:);
rand_weights = weights(rand_seq(1),:);

blocks = 6000;
i = 2
for j=0:blocks-1
    best_data = cat(2,best_data,normalized_data(:,best_seq(i+j)));
    worst_data = cat(2,worst_data,normalized_data(:,worst_seq(i+j)));
    rand_data = cat(2,rand_data,normalized_data(:,rand_seq(i+j)));
    
    best_weights = cat(1,best_weights,weights(best_seq(i+j),:));
    worst_weights = cat(1,worst_weights,weights(worst_seq(i+j),:));
    rand_weights = cat(1,rand_weights,weights(rand_seq(i+j),:));
end

%best_correctB = zeros(no_words,1);
%worst_correctB = zeros(no_words,1);
%rand_correctB = zeros(no_words,1);
%best_correctR = zeros(no_words,1);
%worst_correctR = zeros(no_words,1);
%rand_correctR = zeros(no_words,1);

blocks = 200
for i=6200:blocks:no_words
    for j=0:blocks-1
        best_data = cat(2,best_data,normalized_data(:,best_seq(i+j)));
        worst_data = cat(2,worst_data,normalized_data(:,worst_seq(i+j)));
        rand_data = cat(2,rand_data,normalized_data(:,rand_seq(i+j)));
    
        best_weights = cat(1,best_weights,weights(best_seq(i+j),:));
        worst_weights = cat(1,worst_weights,weights(worst_seq(i+j),:));
        rand_weights = cat(1,rand_weights,weights(rand_seq(i+j),:));
    end
    
    best_res = best_data*best_weights;
    worst_res = worst_data*worst_weights;
    rand_res = rand_data*rand_weights;
    
    for j =1:50000
        [dummy,indexB] = max(best_res(j,1:5));
        [dummy,indexR] = max(best_res(j,6:7));
        if B(j) == indexB-1
            best_correctB(i) = best_correctB(i)+1;
        end
        if R(j) == indexR-1
            best_correctR(i) = best_correctR(i)+1;
        end
    end
    
    for j =1:50000
        [dummy,indexB] = max(worst_res(j,1:5));
        [dummy,indexR] = max(worst_res(j,6:7));
        if B(j) == indexB-1
            worst_correctB(i) = worst_correctB(i)+1;
        end
        if R(j) == indexR-1
            worst_correctR(i) = worst_correctR(i)+1;
        end

    end
    
    for j =1:50000
        [dummy,indexB] = max(rand_res(j,1:5));
        [dummy,indexR] = max(rand_res(j,6:7));
        if B(j) == indexB-1
            rand_correctB(i) = rand_correctB(i)+1;
        end
        if R(j) == indexR-1
            rand_correctR(i) = rand_correctR(i)+1;
        end

    end
    disp([i, best_correctB(i)/500,worst_correctB(i)/500,rand_correctB(i)/500])
    disp([i, best_correctR(i)/500,worst_correctR(i)/500,rand_correctR(i)/500])
end
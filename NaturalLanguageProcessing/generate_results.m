best_new = zeros(400,7);
index = 0
for i=1:length(best_correctB)
    if best_correctB(i)>0
        index=index+1;
        best_new(index,1) = i;
        best_new(index,2) = best_correctB(i);
        best_new(index,3) = best_correctR(i);
        best_new(index,4) = rand_correctB(i);
        best_new(index,5) = rand_correctR(i);
        best_new(index,6) = worst_correctB(i);
        best_new(index,7) = worst_correctR(i);

    end
end

index

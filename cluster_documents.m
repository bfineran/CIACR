data = csvread('./document_data.dat');
data(sum(data,2) > 1,:)=[];
k = 7

idx = kmeans(data,k);
histogram(idx)
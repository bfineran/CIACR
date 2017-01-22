data = csvread('./document_data.dat');
k = 6

idx = kmeans(data,k);
histogram(idx)
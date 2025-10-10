function [NLf] = N(matriz)
NL = [];
[MaxR,MaxC] = size(matriz);
for i=1:MaxR
    for j=1:MaxC
        NL(i,j) = matriz(i,j)/i;
    end
end
NLf = sum(NL);
end
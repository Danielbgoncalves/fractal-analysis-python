function ScriptPERCLACDF3Distances(diretorio_org,destino)
%%Extração de atributos DF, LAC e PERC locais e globais
%%com uso das métricas de distância Chessboard, Euclidi-
%%ana e Manhatan a partir de imagens RGB.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%Guilherme Freire Roberto

%Base LA: uma imagem da class4 foi removida. Corrigir os folds

%%Valor máximo de L
maxr = 41;

%%
%Classe 1
Imagens = dir([diretorio_org '/*.png']);
Tipo = split(diretorio_org,'\');
disp(strcat('Coletando características Fractais das Imagens - ',Tipo{end}))
tic
for n=1:length(Imagens)
originais=Imagens(n).name;
fullname=fullfile(Imagens(n).folder,originais);
PIC=imread(fullname);
PIC = imresize(PIC,[224,224],'bilinear');

disp(strcat('Calculando características fractais - Percolação(',num2str(n),'/',num2str(length(Imagens)),')'))
%PERC
[MinkMaxClusterIndex, MinkMaxPercIndex, MinkMaxMaxClusterIndex, MinkAreaRatioMaxCluster, MinkMaxMaxCluster, MinkSkewnessMaxCluster, MinkAreaMaxCluster, MinkAreaRatioCluster, MinkAreaRatioPerc, MinkMaxCluster, MinkMaxPerc, MinkSkewnessCluster, MinkSkewnessPerc, MinkAreaPerc, MinkAreaCluster, Minkp, Minkg, Minkh] = clustperc(PIC,maxr);
[EuclMaxClusterIndex, EuclMaxPercIndex, EuclMaxMaxClusterIndex, EuclAreaRatioMaxCluster, EuclMaxMaxCluster, EuclSkewnessMaxCluster, EuclAreaMaxCluster, EuclAreaRatioCluster, EuclAreaRatioPerc, EuclMaxCluster, EuclMaxPerc, EuclSkewnessCluster, EuclSkewnessPerc, EuclAreaPerc, EuclAreaCluster, Euclp, Euclg, Euclh] = clustpercEucl(PIC,maxr);
[ManhMaxClusterIndex, ManhMaxPercIndex, ManhMaxMaxClusterIndex, ManhAreaRatioMaxCluster, ManhMaxMaxCluster, ManhSkewnessMaxCluster, ManhAreaMaxCluster, ManhAreaRatioCluster, ManhAreaRatioPerc, ManhMaxCluster, ManhMaxPerc, ManhSkewnessCluster, ManhSkewnessPerc, ManhAreaPerc, ManhAreaCluster, Manhp, Manhg, Manhh] = clustpercManh(PIC,maxr);


disp(strcat('Calculando características fractais - Minkowski(',num2str(n),'/',num2str(length(Imagens)),')'))
%Minkowski LAC DF
MatrizProb = pmr(PIC, maxr);
MinkLAC = lacunaridade(MatrizProb);
r = 3:2:maxr;
MinkAreaLAC = trapz(MinkLAC);
MinkSkewnessLAC = skewness(MinkLAC);
half = ceil(length(MinkLAC)/2);
MinkAreaRatioLAC = trapz(MinkLAC(half+1:end))/trapz(MinkLAC(1:half));
[MinkMaxLAC, MinkMaxLACIndex] = max(MinkLAC);
Minknn = N(MatrizProb);
x = log(r);
y = -log(Minknn);
X = x.';
Y = y.';
mdl = fitlm(X, Y, 'RobustOpts', 'on');
MinkDF = mdl.Coefficients.Estimate(2);
disp(strcat('Calculando características fractais - Euclidian(',num2str(n),'/',num2str(length(Imagens)),')'))
%Euclidian LAC DF
MatrizProb = pmrEucl(PIC, maxr);
EuclLAC = lacunaridade(MatrizProb);
r = 3:2:maxr;
EuclAreaLAC = trapz(EuclLAC);
EuclSkewnessLAC = skewness(EuclLAC);
half = ceil(length(EuclLAC)/2);
EuclAreaRatioLAC = trapz(EuclLAC(half+1:end))/trapz(EuclLAC(1:half));
[EuclMaxLAC, EuclMaxLACIndex] = max(EuclLAC);
Euclnn = N(MatrizProb);
x = log(r);
y = -log(Euclnn);
X = x.';
Y = y.';
mdl = fitlm(X, Y, 'RobustOpts', 'on');
EuclDF = mdl.Coefficients.Estimate(2);
disp(strcat('Calculando características fractais - Manhattan(',num2str(n),'/',num2str(length(Imagens)),')'))
%Manhattan LAC DF
MatrizProb = pmrManh(PIC, maxr);
ManhLAC = lacunaridade(MatrizProb);
r = 3:2:maxr;
ManhAreaLAC = trapz(ManhLAC);
ManhSkewnessLAC = skewness(ManhLAC);
half = ceil(length(ManhLAC)/2);
ManhAreaRatioLAC = trapz(ManhLAC(half+1:end))/trapz(ManhLAC(1:half));
[ManhMaxLAC, ManhMaxLACIndex] = max(ManhLAC);
Manhnn = N(MatrizProb);
x = log(r);
y = -log(Manhnn);
X = x.';
Y = y.';
mdl = fitlm(X, Y, 'RobustOpts', 'on');
ManhDF = mdl.Coefficients.Estimate(2);



clear PIC;
%clear AC
final=strcat(num2str(n),'.mat');
filename=fullfile(destino,final);
save(filename);
toc
end
end

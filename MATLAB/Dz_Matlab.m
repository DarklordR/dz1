% Импортируйте данные из csv-файлов
spectra = importdata('spectra.csv');
starNames = importdata('star_names.csv');
lambdaStart = importdata('lambda_start.csv');
lambdaDelta = importdata('lambda_delta.csv');

% Определите константы
lambdaPr = 656.28; %нм
speedOfLight = 299792.458; %км/c

% Определите диапазон длин волн
nSt = size(starNames);
speed = [];
nObs = size(spectra, 1);
movaway = starNames;

lambdaEnd = lambdaStart + (nObs - 1) * lambdaDelta;
lambda = (lambdaStart : lambdaDelta : lambdaEnd)';

% Рассчитайте скорости звезд относительно Земли
for i=1:nSt
    s = spectra(:, i);
    [sHa,idx] = min(s);
    lambdaHa = lambda(idx);

    z = (lambdaHa / lambdaPr) - 1;
    speed = [speed; z * speedOfLight];
end 



% Постройте график
fg1 = figure;
title('Спектры звезд')
grid on
hold on
xlabel('Длина волны, нм')
ylabel(['Интенсивность, эрг/см^2/с/', char(197)])
text(635, 3.3*10^-13, 'Крейнин Роман Б01-005')
legend('Location', 'northeast')
set(fg1, 'visible', 'on');

for i=1:nSt    
    s = spectra(:, i);
    if speed(i) >= 0
            plot(lambda, s, "-", 'LineWidth' , 3, "DisplayName", starNames{i})
    end
    
    if speed(i) < 0
            plot(lambda, s, "--", 'LineWidth' , 1, "DisplayName", starNames{i})
    end
end
hold off 

% Сохраните график
saveas(fg1, 'spectra.png')
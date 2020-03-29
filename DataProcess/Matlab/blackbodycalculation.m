
h = 6.63*10^-34;
c = 3*10^8;
k = 1.38*10^-23;
T = 500;
w = [1:0.1:30]'*10^-6;
v = c*([0.5:0.05:30]'*10^-6).^-1;
B = 10^-6*(2*h*c^2*w.^-5).*((exp(h*c/(k*T).*w.^-1))-1).^-1;
x = w*10^6;
peaks=[];


%fit tem and transmissivity
%{
fitx = x(peaks(:,1));
fitT = [273:20:373];
p11 =   8.482e-05; 
p21 =    -0.08294; 
p31 =       26.92;
TemT = 323;%temperature threshold
TT =  round(p11*TemT^2 + p21*TemT + p31,2); %transmission threshold
%}

TT = 12;


fun = @(x) (10^-6)*(2*h*c^2*x.^-5).*((exp(h*c/(k*T).*x.^-1))-1).^-1;
q = integral(fun,1*10^-6,30*10^-6);

CoolE= [];
WarmE= [];

%cool/warm efficiency calculation
for T = 273:10:373
    fun = @(x) (10^-6)*(2*h*c^2*x.^-5).*((exp(h*c/(k*T).*x.^-1))-1).^-1;
    emit = integral(fun,1*10^-6,TT*10^-6);
    nonemit = integral(fun,TT*10^-6,30*10^-6);
    q = integral(fun,1*10^-6,30*10^-6);
    cooleff = (emit-nonemit)/q;
    CoolE= [CoolE;[T-273,cooleff]];
end

for T = 273:20:373
    B = 10^-6*(2*h*c^2*w.^-5).*((exp(h*c/(k*T).*w.^-1))-1).^-1;
    [pks,locs] = findpeaks(B);
    peaks=[peaks;[locs,pks]];
    x1 = [1:0.1:TT]';
    w1 = x1*10^-6;
    B1 = 10^-6*(2*h*c^2*w1.^-5).*((exp(h*c/(k*T).*w1.^-1))-1).^-1;
    plot(x1,B1,'Color',[(T-233)/140,(373-T)/255,(373-T)/255],'DisplayName',sprintf('T= %d K', T));
    hold on
    x2 = [TT:0.1:25]';
    w2 = x2*10^-6;
    B2 = 10^-6*(2*h*c^2*w2.^-5).*((exp(h*c/(k*T).*w2.^-1))-1).^-1;
    plot(x2,B2,'--','Color',[(T-233)/140,(373-T)/255,(373-T)/255],'DisplayName',sprintf('T= %d K', T));
    name = sprintf('T= %d K', T);
    scatter(x(locs),pks,'filled','MarkerEdgeColor',[(T-233)/140,(373-T)/255,(373-T)/255],'markerfacecolor',[(T-233)/140,(373-T)/255,(373-T)/255])
    text(x(locs)+0.2,pks+1,name,'Color',[(T-233)/140,(373-T)/255,(373-T)/255],'Fontsize',10)
end


%{
forfitx = x(peaks(:,1));
forfity = peaks(:,2);
p1 =       2.524; 
p2 =      -54.26;  
p3 =       298.2;
fity =  p1*forfitx.^2 + p2.*forfitx + p3;
%}


ylim([0 35])
xlim([1 25])
xlabel('Wavelength(\mum)','fontsize',14)
ylabel('Spectral Radiance','fontsize',14)


%draw the threshold
%{
yyaxis right

plot([1,TT],[1,1],'-')
plot([TT,TT],[1,0],'-')
plot([TT,30],[0,0],'-')
ylim([-0.02 1.1])


text(TT+0.3,1, sprintf('Transmissivity Threshold = %g um',TT))
ylabel('Transmissivity','fontsize',14)
%}




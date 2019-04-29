function ANStaskAnalysis

dataDir = uigetdir;
d = dir(fullfile(dataDir,'*.xls'));
subIDs = {d(:).name}';
%disp(subIDs);
n=length(subIDs);

ANS_allSub=[];

for i=1:n
    ANS_data=zeros(1,17);
    clf
    ID=subIDs(i);
    IDnum = extractBetween(ID,6,8);
    subID=string(IDnum);
    ANS_data(i,1)=subID;
    
    subData=readtable(sprintf('ANS_p%s.xls',subID),'Sheet','summary');
    
    T=subData(2,3);
    ANS_data(i,2)=T{:,:};
    
    for ii=1:13
        r=subData(2,ii+3);
        ANS_data(i,ii+2)=r{:,:};
    end
    
    all=subData(2,17);
    all=all{:,:};
    all=string(all);
    all=str2num(all);
    ANS_data(i,16)=all;
    
    WF=subData(2,32);
    ANS_data(i,17)=WF{:,:};
    
    colNames={'subID','ANSnumTrial','ANS_1058','ANS_11225','ANS_1194','ANS_12519','ANS_13349','ANS_14074','ANS_15','ANS_15854','ANS_16753','ANS_17873','ANS_18847','ANS_2','ANS_25080','ANS_overall','ANS_WeberFraction'};
    data=num2cell(ANS_data(end,:));
    ANSsubDataSummary = cell2struct(data, colNames, 2);
    
    ANSsubData=struct2dataset(ANSsubDataSummary);
    
    path=(sprintf('sub_data/data_%s',subID));
    path1=(sprintf('sub_data/dataset_%s',subID));
    save(path,'ANSsubDataSummary')
    save(path1,'ANSsubData')
    
    ANS_allSub=cat(1,ANS_allSub,ANSsubData);
    
    ratios=[1.058,1.1225,1.1940,1.2519,1.3349,1.4074,1.5,1.5854,1.6753,1.7873,1.8847,2,2.508];
    
    X=ratios';
    y=ANSsubData(1,3:15);
    y=double(y);
    Y=y';
    [curvefit,gof,output]=fit(X,Y,'poly1','normalize','on');
    figure(3)
    plot(curvefit,X,Y)
    %plot(ratios,ANSsubData(1,3:15),'-x')
    hold on
    title(sprintf('ANS accuracy by ratio %s',subID))
    xlabel('ratio')
    ylabel('accuracy')
    %legend('block1 trial','
    
    
    hold off
    
    savefig(figure(3),sprintf('figures/subANS%s.fig',subID))
    
end

ave_acc=mean(double(ANS_allSub(:,3:15)));

ratios=[1.058,1.1225,1.1940,1.2519,1.3349,1.4074,1.5,1.5854,1.6753,1.7873,1.8847,2,2.508];
x2=ratios';
y2=ave_acc';
[curvefit,gof,output]=fit(x2,y2,'poly1','normalize','on');
figure(5)
plot(curvefit,x2,y2)
hold on
title('ANS accuracy by ratio All Sub Average')
xlabel('ratio')
ylabel('accuracy')
hold off
savefig(figure(5),'figures/ANS_allAve.fig')

disp(curvefit)
disp(gof)
disp(output)

text(1.15,109,'SSE=608.6864')
text(1.15,107,'rsquare=0.6389')
text(1.15,105,'adjrsquare=0.6061')

[R,P,RLO,RUP]=corrcoef(x2,y2,'alpha',0.05);

disp(R)
disp(P)


path2=('sub_data/ANS_Alldata');
save(path2,'ANS_allSub')




end

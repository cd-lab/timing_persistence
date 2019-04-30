%% 
load('subDataSummary_allTask.mat')

dataAllTask=struct2dataset(subDataSummary);

k=isoutlier(dataAllTask.Timing_accuracy);
a=find(k==1);

n=length(a);
i=0;
while i<n
    
    disp(dataAllTask.subID(a(end-i)))
    dataAllTask(a(end-i),:) = [];
    
    i=i+1;
end

path=('subDataAll_outliers.mat');
save(path,'dataAllTask')

[R,P,RLO,RUP]=corrcoef(dataAllTask.WTWreward_ttl,dataAllTask.Timing_accuracy,'alpha',0.05);


figure(2)
[curvefit,gof,output]=fit(dataAllTask.WTWreward_ttl,dataAllTask.Timing_accuracy,'poly1','normalize','on');
plot(curvefit,dataAllTask.WTWreward_ttl,dataAllTask.Timing_accuracy)
hold on
title('timing accuracy VS total reward,discard outliers')
xlabel('WTW total reward')
ylabel('Timing task total accuracy')
legend('per subject','linear fit')

text(730,0.99,'SSE=0.1097')
text(730,0.98,'r-square=0.0579')
text(730,0.97,'adjusted r-square=0.0284')
text(730,0.96,'r=0.2405')
text(730,0.95,'p-value=0.1706')

disp(curvefit)
disp(gof)
disp(output)

%600,563,560,461

hold off

savefig(figure(2),sprintf('timing_WTW.fig'))

%% 

load('/Users/ttli/Documents/GitHub/timing_persistence/Panamath_data/sub_data/ANS_Alldata.mat')

load('wtw_timingData.mat')


AllTaskData=join(dataAllTask,ANS_allSub);
path=('AllTaskData');
save(path,'AllTaskData')

%% 
figure(20)
[curvefit,gof,output]=fit(AllTaskData.WTWreward_ttl,AllTaskData.Timing_accuracy,'poly1','normalize','on');
plot(curvefit,AllTaskData.WTWreward_ttl,AllTaskData.Timing_accuracy)
hold on
title('Timing accuracy VS total reward,discard outliers')
xlabel('WTW total reward')
ylabel('Timing task total accuracy')
legend('per subject','linear fit')

disp(curvefit)
disp(gof)
disp(output)

save('gof_TimingWTW','gof')

text(730,0.99,sprintf('SSE=%s',gof.sse))
text(730,0.98,sprintf('rsquare=%s',gof.rsquare))
text(730,0.97,sprintf('adjrsquare=%s',gof.adjrsquare))


[R,P,RLO,RUP]=corrcoef(AllTaskData.WTWreward_ttl,AllTaskData.Timing_accuracy,'alpha',0.05);
disp(R)
disp(P)
%600,563,560,461

pearson=[R,P,RLO,RUP];
save('pearson_TimingWTW','pearson')

text(730,0.96,sprintf('r=%s',R(2)))
text(730,0.95,sprintf('p-value=%s',P(2)))

hold off

savefig(figure(20),sprintf('Timing_WTW.fig'))
%% 
figure(16)
[curvefit,gof,output]=fit(AllTaskData.WTWreward_ttl,AllTaskData.ANS_overall,'poly1','normalize','on');
plot(curvefit,AllTaskData.WTWreward_ttl,AllTaskData.ANS_overall)
hold on
title('ANS accuracy VS total reward,discard outliers')
xlabel('WTW total reward')
ylabel('ANS task total accuracy')
legend('per subject','linear fit')

disp(curvefit)
disp(gof)
disp(output)

save('gof_ANSWTW','gof')


text(730,94,sprintf('SSE=%s',gof.sse))
text(730,93,sprintf('rsquare=%s',gof.rsquare))
text(730,92,sprintf('adjrsquare=%s',gof.adjrsquare))


[R,P,RLO,RUP]=corrcoef(AllTaskData.WTWreward_ttl,AllTaskData.ANS_overall,'alpha',0.05);
disp(R)
disp(P)
%600,563,560,461

pearson=[R,P,RLO,RUP];
save('pearson_ANSWTW','pearson')

text(730,91,sprintf('r=%s',R(2)))
text(730,90,sprintf('p-value=%s',P(2)))

hold off

savefig(figure(16),sprintf('ANS_WTW.fig'))

%% 
figure(18)
[curvefit,gof,output]=fit(AllTaskData.Timing_accuracy,AllTaskData.ANS_overall,'poly1','normalize','on');
plot(curvefit,AllTaskData.Timing_accuracy,AllTaskData.ANS_overall)
hold on
title('Timing accuracy VS ANS accuracy,discard outliers')
xlabel('Timing task total accuracy')
ylabel('ANS task total accuracy')
legend('per subject','linear fit')

disp(curvefit)
disp(gof)
disp(output)

save('gof_ANSTiming','gof')

text(0.730,94,sprintf('SSE=%s',gof.sse))
text(0.730,93,sprintf('rsquare=%s',gof.rsquare))
text(0.730,92,sprintf('adjrsquare=%s',gof.adjrsquare))


[R,P,RLO,RUP]=corrcoef(AllTaskData.Timing_accuracy,AllTaskData.ANS_overall,'alpha',0.05);
disp(R)
disp(P)
%600,563,560,461

pearson=[R,P,RLO,RUP];
save('pearson_ANSTiming','pearson')

text(0.730,91,sprintf('r=%s',R(2)))
text(0.730,90,sprintf('p-value=%s',P(2)))

hold off

savefig(figure(18),sprintf('Timing_ANS.fig'))
%% 

[h,p] = ttest(AllTaskData.WTWfitSlope_bk1,AllTaskData.WTWfitSlope_bk2) ;

l=length(AllTaskData);
new=NaN(l,1);
for p=1:l
    if AllTaskData.WTWfitSlope_bk1(p)<0 & AllTaskData.WTWfitSlope_bk2(p)>0
        new(p,1)=1;
    else
        new(p,1)=0;
    end
end


AllTaskData.Properties.VarNames{30} = 'WTW_adjusted';



%% 
ll=length(AllTaskData);
new=NaN(ll,1);
adjustedSum=zeros(1,3);
notadjustedSum=zeros(1,3);
n1=0;
n2=0;
for c=1:ll
    if AllTaskData.WTW_adjusted(c)==1
        n1=n1+1;
        adjustedSum(1,1)=adjustedSum(1,1)+AllTaskData.WTWreward_ttl(c);
        adjustedSum(1,2)=adjustedSum(1,2)+AllTaskData.Timing_accuracy(c);
        adjustedSum(1,3)=adjustedSum(1,3)+AllTaskData.ANS_overall(c);
    else
        n2=n2+1;
        notadjustedSum(1,1)=notadjustedSum(1,1)+AllTaskData.WTWreward_ttl(c);
        notadjustedSum(1,2)=notadjustedSum(1,2)+AllTaskData.Timing_accuracy(c);
        notadjustedSum(1,3)=notadjustedSum(1,3)+AllTaskData.ANS_overall(c);
    end
end

meanAdj=adjustedSum/n1;
meanNAdj=notadjustedSum/n2;

A=cat(1,meanAdj,meanNAdj);
%% 
load('all_TimingData.mat')

[H,P,CI,STATS] = ttest(plotAll_data(1:5,4),plotAll_data(6:10,4)) ;


%% 

LP=table2array(scheduledWaitLP);
uLP=unique(LP);

a=find(LP==uLP(1));
b=find(LP==uLP(2));
c=find(LP==uLP(3));
d=find(LP==uLP(4));
e=find(LP==uLP(5));
f=find(LP==uLP(6));
g=find(LP==uLP(7));
h=find(LP==uLP(8));

HP=table2array(scheduledWaitHP);
uHP=unique(HP);

a=find(HP==uHP(1));
b=find(HP==uHP(2));
c=find(HP==uHP(3));
d=find(HP==uHP(4));
e=find(HP==uHP(5));
f=find(HP==uHP(6));
g=find(HP==uHP(7));
h=find(HP==uHP(8));


load('AllTaskData.mat')

figure(12)
plot(AllTaskData.WTWauc_bk1,AllTaskData.WTWauc_bk2,'bx')
hold on
plot(uLP(5),16,'ro')
plot(AllTaskData.WTWauc_bk1,AllTaskData.WTWauc_bk1,'r-')
title('HP AUC vs LP AUC')
xlabel('LP AUC')
ylabel('HP AUC')
legend('per subject','optimal')
hold off

LPdiff=abs(AllTaskData.WTWauc_bk1-uLP(5));
HPdiff=abs(AllTaskData.WTWauc_bk2-16);

ttldiff=LPdiff+HPdiff;

%% 
figure(5)
plot(AllTaskData.WTW_diffOptimal,AllTaskData.WTWreward_ttl,'bx')
hold on

[curvefit,gof,output]=fit(AllTaskData.WTW_diffOptimal,AllTaskData.WTWreward_ttl,'poly1','normalize','on');
plot(curvefit,'-r')%,AllTaskData.WTW_diffOptimal,AllTaskData.WTWreward_ttl)

[R,P,RLO,RUP]=corrcoef(AllTaskData.WTW_diffOptimal,AllTaskData.WTWreward_ttl,'alpha',0.05);

title('Total WTW reward VS Performance Optimality')
xlabel('AUC difference from optimal')
ylabel('Total reward earned')

text(4.5,850,sprintf('SSE=%s',gof.sse))
text(4.5,830,sprintf('rsquare=%s',gof.rsquare))
text(4.5,810,sprintf('adjrsquare=%s',gof.adjrsquare))
text(4.5,790,sprintf('r=%s',R(2)))
text(4.5,770,sprintf('p-value=%s',P(2)))

legend('per subject','linear fit')
hold off


%% 
figure(6)
plot(AllTaskData.WTW_diffOptimal,AllTaskData.Timing_accuracy,'bx')
hold on

[curvefit,gof,output]=fit(AllTaskData.WTW_diffOptimal,AllTaskData.Timing_accuracy,'poly1','normalize','on');
plot(curvefit,'-r')%AllTaskData.WTW_diffOptimal,AllTaskData.Timing_accuracy)

[R,P,RLO,RUP]=corrcoef(AllTaskData.WTW_diffOptimal,AllTaskData.Timing_accuracy,'alpha',0.05);

title('Timing accuracy VS WTW Performance Optimality')
xlabel('WTW AUC difference from optimal')
ylabel('Timing accuracy')

text(5,0.81,sprintf('SSE=%s',gof.sse))
text(5,0.8,sprintf('rsquare=%s',gof.rsquare))
text(5,0.79,sprintf('adjrsquare=%s',gof.adjrsquare))
text(5,0.78,sprintf('r=%s',R(2)))
text(5,0.77,sprintf('p-value=%s',P(2)))

legend('per subject','linear fit')

hold off

%% 
figure(7)
plot(AllTaskData.WTW_diffOptimal,AllTaskData.ANS_overall,'bx')
hold on

[curvefit,gof,output]=fit(AllTaskData.WTW_diffOptimal,AllTaskData.ANS_overall,'poly1','normalize','on');
plot(curvefit,'-r')%AllTaskData.WTW_diffOptimal,AllTaskData.Timing_accuracy)

[R,P,RLO,RUP]=corrcoef(AllTaskData.WTW_diffOptimal,AllTaskData.ANS_overall,'alpha',0.05);

title('ANS accuracy VS WTW Performance Optimality')
xlabel('WTW AUC difference from optimal')
ylabel('ANS accuracy')

text(5,81,sprintf('SSE=%s',gof.sse))
text(5,80,sprintf('rsquare=%s',gof.rsquare))
text(5,79,sprintf('adjrsquare=%s',gof.adjrsquare))
text(5,78,sprintf('r=%s',R(2)))
text(5,77,sprintf('p-value=%s',P(2)))

legend('per subject','linear fit')

hold off
%% 


%y=polyval(params,data_allTaskmedian.WTWreward_ttl);
%plot(data_allTaskmedian.WTWreward_ttl, y, 'r-')


%text(730,79,sprintf('slope: %s', params(1)))
%text(730,78,'r=0.25')
%text(730,77,'p-value=0.1538')
%[R,P,RLO,RUP]=corrcoef(data_allTaskmedian.WTWreward_ttl,data_allTaskmedian.Timing_acc,'alpha',0.05);
%disp([R,P,RLO,RUP])

%text(730,75,sprintf('R: %s', R))
%a=struct2cell(subDataSummary)'
%colNames = {'subID','WTWreward_bk1','WTWreward_bk2','WTWreward_ttl','WTWauc_bk1','WTWauc_bk2','WTWfitSlope_bk1','WTWfitParam_bk1','WTWfitSlope_bk2','WTWfitParam_bk2','Timing_ttlCorrect','Timing_trialNum','Timing_accuracy'};
%all=[a,all]
%subDataSummary = cell2struct(all, colNames, 2)
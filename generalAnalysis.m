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

load('Panamath_data/sub_data/ANS_Alldata.mat')

load('subDataAll_outliers.mat')


AllTaskData=join(dataAllTask,ANS_allSub);
path=('AllTaskData');
save(path,'AllTaskData')

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

text(730,94,'SSE=628.7685')
text(730,93,'r-square=0.0195')
text(730,92,'adjusted r-square=-0.0112')
text(730,91,'r=0.1396')
text(730,90,'p-value=0.4311')

[R,P,RLO,RUP]=corrcoef(AllTaskData.WTWreward_ttl,AllTaskData.ANS_overall,'alpha',0.05);
disp(R)
disp(P)
%600,563,560,461

hold off

savefig(figure(16),sprintf('ANS_WTW.fig'))

%% 
figure(18)
[curvefit,gof,output]=fit(AllTaskData.Timing_accuracy,AllTaskData.ANS_overall,'poly1','normalize','on');
plot(curvefit,AllTaskData.Timing_accuracy,AllTaskData.ANS_overall)
hold on
title('Timing accuracy VS ANS accuracy')
xlabel('ANS task total accuracy')
ylabel('Timing task total accuracy')
legend('per subject','linear fit')

disp(curvefit)
disp(gof)
disp(output)

text(0.730,94,'SSE=592.2557')
text(0.730,93,'r-square=0.0764')
text(0.730,92,'adjusted r-square=0.0476')
text(0.730,91,'r=0.2764')
text(0.730,90,'p-value=0.1135')

[R,P,RLO,RUP]=corrcoef(AllTaskData.Timing_accuracy,AllTaskData.ANS_overall,'alpha',0.05);
disp(R)
disp(P)
%600,563,560,461

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
function timingTaskAnalysis

dataDir = uigetdir;
d = dir(fullfile(dataDir,'*.csv'));
subIDs = {d(:).name}';
%disp(subIDs);
n=length(subIDs);

%addpath('data')

ttl_accuracy=NaN(n,5);

all_data=[];

for i=1:n
    clf
    ID=subIDs(i);
    name=string(ID);
    IDnum = extractBetween(ID,1,3);
    subID=string(IDnum);
    ttl_accuracy(i,1)=subID;
    subTimingData=NaN(80,5);
    
    subData=importdata(sprintf('data/%s',name));
    
    %acc_str=string(subData.textdata(:,27));
    %acc_num=str2double(acc_str);
    %ttl_accuracy(i,2)=nansum(acc_num);
    
    dataStr=string(subData.textdata);
    dataNum=str2double(dataStr);
    
    r=0;
    for j=1:length(dataNum)
        if isnan(dataNum(j,1))==0
            r=r+1;
            subTimingData(r,1)=dataNum(j,1);
            subTimingData(r,2)=dataNum(j,2);
            subTimingData(r,3)=dataNum(j,1)/dataNum(j,2);
            subTimingData(r,4)=dataNum(j,27);
            subTimingData(r,5)=dataNum(j,28);
        end
    end
    
    cellData=num2cell(subTimingData);
    colNames={'Timing_Stim1','Timing_Stim2','Timing_ratio','Timing_Correct','Timing_RT'};
    structData=cell2struct(cellData,colNames,2);
    
    outlier_row=isoutlier(subTimingData(:,5),'median');
    
    [row]=find(outlier_row==1);
    
    prev_out=0;
    for ii=1:length(row)
        out=row(ii)-prev_out;
        structData(out) = [];
        prev_out=prev_out+1;
    end
    
    path=(sprintf('dataSum/TimingTaskData_%s',subID));
    save(path,'structData')
    
    
    dataSet=struct2dataset(structData);
    rate=unique(dataSet.Timing_ratio);
    ratios=round(rate,4);
    ratios=unique(ratios);
    
    path1=(sprintf('dataSum/dataTimingTaskData_%s',subID));
    save(path1,'dataSet')
    
    ttl_accuracy(i,2)=sum(dataSet.Timing_Correct);
    ttl_accuracy(i,3)=length(dataSet.Timing_RT);
    ttl_accuracy(i,4)=ttl_accuracy(i,2)/ttl_accuracy(i,3);
    
    plot_data=zeros(length(ratios),4);
    plot_data(:,1)=ratios;
    
    
    for t=1:length(dataSet)
        for tt=1:length(ratios)
            if round(dataSet.Timing_ratio(t),4)==plot_data(tt,1)
                plot_data(tt,3)=plot_data(tt,3)+1;
                plot_data(tt,2)=plot_data(tt,2)+dataSet.Timing_Correct(t);
            end
            plot_data(tt,4)=plot_data(tt,2)/plot_data(tt,3);
        end
        
    end
    
    
    [curvefit,gof,output]=fit(plot_data(:,1),plot_data(:,4),'poly2','normalize','on');
    figure(8)
    plot(curvefit,plot_data(:,1),plot_data(:,4))
    hold on
    %plot(plot_data(:,1),plot_data(:,4),'rx')
    title(sprintf('Individual Timing Task Plot %s',subID))
    xlabel('timing ratio stim1/stim2')
    ylabel('accuracy')
    %legend('block1 average','block2 average')
   
    %p=polyfit(plot_data(:,1),plot_data(:,4),2);
    %y=polyval(p,plot_data(:,1));
    
    %plot(plot_data(:,1),y,'b-')
    
    hold off
    
    savefig(figure(8),sprintf('figures/timing_sub %s.fig',subID))
    
    all_data=cat(1,all_data,plot_data);
    
end

ttl_accuracy(:,5)=isoutlier(ttl_accuracy(:,4),'median');

a=find(ttl_accuracy(:,5)==1);
 
%600,571,563,461

%%i=0;
%while i<n
    
    %disp(ttl_accuracy(a(end-i),1))
    %ttl_accuracy(a(end-i),:) = [];
    
    %i=i+1;
%end


boxplot(ttl_accuracy(:,2))

plotAll_data=zeros(10,4);
plotAll_data(:,1)=all_data(1:10,1);
for jj=1:length(all_data)
    for kk=1:10
        if all_data(jj,1)==plotAll_data(kk,1)
            plotAll_data(kk,2)=plotAll_data(kk,2)+all_data(jj,2);
            plotAll_data(kk,3)=plotAll_data(kk,3)+all_data(jj,3);
        end
        plotAll_data(kk,4)=plotAll_data(kk,2)/plotAll_data(kk,3);
    end
end

%figure(10)
%plot(plotAll_data(:,1),plotAll_data(:,4),'rx')
%hold on
%title(sprintf('All Subjects Timing Task Plot %s',subID))
%xlabel('timing ratio stim1/stim2')
%ylabel('accuracy')

%p1=polyfit(plotAll_data(:,1),plotAll_data(:,4),2);
%y1=polyval(p1,plotAll_data(:,1));

%plot(plotAll_data(:,1),y1,'b-')
%hold off

%savefig(figure(10),'figures/timing_all.fig')



[curvefit,gof,output]=fit(plotAll_data(:,1),plotAll_data(:,4),'poly2','normalize','on');
figure(11)
plot(curvefit,plotAll_data(:,1),plotAll_data(:,4))
hold on

title('All Subjects Timing Task Plot')
xlabel('timing ratio stim1/stim2')
ylabel('accuracy')

text(0.7,0.98,'SSE=0.0623')
text(0.7,0.96,'rsquare=0.3237')
text(0.7,0.93,'adjrsquare=0.1304')
savefig(figure(11),'figures/timing_all.fig')

disp(gof)
disp(output)

hold off

fprintf('mean accuracy: %d\n\n',mean(ttl_accuracy(:,2)));
fprintf('std: %d\n\n',std(ttl_accuracy(:,2)));
fprintf('max accuracy: %d\n\n',max(ttl_accuracy(:,2)));
fprintf('min accuracy: %d\n\n',min(ttl_accuracy(:,2)));
fprintf('mode accuracy: %d\n\n',mode(ttl_accuracy(:,2)));


path2=('timing_ttl_accuracy_all');
save(path2,'ttl_accuracy')

path3=('all_TimingData');
save(path3,'plotAll_data')

%acc_sum=num2cell(ttl_accuracy);

%wtw_sum=struct2cell(subDataSummary);
%wtw_sum=wtw_sum';

%wtw_timing=[wtw_sum,acc_sum];
%colNames = {'subID','WTWreward_bk1','WTWreward_bk2','WTWreward_ttl','WTWauc_bk1','WTWauc_bk2','WTWfitSlope_bk1','WTWfitParam_bk1','WTWfitSlope_bk2','WTWfitParam_bk2','Timing_ttlCorrect','Timing_trialNum','Timing_accuracy'};
%wtw_timingStruct = cell2struct(wtw_timing, colNames, 2);
end


%[subDataSummary(:).timing_acc]=

%for ii=1:length(subDataSummary)
  %  subDataSummary(ii).Timing_acc=ttl_accuracy(ii,2)
%end
%data=struct2dataset(subDataSummary)
%plot(data.WTWreward_ttl,data.Timing_acc,'x')

%parabolic curve fit
%structData(1) = [];
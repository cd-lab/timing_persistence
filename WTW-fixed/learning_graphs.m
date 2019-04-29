function learning_graphs

dataDir = uigetdir; %folder to all the subject data
d = dir(fullfile(dataDir,'*.mat')); 
subIDs = {d(:).name}';



n=length(subIDs);

Fit_all_1=NaN(n,2);
Fit_all_2=NaN(n,2);

num_trial_1=NaN(n,1);
num_trial_2=NaN(n,1);

ttl_fit=NaN(n,4);

for i=1:n
    clf
    ID=subIDs{i};
    IDnum = extractBetween(ID,18,20);
    subID=string(IDnum);
    disp(subID);
    load(sprintf('data/wtw-timing-fixed_%s_1.mat', subID))
    trial_num=length(trialData);
    quit_trial=NaN(trial_num,2);
    
    for ii=1:trial_num
        if isempty(trialData(ii).latency)
            quit_trial(ii,1)=0;
        else
            quit_trial(ii,1)=trialData(ii).latency;
        end
        quit_trial(ii,2)=trialData(ii).blockNum;
    end
    
    
    
    k1=0;
    for j=1:trial_num
        if quit_trial(j,2)==1
            k1=k1+1;
        end
    end
    
    figure(10)
    
    num_trial_1(i,1)=k1;
    K1=(1:k1)';
    Fit1=polyfit(K1,quit_trial(1:k1,1),1);% a simple linear regression model to a set of discrete 2-D data points
    Fit_all_1(i,1)=Fit1(1);
    ttl_fit(i,1)=Fit1(1);
    Fit_all_1(i,2)=Fit1(2);
    ttl_fit(i,2)=Fit1(2);
    r1=polyval(Fit1,K1);
    %r1 = Fit(1).* K1+Fit(2);
    plot(K1,quit_trial(1:k1,1),'rx')
    %legend('block1 trial')
    hold on
    plot(K1, r1, 'r-')
    
    
    %legend('block1 fit')
    line([k1 k1], ylim);
    
    num_trial_2(i,1)=trial_num-k1;
    k2=trial_num(end);
    K2=(k1+1:k2)';
    Fit2=polyfit(K2,quit_trial(k1+1:k2,1),1);
    Fit_all_2(i,1)=Fit2(1);
    ttl_fit(i,3)=Fit2(1);
    Fit_all_2(i,2)=Fit2(2);
    ttl_fit(i,4)=Fit2(2);
    r2=polyval(Fit2,K2);
    %r2 = Fit(1).* K2+Fit(2);
    plot(K2,quit_trial(k1+1:k2,1),'bx')
    %legend('block2 trial')
    hold on
    plot(K2, r2, 'b-')
    %legend('block2 fit')
    
    title(sprintf('learning curve %s',subID))
    xlabel('trials')
    ylabel('quit policy')
    legend('block1 trial','block1 fit','block2 fit','block2 trial')
    text(3,max(quit_trial(:,1)),sprintf('block1 slope %s',Fit1(1)))
    text(3,max(quit_trial(:,1))-2,sprintf('block2 slope %s',Fit2(1)))
    hold off
    savefig(figure(10),sprintf('quit_time/learning_curve%s.fig',subID))

    
end

path=('quit_time/curve_parameters');
save(path,'ttl_fit')
  
ave_trials_1=mean(num_trial_1);
ave_K1=(1:ave_trials_1)';
ave_Fit1=mean(Fit_all_1);
disp(ave_Fit1)
R1 = ave_Fit1(1).*ave_K1 +ave_Fit1(2);
figure(11)
plot(ave_K1,R1,'r-')

hold on
ylim([0 10])
line([ave_trials_1 ave_trials_1], ylim);

ave_trials_2=mean(num_trial_2);
ave_K2=(ave_trials_1:(ave_trials_1+ave_trials_2))';
ave_Fit2=mean(Fit_all_2);
disp(ave_Fit2)
R2 = ave_Fit2(1).*ave_K2 +ave_Fit2(2);
plot(ave_K2, R2, 'b-')

title('Average slope')
xlabel('trials')
ylabel('quit policy')
legend('block1 average','block2 average')
text(3,9,sprintf('average slope %s',ave_Fit1(1)))
text(3,8,sprintf('average slope %s',ave_Fit2(1)))
hold off

savefig(figure(11),sprintf('quit_time/all.fig'))

close all
    
end



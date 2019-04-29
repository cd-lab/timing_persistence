function ttl_reward = subReward

dataDir = uigetdir;
d = dir(fullfile(dataDir,'*.mat'));
subIDs = {d(:).name}';


n=length(subIDs);

ttl_reward=NaN(n,4);

for i=1:n
    subID=subIDs{i};
    
    load(sprintf('data/%s',subID))
    trial_num=length(trialData());
    reward=NaN(trial_num,2);
    wait_time=NaN(trial_num,2);
    for ii=1:trial_num
        if isempty(trialData(ii).payoff)
            reward(ii,1)=NaN;
            reward(ii,2)=trialData(ii).blockNum;
        else
            reward(ii,1)=trialData(ii).payoff;
            reward(ii,2)=trialData(ii).blockNum;
        end
        
        if isempty(trialData(ii).latency)
            wait_time(ii,1)=NaN;
            reward(ii,2)=trialData(ii).blockNum;
        else
            wait_time(ii,1)=floor(trialData(ii).latency);
            reward(ii,2)=trialData(ii).blockNum;
        end
    end
    
    IDnum = extractBetween(subID,18,20);
    %disp(char(IDnum))
    ID = str2double(IDnum);
   
   
    summary=cat(2,reward,wait_time);
    
    
    ttl_reward(i,1)=ID;
    
    
    blk1_reward=0;
    blk2_reward=0;
    for k=1:trial_num
        if reward(k,2)==1
            blk1_reward=blk1_reward+reward(k,1);
        else
            blk2_reward=blk2_reward+reward(k,1);
        end
    end
    
    ttl_reward(i,2)=blk1_reward;
    ttl_reward(i,3)=blk2_reward;
    
    ttlreward=nansum(summary(:,1));
    ttl_reward(i,4)=ttlreward;
    
end

path=('reward/ttl_reward');
save(path,'ttl_reward')



end



%total earn/total time (gen_data: adding up time steps

%ITI is 2s in the task 


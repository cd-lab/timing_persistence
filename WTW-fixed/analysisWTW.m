function analysisWTW(subIDs)

%subIDs = {'461','478','531','559','560','563','565','566','567','568','569','570','571','572','576','579','580','581','582','583','585','589','590','592','593','594','595','596','597','598','599','600','601','602','603','604','605','607','609','632','633','634'};
%594,597,607 

n=length(subIDs);

load('reward/ttl_reward')

ttl_auc=NaN(n,2);


for i=1:n
    subID=subIDs{i}; 
    aucs=quickLook_kmsc2(subID);
    
    ttl_auc(i,1)=aucs(1);
    ttl_auc(i,2)=aucs(2);
    
end

path=('auc_values/ttl_auc');
save(path,'ttl_auc')

all=cat(2,ttl_reward,ttl_auc); 
fit_sum=num2cell(ttl_fit);
summary=num2cell(all);
ALL=[summary,fit_sum];
colNames = {'subID','WTWreward_bk1','WTWreward_bk2','WTWreward_ttl','WTWauc_bk1','WTWauc_bk2','WTWfitSlope_bk1','WTWfitParam_bk1','WTWfitSlope_bk2','WTWfitParam_bk2'};
subDataSummary = cell2struct(ALL, colNames, 2);

path2=('subDataSummary');
save(path2,'subDataSummary')


path1=('summary');
save(path1,'all')

end

    
    
    
    
    
    
function [similarity] = quickLook_kmsc_wtwFixed(subID, generatedData)
% single-subject analysis
% for 2 conditions (run in 2 successive blocks)
%
% this function plots a single participant's trial-by-trial data
%   (same as quickLook.m).
% in addition, it also calculates the kaplan-meier survival curve and area
%   under the curve. This is an estimate of the average number of seconds
%   the participant was willing to wait. 
%
% input: subID (optional) is a string containing the subject ID. If an ID
%   is not supplied, user will be prompted to pick a file.
% input: generatedData (optional) is a boolean which indicates whether generated
%   data is being compared to real data. Defaults to false.

% add path to directory of analysis subfunctions
addpath('../WTW-fixed/anSubFx');

initial_path = '../WTW-fixed';
initial_path2= sprintf('../WTW-fixed/auc_values/aucvalues_%s',subID);


% identify the data file
if nargin>0 && ischar(subID)
    % if subID was given, load the file
    dfname = fullfile(initial_path, 'data', sprintf('wtw-timing-fixed_%s_1.mat',subID));
else
    % otherwise prompt the user to select a file
    [fname,pathname] = uigetfile('data/*');
    dfname = fullfile(pathname,fname);
end

%handle whether this is a comparison with generated data
if nargin<2
    generatedData = false;
end

%reformat data if we're comparing a model to real data

dold = load(dfname);
%dgen = load(dfnamegen);
%dgen(dgen == -1) = NaN;
%d = formatgeneratedData(dold, dgen);

 
%format data
[subInfo, trialold] = formatData(dold);
id = subInfo.id; % the subject ID

%[subInfogen, trialsgen] = formatData(dgen);

trials(1)=trialold(1);
%trials(2)=trialsgen(1);

ceilVal = 40;

% clear figure windows
for f = 1:2, figure(f); clf; end

% analyze one block at a time
nBks = length(trials);
h = nan(1,nBks); % will hold handles to dataseries objects
rtForBoxplot = []; % will accumulate data for a boxplot
cName = cell(nBks,1);
kmCurves = cell(nBks, 1); %use to measure K-M similarity
for b = 1:nBks
    
    try
        cName{b} = subInfo.distribs{b}; % the timing condition
    catch
        cName{b} = '';
    end
    fprintf('  block %d, %s:\n',b,cName{b});
    
    % check if this is the 'active' condition
    if isfield(trials(b),'trialKeypressTimes') && ~isempty(trials(b).trialKeypressTimes{1})
        nTrials = numel(trials(b).trialKeypressTimes);
        iri = []; % will store all inter-response intervals
        for i = 1:nTrials
            iri = [iri; diff(trials(b).trialKeypressTimes{i})']; %#ok<AGROW>
        end
        fprintf('    ACTIVE condition: median IRI = %1.3f s (%1.1f resps/s)\n',...
            median(iri),1/median(iri));
        fprintf('      IQR %1.3f to %1.3f, based on n = %d\n',...
            prctile(iri,[25, 75]), numel(iri));
    end
    
    % plot of the subject's trialwise data
    figure(1);
    subplot(nBks,1,b);
    if b==1
        titleStr = sprintf('%s, subject',id);
    else
        titleStr = sprintf('%s, model',id);
    end
    ssPlot(trials(b),titleStr,ceilVal); % external subfunction
    
    % calculate the kaplan-meier survival curve and print auc results
    [kmsc, auc] = qtask_kmSurvival(trials(b));
    kmCurves{b} = kmsc;
    fprintf('    auc = %1.2f s\n',auc);
    aucs(b)=auc
    save(initial_path2,'aucs')

    % plot the survival curve
    figure(2);
    hold on;
    titleStr = sprintf('%s: KM survival curves',id);
    h(b) = qtask_plotKm(kmsc,titleStr);
    hold off;
    
    % overall reward RT (may later examine as a function of delay length;
    % here the main goal is just to see that RTs are fast enough to suggest
    % participants are engaged with the task). 
    allRTs = trials(b).rewardRT;
    validRTs = allRTs(~isnan(allRTs));
    nRTs = length(validRTs);
    fprintf('    RT (from %d rewarded trials): median = %1.3f s, iqr = %1.3f - %1.3f s\n',...
        nRTs,median(validRTs),prctile(validRTs,[25,75]));
    rtForBoxplot = [rtForBoxplot; [validRTs, b*ones(nRTs,1)]]; %#ok<AGROW>
    
    % print total earnings
    blockEarnings = sum(trials(b).payoff);
    fprintf('    block earnings: $%1.2f\n',blockEarnings/100); % converting cents to dollars
    
    % print info about responding during the ITI
    if isfield(trials,'anyItiKeypress')
        k = trials(b).anyItiKeypress;
        fprintf('    %d of %d trials (%1.1f%%) have keypresses during the ITI.\n',...
            sum(k),length(k),100*sum(k)/length(k));
    else
        fprintf('    No ITI keypress info available.\n');
    end
        
end

% legend and formatting for figure 2 (survival curves)
set(h(1),'Color','b'); % block 1
if numel(h)>1, set(h(2),'Color','r'); end % block 2
legend('subject','model');

% plot RTs in each block
figure(3); clf;
if length(unique(rtForBoxplot(:,2)))==nBks % ONLY if both blocks have data
    boxplot(rtForBoxplot(:,1),rtForBoxplot(:,2));
    set(gca,'Box','off','FontSize',16);
    % set(gca,'XTick',1:nBks,'XTickLabel',subInfo.distribs);
    set(gca,'XTick',1:nBks);
    ylim = get(gca,'YLim');
    set(gca,'YLim',[0, ylim(2)]);
    title(sprintf('%s: RT when rewarded',id),'Interpreter','none');
    xlabel('Block');
    ylabel('Reward RT (s)');
end

%comparison of generated and original data
%similarity = NaN;
%if generatedData
    %similarity = calculate_similarity(kmCurves, d);
%end

savefig(figure(1),sprintf('/Users/tiantianli/Google Drive/BU/Neuroecon/wtw_work/learning_models/qlearning/figures/LP_trial%s',subID))
savefig(figure(2),sprintf('/Users/tiantianli/Google Drive/BU/Neuroecon/wtw_work/learning_models/qlearning/figures/LP_survival%s',subID))
savefig(figure(3),sprintf('/Users/tiantianli/Google Drive/BU/Neuroecon/wtw_work/learning_models/qlearning/figures/LP_RT%s',subID))

end




%%%%%
% subfunction to format one subject's data
function [subInfo, trials] = formatData(d)

% assess the number of blocks
bkIdx = [d.trialData.blockNum]';
nBks = max(bkIdx);

trials = struct([]);
for b = 1:nBks
    
    idx = bkIdx==b;
    
    % add data fields for trials
    trials(b).trialNums = (1:sum(idx))';
    if isfield(d.trialData,'itiKeypresses') % one subject lacks iti keypress data
        trials(b).itiKeypressTimes = {d.trialData(idx).itiKeypresses}';
        trials(b).anyItiKeypress = cellfun(@any,trials(b).itiKeypressTimes,'UniformOutput',true); % logical vector
    end
    if isfield(d.trialData,'trialKeypresses') % if there is an active condition
        trials(b).trialKeypressTimes = {d.trialData(idx).trialKeypresses}';
    end
    trials(b).designatedWait = [d.trialData(idx).designatedWait]';
    trials(b).outcomeWin = [d.trialData(idx).payoff]'>0;
    trials(b).outcomeQuit = [d.trialData(idx).payoff]'==0;
    trials(b).payoff = [d.trialData(idx).payoff]';
    trials(b).startTime = [d.trialData(idx).initialTime]';
    trials(b).rewardTime = [d.trialData(idx).rwdOnsetTime]';
    trials(b).latency = [d.trialData(idx).latency]';
    trials(b).rewardRT = trials(b).latency - trials(b).rewardTime;
    trials(b).outcomeTime = [d.trialData(idx).outcomeTime]';
    trials(b).totalEarned = [d.trialData(idx).totalEarned]';

end

% display some info
subInfo.distribs = d.dataHeader.distribs;
subInfo.id = d.dataHeader.id;
subInfo.points = trials(b).totalEarned(end);
subInfo.money = subInfo.points/100;
fprintf('id: %s\n',subInfo.id);
%fprintf('test date: %s\n',datestr(d.dataHeader.sessionTime));

end % end of subfunction

function [d] = formatgeneratedData(dold, dgen)

genSize = size(dgen);
oldNames = fieldnames(dold.trialData);
oldSize = size(dold.trialData);

d = dold;

%put generated data into existing data object
for i = 1:genSize(1)
    for j = 1:genSize(2)
        d.trialData(i).(oldNames{j}) = dgen(i,j); 
    end
end
%fill remaining slots with empty [] cells
for i = genSize(1)+1:oldSize(2)
    for j = 1:genSize(2)
        d.trialData(i).(oldNames{j}) = [];
    end
end

end

function [similarity] = calculate_similarity(kmCurves, d)

%format x and y variables
x1 = 0.0:0.01:max(kmCurves{1}(:,1));
x2 = 0.0:0.01:max(kmCurves{2}(:,1));
x1size = size(x1);
x2size = size(x2);
kmx1 = kmCurves{1}(:,1);
kmx2 = kmCurves{2}(:,1);
y1 = x1;
y2 = x2;
kmy1 = kmCurves{1}(:,2);
kmy2 = kmCurves{2}(:,2);

for i = 1:x1size(2)
    [val,idx] = max(kmx1(kmx1<=x1(i)));
    y1(i) = kmy1(idx);
end
for i = 1:x2size(2)
    [val,idx] = max(kmx2(kmx2<=x1(i)));
    y2(i) = kmy2(idx);
end

%calculate Frechet distance
frechet_similarity = frechet(x1', y1', x2', y2');

%calculate scaled Frechet distance (time maps to [0,1])
time_scalar = max([x1(end) x2(end)]);
frechet_similarity_scaled = frechet(x1'/time_scalar, y1', x2'/time_scalar, y2');

%calculate logrank statistic
figure(4);
[generated, actual] = logrank_format(d);
uL = logrank(generated, actual);

%OLD, ALTERNATIVE METHODS ARE BELOW
%dfd = DiscreteFrechetDist(kmCurves{1}, kmCurves{2})
%figure(4);
%hold on;
%dtw(kmCurves{1}(:,2), kmCurves{2}(:,2))
%hold off;
%dtw_similarity = dtw(kmCurves{1}(:,2), kmCurves{2}(:,2));
%[h,p,ks_stat] = kstest((1-y1'),'CDF',horzcat(x2',1-y2'))
%[h,p,ks_stat] = kstest2(1-y1',1-y2','Alpha',0.05);
%figure(4);
%hold on;
%[generated, actual] = logrank_format(d);
%hold off;

similarity = [frechet_similarity, frechet_similarity_scaled, uL];

end

function [generated, actual] = logrank_format(d)

blockNum = extractfield(d.trialData, 'blockNum');
generated_trial = 1:sum(blockNum(:) == 1);
generated_outcome = 1:sum(blockNum(:) == 1);
actual_trial = 1:sum(blockNum(:) == 2);
actual_outcome = 1:sum(blockNum(:) == 2);

dSize = size(d.trialData);
gen_trial_idx = 1;
act_trial_idx = 1;
for i = 1:dSize(2)
    trial = d.trialData(i).blockNum;
    if trial == 1
        generated_trial(gen_trial_idx) = d.trialData(i).latency;
        generated_outcome(gen_trial_idx) = d.trialData(i).payoff / 5;
        gen_trial_idx = gen_trial_idx + 1;
    elseif trial == 2
        actual_trial(act_trial_idx) = d.trialData(i).latency;
        actual_outcome(act_trial_idx) = d.trialData(i).payoff / 5;
        act_trial_idx = act_trial_idx + 1;        
    end
end

generated = horzcat(generated_trial', generated_outcome');
actual = horzcat(actual_trial', actual_outcome');

end
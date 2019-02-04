#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v1.90.3),
    on Wed Dec 12 10:08:40 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'TimingTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Volumes/GoogleDrive/My Drive/BU/Fall 2018/Thesis/TimingTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
insRound1 = visual.TextStim(win=win, name='insRound1',
    text='Two stimuli will appear on the screen. \n\nOne white circle, and one black circle, for different durations.\n\nIf you believe that the first stimulus appeared\nfor a longer duration, press the LEFT arrow key.\n\nIf you believe that the second stimulus appeared for \na longer duration, press the RIGHT arrow key.\n\nPress space bar to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "block"
blockClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Block starts\n\nPress space',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "round1_3"
round1_3Clock = core.Clock()
firstcircle_3 = visual.Polygon(
    win=win, name='firstcircle_3',
    edges=50, size=(0.3, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
text_3 = visual.TextStim(win=win, name='text_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
secondcircle = visual.Polygon(
    win=win, name='secondcircle',
    edges=50, size=(0.3, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[-1,-1,-1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_4 = visual.TextStim(win=win, name='text_4',
    text='next',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
respRound1 = event.BuilderKeyResponse()
# keep track of which components have finished
instr1Components = [insRound1, respRound1]
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *insRound1* updates
    if t >= 0.0 and insRound1.status == NOT_STARTED:
        # keep track of start time/frame for later
        insRound1.tStart = t
        insRound1.frameNStart = frameN  # exact frame index
        insRound1.setAutoDraw(True)
    
    # *respRound1* updates
    if t >= 0.0 and respRound1.status == NOT_STARTED:
        # keep track of start time/frame for later
        respRound1.tStart = t
        respRound1.frameNStart = frameN  # exact frame index
        respRound1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if respRound1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block')
thisExp.addLoop(Block)  # add the loop to the experiment
thisBlock = Block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in Block:
    currentLoop = Block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block"-------
    t = 0
    blockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    blockComponents = [text, key_resp_2]
    for thisComponent in blockComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "block"-------
    while continueRoutine:
        # get current time
        t = blockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block"-------
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    Block.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        Block.addData('key_resp_2.rt', key_resp_2.rt)
    # the Routine "block" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditionsTime.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "round1_3"-------
        t = 0
        round1_3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        rtRound1_3 = event.BuilderKeyResponse()
        # keep track of which components have finished
        round1_3Components = [firstcircle_3, rtRound1_3, text_3, secondcircle, text_4]
        for thisComponent in round1_3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "round1_3"-------
        while continueRoutine:
            # get current time
            t = round1_3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *firstcircle_3* updates
            if t >= 0.5 and firstcircle_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                firstcircle_3.tStart = t
                firstcircle_3.frameNStart = frameN  # exact frame index
                firstcircle_3.setAutoDraw(True)
            frameRemains = 0.5 + firstTime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if firstcircle_3.status == STARTED and t >= frameRemains:
                firstcircle_3.setAutoDraw(False)
            
            # *rtRound1_3* updates
            if t >= respStart and rtRound1_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                rtRound1_3.tStart = t
                rtRound1_3.frameNStart = frameN  # exact frame index
                rtRound1_3.status = STARTED
                # keyboard checking is just starting
                rtRound1_3.clock.reset()  # now t=0
            if rtRound1_3.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    rtRound1_3.keys = theseKeys[-1]  # just the last key pressed
                    rtRound1_3.rt = rtRound1_3.clock.getTime()
                    # was this 'correct'?
                    if (rtRound1_3.keys == str(corrAns)) or (rtRound1_3.keys == corrAns):
                        rtRound1_3.corr = 1
                    else:
                        rtRound1_3.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_3* updates
            if t >= plusStart and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            frameRemains = plusStart + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_3.status == STARTED and t >= frameRemains:
                text_3.setAutoDraw(False)
            
            # *secondcircle* updates
            if t >= secondStart and secondcircle.status == NOT_STARTED:
                # keep track of start time/frame for later
                secondcircle.tStart = t
                secondcircle.frameNStart = frameN  # exact frame index
                secondcircle.setAutoDraw(True)
            frameRemains = secondStart + secondTime- win.monitorFramePeriod * 0.75  # most of one frame period left
            if secondcircle.status == STARTED and t >= frameRemains:
                secondcircle.setAutoDraw(False)
            
            # *text_4* updates
            if t >= 0.0 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_4.status == STARTED and t >= frameRemains:
                text_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in round1_3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "round1_3"-------
        for thisComponent in round1_3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if rtRound1_3.keys in ['', [], None]:  # No response was made
            rtRound1_3.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               rtRound1_3.corr = 1;  # correct non-response
            else:
               rtRound1_3.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('rtRound1_3.keys',rtRound1_3.keys)
        trials.addData('rtRound1_3.corr', rtRound1_3.corr)
        if rtRound1_3.keys != None:  # we had a response
            trials.addData('rtRound1_3.rt', rtRound1_3.rt)
        # the Routine "round1_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'Block'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

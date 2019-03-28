#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.4),
    on Thu Mar 28 15:36:23 2019
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
psychopyVersion = '3.0.4'
expName = 'TimingTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/cdlab/Documents/timing_persistence/timing task/TimingTask_lastrun.py',
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
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "block"
blockClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Block 1 starts\n\nPress space',
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

# Initialize components for Routine "block2"
block2Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Block 2 starts\n\nPress space',
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

# Initialize components for Routine "block3"
block3Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Block 3 starts\n\nPress space',
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

# Initialize components for Routine "block4"
block4Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Block 4 starts\n\nPress space',
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

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='The end',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
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
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "block" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
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
            event.clearEvents(eventType='keyboard')
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in round1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "block2"-------
t = 0
block2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
block2Components = [text_5, key_resp_3]
for thisComponent in block2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "block2"-------
while continueRoutine:
    # get current time
    t = block2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block2"-------
for thisComponent in block2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "block2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditionsTime2.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
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
            event.clearEvents(eventType='keyboard')
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in round1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rtRound1_3.keys',rtRound1_3.keys)
    trials_2.addData('rtRound1_3.corr', rtRound1_3.corr)
    if rtRound1_3.keys != None:  # we had a response
        trials_2.addData('rtRound1_3.rt', rtRound1_3.rt)
    # the Routine "round1_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "block3"-------
t = 0
block3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
block3Components = [text_6, key_resp_4]
for thisComponent in block3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "block3"-------
while continueRoutine:
    # get current time
    t = block3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block3"-------
for thisComponent in block3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "block3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditionsTime3.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
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
            event.clearEvents(eventType='keyboard')
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in round1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
    # store data for trials_3 (TrialHandler)
    trials_3.addData('rtRound1_3.keys',rtRound1_3.keys)
    trials_3.addData('rtRound1_3.corr', rtRound1_3.corr)
    if rtRound1_3.keys != None:  # we had a response
        trials_3.addData('rtRound1_3.rt', rtRound1_3.rt)
    # the Routine "round1_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "block4"-------
t = 0
block4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
block4Components = [text_7, key_resp_5]
for thisComponent in block4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "block4"-------
while continueRoutine:
    # get current time
    t = block4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in block4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "block4"-------
for thisComponent in block4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "block4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditionsTime4.csv'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
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
            event.clearEvents(eventType='keyboard')
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
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in round1_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
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
    # store data for trials_4 (TrialHandler)
    trials_4.addData('rtRound1_3.keys',rtRound1_3.keys)
    trials_4.addData('rtRound1_3.corr', rtRound1_3.corr)
    if rtRound1_3.keys != None:  # we had a response
        trials_4.addData('rtRound1_3.rt', rtRound1_3.rt)
    # the Routine "round1_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_2]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

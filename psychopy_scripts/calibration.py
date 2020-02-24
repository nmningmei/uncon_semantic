#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on February 24, 2020, at 18:54
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
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'calibration'  # from the Builder filename that created this script
expInfo = {u'n_square': u'64', u'opacity': u'0.1', u'lowest_opacity': u'0.02', u'probeFrames': u'4', u'participant': u'test', u'session': u'1', u'image_size': u'512', u'premask': u'4', u'step_size': u'0.05', u'postmask': u'4'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s/%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
globalClock = core.Clock()

premask_dur = int(expInfo['premask'])
postmask_dur = int(expInfo['postmask'])
n_square = int(expInfo['n_square'])
image_size = int(expInfo['image_size'])
opacity = float(expInfo['opacity'])
session = int(expInfo['session'])
step_size = float(expInfo['step_size'])

curr = int(expInfo['probeFrames'])
lowest_opacity = float(expInfo['lowest_opacity'])
count = 0

import time
from psychopy import parallel
parallel.setPortAddress(888)
wait_msg = "Wating for Scanner ..."
msg = visual.TextStim(win,color = 'DarkGray',text = wait_msg)

# jitter 1
jitter_counter = 0
jitter1_dur_options = np.concatenate([[1.5]*16,[2.0]*8,[2.5]*6,[3.0]*4,[3.5]*4])
np.random.shuffle(jitter1_dur_options)

# jitter 2
jitter2_dur_options = np.concatenate([[6.0]*16,[6.5]*8,[7.0]*6,[7.5]*4,[8.0]*4])
np.random.shuffle(jitter2_dur_options)

np.random.seed(12345)
masks = np.random.rand(n_square,n_square)*2 - 1

# save corrections of trials of unconscious
unconscious_trials = []
# count unconscious trials
n_unconscious = 0

# Initialize components for Routine "intoPrepare"
intoPrepareClock = core.Clock()
preparation = visual.TextStim(win=win, name='preparation',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
first_blank = visual.TextStim(win=win, name='first_blank',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
blank_period = visual.TextStim(win=win, name='blank_period',
    text=None,
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);


# Initialize components for Routine "premask"
premaskClock = core.Clock()
premasking = visual.GratingStim(
    win=win, name='premasking',units='pix', 
    tex=masks, mask=None,
    ori=0, pos=[0, 0], size=(image_size, image_size), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=256, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import sys
reload(sys)
sys.setdefaultencoding("latin-1")
presentation = visual.ImageStim(
    win=win, name='presentation',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(image_size, image_size),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=256, interpolate=True, depth=-1.0)

# Initialize components for Routine "postmask"
postmaskClock = core.Clock()
postmasking = visual.GratingStim(
    win=win, name='postmasking',units='pix', 
    tex=masks, mask=None,
    ori=0, pos=[0, 0], size=(image_size, image_size), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=256, interpolate=True, depth=0.0)

# Initialize components for Routine "discriminate"
discriminateClock = core.Clock()

response_options = visual.TextStim(win=win, name='response_options',
    text='default text',
    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "visibility"
visibilityClock = core.Clock()

visibility_message = visual.TextStim(win=win, name='visibility_message',
    text=u'?',
    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "jitter2"
jitter2Clock = core.Clock()

post_jitter = visual.TextStim(win=win, name='post_jitter',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "end_experiment"
end_experimentClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
msg.draw()
win.flip()

while True:
    if (event.getKeys() == ['q']):#(parallel.readPin(10) == 1) or 
        break
    else:
        time.sleep(0.0001) # give 1ms to other processes
globalClock.reset()
startTime = globalClock.getTime()
# keep track of which components have finished
introComponents = []
for thisComponent in introComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intoPrepare"-------
t = 0
intoPrepareClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(0.400000)
# update component parameters for each repeat
# keep track of which components have finished
intoPrepareComponents = [preparation, first_blank]
for thisComponent in intoPrepareComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "intoPrepare"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = intoPrepareClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *preparation* updates
    if t >= 0.0 and preparation.status == NOT_STARTED:
        # keep track of start time/frame for later
        preparation.tStart = t
        preparation.frameNStart = frameN  # exact frame index
        preparation.setAutoDraw(True)
    frameRemains = 0.0 + .3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if preparation.status == STARTED and t >= frameRemains:
        preparation.setAutoDraw(False)
    
    # *first_blank* updates
    if t >= .3 and first_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        first_blank.tStart = t
        first_blank.frameNStart = frameN  # exact frame index
        first_blank.setAutoDraw(True)
    frameRemains = .3 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if first_blank.status == STARTED and t >= frameRemains:
        first_blank.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intoPrepareComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intoPrepare"-------
for thisComponent in intoPrepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
main_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'..\\data\\sampled_words.csv'),
    seed=None, name='main_loop')
thisExp.addLoop(main_loop)  # add the loop to the experiment
thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
if thisMain_loop != None:
    for paramName in thisMain_loop:
        exec('{} = thisMain_loop[paramName]'.format(paramName))

for thisMain_loop in main_loop:
    currentLoop = main_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop:
            exec('{} = thisMain_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    main_loop.addData("fixation_onset", globalClock.getTime() - startTime)
    main_loop.addData("blank_dur",blank_dur)
    # keep track of which components have finished
    fixationComponents = [fixation_cross, blank_period]
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 0.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)
        
        # *blank_period* updates
        if (fixation_cross.status == FINISHED) and blank_period.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_period.tStart = t
            blank_period.frameNStart = frameN  # exact frame index
            blank_period.setAutoDraw(True)
        if blank_period.status == STARTED and t >= (blank_period.tStart + blank_dur):
            blank_period.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "premask"-------
    t = 0
    premaskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    premasking.setTex(masks)
    # keep track of which components have finished
    premaskComponents = [premasking]
    for thisComponent in premaskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "premask"-------
    while continueRoutine:
        # get current time
        t = premaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *premasking* updates
        if t >= 0.0 and premasking.status == NOT_STARTED:
            # keep track of start time/frame for later
            premasking.tStart = t
            premasking.frameNStart = frameN  # exact frame index
            premasking.setAutoDraw(True)
        if premasking.status == STARTED and frameN >= (premasking.frameNStart + premask_dur):
            premasking.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in premaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "premask"-------
    for thisComponent in premaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "premask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    main_loop.addData("image_onset_time", globalClock.getTime() - startTime)
    presentation.setImage(PATH_spanish)
    presentation.setOpacity(opacity)
    # keep track of which components have finished
    trialComponents = [presentation]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *presentation* updates
        if t >= 0.0 and presentation.status == NOT_STARTED:
            # keep track of start time/frame for later
            presentation.tStart = t
            presentation.frameNStart = frameN  # exact frame index
            presentation.setAutoDraw(True)
        if presentation.status == STARTED and frameN >= (presentation.frameNStart + curr):
            presentation.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "postmask"-------
    t = 0
    postmaskClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    postmasking.setTex(masks)
    # keep track of which components have finished
    postmaskComponents = [postmasking]
    for thisComponent in postmaskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "postmask"-------
    while continueRoutine:
        # get current time
        t = postmaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *postmasking* updates
        if t >= 0.0 and postmasking.status == NOT_STARTED:
            # keep track of start time/frame for later
            postmasking.tStart = t
            postmasking.frameNStart = frameN  # exact frame index
            postmasking.setAutoDraw(True)
        if postmasking.status == STARTED and frameN >= (postmasking.frameNStart + postmask_dur):
            postmasking.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in postmaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "postmask"-------
    for thisComponent in postmaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "postmask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "discriminate"-------
    t = 0
    discriminateClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    main_loop.addData("discrim_resptime", globalClock.getTime() - startTime)
    resp_options = [['nV_V',['Nonliving_Things','Living_Things']],
                    ['V_nV',['Living_Things','Nonliving_Things']]]
    idx = np.random.choice([0,1])
    resp_msg = '{}'.format(resp_options[idx][0])
    main_loop.addData("response_window", resp_options[idx][0])
    response_options.setText(resp_msg)
    response = event.BuilderKeyResponse()
    # keep track of which components have finished
    discriminateComponents = [response_options, response]
    for thisComponent in discriminateComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "discriminate"-------
    while continueRoutine:
        # get current time
        t = discriminateClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *response_options* updates
        if t >= 0.0 and response_options.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_options.tStart = t
            response_options.frameNStart = frameN  # exact frame index
            response_options.setAutoDraw(True)
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discriminateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discriminate"-------
    for thisComponent in discriminateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    temp_correctAns = np.where(np.array(resp_options[idx][1]) == category)[0][0]+1
    main_loop.addData('correctAns',temp_correctAns)
    # objective accuracy
    if (response.keys == str(temp_correctAns)) or (response.keys == temp_correctAns):
       temp_corr = 1
    else:
        temp_corr = 0
    main_loop.addData('response.corr' , temp_corr)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
    main_loop.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        main_loop.addData('response.rt', response.rt)
    # the Routine "discriminate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "visibility"-------
    t = 0
    visibilityClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    main_loop.addData("visible_resptime", globalClock.getTime() - startTime)
    visible = event.BuilderKeyResponse()
    # keep track of which components have finished
    visibilityComponents = [visibility_message, visible]
    for thisComponent in visibilityComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "visibility"-------
    while continueRoutine:
        # get current time
        t = visibilityClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *visibility_message* updates
        if t >= 0.0 and visibility_message.status == NOT_STARTED:
            # keep track of start time/frame for later
            visibility_message.tStart = t
            visibility_message.frameNStart = frameN  # exact frame index
            visibility_message.setAutoDraw(True)
        
        # *visible* updates
        if t >= 0.0 and visible.status == NOT_STARTED:
            # keep track of start time/frame for later
            visible.tStart = t
            visible.frameNStart = frameN  # exact frame index
            visible.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(visible.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if visible.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                visible.keys = theseKeys[-1]  # just the last key pressed
                visible.rt = visible.clock.getTime()
                # was this 'correct'?
                if (visible.keys == str(u"'1'")) or (visible.keys == u"'1'"):
                    visible.corr = 1
                else:
                    visible.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visibilityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "visibility"-------
    for thisComponent in visibilityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    count += 1
    main_loop.addData('opacity',opacity)
    
    #if (visible.keys == str('1')) or (visible.keys == '1'):# invisible
    #    opacity += np.random.choice([0.02, 0.04, 0.08],size = 1)[0]
    #    if opacity > 1: opacity = 1
    #    #curr += np.random.choice([1,2,3],size=1)[0]
    #    #if curr < 1:  curr = 1
    #elif (visible.keys == str('2')) or (visible.keys == '2'):# partially aware
    #    opacity -= 0.1
    #    if opacity < lowest_opacity: opacity = lowest_opacity
    #    #curr -= 1
    #    #if curr < 1:  curr = 1 
    #elif (visible.keys == str('3')) or (visible.keys == '3'): # visible
    #    opacity -= np.random.choice([0.02, 0.04, 0.08],size = 1)[0]
    #    if opacity < lowest_opacity: opacity = lowest_opacity
    #    #curr -= np.random.choice([2,3],size=1,p=[0.5,0.5])[0]
    #    #if curr < 1: curr = 1
    
    if ((visible.keys == str('1')) or (visible.keys == '1')) and (temp_corr == 0): # invisible and incorrect
        opacity += 2 * step_size
        unconscious_trials.append(temp_corr)
        n_unconscious += 1
    elif ((visible.keys == str('1')) or (visible.keys == '1')) and (temp_corr == 1): # invisible and correct
        opacity += step_size
        unconscious_trials.append(temp_corr)
        n_unconscious += 1
    elif ((visible.keys == str('2')) or (visible.keys == '2')) and (temp_corr == 0): # visible and incorrect
        opacity -= step_size
        if opacity < lowest_opacity: opacity = lowest_opacity
    elif ((visible.keys == str('2')) or (visible.keys == '2')) and (temp_corr == 1): # visible and correct
        opacity -= 2 * step_size
        if opacity < lowest_opacity: opacity = lowest_opacity
    # check responses
    if visible.keys in ['', [], None]:  # No response was made
        visible.keys=None
        # was no response the correct answer?!
        if str(u"'1'").lower() == 'none':
           visible.corr = 1  # correct non-response
        else:
           visible.corr = 0  # failed to respond (incorrectly)
    # store data for main_loop (TrialHandler)
    main_loop.addData('visible.keys',visible.keys)
    main_loop.addData('visible.corr', visible.corr)
    if visible.keys != None:  # we had a response
        main_loop.addData('visible.rt', visible.rt)
    # the Routine "visibility" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "jitter2"-------
    t = 0
    jitter2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # meanacc = main_loop.data['response.corr'].mean()
    if len(unconscious_trials) > 0:
        meanacc = np.mean(unconscious_trials)
    else:
        meanacc = 0
    
    msg_post = '{}/{}, mean unconscious = {:.2f},opacity = {:.1f},p(correct) = {:.2f}'.format(
            main_loop.thisN+1,main_loop.nTotal,
            n_unconscious/(main_loop.thisN+1),opacity,meanacc)
    post_jitter.setText(msg_post)
    # keep track of which components have finished
    jitter2Components = [post_jitter]
    for thisComponent in jitter2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jitter2"-------
    while continueRoutine:
        # get current time
        t = jitter2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *post_jitter* updates
        if t >= 0.0 and post_jitter.status == NOT_STARTED:
            # keep track of start time/frame for later
            post_jitter.tStart = t
            post_jitter.frameNStart = frameN  # exact frame index
            post_jitter.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if post_jitter.status == STARTED and t >= frameRemains:
            post_jitter.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jitter2"-------
    for thisComponent in jitter2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print('{}/{}, mean unconscious = {:.2f},opacity = {:.1f},p(correct) = {:.2f}'.format(
            main_loop.thisN+1,main_loop.nTotal,
            n_unconscious/(main_loop.thisN+1),opacity,meanacc))
    # the Routine "jitter2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_loop'

# get names of stimulus parameters
if main_loop.trialList in ([], [None], None):
    params = []
else:
    params = main_loop.trialList[0].keys()
# save data for this loop
main_loop.saveAsText(filename + 'main_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "end_experiment"-------
t = 0
end_experimentClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
end_experimentComponents = []
for thisComponent in end_experimentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_experiment"-------
while continueRoutine:
    # get current time
    t = end_experimentClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_experimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_experiment"-------
for thisComponent in end_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "end_experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()






print(globalClock.getTime() - startTime)
print("mean unconscious = {:.2f}, frame = {}, p(correct) = {:.2f}".format(
    meanvis,curr,meanacc))
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

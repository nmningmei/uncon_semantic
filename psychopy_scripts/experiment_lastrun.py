#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v3.2.4), February 18, 2020, at 18:49
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'experiment'  # from the Builder filename that created this script
expInfo = {u'n_square': u'32', u'opacity': u'0.6', u'probeFrames': u'5', u'participant': u'test', u'premask': u'20', u'session': u'001', u'image_size': u'128', u'postmask': u'20'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\ning\\Documents\\python_works\\uncon_semantic\\psychopy_scripts\\experiment.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 720), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "intro"
introClock = core.Clock()
globalClock = core.Clock()

premask_dur = int(expInfo['premask'])
postmask_dur = int(expInfo['postmask'])
n_square = int(expInfo['n_square'])
image_size = int(expInfo['image_size'])
opacity = float(expInfo['opacity'])

curr = int(expInfo['probeFrames'])
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


# Initialize components for Routine "intoPrepare"
intoPrepareClock = core.Clock()
preparation = visual.TextStim(win=win, ori=0, name='preparation',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
first_blank = visual.TextStim(win=win, ori=0, name='first_blank',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, ori=0, name='fixation_cross',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
blank_period = visual.TextStim(win=win, ori=0, name='blank_period',
    text=None,    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)


# Initialize components for Routine "premask"
premaskClock = core.Clock()
premasking = visual.GratingStim(win=win, name='premasking',units='pix', 
    tex=np.random.rand(n_square,n_square)*2 - 1, mask=None,
    ori=0, pos=[0, -0], size=(image_size, image_size), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
import sys
reload(sys)
sys.setdefaultencoding("latin-1")
presentation = visual.ImageStim(win=win, name='presentation',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(image_size, image_size),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "postmask"
postmaskClock = core.Clock()
postmasking = visual.GratingStim(win=win, name='postmasking',units='pix', 
    tex=np.random.rand(n_square,n_square)*2 -1, mask=None,
    ori=0, pos=[0, 0], size=(image_size, image_size), sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "jitter1"
jitter1Clock = core.Clock()
jitter_delay = visual.TextStim(win=win, ori=0, name='jitter_delay',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "discriminate"
discriminateClock = core.Clock()

response_options = visual.TextStim(win=win, ori=0, name='response_options',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "visibility"
visibilityClock = core.Clock()

visibility_message = visual.TextStim(win=win, ori=0, name='visibility_message',
    text=u'?',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "jitter2"
jitter2Clock = core.Clock()

post_jitter = visual.TextStim(win=win, ori=0, name='post_jitter',
    text=u'+',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "end_experiment"
end_experimentClock = core.Clock()


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "intro"-------
t = 0
introClock.reset()  # clock 
frameN = -1
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

#-------Start Routine "intro"-------
continueRoutine = True
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

#-------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "intoPrepare"-------
t = 0
intoPrepareClock.reset()  # clock 
frameN = -1
routineTimer.add(13.000000)
# update component parameters for each repeat
# keep track of which components have finished
intoPrepareComponents = []
intoPrepareComponents.append(preparation)
intoPrepareComponents.append(first_blank)
for thisComponent in intoPrepareComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "intoPrepare"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = intoPrepareClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *preparation* updates
    if t >= 0.0 and preparation.status == NOT_STARTED:
        # keep track of start time/frame for later
        preparation.tStart = t  # underestimates by a little under one frame
        preparation.frameNStart = frameN  # exact frame index
        preparation.setAutoDraw(True)
    if preparation.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        preparation.setAutoDraw(False)
    
    # *first_blank* updates
    if t >= 3 and first_blank.status == NOT_STARTED:
        # keep track of start time/frame for later
        first_blank.tStart = t  # underestimates by a little under one frame
        first_blank.frameNStart = frameN  # exact frame index
        first_blank.setAutoDraw(True)
    if first_blank.status == STARTED and t >= (3 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
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

#-------Ending Routine "intoPrepare"-------
for thisComponent in intoPrepareComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
main_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=u'C:\\Users\\ning\\Documents\\python_works\\uncon_semantic\\psychopy_scripts\\experiment.psyexp',
    trialList=data.importConditions(u'..\\data\\sampled_words.csv'),
    seed=None, name='main_loop')
thisExp.addLoop(main_loop)  # add the loop to the experiment
thisMain_loop = main_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisMain_loop.rgb)
if thisMain_loop != None:
    for paramName in thisMain_loop.keys():
        exec(paramName + '= thisMain_loop.' + paramName)

for thisMain_loop in main_loop:
    currentLoop = main_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_loop.rgb)
    if thisMain_loop != None:
        for paramName in thisMain_loop.keys():
            exec(paramName + '= thisMain_loop.' + paramName)
    
    #------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    main_loop.addData("fixation_onset", globalClock.getTime() - startTime)
    main_loop.addData("blank_dur",blank_dur)
    # keep track of which components have finished
    fixationComponents = []
    fixationComponents.append(fixation_cross)
    fixationComponents.append(blank_period)
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fixation"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 0.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # underestimates by a little under one frame
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation_cross.setAutoDraw(False)
        
        # *blank_period* updates
        if (fixation_cross.status == FINISHED) and blank_period.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_period.tStart = t  # underestimates by a little under one frame
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
    
    #-------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "premask"-------
    t = 0
    premaskClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    premaskComponents = []
    premaskComponents.append(premasking)
    for thisComponent in premaskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "premask"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = premaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *premasking* updates
        if t >= 0.0 and premasking.status == NOT_STARTED:
            # keep track of start time/frame for later
            premasking.tStart = t  # underestimates by a little under one frame
            premasking.frameNStart = frameN  # exact frame index
            premasking.setAutoDraw(True)
        if premasking.status == STARTED and frameN >= (premasking.frameNStart + premask_dur):
            premasking.setAutoDraw(False)
        if premasking.status == STARTED:  # only update if being drawn
            premasking.setTex(np.random.rand(n_square,n_square)*2 - 1, log=False)
        
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
    
    #-------Ending Routine "premask"-------
    for thisComponent in premaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "premask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    main_loop.addData("image_onset_time", globalClock.getTime() - startTime)
    presentation.setImage(PATH)
    presentation.setOpacity(opacity)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(presentation)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *presentation* updates
        if t >= 0.0 and presentation.status == NOT_STARTED:
            # keep track of start time/frame for later
            presentation.tStart = t  # underestimates by a little under one frame
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "postmask"-------
    t = 0
    postmaskClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    # keep track of which components have finished
    postmaskComponents = []
    postmaskComponents.append(postmasking)
    for thisComponent in postmaskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "postmask"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = postmaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *postmasking* updates
        if t >= 0.0 and postmasking.status == NOT_STARTED:
            # keep track of start time/frame for later
            postmasking.tStart = t  # underestimates by a little under one frame
            postmasking.frameNStart = frameN  # exact frame index
            postmasking.setAutoDraw(True)
        if postmasking.status == STARTED and frameN >= (postmasking.frameNStart + postmask_dur):
            postmasking.setAutoDraw(False)
        if postmasking.status == STARTED:  # only update if being drawn
            postmasking.setTex(np.random.rand(n_square,n_square)*2 -1, log=False)
        
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
    
    #-------Ending Routine "postmask"-------
    for thisComponent in postmaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "postmask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "jitter1"-------
    t = 0
    jitter1Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    jitter1_dur = jitter1_dur_options[jitter_counter]
    main_loop.addData('jitter1',jitter1_dur)
    # keep track of which components have finished
    jitter1Components = []
    jitter1Components.append(jitter_delay)
    for thisComponent in jitter1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "jitter1"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = jitter1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter_delay* updates
        if t >= 0.0 and jitter_delay.status == NOT_STARTED:
            # keep track of start time/frame for later
            jitter_delay.tStart = t  # underestimates by a little under one frame
            jitter_delay.frameNStart = frameN  # exact frame index
            jitter_delay.setAutoDraw(True)
        if jitter_delay.status == STARTED and t >= (0.0 + (jitter1_dur-win.monitorFramePeriod*0.75)): #most of one frame period left
            jitter_delay.setAutoDraw(False)
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitter1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "jitter1"-------
    for thisComponent in jitter1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "jitter1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "discriminate"-------
    t = 0
    discriminateClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    main_loop.addData("discrim_resptime", globalClock.getTime() - startTime)
    resp_options = [['nV_V',['Nonliving_Things','Living_Things']],
                    ['V_nV',['Living_Things','Nonliving_Things']]]
    idx = np.random.choice([0,1])
    resp_msg = '{}'.format(resp_options[idx][0])
    main_loop.addData("response_window", resp_options[idx][0])
    response_options.setText(resp_msg)
    response = event.BuilderKeyResponse()  # create an object of type KeyResponse
    response.status = NOT_STARTED
    # keep track of which components have finished
    discriminateComponents = []
    discriminateComponents.append(response_options)
    discriminateComponents.append(response)
    for thisComponent in discriminateComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "discriminate"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = discriminateClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *response_options* updates
        if t >= 0.0 and response_options.status == NOT_STARTED:
            # keep track of start time/frame for later
            response_options.tStart = t  # underestimates by a little under one frame
            response_options.frameNStart = frameN  # exact frame index
            response_options.setAutoDraw(True)
        if response_options.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            response_options.setAutoDraw(False)
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # underestimates by a little under one frame
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            response.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if response.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            response.status = STOPPED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
        
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
    
    #-------Ending Routine "discriminate"-------
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
    # store data for main_loop (TrialHandler)
    main_loop.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        main_loop.addData('response.rt', response.rt)
    
    #------Prepare to start Routine "visibility"-------
    t = 0
    visibilityClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    main_loop.addData("visible_resptime", globalClock.getTime() - startTime)
    visible = event.BuilderKeyResponse()  # create an object of type KeyResponse
    visible.status = NOT_STARTED
    # keep track of which components have finished
    visibilityComponents = []
    visibilityComponents.append(visibility_message)
    visibilityComponents.append(visible)
    for thisComponent in visibilityComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "visibility"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = visibilityClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *visibility_message* updates
        if t >= 0.0 and visibility_message.status == NOT_STARTED:
            # keep track of start time/frame for later
            visibility_message.tStart = t  # underestimates by a little under one frame
            visibility_message.frameNStart = frameN  # exact frame index
            visibility_message.setAutoDraw(True)
        if visibility_message.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            visibility_message.setAutoDraw(False)
        
        # *visible* updates
        if t >= 0.0 and visible.status == NOT_STARTED:
            # keep track of start time/frame for later
            visible.tStart = t  # underestimates by a little under one frame
            visible.frameNStart = frameN  # exact frame index
            visible.status = STARTED
            # keyboard checking is just starting
            visible.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if visible.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            visible.status = STOPPED
        if visible.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
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
    
    #-------Ending Routine "visibility"-------
    for thisComponent in visibilityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    count += 1
    main_loop.addData('probe_Frames',curr)
    if (visible.keys == str('1')) or (visible.keys == '1'):# invisible
        curr += np.random.choice([1,2,3],size=1)[0]
        if curr < 1:  curr = 1
    elif (visible.keys == str('2')) or (visible.keys == '2'):# partially aware
        curr -= 1
        if curr < 1:  curr = 1 
    elif (visible.keys == str('3')) or (visible.keys == '3'): # visible
        curr -= np.random.choice([2,3],size=1,p=[0.5,0.5])[0]
        if curr < 1: curr = 1
    
    # check responses
    if visible.keys in ['', [], None]:  # No response was made
       visible.keys=None
       # was no response the correct answer?!
       if str(u"'1'").lower() == 'none': visible.corr = 1  # correct non-response
       else: visible.corr = 0  # failed to respond (incorrectly)
    # store data for main_loop (TrialHandler)
    main_loop.addData('visible.keys',visible.keys)
    main_loop.addData('visible.corr', visible.corr)
    if visible.keys != None:  # we had a response
        main_loop.addData('visible.rt', visible.rt)
    
    #------Prepare to start Routine "jitter2"-------
    t = 0
    jitter2Clock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    jitter2_delay_dur = jitter2_dur_options[jitter_counter]
    main_loop.addData('jitter2',jitter2_delay_dur)
    jitter_counter += 1
    # keep track of which components have finished
    jitter2Components = []
    jitter2Components.append(post_jitter)
    for thisComponent in jitter2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "jitter2"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = jitter2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *post_jitter* updates
        if t >= 0.0 and post_jitter.status == NOT_STARTED:
            # keep track of start time/frame for later
            post_jitter.tStart = t  # underestimates by a little under one frame
            post_jitter.frameNStart = frameN  # exact frame index
            post_jitter.setAutoDraw(True)
        if post_jitter.status == STARTED and t >= (0.0 + (jitter2_delay_dur-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    
    #-------Ending Routine "jitter2"-------
    for thisComponent in jitter2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    meanacc = main_loop.data['response.corr'].mean()
    meanvis = main_loop.data['visible.corr'].mean()
    
    print('{}/{}, mean unconscious = {:.2f},frame = {},p(correct) = {:.2f}'.format(
            main_loop.thisN,main_loop.nTotal,
            meanvis,curr,meanacc))
    # the Routine "jitter2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_loop'

# get names of stimulus parameters
if main_loop.trialList in ([], [None], None):  params = []
else:  params = main_loop.trialList[0].keys()
# save data for this loop
main_loop.saveAsText(filename + 'main_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

#------Prepare to start Routine "end_experiment"-------
t = 0
end_experimentClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

# keep track of which components have finished
end_experimentComponents = []
for thisComponent in end_experimentComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "end_experiment"-------
continueRoutine = True
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

#-------Ending Routine "end_experiment"-------
for thisComponent in end_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "end_experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()







print(globalClock.getTime() - startTime)
print("mean unconscious = {:.2f}, frame = {}, p(correct) = {:.2f}".format(
    meanvis,curr,meanacc))
win.close()
core.quit()

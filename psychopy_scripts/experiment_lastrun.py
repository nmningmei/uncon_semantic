#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v3.2.4), February 18, 2020, at 16:38
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
expName = 'experiment'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
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
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

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

# Initialize components for Routine "trial"
trialClock = core.Clock()
presentation = visual.ImageStim(win=win, name='presentation',units='pix', 
    image='sin', mask=None,
    ori=0, pos=(-30, -40), size=(1024, 1024),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
import sys
reload(sys)
sys.setdefaultencoding("latin-1")

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
        if fixation_cross.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            fixation_cross.setAutoDraw(False)
        
        # *blank_period* updates
        if (fixation_cross.status == FINISHED) and blank_period.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_period.tStart = t  # underestimates by a little under one frame
            blank_period.frameNStart = frameN  # exact frame index
            blank_period.setAutoDraw(True)
        if blank_period.status == STARTED and t >= (blank_period.tStart + 1.0):
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
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    presentation.setImage(PATH)
    
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(presentation)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
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
        if presentation.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'main_loop'


win.close()
core.quit()

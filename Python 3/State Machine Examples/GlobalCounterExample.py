'''
----------------------------------------------------------------------------

This file is part of the Sanworks Bpod repository
Copyright (C) 2017 Sanworks LLC, Stony Brook, New York, USA

----------------------------------------------------------------------------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed  WITHOUT ANY WARRANTY and without even the
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__)[:-22], "Modules")) # Add Bpod system files to Python path

from BpodClass import BpodObject # Import BpodObject
from StateMachineAssembler import stateMachine # Import state machine assembler

myBpod = BpodObject('COM13') # Create a new instance of a Bpod object on serial port COM13
sma = stateMachine(myBpod) # Create a new state machine (events + outputs tailored for myBpod)
sma.setGlobalCounter(1, 'Port1In', 5) # Arguments: (CounterNumber, TargetEvent, Threshold)

sma.addState('Name', 'InitialDelay',
    'Timer', 2,
    'StateChangeConditions', ('Tup', 'ResetGlobalCounter1'),
    'OutputActions', ('PWM2', 255))
sma.addState('Name', 'ResetGlobalCounter1',
    'Timer', 0,
    'StateChangeConditions', ('Tup', 'Port1Lit'),
    'OutputActions', ('GlobalCounterReset', 1))
sma.addState('Name', 'Port1Lit', # Infinite loop (with next state). Only a global counter can save us.
    'Timer', .25,
    'StateChangeConditions', ('Tup', 'Port3Lit', 'GlobalCounter1_End', 'exit'),
    'OutputActions', ('PWM1', 255))
sma.addState('Name', 'Port3Lit',
    'Timer', .25,
    'StateChangeConditions', ('Tup', 'Port1Lit', 'GlobalCounter1_End', 'exit'),
    'OutputActions', ('PWM3', 255))

myBpod.sendStateMachine(sma) # Send state machine description to Bpod device
RawEvents = myBpod.runStateMachine() # Run state machine and return events
print(RawEvents.__dict__) # Print events to console

myBpod.disconnect() # Disconnect Bpod

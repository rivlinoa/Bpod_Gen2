function Firmware = CurrentFirmwareList

% Retuns a struct with current firmware versions for 
% state machine + all curated modules.

Firmware = struct;
Firmware.StateMachine = 17;
Firmware.WavePlayer = 1;
Firmware.PulsePal = 1;
Firmware.AnalogIn = 1;
Firmware.DDSModule = 1;
Firmware.DDSSeq = 1;
Firmware.I2C = 1;
Firmware.ValveDriver = 1;
Firmware.RotaryEncoder = 1;
Firmware.EchoModule = 1;
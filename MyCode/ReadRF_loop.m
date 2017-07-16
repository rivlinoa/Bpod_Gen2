%RF read

RFID=serial('COM4'); %chnage the port number if RFreader is connected to different port
fopen(RFID);

while(1)
    tag=fscanf(RFID);
    if ~isempty(tag)
        disp(tag)
    end
end


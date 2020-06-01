function generateScript_LinearAxicon201907
filename = 'linearaxicon.gwl';
fid = fopen(filename,'w');
%NEED BEGINNING/STANDARD PARAMETERS
fprintf(fid,'ContinuousMode\r\n');
fprintf(fid,'PowerScaling 1.0\r\n');
fprintf(fid,'GalvoScanMode\r\n');
% fprintf(fid,'ScanSpeed 10000\r\n');
fprintf(fid,'FindInterfaceAt 0\r\n');
fprintf(fid,'TextFontSize 10\r\n');
fprintf(fid,'TextPositionX -60\r\n');
fprintf(fid,'TextPositionY 50\r\n');
fprintf(fid,'TextPositionZ 25\r\n');
fprintf(fid,'WriteText "ShAXOX-1.55to1.65"\r\n');
fprintf(fid,'FindInterfaceAt 0\r\n\r\n');
fprintf(fid,'ZOffset 14\r\n\r\n');

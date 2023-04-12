% clc;
% clear;

% Load the traclets and from it as needed.
load Quarter_1_trklts;
% load Quarter_2_trklts;
% load Quarter_3_trklts;
% load Quarter_4_trklts;
% load Quarter_5_trklts;
% load Quarter_6_trklts;
% load Quarter_7_trklts;
% load Quarter_8_trklts;
% load Quarter_9_trklts;


Quarter_1_trklts_x_y=[];

for i=1:length(Quarter_1_trklts)
  trklt=Quarter_1_trklts(i);
  x=[];
  y=[];
  for u=1:length(Quarter_1_trklts(i).x)
    x(1,u)=Quarter_1_trklts(i).x(u);
    y(1,u)=Quarter_1_trklts(i).y(u);
  end
  Quarter_1_trklts_x_y{i,1}=[x;y];
end
    
% Quarter_3_trklts_x_y=[];
% Quarter_4_trklts_x_y=[];
% % Quarter_5_trklts_x_y=[];
% Quarter_6_trklts_x_y=[];
% Quarter_7_trklts_x_y=[];
% Quarter_8_trklts_x_y=[];
% Quarter_9_trklts_x_y=[];
% 
% Quarter_3_trklts_x_y=Reshaping_parts(Quarter_3_trklts);
% Quarter_4_trklts_x_y=Reshaping_parts(Quarter_4_trklts);
% % Quarter_5_trklts_x_y=Reshaping_parts(Quarter_5_trklts);
% Quarter_6_trklts_x_y=Reshaping_parts(Quarter_6_trklts);
% Quarter_7_trklts_x_y=Reshaping_parts(Quarter_7_trklts);
% Quarter_8_trklts_x_y=Reshaping_parts(Quarter_8_trklts);
% Quarter_9_trklts_x_y=Reshaping_parts(Quarter_9_trklts);
% -------------------------------------------------------------------------------
%  This Part is to fromat the all tracklets just like the example.
% just like :
%  X1,Y1,x2,y2,x3,y3,x4,y4----> X'Y'
% each tracklet is represented by 24 row

New_Form_data_Current_Quarter_1_trklts_x_y=[];
New_Form_data_Next_Quarter_1_trklts_x_y=[];
for i=1:length(Quarter_1_trklts_x_y)
    Crrnt_trklt=Quarter_1_trklts_x_y{i,1};
for j=1:length(Crrnt_trklt)-4
 New_Form_data_Current_Quarter_1_trklts_x_y(end+1,1)=Crrnt_trklt(1,j);
 New_Form_data_Current_Quarter_1_trklts_x_y(end,2)=Crrnt_trklt(2,j);
 
 New_Form_data_Current_Quarter_1_trklts_x_y(end,3)=Crrnt_trklt(1,j+1);
 New_Form_data_Current_Quarter_1_trklts_x_y(end,4)=Crrnt_trklt(2,j+1);
 
 New_Form_data_Current_Quarter_1_trklts_x_y(end,5)=Crrnt_trklt(1,j+2);
 New_Form_data_Current_Quarter_1_trklts_x_y(end,6)=Crrnt_trklt(2,j+2);
 
 New_Form_data_Current_Quarter_1_trklts_x_y(end,7)=Crrnt_trklt(1,j+3);
 New_Form_data_Current_Quarter_1_trklts_x_y(end,8)=Crrnt_trklt(2,j+3);
 
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,9)=Crrnt_trklt(1,j+4);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,10)=Crrnt_trklt(2,j+4);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,11)=Crrnt_trklt(1,j+5);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,12)=Crrnt_trklt(2,j+5);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,13)=Crrnt_trklt(1,j+6);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,14)=Crrnt_trklt(2,j+6);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,15)=Crrnt_trklt(1,j+7);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,16)=Crrnt_trklt(2,j+7);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,17)=Crrnt_trklt(1,j+8);
%  New_Form_data_Current_Quarter_1_trklts_x_y(end,18)=Crrnt_trklt(2,j+8);
 
 New_Form_data_Next_Quarter_1_trklts_x_y(end+1,1)=Crrnt_trklt(1,j+4);
 New_Form_data_Next_Quarter_1_trklts_x_y(end,2)=Crrnt_trklt(2,j+4); 
end
end
% save New_Form_data New_Form_data;
%  csvwrite('New_Form_data_Current_Quarter_1_trklts_x_y.csv',New_Form_data_Current_Quarter_1_trklts_x_y);
%  csvwrite('New_Form_data_Next_Quarter_1_trklts_x_y.csv',New_Form_data_Next_Quarter_1_trklts_x_y);
%  
 dlmwrite('New_Form_data_Current_Quarter_1_trklts_x_y.txt',New_Form_data_Current_Quarter_1_trklts_x_y,'precision',7);
 dlmwrite('New_Form_data_Next_Quarter_1_trklts_x_y.txt',New_Form_data_Next_Quarter_1_trklts_x_y,'precision',7);
 
% New_Form_data_Current_Quarter_3_trklts_x_y=[];
% New_Form_data_Current_Quarter_4_trklts_x_y=[];
% New_Form_data_Current_Quarter_6_trklts_x_y=[];
% New_Form_data_Current_Quarter_7_trklts_x_y=[];
% New_Form_data_Current_Quarter_8_trklts_x_y=[];
% New_Form_data_Current_Quarter_9_trklts_x_y=[];
% 
% New_Form_data_Next_Quarter_3_trklts_x_y=[];
% New_Form_data_Next_Quarter_4_trklts_x_y=[];
% New_Form_data_Next_Quarter_6_trklts_x_y=[];
% New_Form_data_Next_Quarter_7_trklts_x_y=[];
% New_Form_data_Next_Quarter_8_trklts_x_y=[];
% New_Form_data_Next_Quarter_9_trklts_x_y=[];
% 
% [New_Form_data_Current_Quarter_3_trklts_x_y ,New_Form_data_Next_Quarter_3_trklts_x_y] = Format_the_data_for_training(Quarter_3_trklts_x_y);
% [New_Form_data_Current_Quarter_4_trklts_x_y ,New_Form_data_Next_Quarter_4_trklts_x_y] = Format_the_data_for_training(Quarter_4_trklts_x_y);
% [New_Form_data_Current_Quarter_6_trklts_x_y ,New_Form_data_Next_Quarter_6_trklts_x_y] = Format_the_data_for_training(Quarter_6_trklts_x_y);
% [New_Form_data_Current_Quarter_7_trklts_x_y ,New_Form_data_Next_Quarter_7_trklts_x_y] = Format_the_data_for_training(Quarter_7_trklts_x_y);
% [New_Form_data_Current_Quarter_8_trklts_x_y ,New_Form_data_Next_Quarter_8_trklts_x_y] = Format_the_data_for_training(Quarter_8_trklts_x_y);
% [New_Form_data_Current_Quarter_9_trklts_x_y ,New_Form_data_Next_Quarter_9_trklts_x_y] = Format_the_data_for_training(Quarter_9_trklts_x_y);
% 
% csvwrite('New_Form_data_Current_Quarter_3_trklts_x_y.csv',New_Form_data_Current_Quarter_3_trklts_x_y);
% csvwrite('New_Form_data_Current_Quarter_4_trklts_x_y.csv',New_Form_data_Current_Quarter_4_trklts_x_y);
% csvwrite('New_Form_data_Current_Quarter_6_trklts_x_y.csv',New_Form_data_Current_Quarter_6_trklts_x_y);
% csvwrite('New_Form_data_Current_Quarter_7_trklts_x_y.csv',New_Form_data_Current_Quarter_7_trklts_x_y);
% csvwrite('New_Form_data_Current_Quarter_8_trklts_x_y.csv',New_Form_data_Current_Quarter_8_trklts_x_y);
% csvwrite('New_Form_data_Current_Quarter_9_trklts_x_y.csv',New_Form_data_Current_Quarter_9_trklts_x_y);
% 
% csvwrite('New_Form_data_Next_Quarter_3_trklts_x_y.csv',New_Form_data_Next_Quarter_3_trklts_x_y);
% csvwrite('New_Form_data_Next_Quarter_4_trklts_x_y.csv',New_Form_data_Next_Quarter_4_trklts_x_y);
% csvwrite('New_Form_data_Next_Quarter_6_trklts_x_y.csv',New_Form_data_Next_Quarter_6_trklts_x_y);
% csvwrite('New_Form_data_Next_Quarter_7_trklts_x_y.csv',New_Form_data_Next_Quarter_7_trklts_x_y);
% csvwrite('New_Form_data_Next_Quarter_8_trklts_x_y.csv',New_Form_data_Next_Quarter_8_trklts_x_y);
% csvwrite('New_Form_data_Next_Quarter_9_trklts_x_y.csv',New_Form_data_Next_Quarter_9_trklts_x_y);
 
 
 
 
 
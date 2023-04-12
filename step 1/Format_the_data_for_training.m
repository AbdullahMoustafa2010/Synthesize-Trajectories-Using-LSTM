function [New_Form_data_Current_Quarter_1_trklts_x_y,New_Form_data_Next_Quarter_1_trklts_x_y] = Format_the_data_for_training(tracklets_x_y)
New_Form_data_Current_Quarter_1_trklts_x_y=[];
New_Form_data_Next_Quarter_1_trklts_x_y=[];
for i=1:length(tracklets_x_y)
    Crrnt_trklt=tracklets_x_y{i,1};
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
 
 New_Form_data_Next_Quarter_1_trklts_x_y(end+1,1)=Crrnt_trklt(1,j+2);
 New_Form_data_Next_Quarter_1_trklts_x_y(end,2)=Crrnt_trklt(2,j+2); 
end
end

end


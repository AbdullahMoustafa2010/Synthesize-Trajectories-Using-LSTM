clc;
clear;
%close all;

% load Quarter_1_trklts;
% Test_Cluster=Quarter_1_trklts;
% Visulaize the Train tracklets first 273 tracklets
% test=imread('000000_segmented.jpg');
test=imread('000000_Q2.jpg');
% test=imread('000000.jpg');

figure,imshow(test);
% hold on;
% color='yellow';
% for i=1:length(Test_Cluster)
%     tr=Test_Cluster(i);
%    plot(tr.x,tr.y,'LineWidth',1,'Color',color);
% end
%Read Both the original and Predicted tracklets
% Original_Test_Tracklets = csvread('TestOriginal.csv');
% Predicted_Test_Tracklets=csvread('TestPredict.csv');
 Created_Tracklet1=csvread('Created_Traj_M1.csv');
 hold on;
clr1='red';
% plot(Created_Tracklet1(1,1),Created_Tracklet1(1,2),'r*')
% plot(Created_Tracklet1(:,1),Created_Tracklet1(:,2),'LineWidth',3,'color',clr1);
plot(Created_Tracklet1(:,1),Created_Tracklet1(:,2),'d','color',clr1);
plot(Created_Tracklet1(:,1),Created_Tracklet1(:,2),'LineWidth',3,'color','blue');


  Created_Tracklet2=csvread('Created_Traj_M2.csv');
  hold on;
 clr1='cyan';
% plot(Created_Tracklet2(1,1),Created_Tracklet2(1,2),'r*')
 plot(Created_Tracklet2(:,1),Created_Tracklet2(:,2),'LineWidth',3,'color',clr1);
% 
  Created_Tracklet3=csvread('Created_Traj_M3.csv');
  hold on;
 clr1='yellow';
% plot(Created_Tracklet3(1,1),Created_Tracklet3(1,2),'r*')
 plot(Created_Tracklet3(:,1),Created_Tracklet3(:,2),'LineWidth',3,'color',clr1);
% 
  Created_Tracklet4=csvread('Created_Traj_M4.csv');
  hold on;
 clr1='white';
% plot(Created_Tracklet4(1,1),Created_Tracklet4(1,2),'r*')
 plot(Created_Tracklet4(:,1),Created_Tracklet4(:,2),'LineWidth',3,'color',clr1);
% 
  Created_Tracklet5=csvread('Created_Traj_M5.csv');
  hold on;
 clr1='green';
% plot(Created_Tracklet5(1,1),Created_Tracklet5(1,2),'r*')
 plot(Created_Tracklet5(:,1),Created_Tracklet5(:,2),'LineWidth',3,'color',clr1);

% load Quarter_1_trklts;
% hold on;
% % plot(Quarter_1_trklts(101).x(:),Quarter_1_trklts(101).y(:),'.','LineWidth',1,'color','black');
% plot(Quarter_1_trklts(101).x(:),Quarter_1_trklts(101).y(:),'.','color','black');
% 
% % plot(Quarter_1_trklts(26).x(:),Quarter_1_trklts(26).y(:),'LineWidth',3,'color','black');
% % plot(Quarter_1_trklts(51).x(:),Quarter_1_trklts(51).y(:),'LineWidth',3,'color','black');
% % plot(Quarter_1_trklts(76).x(:),Quarter_1_trklts(76).y(:),'LineWidth',3,'color','black');
% % plot(Quarter_1_trklts(61).x(:),Quarter_1_trklts(61).y(:),'LineWidth',3,'color','black');
% 

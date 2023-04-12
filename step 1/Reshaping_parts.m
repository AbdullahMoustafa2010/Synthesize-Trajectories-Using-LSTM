function [Reshaped_Part_tracklets] = Reshaping_parts(Part_tracklets)
for i=1:length(Part_tracklets)
  trklt=Part_tracklets(i);
  x=[];
  y=[];
  for u=1:length(Part_tracklets(i).x)
    x(1,u)=Part_tracklets(i).x(u);
    y(1,u)=Part_tracklets(i).y(u);
  end
  Reshaped_Part_tracklets{i,1}=[x;y];
end
end


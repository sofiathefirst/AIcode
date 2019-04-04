x=[-2:0.1:2];
y = 4*x;
z=normrnd(0,0.6,1,41);
y = y+z;

w = 0.1;
plot(x,y,'.')
%hold on
for i =[1:1000]
    d=w*x*x' - y*x'
    w = w-0.001*d
    plot(x,y,'.',x,w*x)
    pause(0.1)
end

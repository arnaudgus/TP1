// Parameters
a0 = 0.1; // growth rate
tau = 0.1; // time interval between two points
nt = 1000; // nb of timepoints
N0 = 10; //Initinal nb of indivs

// Initialization
N = zeros(1, nt);
t = zeros(1, nt);
N(1) = N0

// Algorithm
for i = 1:nt
    N(i+1) = N(i) + tau*a0*N(i);
    t(i+1) = t(i) + tau;
end
disp(N)


// Visualization
figure;
plot(t, N)

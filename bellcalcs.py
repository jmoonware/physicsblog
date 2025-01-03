import numpy as np

def bias_binary(bias):
	return(bool(int(max(0,min(1,np.round(np.random.rand()+(bias-0.5)))))))

def bell_state_lrx(b_bias=0.5,c_bias=0.5,t_bias=0.5,bc_lrx=0):
	# left output with possible left-right interaction
	b = bias_binary(b_bias)
	c = bias_binary(c_bias)
	t = bias_binary(t_bias)
	x = bias_binary(bc_lrx)
	if x: # left-right interaction
		c = not(b)
	return np.array([b, c, t])

def count_bell_events(states):
	# states is numpy bool array of left hand b, c, t tuples
	# We pick out different event lists 
	# corresponding to different settings on the machine
	N = int(len(states)/3) # should be multiple of 3
	Nbwcw = np.sum(states[:,0][:N]&~states[:,1][:N])
	Nbwtw = np.sum(states[:,0][N:2*N]&~states[:,2][N:2*N])
	Ntwcw = np.sum(states[:,2][2*N:]&~states[:,1][2*N:])
	return Nbwcw,Nbwtw,Ntwcw

def gen_bell_run(N=10,b_bias=0.5,c_bias=0.5,t_bias=0.5,bc_lrx=0):
	# We need data for three different settings, so need 3x the events
	states = []
	[states.append(bell_state_lrx(b_bias=b_bias,c_bias=c_bias,t_bias=t_bias,bc_lrx=bc_lrx)) for _ in range(3*N)]
	return(np.array(states))

def gen_bell_stats(T=10,N=10,b_bias=0.5,c_bias=0.5,t_bias=0.5,bc_lrx=0):
	# T is the number of trials, N is the number of events/trial
	counts = []
	for _ in range(T):
		states = gen_bell_run(N,b_bias,c_bias,t_bias,bc_lrx)
		counts.append(count_bell_events(states))
	c = np.array(counts)
	return(c[:,0],c[:,1]+c[:,2])



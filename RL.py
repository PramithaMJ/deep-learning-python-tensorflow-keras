import random
import time
import math



try:	
	#Setting hyper-parameters
	epsilon_0_initial = 0.9
	learning_rate = 0.1
	discount_factor = 0.5
	iterations = 200
	steps = 20
	
	print('RL statrted at ' + str(time.time()))
	source = 2
	destination = 5
	rows, cols = (6, 6)	
	
	#Initialization of Q-values
	initial_value_low = 0.0
	Q = [[initial_value_low for i in range(cols)] for i in range(rows)] # [[0.0, 0.0, 0.0, 0.0,0.0, 0.0], [0.0, 0.0, 0.0, 0.0,0.0, 0.0], ......, [0.0, 0.0, 0.0, 0.0,0.0, 0.0]]
	initial_value_high = 1.0 
	Q[0][4] = initial_value_high
	Q[4][0] = initial_value_high
	Q[4][3] = initial_value_high
	Q[3][4] = initial_value_high
	Q[4][5] = initial_value_high
	Q[5][4] = initial_value_high
	Q[2][3] = initial_value_high
	Q[3][2] = initial_value_high
	Q[3][1] = initial_value_high
	Q[1][3] = initial_value_high
	Q[1][5] = initial_value_high
	Q[5][1] = initial_value_high
	Q[5][5] = initial_value_high
	print('Q values initialized')
	
	for m in range(iterations):
		print('Iteration '+str(m))
		##cid is present state
		cid = 2
		##nid action at present state (next state)
		nid = 3
		actions = 0 ##Number of possible actions at a present state
		action_set = list() ##List of actions at present state
		
		for i in range(6):
			if Q[cid][i] > 0.0:
				action_set.append(i)
				actions = actions + 1
		
		print('Action space is ' + str(actions))
		
		for x in range(steps):
			#Epsilon-greedy approach for RL
			epsilon_th = (random.randint(0,10))/10.0
			print('epsilon threshold is '+str(epsilon_th))
			lamda = 1/50
			epsilon = epsilon_0_initial*math.exp(-lamda*m)
			print('epsilon ' + str(epsilon))
			index = 0
			if (epsilon > epsilon_th):
				##EXPLORE
				index = random.randint(0, actions-1)
				nid = action_set[index]
				print('Exploring')
			else:
				##Exploiting
				maximum_q = 0
				max_index = 0
				for i in range(6):
					if(Q[cid][i] > maximum_q):
						maximum_q = Q[cid][i]
						nid = i
				print('Exploiting')
				
			print('Current state is '+str(cid)+'next state is '+str(nid))
			
			nextstate_actions = 0 ##Number of possible actions at a next state
			nextstate_action_set = list() ##List of actions at next state
			
			for i in range(6):
				if Q[nid][i] > 0.0:
					nextstate_action_set.append(i)
					nextstate_actions = nextstate_actions + 1
			
			#Calculation of reward
			reward = 0 
			if((nid==destination) or (cid==destination)):
				reward = 100
				
			#Calculation of Q-values using Bellman Equation
			max_q = 0.0##max_q holds the maximum q value of the next state
			for i in range(nextstate_actions):
				if(Q[nid][nextstate_action_set[i]] > max_q):
					max_q = Q[nid][nextstate_action_set[i]]
			q_term1 = (1-learning_rate)*Q[cid][nid]
			q_term2 = (learning_rate)*(reward +(discount_factor*max_q))	
			
			Q[cid][nid] = q_term1 + q_term2
			
			print('Q value updated as '+str(Q[cid][nid]) + 'for current state '+ str(cid) +' and next state '+ str(nid))		
			
			#go to next state
			cid = nid
			
			actions = 0 ##Number of possible actions at a given state
			action_set = list() ##List of actions at a given state
			
			for i in range(6):
				if Q[cid][i] > 0.0:
					action_set.append(i)
					actions = actions + 1
					
	print('RL finished at ' + str(time.time()))
	print('Q[0][4] is '+ str(Q[0][4]))
	print('Q[4][0] is ' + str(Q[4][0]))
	print('Q[4][3] is ' + str(Q[4][3]))
	print('Q[4][5] is ' + str(Q[4][5]))
	print('Q[2][3] is ' + str(Q[2][3]))
	print('Q[3][2] is ' + str(Q[3][2]))
	print('Q[3][1] is ' + str(Q[3][1]))
	print('Q[3][4] is ' + str(Q[3][4]))
	print('Q[1][3] is ' + str(Q[1][3]))
	print('Q[1][5] is ' + str(Q[1][5])) 
	print('Q[5][1] is ' + str(Q[5][1]))
	print('Q[5][5] is ' + str(Q[5][5]))
	print('Q[5][4] is ' + str(Q[5][4]))
	
except AttributeError:
 print('Attribute error')

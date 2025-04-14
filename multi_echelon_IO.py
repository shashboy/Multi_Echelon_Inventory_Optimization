import pulp 
import numpy as np 
import pandas as pd 


model = pulp.LpProblem('MEIO',pulp.LpMinimize)


def make_factory_vars(prod_upbound_1,prod_upbound_2,dispatch_upbound_1,dispatch_upbound_2):

	factory_vars = {}

	factory_1_inventory = []
	factory_2_inventory = []

	factory_1_dispatch = []
	factory_2_dispatch = []

	factory_1_prod = []
	factory_2_prod = []



	for i in range(1,32):
		factory_1_inventory.append('f1_inv_{}'.format(i))
		factory_2_inventory.append('f2_inv_{}'.format(i))

		factory_1_prod.append('f1_prod_{}'.format(i))
		factory_1_prod.append('f1_prod_{}'.format(i))

		factory_1_dispatch.append('f1_r1_disp_{}'.format(i))
		factory_1_dispatch.append('f1_r2_disp_{}'.format(i))

		factory_2_dispatch.append('f2_r1_disp_{}'.format(i))
		factory_2_dispatch.append('f2_r2_disp_{}'.format(i))

		factory_vars['f1_inv_{}'.format(i)] = pulp.LpVariable('f1_inv_{}'.format(i),lowBound=0,cat='Continuous')
		factory_vars['f2_inv_{}'.format(i)] = pulp.LpVariable('f2_inv_{}'.format(i),lowBound=0,cat='Continuous')

		factory_vars['f1_prod_{}'.format(i)] = pulp.LpVariable('f1_prod_{}'.format(i),lowBound=0,upBound=prod_upbound_1,cat='Continuous')
		factory_vars['f2_prod_{}'.format(i)] = pulp.LpVariable('f2_prod_{}'.format(i),lowBound=0,upBound=prod_upbound_2,cat='Continuous')

		factory_vars['f1_r1_disp_{}'.format(i)] = pulp.LpVariable('f1_r1_disp_{}'.format(i),lowBound=0,upBound=dispatch_upbound_1,cat='Continuous')
		factory_vars['f1_r2_disp_{}'.format(i)] = pulp.LpVariable('f1_r2_disp_{}'.format(i),lowBound=0,upBound=dispatch_upbound_1,cat='Continuous')

		factory_vars['f2_r1_disp_{}'.format(i)] = pulp.LpVariable('f2_r1_disp_{}'.format(i),lowBound=0,upBound=dispatch_upbound_2,cat='Continuous')
		factory_vars['f2_r2_disp_{}'.format(i)] = pulp.LpVariable('f2_r2_disp_{}'.format(i),lowBound=0,upBound=dispatch_upbound_2,cat='Continuous')

	return factory_vars,factory_1_inventory,factory_2_inventory,factory_1_dispatch,factory_2_dispatch,factory_1_prod,factory_2_prod




def rdc_vars(dispatch_upbound_1,dispatch_upbound_2):

	rdc_vars = {}

	rdc_inventory_1 = []
	rdc_inventory_2 = []


	rdc_dispatch_1_c1 = []
	rdc_dispatch_1_c2 = []
	rdc_dispatch_1_c3 = []

	rdc_dispatch_2_c1 = []
	rdc_dispatch_2_c2 = []
	rdc_dispatch_2_c3 = []


	for i in range(1,32):

		rdc_inventory_1.append('rdc_1_inv_{}'.format(i))
		rdc_inventory_2.append('rdc_2_inv_{}'.format(i))


		rdc_dispatch_1_c1.append('rdc_1_disp_c1_{}'.format(i))
		rdc_dispatch_1_c2.append('rdc_1_disp_c2_{}'.format(i))
		rdc_dispatch_1_c3.append('rdc_1_disp_c3_{}'.format(i))



		rdc_dispatch_2_c1.append('rdc_2_disp_c1_{}'.format(i))
		rdc_dispatch_2_c2.append('rdc_2_disp_c2_{}'.format(i))
		rdc_dispatch_2_c3.append('rdc_2_disp_c3_{}'.format(i))


		rdc_vars['rdc_1_inv_{}'.format(i)] = pulp.LpVariable('rdc_1_inv_{}'.format(i),lowBound=0,cat='Continuous')
		rdc_vars['rdc_2_inv_{}'.format(i)] = pulp.LpVariable('rdc_2_inv_{}'.format(i),lowBound=0,cat='Continuous')

		rdc_vars['rdc_1_disp_c1_{}'.format(i)] = pulp.LpVariable('rdc_1_disp_c1_{}'.format(i),lowBound=0,upBound=dispatch_upbound_1,cat='Continuous')
		rdc_vars['rdc_1_disp_c2_{}'.format(i)] = pulp.LpVariable('rdc_1_disp_c2_{}'.format(i),lowBound=0,upBound=dispatch_upbound_1,cat='Continuous')
		rdc_vars['rdc_1_disp_c3_{}'.format(i)] = pulp.LpVariable('rdc_1_disp_c3_{}'.format(i),lowBound=0,upBound=dispatch_upbound_1,cat='Continuous')


		rdc_vars['rdc_2_disp_c1_{}'.format(i)] = pulp.LpVariable('rdc_2_disp_c1_{}'.format(i),lowBound=0,upBound=dispatch_upbound_2,cat='Continuous')
		rdc_vars['rdc_2_disp_c2_{}'.format(i)] = pulp.LpVariable('rdc_2_disp_c2_{}'.format(i),lowBound=0,upBound=dispatch_upbound_2,cat='Continuous')
		rdc_vars['rdc_2_disp_c3_{}'.format(i)] = pulp.LpVariable('rdc_2_disp_c3_{}'.format(i),lowBound=0,upBound=dispatch_upbound_2,cat='Continuous')


	return rdc_vars,rdc_inventory_1,rdc_inventory_2,rdc_dispatch_1_c1,rdc_dispatch_1_c2,rdc_dispatch_1_c3,rdc_dispatch_2_c1,rdc_dispatch_2_c2,rdc_dispatch_2_c3






def customer_vars():

	cust_vars = {}

	customer_1_inventory = []
	customer_2_inventory = []
	customer_3_inventory = []


	customer_1_disp = []
	customer_2_disp = []
	customer_3_disp = []


	customer_1_slack = []
	customer_2_slack = []
	customer_3_slack = []


	cust_1_binary = []
	cust_2_binary = []
	cust_3_binary = []


	for i in range(1,32):
		customer_1_inventory.append('cust_1_inv_{}'.format(i))
		customer_2_inventory.append('cust_2_inv_{}'.format(i))
		customer_3_inventory.append('cust_3_inv_{}'.format(i))


		customer_1_disp.append('cust_1_disp_{}'.format(i))
		customer_2_disp.append('cust_2_disp_{}'.format(i))
		customer_3_disp.append('cust_3_disp_{}'.format(i))


		customer_1_slack.append('cust_1_slack_{}'.format(i))
		customer_2_slack.append('cust_2_slack_{}'.format(i))
		customer_3_slack.append('cust_3_slack_{}'.format(i))

		cust_1_binary.append('cust_1_bin_{}'.format(i))
		cust_2_binary.append('cust_2_bin_{}'.format(i))
		cust_3_binary.append('cust_3_bin_{}'.format(i))



		cust_vars['cust_1_inv_{}'.format(i)] = pulp.LpVariable('cust_1_inv_{}'.format(i),lowBound=0,cat='Continuous')
		cust_vars['cust_2_inv_{}'.format(i)] = pulp.LpVariable('cust_2_inv_{}'.format(i),lowBound=0,cat='Continuous')
		cust_vars['cust_3_inv_{}'.format(i)] = pulp.LpVariable('cust_3_inv_{}'.format(i),lowBound=0,cat='Continuous')


		cust_vars['cust_1_disp_{}'.format(i)] =  pulp.LpVariable('cust_1_disp_{}'.format(i),lowBound=0,cat='Continuous')
		cust_vars['cust_2_disp_{}'.format(i)] =  pulp.LpVariable('cust_2_disp_{}'.format(i),lowBound=0,cat='Continuous')
		cust_vars['cust_3_disp_{}'.format(i)] =  pulp.LpVariable('cust_3_disp_{}'.format(i),lowBound=0,cat='Continuous')

		cust_vars['cust_1_slack_{}'.format(i)] = pulp.LpVariable('cust_1_slack_{}'.format(i),lowBound=0,cat='Continuous')
		cust_vars['cust_2_slack_{}'.format(i)] = pulp.LpVariable('cust_2_slack_{}'.format(i),lowBound=0,cat='Continuous')
		cust_vars['cust_3_slack_{}'.format(i)] = pulp.LpVariable('cust_3_slack_{}'.format(i),lowBound=0,cat='Continuous')


		cust_vars['cust_1_bin_{}'.format(i)] = pulp.LpVariable('cust_1_bin_{}'.format(i),lowBound=0,upBound=1,cat='Binary')
		cust_vars['cust_2_bin_{}'.format(i)] = pulp.LpVariable('cust_2_bin_{}'.format(i),lowBound=0,upBound=1,cat='Binary')
		cust_vars['cust_3_bin_{}'.format(i)] = pulp.LpVariable('cust_3_bin_{}'.format(i),lowBound=0,upBound=1,cat='Binary')


	return cust_vars,customer_1_inventory,customer_2_inventory,customer_3_inventory,customer_1_disp,customer_2_disp,customer_3_disp



factory_vars,factory_1_inventory_name,factory_2_inventory_name,factory_1_dispatch_name,factory_2_dispatch_name,factory_1_prod_name,factory_2_prod_name = make_factory_vars(prod_upbound_1=300,prod_upbound_2=300,dispatch_upbound_1=150,dispatch_upbound_2=120)
rdc_vars,rdc_inventory_1_c1,rdc_inventory_2,rdc_dispatch_1_c1,rdc_dispatch_1_c2,rdc_dispatch_1_c3,rdc_dispatch_2_c1,rdc_dispatch_2_c2,rdc_dispatch_2_c3 = rdc_vars(dispatch_upbound_1=100,dispatch_upbound_2=110)
cust_vars,customer_1_inventory,customer_2_inventory,customer_3_inventory,customer_1_disp,customer_2_disp,customer_3_disp = customer_vars()



def non_neg(x):
	return float(int(max(0,x)))

non_neg_vec = np.vectorize(non_neg)

def generate_cust_demand(mean_demand,scale_demand):
	demand = non_neg_vec(np.random.normal(mean_demand,scale_demand,size=(31)))
	return demand


def inventory_opng(f1,f2,rdc1,rdc2,c1,c2,c3):
	return f1,f2,rdc1,rdc2,c1,c2,c3

c1 = generate_cust_demand(65,35)
c2 = generate_cust_demand(100,50)
c3 = generate_cust_demand(35,8)

f1_opng,f2_opng,rdc1_opng,rdc2_opng,c1_opng,c2_opng,c3_opng = inventory_opng(400,500,200,200,100,100,100)



#####make the factory_1 Inventory Flow Constraints 
model += f1_opng  - factory_vars['f1_r1_disp_1'] - factory_vars['f1_r2_disp_1'] +  factory_vars['f1_prod_1'] == factory_vars['f1_inv_1'] 
model += factory_vars['f1_inv_1'] >= 0 
model += factory_vars['f1_r1_disp_1'] >=0 
model += factory_vars['f1_r2_disp_1'] >=0 
model += factory_vars['f1_prod_1'] >= 0
for i in range(1,31):
	model += factory_vars['f1_inv_{}'.format(i)]   - factory_vars['f1_r1_disp_{}'.format(i+1)] - factory_vars['f1_r2_disp_{}'.format(i+1)] +  factory_vars['f1_prod_{}'.format(i+1)] == factory_vars['f1_inv_{}'.format(i+1)]
	model += factory_vars['f1_inv_{}'.format(i+1)]>=0
	model += factory_vars['f1_r1_disp_{}'.format(i+1)] >=0
	model += factory_vars['f1_r2_disp_{}'.format(i+1)] >=0 
	model += factory_vars['f1_prod_{}'.format(i+1)] >= 0



###make the factory 2 Inventory FLow Constraints 

model += f2_opng  - factory_vars['f2_r1_disp_1'] - factory_vars['f2_r2_disp_1'] +  factory_vars['f2_prod_1'] == factory_vars['f2_inv_1'] 
model += factory_vars['f2_inv_1'] >= 0 
model += factory_vars['f2_r1_disp_1'] >=0 
model += factory_vars['f2_r2_disp_1'] >=0 
model += factory_vars['f2_prod_1'] >= 0
for i in range(1,31):
	model += factory_vars['f2_inv_{}'.format(i)]   - factory_vars['f2_r1_disp_{}'.format(i+1)] - factory_vars['f2_r2_disp_{}'.format(i+1)] +  factory_vars['f2_prod_{}'.format(i+1)] == factory_vars['f2_inv_{}'.format(i+1)]
	model += factory_vars['f2_inv_{}'.format(i+1)]>=0
	model += factory_vars['f2_r1_disp_{}'.format(i+1)] >=0
	model += factory_vars['f2_r2_disp_{}'.format(i+1)] >=0 
	model += factory_vars['f2_prod_{}'.format(i+1)] >= 0




### Make the RDC1 constraints, RDC 1 is connect to only C1, though all connections are defined. C2 and C3 connections are made Zero. 


model += rdc1_opng  - rdc_vars['rdc_1_disp_c1_1'] - rdc_vars['rdc_1_disp_c2_1'] - rdc_vars['rdc_1_disp_c3_1'] == rdc_vars['rdc_1_inv_1']
model += rdc_vars['rdc_1_disp_c2_1'] == 0
model += rdc_vars['rdc_1_disp_c3_1'] == 0
model += rdc_vars['rdc_1_inv_1'] >=0
model += rdc_vars['rdc_1_disp_c1_1'] >=0

model += rdc_vars['rdc_1_inv_1'] -  rdc_vars['rdc_1_disp_c1_2'] - rdc_vars['rdc_1_disp_c2_2'] - rdc_vars['rdc_1_disp_c3_2'] == rdc_vars['rdc_1_inv_2']
model += rdc_vars['rdc_1_disp_c2_2'] == 0
model += rdc_vars['rdc_1_disp_c3_2'] == 0
model += rdc_vars['rdc_1_inv_2'] >=0
model += rdc_vars['rdc_1_disp_c1_2'] >=0


model += rdc_vars['rdc_1_inv_2'] -  rdc_vars['rdc_1_disp_c1_3'] - rdc_vars['rdc_1_disp_c2_3'] - rdc_vars['rdc_1_disp_c3_3'] == rdc_vars['rdc_1_inv_3']
model += rdc_vars['rdc_1_disp_c2_3'] == 0
model += rdc_vars['rdc_1_disp_c3_3'] == 0
model += rdc_vars['rdc_1_inv_3'] >=0
model += rdc_vars['rdc_1_disp_c1_3'] >=0


for i in range(3,31):
	model += rdc_vars['rdc_1_inv_{}'.format(i)] - rdc_vars['rdc_1_disp_c1_{}'.format(i+1)] - rdc_vars['rdc_1_disp_c2_{}'.format(i+1)]  - rdc_vars['rdc_1_disp_c3_{}'.format(i+1)] + factory_vars['f1_r1_disp_{}'.format(i+1-3)] + factory_vars['f2_r1_disp_{}'.format(i+1-3)]== rdc_vars['rdc_1_inv_{}'.format(i+1)]
	model += rdc_vars['rdc_1_disp_c2_{}'.format(i+1)]==0
	model += rdc_vars['rdc_1_disp_c3_{}'.format(i+1)]==0
	model += rdc_vars['rdc_1_inv_{}'.format(i+1)]>=0
	model += rdc_vars['rdc_1_disp_c1_{}'.format(i+1)]>=0

###make the RDC2 constraints, 

model += rdc2_opng  - rdc_vars['rdc_2_disp_c1_1'] - rdc_vars['rdc_2_disp_c2_1'] - rdc_vars['rdc_2_disp_c3_1'] == rdc_vars['rdc_2_inv_1']
model += rdc_vars['rdc_2_disp_c2_1'] >= 0
model += rdc_vars['rdc_2_disp_c3_1'] >= 0
model += rdc_vars['rdc_2_inv_1'] >=0
model += rdc_vars['rdc_2_disp_c1_1'] ==0

model += rdc_vars['rdc_2_inv_1']  - rdc_vars['rdc_2_disp_c1_2'] - rdc_vars['rdc_2_disp_c2_2'] - rdc_vars['rdc_2_disp_c3_2'] == rdc_vars['rdc_2_inv_2']
model += rdc_vars['rdc_2_disp_c2_2'] >= 0
model += rdc_vars['rdc_2_disp_c3_2'] >= 0
model += rdc_vars['rdc_2_inv_2'] >=0
model += rdc_vars['rdc_2_disp_c1_2'] ==0


model += rdc_vars['rdc_2_inv_2']  - rdc_vars['rdc_2_disp_c1_3'] - rdc_vars['rdc_2_disp_c2_3'] - rdc_vars['rdc_2_disp_c3_3'] == rdc_vars['rdc_2_inv_3']
model += rdc_vars['rdc_2_disp_c2_3'] >= 0
model += rdc_vars['rdc_2_disp_c3_3'] >= 0
model += rdc_vars['rdc_2_inv_3'] >=0
model += rdc_vars['rdc_2_disp_c1_3'] ==0



for i in range(3,31):

	model += rdc_vars['rdc_2_inv_{}'.format(i)] - rdc_vars['rdc_2_disp_c1_{}'.format(i+1)] - rdc_vars['rdc_2_disp_c2_{}'.format(i+1)]  - rdc_vars['rdc_2_disp_c3_{}'.format(i+1)] + factory_vars['f1_r2_disp_{}'.format(i+1-3)] + factory_vars['f2_r2_disp_{}'.format(i+1-3)]== rdc_vars['rdc_2_inv_{}'.format(i+1)]
	model += rdc_vars['rdc_2_disp_c1_{}'.format(i+1)] == 0
	model += rdc_vars['rdc_2_disp_c2_{}'.format(i+1)] >= 0
	model += rdc_vars['rdc_2_disp_c3_{}'.format(i+1)] >= 0
	model += rdc_vars['rdc_2_inv_{}'.format(i+1)]>=0


M = 10000
service_level = 0.95

###make the C1 constraints 

model += c1_opng - c1[0] + cust_vars['cust_1_slack_1'] == cust_vars['cust_1_inv_1']
model += c1_opng - c1[0] >= -M * cust_vars['cust_1_bin_1']
model += c1_opng - c1[0] <= 0.001 + M * (1 - cust_vars['cust_1_bin_1'])
model += cust_vars['cust_1_inv_1']>=0
model += cust_vars['cust_1_slack_1'] <= M*cust_vars['cust_1_bin_1']
model += cust_vars['cust_1_slack_1'] >= 0
model += cust_vars['cust_1_inv_1'] <= M*(1-cust_vars['cust_1_bin_1'])

model += cust_vars['cust_1_inv_1'] - c1[1] + cust_vars['cust_1_slack_2'] == cust_vars['cust_1_inv_2']
model += cust_vars['cust_1_inv_1'] - c1[1] >= -M * cust_vars['cust_1_bin_2']
model += cust_vars['cust_1_inv_1'] - c1[1] <= 0.001 + M * (1 - cust_vars['cust_1_bin_2'])
model += cust_vars['cust_1_inv_2']>=0
model += cust_vars['cust_1_slack_2'] <= M*cust_vars['cust_1_bin_2']
model += cust_vars['cust_1_slack_2'] >= 0
model += cust_vars['cust_1_inv_2'] <= M*(1-cust_vars['cust_1_bin_2'])


for i in range(2,31):
	model += cust_vars['cust_1_inv_{}'.format(i)] - c1[i] + cust_vars['cust_1_slack_{}'.format(i+1)] + rdc_vars['rdc_1_disp_c1_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c1_{}'.format(i+1-2)] == cust_vars['cust_1_inv_{}'.format(i+1)]
	model += rdc_vars['rdc_2_disp_c1_{}'.format(i+1-2)]==0

	model += cust_vars['cust_1_inv_{}'.format(i)]+rdc_vars['rdc_1_disp_c1_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c1_{}'.format(i+1-2)]   - c1[i] >= -M * cust_vars['cust_1_bin_{}'.format(i+1)]
	model += cust_vars['cust_1_inv_{}'.format(i)]+rdc_vars['rdc_1_disp_c1_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c1_{}'.format(i+1-2)] - c1[i] <= 0.001 + M * (1 - cust_vars['cust_1_bin_{}'.format(i+1)])

	model += cust_vars['cust_1_inv_{}'.format(i+1)]>=0
	model += cust_vars['cust_1_slack_{}'.format(i+1)] <= M*cust_vars['cust_1_bin_{}'.format(i+1)]
	model += cust_vars['cust_1_slack_{}'.format(i+1)] >= 0
	model += cust_vars['cust_1_inv_{}'.format(i+1)] <= M*(1-cust_vars['cust_1_bin_{}'.format(i+1)])



# make the C2 constraints

model += c2_opng - c2[0] + cust_vars['cust_2_slack_1'] == cust_vars['cust_2_inv_1']
model += c2_opng - c2[0] >= -M * cust_vars['cust_2_bin_1']
model += c2_opng - c2[0] <= 0.001 + M * (1 - cust_vars['cust_2_bin_1'])
model += cust_vars['cust_2_inv_1']>=0
model += cust_vars['cust_2_slack_1'] <= M*cust_vars['cust_2_bin_1']
model += cust_vars['cust_2_slack_1'] >= 0
model += cust_vars['cust_2_inv_1'] <= M*(1-cust_vars['cust_2_bin_1'])



model += cust_vars['cust_2_inv_1'] - c2[1] + cust_vars['cust_2_slack_2'] == cust_vars['cust_2_inv_2']
model += cust_vars['cust_2_inv_1'] - c2[1] >= -M * cust_vars['cust_2_bin_2']
model += cust_vars['cust_2_inv_1'] - c2[1] <= 0.001 + M * (1 - cust_vars['cust_2_bin_2'])
model += cust_vars['cust_2_inv_2']>=0
model += cust_vars['cust_2_slack_2'] <= M*cust_vars['cust_2_bin_2']
model += cust_vars['cust_2_slack_2'] >= 0
model += cust_vars['cust_2_inv_2'] <= M*(1-cust_vars['cust_2_bin_2'])



for i in range(2,31):
	model += cust_vars['cust_2_inv_{}'.format(i)] - c1[i] + cust_vars['cust_2_slack_{}'.format(i+1)] + rdc_vars['rdc_1_disp_c2_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c2_{}'.format(i+1-2)] == cust_vars['cust_2_inv_{}'.format(i+1)]
	# model += rdc_vars['rdc_2_disp_c1_{}'.format(i+1-2)]==0

	model += cust_vars['cust_2_inv_{}'.format(i)]+rdc_vars['rdc_1_disp_c2_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c2_{}'.format(i+1-2)]   - c2[i] >= -M * cust_vars['cust_2_bin_{}'.format(i+1)]
	model += cust_vars['cust_2_inv_{}'.format(i)]+rdc_vars['rdc_1_disp_c2_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c2_{}'.format(i+1-2)] - c2[i] <= 0.001 + M * (1 - cust_vars['cust_2_bin_{}'.format(i+1)])

	model += cust_vars['cust_2_inv_{}'.format(i+1)]>=0
	model += cust_vars['cust_2_slack_{}'.format(i+1)] <= M*cust_vars['cust_2_bin_{}'.format(i+1)]
	model += cust_vars['cust_2_slack_{}'.format(i+1)] >= 0
	model += cust_vars['cust_2_inv_{}'.format(i+1)] <= M*(1-cust_vars['cust_2_bin_{}'.format(i+1)])


##make the C3 constraints




model += c3_opng - c3[0] + cust_vars['cust_3_slack_1'] == cust_vars['cust_3_inv_1']
model += c3_opng - c3[0] >= -M * cust_vars['cust_3_bin_1']
model += c3_opng - c3[0] <= 0.001 + M * (1 - cust_vars['cust_3_bin_1'])
model += cust_vars['cust_3_inv_1']>=0
model += cust_vars['cust_3_slack_1'] <= M*cust_vars['cust_3_bin_1']
model += cust_vars['cust_3_slack_1'] >= 0
model += cust_vars['cust_3_inv_1'] <= M*(1-cust_vars['cust_3_bin_1'])



model += cust_vars['cust_3_inv_1'] - c3[1] + cust_vars['cust_3_slack_2'] == cust_vars['cust_3_inv_2']
model += cust_vars['cust_3_inv_1'] - c3[1] >= -M * cust_vars['cust_3_bin_2']
model += cust_vars['cust_3_inv_1'] - c3[1] <= 0.001 + M * (1 - cust_vars['cust_3_bin_2'])
model += cust_vars['cust_3_inv_2']>=0
model += cust_vars['cust_3_slack_2'] <= M*cust_vars['cust_3_bin_2']
model += cust_vars['cust_3_slack_2'] >= 0
model += cust_vars['cust_3_inv_2'] <= M*(1-cust_vars['cust_3_bin_2'])



for i in range(2,31):
	model += cust_vars['cust_3_inv_{}'.format(i)] - c1[i] + cust_vars['cust_3_slack_{}'.format(i+1)] + rdc_vars['rdc_1_disp_c3_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c3_{}'.format(i+1-2)] == cust_vars['cust_3_inv_{}'.format(i+1)]
	# model += rdc_vars['rdc_2_disp_c1_{}'.format(i+1-2)]==0

	model += cust_vars['cust_3_inv_{}'.format(i)]+rdc_vars['rdc_1_disp_c3_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c3_{}'.format(i+1-2)]   - c3[i] >= -M * cust_vars['cust_3_bin_{}'.format(i+1)]
	model += cust_vars['cust_3_inv_{}'.format(i)]+rdc_vars['rdc_1_disp_c3_{}'.format(i+1-2)] + rdc_vars['rdc_2_disp_c3_{}'.format(i+1-2)] - c3[i] <= 0.001 + M * (1 - cust_vars['cust_3_bin_{}'.format(i+1)])

	model += cust_vars['cust_3_inv_{}'.format(i+1)]>=0
	model += cust_vars['cust_3_slack_{}'.format(i+1)] <= M*cust_vars['cust_3_bin_{}'.format(i+1)]
	model += cust_vars['cust_3_slack_{}'.format(i+1)] >= 0
	model += cust_vars['cust_3_inv_{}'.format(i+1)] <= M*(1-cust_vars['cust_3_bin_{}'.format(i+1)])




factory_holding_cost = 1
rdc1_holding_cost = 2
rdc2_holding_cost = 1.8
customer_holding_cost = 3

factory_holding = factory_vars['f1_inv_1']
rdc_1_holding = rdc_vars['rdc_1_inv_1']
rdc_2_holding = rdc_vars['rdc_2_inv_1']
c1_holding = cust_vars['cust_1_inv_1']
c2_holding = cust_vars['cust_2_inv_1']
c3_holding = cust_vars['cust_3_inv_1']
slack_volume = cust_vars['cust_1_slack_1']+cust_vars['cust_2_slack_1']+cust_vars['cust_3_slack_1']

for i in range(2,32):
	factory_holding = factory_holding+factory_vars['f1_inv_{}'.format(i)]
	rdc_1_holding = rdc_1_holding+rdc_vars['rdc_1_inv_{}'.format(i)]
	rdc_2_holding = rdc_2_holding+rdc_vars['rdc_2_inv_{}'.format(i)]
	c1_holding = c1_holding+cust_vars['cust_1_inv_{}'.format(i)]
	c2_holding = c2_holding+cust_vars['cust_2_inv_{}'.format(i)]
	c3_holding = c3_holding+cust_vars['cust_3_inv_{}'.format(i)]
	slack_volume = slack_volume + cust_vars['cust_1_slack_{}'.format(i)]+ cust_vars['cust_2_slack_{}'.format(i)]+ cust_vars['cust_3_slack_{}'.format(i)]



model += slack_volume <= (1-service_level)*(sum(c1)+sum(c2)+sum(c3))

model += factory_holding_cost*factory_holding + rdc_1_holding*rdc1_holding_cost + rdc_2_holding * rdc2_holding_cost + (c1_holding+c2_holding+c3_holding)*customer_holding_cost



model.solve()

df = pd.DataFrame()

f1_holding = []
f1_dispatch_r1 = []
f1_dispatch_r2 = []
f1_production = []

f2_holding = []
f2_dispatch_r1 = []
f2_dispatch_r2 = []
f2_production = []


rdc1_holding = []
rdc1_dispatch_c1 = []
rdc1_dispatch_c2 = []
rdc1_dispatch_c3 = []



rdc2_holding = []
rdc2_dispatch_c1 = []
rdc2_dispatch_c2 = []
rdc2_dispatch_c3 = []


c1_holding = []
c1_demand = []
c1_slack = []


c2_holding = []
c2_demand = []
c2_slack = []


c3_holding = []
c3_demand = []
c3_slack = []

for i in range(1,32):

	f1_holding.append(factory_vars['f1_inv_{}'.format(i)].varValue)
	f1_dispatch_r1.append(factory_vars['f1_r1_disp_{}'.format(i)].varValue)
	f1_dispatch_r2.append(factory_vars['f1_r2_disp_{}'.format(i)].varValue)
	f1_production.append(factory_vars['f1_prod_{}'.format(i)].varValue)


	f2_holding.append(factory_vars['f2_inv_{}'.format(i)].varValue)
	f2_dispatch_r1.append(factory_vars['f2_r1_disp_{}'.format(i)].varValue)
	f2_dispatch_r2.append(factory_vars['f2_r2_disp_{}'.format(i)].varValue)
	f2_production.append(factory_vars['f2_prod_{}'.format(i)].varValue)



	rdc1_holding.append(rdc_vars['rdc_1_inv_{}'.format(i)].varValue)
	rdc1_dispatch_c1.append(rdc_vars['rdc_1_disp_c1_{}'.format(i)].varValue)
	rdc1_dispatch_c2.append(rdc_vars['rdc_1_disp_c2_{}'.format(i)].varValue)
	rdc1_dispatch_c3.append(rdc_vars['rdc_1_disp_c3_{}'.format(i)].varValue)

	rdc2_holding.append(rdc_vars['rdc_2_inv_{}'.format(i)].varValue)
	rdc2_dispatch_c1.append(rdc_vars['rdc_2_disp_c1_{}'.format(i)].varValue)
	rdc2_dispatch_c2.append(rdc_vars['rdc_2_disp_c2_{}'.format(i)].varValue)
	rdc2_dispatch_c3.append(rdc_vars['rdc_2_disp_c3_{}'.format(i)].varValue)


	c1_holding.append(cust_vars['cust_1_inv_{}'.format(i)].varValue)
	c1_demand = c1
	c1_slack.append(cust_vars['cust_1_slack_{}'.format(i)].varValue)

	c2_holding.append(cust_vars['cust_2_inv_{}'.format(i)].varValue)
	c2_demand = c2
	c2_slack.append(cust_vars['cust_2_slack_{}'.format(i)].varValue)

	c3_holding.append(cust_vars['cust_3_inv_{}'.format(i)].varValue)
	c3_demand = c3
	c3_slack.append(cust_vars['cust_3_slack_{}'.format(i)].varValue)



df['f1_holding'] = f1_holding
df['f1_dispatch_r1'] = f1_dispatch_r1
df['f1_dispatch_r2'] = f1_dispatch_r2 
df['f1_production'] = f1_production 


df['f2_holding'] = f2_holding
df['f2_dispatch_r1'] = f2_dispatch_r1 
df['f2_dispatch_r2'] = f2_dispatch_r2
df['f2_production'] = f2_production



df['rdc1_holding'] =  rdc1_holding
df['rdc1_dispatch_c1'] = rdc1_dispatch_c1 
df['rdc1_dispatch_c2'] = rdc1_dispatch_c2
df['rdc1_dispatch_c3'] = rdc1_dispatch_c3

df['rdc2_holding'] = rdc2_holding 
df['rdc2_dispatch_c1'] = rdc2_dispatch_c1 
df['rdc2_dispatch_c2'] = rdc2_dispatch_c2
df['rdc2_dispatch_c3'] = rdc2_dispatch_c3 


df['c1_holding'] = c1_holding
df['c1_demand']  = c1_demand  
df['c1_slack'] = c1_slack 

df['c2_holding'] = c2_holding 
df['c2_demand']  = c2_demand
df['c2_slack'] = c2_slack

df['c3_holding'] = c3_holding 
df['c3_demand']  = c3_demand
df['c3_slack'] = c3_slack


print(df)

df.to_csv('results_MEIO.csv')



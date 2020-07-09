import simulator
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--scenario", type=str, help='scenario',default='scenario1')
parser.add_argument("--save_name", type=str, help='save_name',default='test')

parser.add_argument("--control_period", type=int, help='total_period',default=14)
parser.add_argument("--prob_s", type=float, help='prob_s',default=0.005)
parser.add_argument("--i_threshold", type=float, help='isolate_threshold',default=0.001)
parser.add_argument("--i_days", type=int, help='isolate_threshold',default=5)

args = parser.parse_args()

# Parameters
pop = 10000
total_period = 840 if args.scenario != 'submit' else 12600
control_period = args.control_period
prob_s = args.prob_s
isolate_threshold = args.i_threshold
isolate_days= args.i_days

# Initialize engine
file_name = args.save_name + '_' + str(args.i_threshold) + '_' + str(args.i_days)
engine = simulator.Engine(thread_num=8, write_mode="write", specified_run_name=file_name, scenario=args.scenario)
engine.reset()

# Start
for control_period_ in range(total_period // control_period):
    # Get current observations
    current_intervene = np.array([engine.get_individual_intervention_state(i) for i in range(pop)])
    current_infection = np.array([engine.get_individual_infection_state(i) for i in range(pop)])
    current_symptomatic = np.bitwise_or(current_infection == 3, current_infection == 4)
    current_symptomatic_set = set(np.where(current_symptomatic)[0])
    current_notsymptomatic_set = set(np.where(~current_symptomatic)[0])
    # Set treat
    set_treat = np.bitwise_and(current_symptomatic, current_intervene != 5) 
    set_treat = np.where(set_treat)[0]
    set_individual_hospitalize = {i:True for i in set_treat}
    engine.set_individual_to_treat(set_individual_hospitalize) 
    # Estimate the prob of being (not) infected
    current_discovered = set_treat
    num_areas = len(engine.get_all_area_category())
    prob_not_infected_by_discovered = np.ones(10000) # Initialize prob_not_infected_by_discovered
    prob_not_infected_by_discovered[current_symptomatic] = 0
    for loc_id in range(num_areas):
        his = engine.get_area_visited_history(loc_id) # find past individuals that visited the area
        for his_ in his: # for one hour 
            his_set = set(his_)
            # symtomatic/non-symtomatic individuals visited loc_id during this hour
            his_discovered = his_set & current_symptomatic_set 
            his_healthy = his_set & current_notsymptomatic_set
            # estimate the probability of being infected by symptomatic individuals
            sum_prob_infected = (1-prob_not_infected_by_discovered[list(his_healthy)]).sum()
            his_prob_infect = prob_s * len(his_discovered) / (len(his_)+1e-7)
            prob_not_infected_by_discovered[list(his_healthy)] *= 1-his_prob_infect
    # Set isolate
    set_isolate = np.bitwise_and(prob_not_infected_by_discovered < 1 - isolate_threshold, current_intervene == 1)
    set_isolate = np.where(set_isolate)[0]
    set_individual_isolate = {i:isolate_days for i in set_isolate}
    engine.set_individual_isolate_days(set_individual_isolate) 
    # Simulate
    for i in range(control_period):
        engine.next_step()

import simulator
import os
import json

period = 840

engine = simulator.Engine(thread_num=1, write_mode="write", specified_run_name="test", scenario="submit")

engine.reset()
for ind_round in range(15):
    # Here, we have 15 rounds of testing. Each round contains 840 steps.
    # Each of the 5 scenarios will be run for 3 times. But their order is unknown here.
    for i in range(period):

        engine.next_step()
        engine.get_current_time()

        # Here, we give the example to get the information about individual with id 1
        individual_id = 1
        engine.get_individual_visited_history(individual_id)
        engine.get_individual_infection_state(individual_id)
        engine.get_individual_visited_history(individual_id)

        # Here, we give the example to get the information about region with id 1
        region_id = 1
        engine.get_area_infected_cnt(region_id)

        # Here, we give the example to set actions for individual with id 1, 2, 3, and 4 respectively
        engine.set_individual_confine_days({1: 5}) # {individualID: day}
        engine.set_individual_quarantine_days({2: 5}) # {individualID: day}
        engine.set_individual_isolate_days({3: 5}) # {individualID: day}
        engine.set_individual_to_treat({4: True}) # {individualID: day}


del engine

import simulator
import os
import json

period = 840

for round in range(10):
    if round == 0:
        engine = simulator.Engine(thread_num=1, write_mode="write", specified_run_name="test")
    else:
        engine = simulator.Engine(thread_num=1, write_mode="append", specified_run_name="test")

    engine.reset()
    for i in range(period):
        print(engine.get_current_time())
        engine.next_step()

        engine.get_man_visited_history(1)
        engine.get_man_infection_state(1)
        engine.get_man_visited_history(1)
        engine.get_region_infected_cnt(1)

        engine.set_man_confine_days({1: 5}) # {manID: day}
        engine.set_man_quarantine_days({2: 5}) # {manID: day}
        engine.set_man_isolate_days({3: 5}) # {manID: day}
        engine.set_man_to_treat({4: True}) # {manID: day}

    del engine

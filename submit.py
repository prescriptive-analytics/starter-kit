import simulator
import os
import json

period = 840

engine = simulator.Engine()

engine.reset()
for i in range(period):
    engine.next_step()
    print(engine.get_current_time())
    print(engine.get_man_visited_history(1))
    print(engine.get_man_infection_state(1))
    print(engine.get_man_visited_history(1))
    print(engine.get_region_infected_cnt(1))

    engine.set_man_confine_days({1: 5}) # {manID: day}
    engine.set_man_quarantine_days({2: 5}) # {manID: day}
    engine.set_man_isolate_days({3: 5}) # {manID: day}
    engine.set_man_to_treat({4: True}) # {manID: day}

del engine

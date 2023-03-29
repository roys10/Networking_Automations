from nornir import InitNornir
from nornir.core.filter import F
# from nornir_utils.plugins.tasks import napalm_configure
# from nornir_utils.plugins.functions import print_result
import napalm

# https://www.youtube.com/watch?v=vrZ4FD5BuXs&ab_channel=RAYKA
# https://www.youtube.com/watch?v=NHEusQfBgHw&ab_channel=NANOG
# https://www.youtube.com/watch?v=DAAYN75kVfw&ab_channel=RogerPerkin

def nornir_napalm_send_config(task):
    task.run(task=napalm_configure, filename="config_file.txt")

nr = InitNornir(config_file="config.yml")

results = nr.run(task=nornir_napalm_send_config)
print(results)

switch_groups = nr.filter(F(group_contains="Mamram"))



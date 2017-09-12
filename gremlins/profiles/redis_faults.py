import signal

from gremlins import faults, metafaults, triggers, tc


clear_network_faults = faults.clear_network_faults()
introduce_packet_loss = faults.introduce_network_packet_loss()
introduce_partition = faults.introduce_network_partition()
introduce_latency = faults.introduce_network_latency()
introduce_packet_reordering = faults.introduce_packet_reordering()


profile = [
    triggers.OneShot(clear_network_faults),
    triggers.Periodic(
        10, metafaults.pick_fault([
            (10, clear_network_faults),
            # (10, introduce_packet_loss),
            (10, introduce_partition),
            (10, introduce_latency),
            # (10, introduce_packet_reordering),
        ])),
    #  triggers.WebServerTrigger(12321)
]

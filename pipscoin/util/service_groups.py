from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "pipscoin_harvester pipscoin_timelord_launcher pipscoin_timelord pipscoin_farmer pipscoin_full_node pipscoin_wallet".split(),
    "node": "pipscoin_full_node".split(),
    "harvester": "pipscoin_harvester".split(),
    "farmer": "pipscoin_harvester pipscoin_farmer pipscoin_full_node pipscoin_wallet".split(),
    "farmer-no-wallet": "pipscoin_harvester pipscoin_farmer pipscoin_full_node".split(),
    "farmer-only": "pipscoin_farmer".split(),
    "timelord": "pipscoin_timelord_launcher pipscoin_timelord pipscoin_full_node".split(),
    "timelord-only": "pipscoin_timelord".split(),
    "timelord-launcher-only": "pipscoin_timelord_launcher".split(),
    "wallet": "pipscoin_wallet pipscoin_full_node".split(),
    "wallet-only": "pipscoin_wallet".split(),
    "introducer": "pipscoin_introducer".split(),
    "simulator": "pipscoin_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())

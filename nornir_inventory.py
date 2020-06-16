from nornir.core.deserializer.inventory import Inventory
import io


class MyInventory(Inventory):
    def __init__(self, **kwargs):
        hosts = {
            "sw1": {
                "data": {
                    "foo": "bar",
                    "log": io.BytesIO()
                },
                "hostname": "192.168.123.21",
                "username": "neops",
                "password": "cisco",
                "platform": "ios",
                "groups": [],
                "connection_options": {
                    "napalm": {
                        "extras": {
                            "optional_args": {}
                        }
                    },
                    "netmiko": {
                        "extras": {}
                    }
                }
            },
            "sw2": {
                "data": {
                    "foo": "foo",
                    "log": io.BytesIO()
                },
                "hostname": "192.168.123.22",
                "username": "neops",
                "password": "cisco",
                "platform": "ios",
                "groups": [],
                "connection_options": {
                    "napalm": {
                        "extras": {
                            "optional_args": {}
                        }
                    },
                    "netmiko": {
                        "extras": {}
                    }
                }
            }
        }

        # set logging
        for key, item in hosts.items():
            item["connection_options"]["napalm"]["extras"]["optional_args"]["session_log"] = item["data"]["log"]  # noqa 501
            item["connection_options"]["netmiko"]["extras"]["session_log"] = item["data"]["log"]  # noqa 501

        groups = {
        }
        defaults = {
        }

        super().__init__(
            hosts=hosts,
            groups=groups,
            defaults=defaults,
            **kwargs
        )

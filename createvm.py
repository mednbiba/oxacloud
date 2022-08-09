#Converted CURL request from Vcenter's API Documentation

import requests

headers = {
    'vmware-api-session-id': 'b00db39f948d13ea1e59b4d6fce56389',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
}

json_data = {
    'boot': {
        'delay': 0,
        'efi_legacy_boot': False,
        'enter_setup_mode': False,
        'network_protocol': 'IPV4',
        'retry': False,
        'retry_delay': 0,
        'type': 'BIOS',
    },
    'boot_devices': [
        {
            'type': 'CDROM',
        },
    ],
    'cdroms': [
        {
            'allow_guest_control': False,
            'backing': {
                'device_access_type': 'EMULATION',
                'host_device': 'string',
                'iso_file': 'string',
                'type': 'ISO_FILE',
            },
            'ide': {
                'master': False,
                'primary': False,
            },
            'sata': {
                'bus': 0,
                'unit': 0,
            },
            'start_connected': False,
            'type': 'IDE',
        },
    ],
    'cpu': {
        'cores_per_socket': 0,
        'count': 0,
        'hot_add_enabled': False,
        'hot_remove_enabled': False,
    },
    'disks': [
        {
            'backing': {
                'type': 'VMDK_FILE',
                'vmdk_file': 'string',
            },
            'ide': {
                'master': False,
                'primary': False,
            },
            'new_vmdk': {
                'capacity': 0,
                'name': 'string',
                'storage_policy': {
                    'policy': 'string',
                },
            },
            'nvme': {
                'bus': 0,
                'unit': 0,
            },
            'sata': {
                'bus': 0,
                'unit': 0,
            },
            'scsi': {
                'bus': 0,
                'unit': 0,
            },
            'type': 'IDE',
        },
    ],
    'floppies': [
        {
            'allow_guest_control': False,
            'backing': {
                'host_device': 'string',
                'image_file': 'string',
                'type': 'IMAGE_FILE',
            },
            'start_connected': False,
        },
    ],
    'guest_OS': 'DOS',
    'hardware_version': 'VMX_03',
    'memory': {
        'hot_add_enabled': False,
        'size_MiB': 0,
    },
    'name': 'string',
    'nics': [
        {
            'allow_guest_control': False,
            'backing': {
                'distributed_port': 'string',
                'network': 'string',
                'type': 'STANDARD_PORTGROUP',
            },
            'mac_address': 'string',
            'mac_type': 'MANUAL',
            'pci_slot_number': 0,
            'start_connected': False,
            'type': 'E1000',
            'upt_compatibility_enabled': False,
            'wake_on_lan_enabled': False,
        },
    ],
    'nvme_adapters': [
        {
            'bus': 0,
            'pci_slot_number': 0,
        },
    ],
    'parallel_ports': [
        {
            'allow_guest_control': False,
            'backing': {
                'file': 'string',
                'host_device': 'string',
                'type': 'FILE',
            },
            'start_connected': False,
        },
    ],
    'placement': {
        'cluster': 'string',
        'datastore': 'string',
        'folder': 'string',
        'host': 'string',
        'resource_pool': 'string',
    },
    'sata_adapters': [
        {
            'bus': 0,
            'pci_slot_number': 0,
            'type': 'AHCI',
        },
    ],
    'scsi_adapters': [
        {
            'bus': 0,
            'pci_slot_number': 0,
            'sharing': 'NONE',
            'type': 'BUSLOGIC',
        },
    ],
    'serial_ports': [
        {
            'allow_guest_control': False,
            'backing': {
                'file': 'string',
                'host_device': 'string',
                'network_location': 'string',
                'no_rx_loss': False,
                'pipe': 'string',
                'proxy': 'string',
                'type': 'FILE',
            },
            'start_connected': False,
            'yield_on_poll': False,
        },
    ],
    'storage_policy': {
        'policy': 'string',
    },
}

response = requests.post('https://{api_host}/api/vcenter/vm', headers=headers, json=json_data)
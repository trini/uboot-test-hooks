# Copyright (c) 2015, NVIDIA CORPORATION. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

#env__mount_points = (
#    "/mnt/ubtest-mnt-p2371-2180-na",
#)
#
#env__usb_dev_ports = (
#    {
#        "fixture_id": "micro_b",
#        "tgt_usb_ctlr": "0",
#        "host_usb_dev_node": "/dev/bus/usb/by-path/pci-0000:02:00.0-usb-0:1.4.4.3",
#    },
#)

#env__block_devs = (
#    # SD card; present since I plugged one in
#    {
#        "fixture_id": "sd",
#        "type": "mmc",
#        "id": "0",
#        "writable_fs_partition": 2,
#        "writable_fs_subdir": "tmp/",
#    },
#)

#env__dfu_configs = (
    # SD card, partition 2, ext4 filesystem
#    {
#        "fixture_id": "sd_fs",
#        "alt_info": "/tmp/dfu_test.bin ext4 0 2;/tmp/dfu_dummy.bin ext4 0 2",
#        "cmd_params": "mmc 0",
#    },
    # RAM
#    {
#        "fixture_id": "ram",
#        "alt_info": "alt0 ram 80000000 01000000;alt1 ram 81000000 01000000",
#        "cmd_params": "ram na",
#        "test_sizes": (63, 64, 65),
#    },
#)

env__net_uses_usb = False

env__net_dhcp_server = True

env__net_tftp_readable_file = {
    "fn": "1MiBtest.bin",
    "size": 1048576,
    "crc32": "2fa737e0",
}

env__net_nfs_readable_file = {
    "fn": "/tftpboot/1MiBtest.bin",
    "size": 1048576,
    "crc32": "2fa737e0",
}

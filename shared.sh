#!/bin/sh
# Shared definitions for buildroot scripts

# The defconfig from the buildroot directory we use as our starting point
RPI5_DEFCONFIG=configs/raspberrypi5_defconfig
# The place we store customizations to the Pi 5 configuration
MODIFIED_RPI5_DEFCONFIG=base_external/configs/pilink_rpi5_defconfig
# The defconfig from the buildroot directory we use for the project
AESD_DEFAULT_DEFCONFIG=${RPI5_DEFCONFIG}
AESD_MODIFIED_DEFCONFIG=${MODIFIED_RPI5_DEFCONFIG}
AESD_MODIFIED_DEFCONFIG_REL_BUILDROOT=../${AESD_MODIFIED_DEFCONFIG}

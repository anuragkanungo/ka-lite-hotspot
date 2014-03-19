cat <<EOF | tee "/etc/udev/rules.d/95-ka-lite-hotspot.rules" > /dev/null 2>&1
ACTION=="add", SUBSYSTEM=="usb", ENV{ID_VENDOR_ID}=="148f", RUN+="`pwd`/ka-lite-hotspot restart"
ACTION=="remove", SUBSYSTEM=="usb", ENV{ID_VENDOR_ID}=="148f", RUN+="`pwd`/ka-lite-hotspot stop"
EOF


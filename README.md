ka-lite-hotspot
===============

Ubuntu scripts for generating a hotspot with ssid "kalite" upon connecting a Wi-Pi dongle.

The package also configures dnsmasq to route all DNS requests to the hotspot's adapter, and sets up port 80 to redirect to port 8008, so that all incoming requests are resolved to KA Lite.

To build the deb file, install the `devscripts` package and run the `./build_deb_file.sh` command.

# WP4: publish_device_temp_data
This repository is intended to publish time series temperature data to DHT to invoke the [Privacy-Aware Device Fault Detection Analytic](https://github.com/sifis-home/flask-device-anomaly-detection)

Build the image using the following command:

`docker build -t publish_device_temp_data .`

Run the Docker container using the commands shown below:

First Command:

`docker run -it -v /var/run/docker.sock:/var/run/docker.sock --net=host publish_device_temp_data python -m publish_device_temp_data --requestor_type NSSD --temp 22,23,21,26,25,20,28,29,23,28,21,22,25,27,30,29,29,26,21,26,23,24,25,24,22,23,21,26,25,20,28,29,23,28,21,22,25,27,30,29,29,26,21,26,23,24,25,24`

Second Command:

`docker run -it -v /var/run/docker.sock:/var/run/docker.sock --net=host publish_device_temp_data python -m publish_device_temp_data --requestor_type NSSD --temp 19.12986842,18.97528276,18.78109444,18.61134194,18.46130435,18.30064878,18.1754,18.065395,17.95954872,17.85228,17.75864211,17.62884,17.51735882,17.4929,17.46825263,17.50991875,17.88537297,19.29543684,20.3559,20.25651795,20.274,20.95731053,21.19933913,21.20485641,21.28777949,20.93873514,21.19835814,21.46036,21.21860625,21.21743529,20.80544,20.37007027,20.06127179,19.90968387,19.74453953,19.56573548,19.39732,19.26005,19.1358,19.04670909,18.971405,18.89797073,18.84261667,18.8075,18.734,18.64976667,18.56043684,18.4792`

---
## License

Released under the [MIT License](LICENSE).

## Acknowledgements

This software has been developed in the scope of the H2020 project SIFIS-Home with GA n. 952652.

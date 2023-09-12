# WP4: publish_device_temp_data_tado
This repository is intended to publish tado time series temperature data to DHT to invoke the [Privacy-Aware Device Fault Detection Analytic](https://github.com/sifis-home/flask-device-anomaly-detection)

Build the image using the following command:

`docker build -f Dockerfile -t publish_device_temp_data_tado .`

Run the Docker container using the following command:

`docker run -it -v /var/run/docker.sock:/var/run/docker.sock --net=host publish_device_temp_data_tado python -m publish_device_temp_data_tado --requestor_type NSSD`

---
## License

Released under the [MIT License](LICENSE).

## Acknowledgements

This software has been developed in the scope of the H2020 project SIFIS-Home with GA n. 952652.

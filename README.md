# Servarr

This project is a complete Servarr Helm Chart that includes also Sonarr, Radarr, Prowlarr, qBitTorrent, Jellyseerr, Jellyfin and Flaresovlerr as sub-charts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

- Git
- Helm
- Kuberentes Cluster (for testing purposes)
- Python 3

### Installing

1. Clone the repository:

```shell
$ git clone https://github.com/fonzdm/servarr.git && cd servarr
```

2. Do your magic by updating/adding files 😎
3. Prepare your [`values.yaml`](#values)
4. Try it in your cluster to check that everything is fine (replace the dot with the `servarr` folder if you workdir is different):

```shell
$ helm install servarr-dev . \
--namespace servarr-dev \
--create-namespace \
--values values.yaml
```

## Deployment

The deployment is as easy as running the following command:

```shell
$ helm install <release-name> <servarr-chart> \
--namespace servarr \
--create-namespace \
--values values.yaml
```

### Values

| **Parameter** | **Optional** | **Description** | **Default Value** | **Example Value** |
|---------------|--------------|-----------------|-------------------|-------------------|
| `global.apikey` | Required | Define a common API key that will be used to automate the entire integration. | `None` | `6d9df216-cac6-4f4a-9b25-5462026ce7be` |
| `global.storageClassName` | Required | Cluster storage class to be used for the volume creation. | `None` | `longhorn` |

<!-- Table init with some values just to give the idea on how it will be. A lot of values (almost all of them) are missing and MUST be filled in the table. -->

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/fonzdm/servarr/releases). 

## Authors

* **Alfonso De Masi** - *Chart idea and main development* - [fonzdm](https://github.com/fonzdm)

See also the list of [contributors](https://github.com/fonzdm/servarr/contributors) who participated in this project.

###### Keep in mind that each dependency has its own author and their contributors. Please, reach them out on their repositories.

<!--
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->

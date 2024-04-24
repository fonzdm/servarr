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

2. Prepare your [`values.yaml`](#values)
3. Try it in your cluster to check that everything is fine (replace the `servarr/servarr-chart` with the chart folder if your workdir is different):

```shell
$ helm install servarr-dev servarr/servarr-chart \
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

Please read [Helm Chart README.md](./servarr/servarr-chartREADME.md) for details on how to configure the values needed for this chart.

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Contributors

<a href="https://github.com/fonzdm/servarr/servarr-chartgraphs/contributors">
  <img src="https://contrib.rocks/image?repo=fonzdm/servarr" />
</a>

See the full list of [contributors](https://github.com/fonzdm/servarr/servarr-chartcontributors) who participated in this project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/fonzdm/servarr/servarr-chartreleases).

###### Keep in mind that each dependency has its own author and their contributors. Please, reach them out on their repositories.

## License

This project is licensed under the GNU AGPL v3 License - see the [LICENSE](LICENSE) file for details.

<!--
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->

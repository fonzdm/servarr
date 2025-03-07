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

2. Retrieve the dependencies

```shell
$ helm dependency update
```

> [!NOTE]
> If the previous command fails or goes in timeout (or takes too much), try adding the truecharts Helm repository:
> ```shell
> $ helm repo add truecharts https://charts.truecharts.org
> ```
> and then execute again the `helm dependency update` command.
  
3. Prepare your [`values.yaml`](#values)
4. Try it in your cluster to check that everything is fine (replace the `servarr/` with the chart folder if your workdir is different):

```shell
$ helm install servarr-dev servarr/ \
--namespace servarr-dev \
--create-namespace \
--values values.yaml
```

## Deployment

To deploy the Helm Chart:

1. Add the Helm repository:

```shell
$ helm repo add fonzdm https://fonzdm.github.io/servarr
```

2. Install the release:

```shell
$ helm install <release-name> fonzdm/servarr \
--namespace servarr \
--create-namespace \
--values values.yaml
```

> [!WARNING]
>
> A minimum set of values must include the various parameters with the anchor reference, otherwise the anchors won't work as intended and the deployment may fail. Please, read the [Helm Chart README.md](./servarr/README.md) section to see a minimal `values.yaml` sample.

If you want to install a specific version, execute the previous command adding: `--version x.y.z`

### Values

Please read [Helm Chart README.md](./servarr/README.md) for further details on the values supported by the Chart.

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Contributors

<a href="https://github.com/fonzdm/servarr/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=fonzdm/servarr" />
</a>

See the full list of [contributors](https://github.com/fonzdm/servarr/contributors) who participated in this project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [releases on this repository](https://github.com/fonzdm/servarr/releases). 

###### Keep in mind that each dependency has its own author and their contributors. Please, reach them out on their repositories.

## License

This project is licensed under the GNU AGPL v3 License - see the [LICENSE](LICENSE) file for details.

<!--
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->

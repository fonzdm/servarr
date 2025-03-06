# servarr



![Version: 1.0.2](https://img.shields.io/badge/Version-1.0.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.2](https://img.shields.io/badge/AppVersion-1.0.2-informational?style=flat-square) 

Servarr complete Helm Chart for Kubernetes

**Homepage:** <https://github.com/fonzdm/servarr>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Alfonso De Masi | <adm220297@proton.me> |  |

## Source Code

* <https://github.com/fonzdm/servarr>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://imgios.github.io/scraparr | scraparr | 1.0.1 |
| oci://tccr.io/truecharts | flaresolverr | 13.4.1 |
| oci://tccr.io/truecharts | jellyfin | 18.7.7 |
| oci://tccr.io/truecharts | jellyseerr | 9.5.2 |
| oci://tccr.io/truecharts | prowlarr | 16.2.1 |
| oci://tccr.io/truecharts | qbittorrent | 19.4.1 |
| oci://tccr.io/truecharts | radarr | 21.2.1 |
| oci://tccr.io/truecharts | sonarr | 21.2.1 |

---

> [!IMPORTANT]  
> Please consider that this chart is a collection of several public helm charts.
> These are included as sub-charts of the Servarr chart and, due to some Helm limitation, some configuration are only possible via values file.
> For this reason, the servarr default [values.yaml](#./values.yaml) included in the chart is quite huge and it used to model the configuration of the subcharts.
> But don't you worry! I provided some handy values, using [yaml anchors](https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd), to defined top-level fields.
> Follow the table below and forget everything else. 

> [!CAUTION] 
> Please, do not remove Anchors when you see them (the strange syntax with the `&`)

---

## Values

### Jellyfin

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dash.countryCode | string | US | Insert the Jellyfin country code |
| dash.mail | string | No default value | Insert Jellyfin login mail (will be used also for Jellyseerr integration) |
| dash.password | string | No default value | Insert Jellyfin password (will be used also for Jellyseerr) |
| dash.preferredLanguage | string | en | Insert the Jellyfin preferred language |
| dash.username | string | No default value | Insert the Jellyfin username (will be used also for Jellyseerr) |

### Global

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apikey | string | No default value is configured for security reasons | Insert your Prowlarr, Sonarr, Radarr API key here (one to rule them all!). Do not remove the `&` anchor! |
| global.certManagerClusterIssuer | string | No default value, leave empty if not required | Insert your cert manager cluster issuer, e.g.: letsencrypt-cloudflare. Do not remove the `&issuer` anchor! |
| global.ingressClassName | string | nginx | Insert your ingress class here, e.g.: &ingressClassName nginx. Do not remove the `&ingressCassName` anchor, and do not leave the anchor value empty, otherwise you will face a `null` value error! |
| global.storageClassName | string | `"network-block"` | Insert your storage class here, e.g.: &storageClassName network-block. Do not remove the `&storageClassName` anchor! |

### Prowlarr

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| indexers | list | The body of the 1337x index is provided as default | The indexers list. Each element of the list is the yaml-formatted body of the [Prowlarr API request](https://prowlarr.com/docs/api/#/Indexer/post_api_v1_indexer) to add that index. |

### Metrics

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| metrics.enabled | bool | `false` | Anchor to set wether to deploy the export sidecar pods or not. Requires the Prometheus stack. Do not remove the `&metricsEnabled` anchor! |

### Jellyseerr

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| notifications.telegram.bot_apitoken | string | No default value | Insert your Telegram Bot API token |
| notifications.telegram.chat_id | string | No default value | Insert the Telegram Chat id, check @get_id_bot for this |
| notifications.telegram.enabled | bool | `true` | Enable the Telegram notifications |

### Torrent

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| qbittorrent.addons.vpn | object | See configuration below | Addon configuration for the VPN |
| qbittorrent.addons.vpn.env | map | Empty map | Environment variables to inject into the sidecar container. See the related VPN config in TrueCharts |
| qbittorrent.addons.vpn.excludedNetworks_IPv4 | list | 192.168.0.1/24 | Which subnets to exclude from the VPN |
| qbittorrent.addons.vpn.inputPorts | list | [80, 8080, 443, 50513] | Ports to be mapped for external access |
| qbittorrent.addons.vpn.killSwitch | bool | true | The flag changes the behavior in case of a tunnel failure (for example, the VPN tunnel cannot be established because the credentials are incorrect). If set to true, a failed tunnel will result in a missing connection (qBitTorrent won't connect externally). If set to false, the connection will use the standard configuration (exposing the user IP). |
| qbittorrent.addons.vpn.type | string | disabled | Type of the VPN to use, defaults to disabled. See: https://truecharts.org/guides/addons/vpn-setup/ |
| qbittorrent.csrf_protection | bool | false | Whether to enable or disable CSRF Protection on qBitTorrent WebGUI |
| torrent.password | string | No default value | password of the qBitTorrent admin user. Must be at least of 8 characters. |
| torrent.username | string | No default value | username of the qBitTorrent admin user |

### Scraparr

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| scraparr.config.prowlarr.api_key | string | *apikey | Anchor to apiKey. As a single key is used for all services, same will be used for interacting with Sonarr, Radarr, Prowlarr |
| scraparr.config.prowlarr.api_version | string | v3 | - Insert Prowlarr API versions, if different version wants to be used |
| scraparr.config.prowlarr.url | string | No default value | Mandatory - Insert Prowlarr service name in format: {{ .Release.Namespace }}-prowlarr |
| scraparr.config.radarr.api_key | string | *apikey | Anchor to apiKey. As a single key is used for all services, same will be used for interacting with Sonarr, Radarr, Prowlarr |
| scraparr.config.radarr.api_version | string | v3 | - Insert Radarr API versions, if different version wants to be used |
| scraparr.config.radarr.url | string | No default value | Mandatory - Insert Radarr service name in format: {{ .Release.Namespace }}-radarr |
| scraparr.config.sonarr.api_key | string | *apikey | Anchor to apiKey. As a single key is used for all services, same will be used for interacting with Sonarr, Radarr, Prowlarr |
| scraparr.config.sonarr.api_version | string | v3 | - Insert Sonarr API versions, if different version wants to be used |
| scraparr.config.sonarr.url | string | No default value | Mandatory - Insert Sonarr service name in format: {{ .Release.Namespace }}-sonarr |

### Tags

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| tags.movies | bool | true | This tag will deploy: Radarr, Prowlarr, QBitTorrent, Jellyseerr, Jellyfin, Flaresolverr |
| tags.music | bool | true | This tag will deploy: Prowlarr, QBitTorrent, Jellyfin, Flaresolverr |
| tags.tvseries | bool | true | This tag will deploy: Sonarr, Prowlarr, QBitTorrent, Jellyseerr, Jellyfin, Flaresolverr |

### Storage

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| volumes.downloads | object | See the sub fields | configuration of the volume used for torrent downloads |
| volumes.downloads.name | string | `"downloads-volume"` | Name of the download pvc. Do not remove the `&downloads-volume` anchor! |
| volumes.downloads.size | string | `"100Gi"` | Size of the downloads volume, in Kubernets format |
| volumes.media | object | See the sub fields | configuration of the volume used for media storage (i.e.: where movies and tv shows file will be permanently stored) |
| volumes.media.name | string | `"media-volume"` | Name of the media pvc. Do not remove the `&media-volume` anchor! |
| volumes.media.size | string | `"250Gi"` | Size of the media volume, in Kubernets format |
| volumes.torrentConfig | object | See the sub fields | configuration of the volume used for qBitTorrent internal configuration |
| volumes.torrentConfig.name | string | `"torrent-config"` | Name of the torrent configuration pvc. Do not remove the `&torrentConfig` anchor! |
| volumes.torrentConfig.size | string | `"250Mi"` | Size of the torrent configuration volume, in Kubernets format |

### Other Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| flaresolverr | object | `{}` |  |
| jellyfin | object | `{}` |  |
| jellyseerr | object | `{}` |  |
| prowlarr | object | `{}` |  |
| radarr | object | `{}` |  |
| scraparr.enabled | bool | `false` |  |
| sonarr | object | `{}` |  |


----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

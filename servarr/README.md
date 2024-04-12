# servarr

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

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
| https://charts.truecharts.org | flaresolverr | 13.4.1 |
| https://charts.truecharts.org | jellyfin | 18.7.7 |
| https://charts.truecharts.org | jellyseerr | 9.5.2 |
| https://charts.truecharts.org | prowlarr | 16.2.1 |
| https://charts.truecharts.org | qbittorrent | 19.4.1 |
| https://charts.truecharts.org | radarr | 21.2.1 |
| https://charts.truecharts.org | sonarr | 21.2.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dash.mail | string | `nil` | Insert Jellyfin login mail (will be used also for Jellyseerr integration) |
| dash.password | string | `nil` | Insert Jellyfin password (will be used also for Jellyseerr) |
| dash.username | string | `nil` | Insert the Jellyfin username (will be used also for Jellyseerr) |
| flaresolverr.metrics.main.enabled | bool | `false` |  |
| flaresolverr.persistence.config.accessModes | string | `"ReadWriteMany"` |  |
| flaresolverr.persistence.config.enabled | bool | `true` |  |
| flaresolverr.persistence.config.size | string | `"500Mi"` |  |
| flaresolverr.persistence.config.storageClass | string | `nil` |  |
| flaresolverr.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| flaresolverr.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| flaresolverr.persistence.config.targetSelector.main.main.mountPath | string | `"/config"` |  |
| flaresolverr.persistence.config.type | string | `"pvc"` |  |
| global.apikey | string | `nil` | Insert your API key here, e.g.: &apikey 123abc.. |
| global.certManagerClusterIssuer | string | `nil` | Insert your cert manager cluster issuer, e.g.: letsencrypt-cloudflare |
| global.storageClassName | string | `nil` | Insert your storage class here, e.g.: &storageClassName longhorn |
| indexers | list | The body of the 1337x index is provided as default | The indexers list. Each element of the list is the yaml-formatted boody of the [Prowlarr API request](https://prowlarr.com/docs/api/#/Indexer/post_api_v1_indexer) to add that index. |
| initJellyseerr | bool | `true` | Set initJellyseerr to false if Jellyseerr setup should not be performed automatically |
| issuer | object | `{"cloudFlareKey":null,"email":null,"ingressClassName":"nginx","secretName":"letsencrypt-prod","server":"https://acme-v02.api.letsencrypt.org/directory"}` | For tracking purpose, not used - replaced with pre-existing cluster issuer |
| issuer.cloudFlareKey | string | `nil` | Insert your CloudFlare key |
| issuer.email | string | `nil` | Insert your email address |
| jellyfin.fallbackDefaults.accessModes[0] | string | `"ReadWriteMany"` |  |
| jellyfin.fallbackDefaults.persistenceType | string | `"pvc"` |  |
| jellyfin.fallbackDefaults.pgVersion | int | `16` |  |
| jellyfin.fallbackDefaults.probeTimeouts.liveness.failureThreshold | int | `5` |  |
| jellyfin.fallbackDefaults.probeTimeouts.liveness.initialDelaySeconds | int | `10` |  |
| jellyfin.fallbackDefaults.probeTimeouts.liveness.periodSeconds | int | `10` |  |
| jellyfin.fallbackDefaults.probeTimeouts.liveness.successThreshold | int | `1` |  |
| jellyfin.fallbackDefaults.probeTimeouts.liveness.timeoutSeconds | int | `5` |  |
| jellyfin.fallbackDefaults.probeTimeouts.readiness.failureThreshold | int | `5` |  |
| jellyfin.fallbackDefaults.probeTimeouts.readiness.initialDelaySeconds | int | `10` |  |
| jellyfin.fallbackDefaults.probeTimeouts.readiness.periodSeconds | int | `10` |  |
| jellyfin.fallbackDefaults.probeTimeouts.readiness.successThreshold | int | `2` |  |
| jellyfin.fallbackDefaults.probeTimeouts.readiness.timeoutSeconds | int | `5` |  |
| jellyfin.fallbackDefaults.probeTimeouts.startup.failureThreshold | int | `60` |  |
| jellyfin.fallbackDefaults.probeTimeouts.startup.initialDelaySeconds | int | `10` |  |
| jellyfin.fallbackDefaults.probeTimeouts.startup.periodSeconds | int | `5` |  |
| jellyfin.fallbackDefaults.probeTimeouts.startup.successThreshold | int | `1` |  |
| jellyfin.fallbackDefaults.probeTimeouts.startup.timeoutSeconds | int | `2` |  |
| jellyfin.fallbackDefaults.probeType | string | `"http"` |  |
| jellyfin.fallbackDefaults.pvcRetain | bool | `false` |  |
| jellyfin.fallbackDefaults.pvcSize | string | `"100Gi"` |  |
| jellyfin.fallbackDefaults.serviceProtocol | string | `"tcp"` |  |
| jellyfin.fallbackDefaults.serviceType | string | `"ClusterIP"` |  |
| jellyfin.fallbackDefaults.storageClass | string | `nil` |  |
| jellyfin.fallbackDefaults.vctAccessModes[0] | string | `"ReadWriteMany"` |  |
| jellyfin.fallbackDefaults.vctSize | string | `"100Gi"` |  |
| jellyfin.ingress.jellyfin-ing.annotations."cert-manager.io/cluster-issuer" | string | `nil` |  |
| jellyfin.ingress.jellyfin-ing.enabled | bool | `true` |  |
| jellyfin.ingress.jellyfin-ing.expandObjectName | bool | `false` |  |
| jellyfin.ingress.jellyfin-ing.hosts[0].host | string | `"jellyfin.local"` |  |
| jellyfin.ingress.jellyfin-ing.hosts[0].paths[0].path | string | `"/"` |  |
| jellyfin.ingress.jellyfin-ing.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| jellyfin.ingress.jellyfin-ing.ingressClassName | string | `"nginx"` |  |
| jellyfin.ingress.jellyfin-ing.integrations.certManager.enabled | bool | `false` |  |
| jellyfin.ingress.jellyfin-ing.integrations.traefik.enabled | bool | `false` |  |
| jellyfin.ingress.jellyfin-ing.primary | bool | `true` |  |
| jellyfin.ingress.jellyfin-ing.required | bool | `true` |  |
| jellyfin.ingress.jellyfin-ing.tls[0].hosts[0] | string | `"jellyfin.local"` |  |
| jellyfin.ingress.jellyfin-ing.tls[0].secretName | string | `"jellyfin-tls"` |  |
| jellyfin.metrics.main.enabled | bool | `false` |  |
| jellyfin.persistence.config.accessModes | string | `"ReadWriteMany"` |  |
| jellyfin.persistence.config.enabled | bool | `true` |  |
| jellyfin.persistence.config.size | string | `"500Mi"` |  |
| jellyfin.persistence.config.storageClass | string | `nil` |  |
| jellyfin.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| jellyfin.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| jellyfin.persistence.config.targetSelector.main.main.mountPath | string | `"/config"` |  |
| jellyfin.persistence.config.type | string | `"pvc"` |  |
| jellyfin.persistence.media.enabled | bool | `true` |  |
| jellyfin.persistence.media.existingClaim | string | `"media-volume"` |  |
| jellyfin.persistence.media.targetSelector.main.main.mountPath | string | `"/mnt/media"` |  |
| jellyfin.persistence.media.type | string | `"pvc"` |  |
| jellyfin.persistence.transcode.enabled | bool | `false` |  |
| jellyfin.serviceProtocol | string | `"tcp"` |  |
| jellyseerr.fallbackDefaults.accessModes[0] | string | `"ReadWriteMany"` |  |
| jellyseerr.fallbackDefaults.persistenceType | string | `"pvc"` |  |
| jellyseerr.fallbackDefaults.pgVersion | int | `16` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.liveness.failureThreshold | int | `5` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.liveness.initialDelaySeconds | int | `10` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.liveness.periodSeconds | int | `10` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.liveness.successThreshold | int | `1` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.liveness.timeoutSeconds | int | `5` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.readiness.failureThreshold | int | `5` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.readiness.initialDelaySeconds | int | `10` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.readiness.periodSeconds | int | `10` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.readiness.successThreshold | int | `2` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.readiness.timeoutSeconds | int | `5` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.startup.failureThreshold | int | `60` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.startup.initialDelaySeconds | int | `10` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.startup.periodSeconds | int | `5` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.startup.successThreshold | int | `1` |  |
| jellyseerr.fallbackDefaults.probeTimeouts.startup.timeoutSeconds | int | `2` |  |
| jellyseerr.fallbackDefaults.probeType | string | `"http"` |  |
| jellyseerr.fallbackDefaults.pvcRetain | bool | `false` |  |
| jellyseerr.fallbackDefaults.pvcSize | string | `"100Gi"` |  |
| jellyseerr.fallbackDefaults.serviceProtocol | string | `"tcp"` |  |
| jellyseerr.fallbackDefaults.serviceType | string | `"ClusterIP"` |  |
| jellyseerr.fallbackDefaults.storageClass | string | `nil` |  |
| jellyseerr.fallbackDefaults.vctAccessModes[0] | string | `"ReadWriteMany"` |  |
| jellyseerr.fallbackDefaults.vctSize | string | `"100Gi"` |  |
| jellyseerr.ingress.jellyseerr-ing.annotations."cert-manager.io/cluster-issuer" | string | `nil` |  |
| jellyseerr.ingress.jellyseerr-ing.enabled | bool | `true` |  |
| jellyseerr.ingress.jellyseerr-ing.expandObjectName | bool | `false` |  |
| jellyseerr.ingress.jellyseerr-ing.hosts[0].host | string | `"jellyseerr.local"` |  |
| jellyseerr.ingress.jellyseerr-ing.hosts[0].paths[0].path | string | `"/"` |  |
| jellyseerr.ingress.jellyseerr-ing.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| jellyseerr.ingress.jellyseerr-ing.ingressClassName | string | `"nginx"` |  |
| jellyseerr.ingress.jellyseerr-ing.integrations.certManager.enabled | bool | `false` |  |
| jellyseerr.ingress.jellyseerr-ing.integrations.traefik.enabled | bool | `false` |  |
| jellyseerr.ingress.jellyseerr-ing.primary | bool | `true` |  |
| jellyseerr.ingress.jellyseerr-ing.required | bool | `true` |  |
| jellyseerr.ingress.jellyseerr-ing.tls[0].hosts[0] | string | `"jellyseerr.local"` |  |
| jellyseerr.ingress.jellyseerr-ing.tls[0].secretName | string | `"jellyseerr-tls"` |  |
| jellyseerr.metrics.main.enabled | bool | `false` |  |
| jellyseerr.persistence.config.accessModes | string | `"ReadWriteMany"` |  |
| jellyseerr.persistence.config.enabled | bool | `true` |  |
| jellyseerr.persistence.config.size | string | `"500Mi"` |  |
| jellyseerr.persistence.config.storageClass | string | `nil` |  |
| jellyseerr.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| jellyseerr.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| jellyseerr.persistence.config.targetSelector.main.main.mountPath | string | `"/app/config"` |  |
| jellyseerr.persistence.config.type | string | `"pvc"` |  |
| jellyseerr.persistence.media.enabled | bool | `true` |  |
| jellyseerr.persistence.media.existingClaim | string | `"media-volume"` |  |
| jellyseerr.persistence.media.targetSelector.main.main.mountPath | string | `"/mnt/media"` |  |
| jellyseerr.persistence.media.type | string | `"pvc"` |  |
| metrics.enabled | bool | `false` |  |
| notifications.telegram.bot_apitoken | string | `nil` | Insert your Telegram Bot API token |
| notifications.telegram.chat_id | string | `nil` | Insert the Telegram Chat id, check @get_id_bot for this |
| notifications.telegram.enabled | bool | `true` | Enable the Telegram notifications |
| prowlarr.ingress.prowlarr-ing.annotations."cert-manager.io/cluster-issuer" | string | `nil` |  |
| prowlarr.ingress.prowlarr-ing.enabled | bool | `true` |  |
| prowlarr.ingress.prowlarr-ing.expandObjectName | bool | `false` |  |
| prowlarr.ingress.prowlarr-ing.hosts[0].host | string | `"prowlarr.local"` |  |
| prowlarr.ingress.prowlarr-ing.hosts[0].paths[0].path | string | `"/"` |  |
| prowlarr.ingress.prowlarr-ing.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| prowlarr.ingress.prowlarr-ing.ingressClassName | string | `"nginx"` |  |
| prowlarr.ingress.prowlarr-ing.integrations.certManager.enabled | bool | `false` |  |
| prowlarr.ingress.prowlarr-ing.integrations.traefik.enabled | bool | `false` |  |
| prowlarr.ingress.prowlarr-ing.primary | bool | `true` |  |
| prowlarr.ingress.prowlarr-ing.required | bool | `true` |  |
| prowlarr.ingress.prowlarr-ing.tls[0].hosts[0] | string | `"prowlarr.local"` |  |
| prowlarr.ingress.prowlarr-ing.tls[0].secretName | string | `"prowlarr-tls"` |  |
| prowlarr.metrics.main.enabled | bool | `false` |  |
| prowlarr.persistence.config.accessModes | string | `"ReadWriteMany"` |  |
| prowlarr.persistence.config.enabled | bool | `true` |  |
| prowlarr.persistence.config.size | string | `"500Mi"` |  |
| prowlarr.persistence.config.storageClass | string | `nil` |  |
| prowlarr.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| prowlarr.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| prowlarr.persistence.config.targetSelector.main.main.mountPath | string | `"/config"` |  |
| prowlarr.persistence.config.type | string | `"pvc"` |  |
| prowlarr.workload.main.podSpec.containers.main.env.PROWLARR__API_KEY | string | `nil` |  |
| qbittorrent.ingress.qbittorrent-ing.annotations."cert-manager.io/cluster-issuer" | string | `nil` |  |
| qbittorrent.ingress.qbittorrent-ing.enabled | bool | `true` |  |
| qbittorrent.ingress.qbittorrent-ing.expandObjectName | bool | `false` |  |
| qbittorrent.ingress.qbittorrent-ing.hosts[0].host | string | `"torrent.local"` |  |
| qbittorrent.ingress.qbittorrent-ing.hosts[0].paths[0].path | string | `"/"` |  |
| qbittorrent.ingress.qbittorrent-ing.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| qbittorrent.ingress.qbittorrent-ing.ingressClassName | string | `"nginx"` |  |
| qbittorrent.ingress.qbittorrent-ing.integrations.certManager.enabled | bool | `false` |  |
| qbittorrent.ingress.qbittorrent-ing.integrations.traefik.enabled | bool | `false` |  |
| qbittorrent.ingress.qbittorrent-ing.primary | bool | `true` |  |
| qbittorrent.ingress.qbittorrent-ing.required | bool | `true` |  |
| qbittorrent.ingress.qbittorrent-ing.tls[0].hosts[0] | string | `"torrent.local"` |  |
| qbittorrent.ingress.qbittorrent-ing.tls[0].secretName | string | `"torrent-tls"` |  |
| qbittorrent.metrics.main.enabled | bool | `false` |  |
| qbittorrent.persistence.config.enabled | bool | `true` |  |
| qbittorrent.persistence.config.existingClaim | string | `"torrent-config"` |  |
| qbittorrent.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| qbittorrent.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| qbittorrent.persistence.config.targetSelector.main.main.mountPath | string | `"/config"` |  |
| qbittorrent.persistence.config.type | string | `"pvc"` |  |
| qbittorrent.persistence.downloads.enabled | bool | `true` |  |
| qbittorrent.persistence.downloads.existingClaim | string | `"downloads-volume"` |  |
| qbittorrent.persistence.downloads.targetSelector.main.main.mountPath | string | `"/downloads"` |  |
| qbittorrent.persistence.downloads.type | string | `"pvc"` |  |
| qbittorrent.workload.main.podSpec.containers.main.env.QBITTORRENT__USE_PROFILE | bool | `true` |  |
| radarr.ingress.radarr-ing.annotations."cert-manager.io/cluster-issuer" | string | `nil` |  |
| radarr.ingress.radarr-ing.enabled | bool | `true` |  |
| radarr.ingress.radarr-ing.expandObjectName | bool | `false` |  |
| radarr.ingress.radarr-ing.hosts[0].host | string | `"radarr.local"` |  |
| radarr.ingress.radarr-ing.hosts[0].paths[0].path | string | `"/"` |  |
| radarr.ingress.radarr-ing.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| radarr.ingress.radarr-ing.ingressClassName | string | `"nginx"` |  |
| radarr.ingress.radarr-ing.integrations.certManager.enabled | bool | `false` |  |
| radarr.ingress.radarr-ing.integrations.traefik.enabled | bool | `false` |  |
| radarr.ingress.radarr-ing.primary | bool | `true` |  |
| radarr.ingress.radarr-ing.required | bool | `true` |  |
| radarr.ingress.radarr-ing.tls[0].hosts[0] | string | `"radarr.local"` |  |
| radarr.ingress.radarr-ing.tls[0].secretName | string | `"radarr-tls"` |  |
| radarr.metrics.main.enabled | bool | `false` |  |
| radarr.persistence.config.accessModes | string | `"ReadWriteMany"` |  |
| radarr.persistence.config.enabled | bool | `true` |  |
| radarr.persistence.config.size | string | `"500Mi"` |  |
| radarr.persistence.config.storageClass | string | `nil` |  |
| radarr.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| radarr.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| radarr.persistence.config.targetSelector.main.main.mountPath | string | `"/config"` |  |
| radarr.persistence.config.type | string | `"pvc"` |  |
| radarr.persistence.downloads.enabled | bool | `true` |  |
| radarr.persistence.downloads.existingClaim | string | `"downloads-volume"` |  |
| radarr.persistence.downloads.targetSelector.main.main.mountPath | string | `"/mnt/downloads"` |  |
| radarr.persistence.downloads.type | string | `"pvc"` |  |
| radarr.persistence.media.enabled | bool | `true` |  |
| radarr.persistence.media.existingClaim | string | `"media-volume"` |  |
| radarr.persistence.media.targetSelector.main.main.mountPath | string | `"/mnt/media"` |  |
| radarr.persistence.media.type | string | `"pvc"` |  |
| radarr.workload.main.podSpec.containers.main.env.RADARR__API_KEY | string | `nil` |  |
| sonarr.ingress.sonarr-ing.annotations."cert-manager.io/cluster-issuer" | string | `nil` |  |
| sonarr.ingress.sonarr-ing.enabled | bool | `true` |  |
| sonarr.ingress.sonarr-ing.expandObjectName | bool | `false` |  |
| sonarr.ingress.sonarr-ing.hosts[0].host | string | `"sonarr.local"` |  |
| sonarr.ingress.sonarr-ing.hosts[0].paths[0].path | string | `"/"` |  |
| sonarr.ingress.sonarr-ing.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| sonarr.ingress.sonarr-ing.ingressClassName | string | `"nginx"` |  |
| sonarr.ingress.sonarr-ing.integrations.certManager.enabled | bool | `false` |  |
| sonarr.ingress.sonarr-ing.integrations.traefik.enabled | bool | `false` |  |
| sonarr.ingress.sonarr-ing.primary | bool | `true` |  |
| sonarr.ingress.sonarr-ing.required | bool | `true` |  |
| sonarr.ingress.sonarr-ing.tls[0].hosts[0] | string | `"sonarr.local"` |  |
| sonarr.ingress.sonarr-ing.tls[0].secretName | string | `"sonarr-tls"` |  |
| sonarr.metrics.main.enabled | bool | `false` |  |
| sonarr.persistence.config.accessModes | string | `"ReadWriteMany"` |  |
| sonarr.persistence.config.enabled | bool | `true` |  |
| sonarr.persistence.config.size | string | `"500Mi"` |  |
| sonarr.persistence.config.storageClass | string | `nil` |  |
| sonarr.persistence.config.targetSelector.exportarr.exportarr.mountPath | string | `"/config"` |  |
| sonarr.persistence.config.targetSelector.exportarr.exportarr.readOnly | bool | `true` |  |
| sonarr.persistence.config.targetSelector.main.main.mountPath | string | `"/config"` |  |
| sonarr.persistence.config.type | string | `"pvc"` |  |
| sonarr.persistence.downloads.enabled | bool | `true` |  |
| sonarr.persistence.downloads.existingClaim | string | `"downloads-volume"` |  |
| sonarr.persistence.downloads.targetSelector.main.main.mountPath | string | `"/mnt/downloads"` |  |
| sonarr.persistence.downloads.type | string | `"pvc"` |  |
| sonarr.persistence.media.enabled | bool | `true` |  |
| sonarr.persistence.media.existingClaim | string | `"media-volume"` |  |
| sonarr.persistence.media.targetSelector.main.main.mountPath | string | `"/mnt/media"` |  |
| sonarr.persistence.media.type | string | `"pvc"` |  |
| sonarr.workload.main.podSpec.containers.main.env.SONARR__API_KEY | string | `nil` |  |
| torrent.password | string | `nil` |  |
| torrent.username | string | `nil` | The following credentials are here just for tracking purposes and they are not used to configure qBitTorrent. The credentials are configured in config/qbittorrent/qBittorrent.conf |
| volumes.downloads.name | string | `"downloads-volume"` |  |
| volumes.downloads.size | string | `"100Gi"` |  |
| volumes.media.name | string | `"media-volume"` |  |
| volumes.media.size | string | `"250Gi"` |  |
| volumes.storageClass | string | `"longhorn"` |  |
| volumes.torrentConfig.name | string | `"torrent-config"` |  |
| volumes.torrentConfig.size | string | `"250Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.13.1](https://github.com/norwoodj/helm-docs/releases/v1.13.1)

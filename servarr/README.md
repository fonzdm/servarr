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

<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>dash.mail</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert Jellyfin login mail (will be used also for Jellyseerr integration)</td>
		</tr>
		<tr>
			<td>dash.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert Jellyfin password (will be used also for Jellyseerr)</td>
		</tr>
		<tr>
			<td>dash.username</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert the Jellyfin username (will be used also for Jellyseerr)</td>
		</tr>
		<tr>
			<td>flaresolverr.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.accessModes</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteMany"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.size</td>
			<td>string</td>
			<td><pre lang="json">
"500Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>flaresolverr.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.apikey</td>
			<td>string</td>
			<td><pre lang="">
No default value is configured for security reasons, it is mandatory to set this parameter
</pre>
</td>
			<td>Insert your API key here, e.g.: &apikey 123abc..</td>
		</tr>
		<tr>
			<td>global.certManagerClusterIssuer</td>
			<td>string</td>
			<td><pre lang="">
No default value, leave empty if not required
</pre>
</td>
			<td>Insert your cert manager cluster issuer, e.g.: letsencrypt-cloudflare</td>
		</tr>
		<tr>
			<td>global.storageClassName</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td>Insert your storage class here, e.g.: &storageClassName longhorn</td>
		</tr>
		<tr>
			<td>indexers</td>
			<td>list</td>
			<td><pre lang="">
The body of the 1337x index is provided as default
</pre>
</td>
			<td>The indexers list. Each element of the list is the yaml-formatted boody of the [Prowlarr API request](https://prowlarr.com/docs/api/#/Indexer/post_api_v1_indexer) to add that index.</td>
		</tr>
		<tr>
			<td>initJellyseerr</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Set initJellyseerr to false if Jellyseerr setup should not be performed automatically</td>
		</tr>
		<tr>
			<td>issuer</td>
			<td>object</td>
			<td><pre lang="json">
{
  "cloudFlareKey": null,
  "email": null,
  "ingressClassName": "nginx",
  "secretName": "letsencrypt-prod",
  "server": "https://acme-v02.api.letsencrypt.org/directory"
}
</pre>
</td>
			<td>For tracking purpose, not used - replaced with pre-existing cluster issuer</td>
		</tr>
		<tr>
			<td>issuer.cloudFlareKey</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert your CloudFlare key</td>
		</tr>
		<tr>
			<td>issuer.email</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert your email address</td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.expandObjectName</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.hosts[0].host</td>
			<td>string</td>
			<td><pre lang="json">
"jellyfin.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.hosts[0].paths[0].path</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.hosts[0].paths[0].pathType</td>
			<td>string</td>
			<td><pre lang="json">
"Prefix"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
"nginx"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.integrations.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.integrations.traefik.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.primary</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.required</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.tls[0].hosts[0]</td>
			<td>string</td>
			<td><pre lang="json">
"jellyfin.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.ingress.jellyfin-ing.tls[0].secretName</td>
			<td>string</td>
			<td><pre lang="json">
"jellyfin-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.accessModes</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteMany"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.size</td>
			<td>string</td>
			<td><pre lang="json">
"500Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.media.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.media.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"media-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.media.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/mnt/media"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.media.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.persistence.transcode.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyfin.serviceProtocol</td>
			<td>string</td>
			<td><pre lang="json">
"tcp"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.expandObjectName</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.hosts[0].host</td>
			<td>string</td>
			<td><pre lang="json">
"jellyseerr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.hosts[0].paths[0].path</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.hosts[0].paths[0].pathType</td>
			<td>string</td>
			<td><pre lang="json">
"Prefix"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
"nginx"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.integrations.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.integrations.traefik.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.primary</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.required</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.tls[0].hosts[0]</td>
			<td>string</td>
			<td><pre lang="json">
"jellyseerr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.ingress.jellyseerr-ing.tls[0].secretName</td>
			<td>string</td>
			<td><pre lang="json">
"jellyseerr-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.accessModes</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteMany"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.size</td>
			<td>string</td>
			<td><pre lang="json">
"500Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/app/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.media.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.media.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"media-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.media.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/mnt/media"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>jellyseerr.persistence.media.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>metrics.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Anchor to set wether to deploy the export sidecar pods or not. Requires the Prometheus stack</td>
		</tr>
		<tr>
			<td>notifications.telegram.bot_apitoken</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert your Telegram Bot API token</td>
		</tr>
		<tr>
			<td>notifications.telegram.chat_id</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>Insert the Telegram Chat id, check @get_id_bot for this</td>
		</tr>
		<tr>
			<td>notifications.telegram.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable the Telegram notifications</td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.expandObjectName</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.hosts[0].host</td>
			<td>string</td>
			<td><pre lang="json">
"prowlarr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.hosts[0].paths[0].path</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.hosts[0].paths[0].pathType</td>
			<td>string</td>
			<td><pre lang="json">
"Prefix"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
"nginx"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.integrations.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.integrations.traefik.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.primary</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.required</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.tls[0].hosts[0]</td>
			<td>string</td>
			<td><pre lang="json">
"prowlarr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.ingress.prowlarr-ing.tls[0].secretName</td>
			<td>string</td>
			<td><pre lang="json">
"prowlarr-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.accessModes</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteMany"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.size</td>
			<td>string</td>
			<td><pre lang="json">
"500Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>prowlarr.workload.main.podSpec.containers.main.env.PROWLARR__API_KEY</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.expandObjectName</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.hosts[0].host</td>
			<td>string</td>
			<td><pre lang="json">
"torrent.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.hosts[0].paths[0].path</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.hosts[0].paths[0].pathType</td>
			<td>string</td>
			<td><pre lang="json">
"Prefix"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
"nginx"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.integrations.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.integrations.traefik.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.primary</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.required</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.tls[0].hosts[0]</td>
			<td>string</td>
			<td><pre lang="json">
"torrent.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.ingress.qbittorrent-ing.tls[0].secretName</td>
			<td>string</td>
			<td><pre lang="json">
"torrent-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.config.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"torrent-config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.downloads.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.downloads.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"downloads-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.downloads.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/downloads"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.persistence.downloads.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>qbittorrent.workload.main.podSpec.containers.main.env.QBITTORRENT__USE_PROFILE</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.expandObjectName</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.hosts[0].host</td>
			<td>string</td>
			<td><pre lang="json">
"radarr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.hosts[0].paths[0].path</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.hosts[0].paths[0].pathType</td>
			<td>string</td>
			<td><pre lang="json">
"Prefix"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
"nginx"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.integrations.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.integrations.traefik.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.primary</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.required</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.tls[0].hosts[0]</td>
			<td>string</td>
			<td><pre lang="json">
"radarr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.ingress.radarr-ing.tls[0].secretName</td>
			<td>string</td>
			<td><pre lang="json">
"radarr-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.accessModes</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteMany"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.size</td>
			<td>string</td>
			<td><pre lang="json">
"500Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.downloads.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.downloads.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"downloads-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.downloads.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/mnt/downloads"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.downloads.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.media.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.media.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"media-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.media.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/mnt/media"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.persistence.media.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>radarr.workload.main.podSpec.containers.main.env.RADARR__API_KEY</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.expandObjectName</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.hosts[0].host</td>
			<td>string</td>
			<td><pre lang="json">
"sonarr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.hosts[0].paths[0].path</td>
			<td>string</td>
			<td><pre lang="json">
"/"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.hosts[0].paths[0].pathType</td>
			<td>string</td>
			<td><pre lang="json">
"Prefix"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
"nginx"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.integrations.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.integrations.traefik.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.primary</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.required</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.tls[0].hosts[0]</td>
			<td>string</td>
			<td><pre lang="json">
"sonarr.local"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.ingress.sonarr-ing.tls[0].secretName</td>
			<td>string</td>
			<td><pre lang="json">
"sonarr-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.metrics.main.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.accessModes</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteMany"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.size</td>
			<td>string</td>
			<td><pre lang="json">
"500Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"network-block"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.targetSelector.exportarr.exportarr.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.targetSelector.exportarr.exportarr.readOnly</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.config.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.downloads.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.downloads.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"downloads-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.downloads.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/mnt/downloads"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.downloads.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.media.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.media.existingClaim</td>
			<td>string</td>
			<td><pre lang="json">
"media-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.media.targetSelector.main.main.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/mnt/media"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.persistence.media.type</td>
			<td>string</td>
			<td><pre lang="json">
"pvc"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>sonarr.workload.main.podSpec.containers.main.env.SONARR__API_KEY</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>torrent</td>
			<td>object</td>
			<td><pre lang="json">
{
  "password": null,
  "username": null
}
</pre>
</td>
			<td>The following credentials are here just for tracking purposes and they are not used to configure qBitTorrent. The credentials are configured in config/qbittorrent/qBittorrent.conf</td>
		</tr>
		<tr>
			<td>torrent.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>password of the qBitTorrent admin user</td>
		</tr>
		<tr>
			<td>torrent.username</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td>username of the qBitTorrent admin user</td>
		</tr>
		<tr>
			<td>volumes.downloads.name</td>
			<td>string</td>
			<td><pre lang="json">
"downloads-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes.downloads.size</td>
			<td>string</td>
			<td><pre lang="json">
"100Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes.media.name</td>
			<td>string</td>
			<td><pre lang="json">
"media-volume"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes.media.size</td>
			<td>string</td>
			<td><pre lang="json">
"250Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
"longhorn"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes.torrentConfig.name</td>
			<td>string</td>
			<td><pre lang="json">
"torrent-config"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>volumes.torrentConfig.size</td>
			<td>string</td>
			<td><pre lang="json">
"250Mi"
</pre>
</td>
			<td></td>
		</tr>
	</tbody>
</table>




----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.13.1](https://github.com/norwoodj/helm-docs/releases/v1.13.1)

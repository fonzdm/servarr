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

<h3>jellyfin</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>dash</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>Jellyfin User configuration section </td>
		</tr>
		<tr>
			<td>dash.mail</td>
			<td>string</td>
			<td><pre lang="">
No default value
</pre>
</td>
			<td>Insert Jellyfin login mail (will be used also for Jellyseerr integration)</td>
		</tr>
		<tr>
			<td>dash.password</td>
			<td>string</td>
			<td><pre lang="">
No default value
</pre>
</td>
			<td>Insert Jellyfin password (will be used also for Jellyseerr)</td>
		</tr>
		<tr>
			<td>dash.username</td>
			<td>string</td>
			<td><pre lang="">
No default value
</pre>
</td>
			<td>Insert the Jellyfin username (will be used also for Jellyseerr)</td>
		</tr>
		<tr>
			<td>jellyfin</td>
			<td>object</td>
			<td><pre lang="json">
{
  "ingress": {
    "jellyfin-ing": {
      "annotations": {
        "cert-manager.io/cluster-issuer": null
      },
      "enabled": true,
      "expandObjectName": false,
      "hosts": [
        {
          "host": "jellyfin.local",
          "paths": [
            {
              "path": "/",
              "pathType": "Prefix"
            }
          ]
        }
      ],
      "ingressClassName": "nginx",
      "integrations": {
        "certManager": {
          "enabled": false
        },
        "traefik": {
          "enabled": false
        }
      },
      "primary": true,
      "required": true,
      "tls": [
        {
          "hosts": [
            "jellyfin.local"
          ],
          "secretName": "jellyfin-tls"
        }
      ]
    }
  },
  "metrics": {
    "main": {
      "enabled": false
    }
  },
  "persistence": {
    "config": {
      "accessModes": "ReadWriteMany",
      "enabled": true,
      "size": "500Mi",
      "storageClass": "network-block",
      "targetSelector": {
        "exportarr": {
          "exportarr": {
            "mountPath": "/config",
            "readOnly": true
          }
        },
        "main": {
          "main": {
            "mountPath": "/config"
          }
        }
      },
      "type": "pvc"
    },
    "media": {
      "enabled": true,
      "existingClaim": "media-volume",
      "targetSelector": {
        "main": {
          "main": {
            "mountPath": "/mnt/media"
          }
        }
      },
      "type": "pvc"
    },
    "transcode": {
      "enabled": false
    }
  },
  "serviceProtocol": "tcp"
}
</pre>
</td>
			<td>Jellyfin configuration section</td>
		</tr>
	</tbody>
</table>
<h3>prowlarr</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>flaresolverr</td>
			<td>object</td>
			<td><pre lang="json">
{
  "metrics": {
    "main": {
      "enabled": false
    }
  },
  "persistence": {
    "config": {
      "accessModes": "ReadWriteMany",
      "enabled": true,
      "size": "500Mi",
      "storageClass": "network-block",
      "targetSelector": {
        "exportarr": {
          "exportarr": {
            "mountPath": "/config",
            "readOnly": true
          }
        },
        "main": {
          "main": {
            "mountPath": "/config"
          }
        }
      },
      "type": "pvc"
    }
  }
}
</pre>
</td>
			<td>Flaresolverr configuration section</td>
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
			<td>prowlarr</td>
			<td>object</td>
			<td><pre lang="json">
{
  "ingress": {
    "prowlarr-ing": {
      "annotations": {
        "cert-manager.io/cluster-issuer": null
      },
      "enabled": true,
      "expandObjectName": false,
      "hosts": [
        {
          "host": "prowlarr.local",
          "paths": [
            {
              "path": "/",
              "pathType": "Prefix"
            }
          ]
        }
      ],
      "ingressClassName": "nginx",
      "integrations": {
        "certManager": {
          "enabled": false
        },
        "traefik": {
          "enabled": false
        }
      },
      "primary": true,
      "required": true,
      "tls": [
        {
          "hosts": [
            "prowlarr.local"
          ],
          "secretName": "prowlarr-tls"
        }
      ]
    }
  },
  "metrics": {
    "main": {
      "enabled": false
    }
  },
  "persistence": {
    "config": {
      "accessModes": "ReadWriteMany",
      "enabled": true,
      "size": "500Mi",
      "storageClass": "network-block",
      "targetSelector": {
        "exportarr": {
          "exportarr": {
            "mountPath": "/config",
            "readOnly": true
          }
        },
        "main": {
          "main": {
            "mountPath": "/config"
          }
        }
      },
      "type": "pvc"
    }
  },
  "workload": {
    "main": {
      "podSpec": {
        "containers": {
          "main": {
            "env": {
              "PROWLARR__API_KEY": null
            }
          }
        }
      }
    }
  }
}
</pre>
</td>
			<td>Prowlarr configuration section</td>
		</tr>
	</tbody>
</table>
<h3>global</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
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
	</tbody>
</table>
<h3>Required</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
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
			<td>metrics.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Anchor to set wether to deploy the export sidecar pods or not. Requires the Prometheus stack</td>
		</tr>
		<tr>
			<td>volumes</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>Volumes configuration section</td>
		</tr>
		<tr>
			<td>volumes.downloads</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>configuration of the volume used for torrent downloads</td>
		</tr>
		<tr>
			<td>volumes.downloads.name</td>
			<td>string</td>
			<td><pre lang="json">
"downloads-volume"
</pre>
</td>
			<td>Name of the download pvc. Leave the anchor declaration, as it will be used in the service configuration</td>
		</tr>
		<tr>
			<td>volumes.downloads.size</td>
			<td>string</td>
			<td><pre lang="json">
"100Gi"
</pre>
</td>
			<td>Size of the downloads volume, in Kubernets format</td>
		</tr>
		<tr>
			<td>volumes.media</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>configuration of the volume used for media storage (i.e.: where movies and tv shows file will be permanently stored)</td>
		</tr>
		<tr>
			<td>volumes.media.name</td>
			<td>string</td>
			<td><pre lang="json">
"media-volume"
</pre>
</td>
			<td>Name of the media pvc. Leave the anchor declaration, as it will be used in the service configuration</td>
		</tr>
		<tr>
			<td>volumes.media.size</td>
			<td>string</td>
			<td><pre lang="json">
"250Gi"
</pre>
</td>
			<td>Size of the media volume, in Kubernets format</td>
		</tr>
		<tr>
			<td>volumes.storageClass</td>
			<td>string</td>
			<td><pre lang="">
equal to global.storageClassName value, do not edit
</pre>
</td>
			<td>Storage class of the PVCs. Refer to global.storageClassName, as this is automatically set using the anchor</td>
		</tr>
		<tr>
			<td>volumes.torrentConfig</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>configuration of the volume used for qBitTorrent internal configuration</td>
		</tr>
		<tr>
			<td>volumes.torrentConfig.name</td>
			<td>string</td>
			<td><pre lang="json">
"torrent-config"
</pre>
</td>
			<td>Name of the torrent configuration pvc. Leave the anchor declaration, as it will be used in the service configuration</td>
		</tr>
		<tr>
			<td>volumes.torrentConfig.size</td>
			<td>string</td>
			<td><pre lang="json">
"250Mi"
</pre>
</td>
			<td>Size of the torrent configuration volume, in Kubernets format</td>
		</tr>
	</tbody>
</table>
<h3>Optional</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>issuer</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
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
	</tbody>
</table>
<h3>jellyseerr</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>jellyseerr</td>
			<td>object</td>
			<td><pre lang="json">
{
  "ingress": {
    "jellyseerr-ing": {
      "annotations": {
        "cert-manager.io/cluster-issuer": null
      },
      "enabled": true,
      "expandObjectName": false,
      "hosts": [
        {
          "host": "jellyseerr.local",
          "paths": [
            {
              "path": "/",
              "pathType": "Prefix"
            }
          ]
        }
      ],
      "ingressClassName": "nginx",
      "integrations": {
        "certManager": {
          "enabled": false
        },
        "traefik": {
          "enabled": false
        }
      },
      "primary": true,
      "required": true,
      "tls": [
        {
          "hosts": [
            "jellyseerr.local"
          ],
          "secretName": "jellyseerr-tls"
        }
      ]
    }
  },
  "metrics": {
    "main": {
      "enabled": false
    }
  },
  "persistence": {
    "config": {
      "accessModes": "ReadWriteMany",
      "enabled": true,
      "size": "500Mi",
      "storageClass": "network-block",
      "targetSelector": {
        "exportarr": {
          "exportarr": {
            "mountPath": "/config",
            "readOnly": true
          }
        },
        "main": {
          "main": {
            "mountPath": "/app/config"
          }
        }
      },
      "type": "pvc"
    },
    "media": {
      "enabled": true,
      "existingClaim": "media-volume",
      "targetSelector": {
        "main": {
          "main": {
            "mountPath": "/mnt/media"
          }
        }
      },
      "type": "pvc"
    }
  }
}
</pre>
</td>
			<td>Jallyseerr configuration section</td>
		</tr>
		<tr>
			<td>notifications</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>Sections wherer Jellyseerr notifications are configured. Only telegram notification is supported for now</td>
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
	</tbody>
</table>
<h3>torrent</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>qbittorrent</td>
			<td>object</td>
			<td><pre lang="json">
{
  "ingress": {
    "qbittorrent-ing": {
      "annotations": {
        "cert-manager.io/cluster-issuer": null
      },
      "enabled": true,
      "expandObjectName": false,
      "hosts": [
        {
          "host": "torrent.local",
          "paths": [
            {
              "path": "/",
              "pathType": "Prefix"
            }
          ]
        }
      ],
      "ingressClassName": "nginx",
      "integrations": {
        "certManager": {
          "enabled": false
        },
        "traefik": {
          "enabled": false
        }
      },
      "primary": true,
      "required": true,
      "tls": [
        {
          "hosts": [
            "torrent.local"
          ],
          "secretName": "torrent-tls"
        }
      ]
    }
  },
  "metrics": {
    "main": {
      "enabled": false
    }
  },
  "persistence": {
    "config": {
      "enabled": true,
      "existingClaim": "torrent-config",
      "targetSelector": {
        "exportarr": {
          "exportarr": {
            "mountPath": "/config",
            "readOnly": true
          }
        },
        "main": {
          "main": {
            "mountPath": "/config"
          }
        }
      },
      "type": "pvc"
    },
    "downloads": {
      "enabled": true,
      "existingClaim": "downloads-volume",
      "targetSelector": {
        "main": {
          "main": {
            "mountPath": "/downloads"
          }
        }
      },
      "type": "pvc"
    }
  },
  "workload": {
    "main": {
      "podSpec": {
        "containers": {
          "main": {
            "env": {
              "QBITTORRENT__USE_PROFILE": true
            }
          }
        }
      }
    }
  }
}
</pre>
</td>
			<td>qBitTorrent configuration section</td>
		</tr>
		<tr>
			<td>torrent</td>
			<td>object</td>
			<td><pre lang="">
See the sub fields
</pre>
</td>
			<td>The following credentials are here just for tracking purposes and they are not used to configure qBitTorrent. The credentials are configured in config/qbittorrent/qBittorrent.conf</td>
		</tr>
		<tr>
			<td>torrent.password</td>
			<td>string</td>
			<td><pre lang="">
No default value
</pre>
</td>
			<td>password of the qBitTorrent admin user</td>
		</tr>
		<tr>
			<td>torrent.username</td>
			<td>string</td>
			<td><pre lang="">
No default value
</pre>
</td>
			<td>username of the qBitTorrent admin user</td>
		</tr>
	</tbody>
</table>
<h3>radarr</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>radarr</td>
			<td>object</td>
			<td><pre lang="json">
{
  "persistence": {
    "config": {
      "accessModes": "ReadWriteMany",
      "enabled": true,
      "size": "500Mi",
      "storageClass": "network-block",
      "targetSelector": {
        "exportarr": {
          "exportarr": {
            "mountPath": "/config",
            "readOnly": true
          }
        },
        "main": {
          "main": {
            "mountPath": "/config"
          }
        }
      },
      "type": "pvc"
    },
    "downloads": {
      "enabled": true,
      "existingClaim": "downloads-volume",
      "targetSelector": {
        "main": {
          "main": {
            "mountPath": "/mnt/downloads"
          }
        }
      },
      "type": "pvc"
    },
    "media": {
      "enabled": true,
      "existingClaim": "media-volume",
      "targetSelector": {
        "main": {
          "main": {
            "mountPath": "/mnt/media"
          }
        }
      },
      "type": "pvc"
    }
  }
}
</pre>
</td>
			<td>Radarr configuration section</td>
		</tr>
	</tbody>
</table>
<h3>sonarr</h3>
<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>sonarr</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Sonarr configuration section</td>
		</tr>
	</tbody>
</table>




----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.13.1](https://github.com/norwoodj/helm-docs/releases/v1.13.1)

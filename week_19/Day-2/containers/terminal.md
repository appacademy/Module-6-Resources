# DOCKER CONTAINER CLI

cb02c38efa91   bradsimpson213/tuesday_taco_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago        0.0.0.0:3000->3000/tcp   zen_curie
dbada9136a38   postgres                            "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                   postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container run -it alpine ash
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd lib/
/lib # \ls
apk                     libc.musl-aarch64.so.1  libz.so.1.2.13
firmware                libcrypto.so.3          mdev
ld-musl-aarch64.so.1    libssl.so.3             modules-load.d
libapk.so.2.14.0        libz.so.1               sysctl.d
/lib # cd ..
/ # cd bin/
/bin # \ls
arch           dmesg          gzip           lzop           ping6          sleep
ash            dnsdomainname  hostname       makemime       pipe_progress  stat
base64         dumpkmap       ionice         mkdir          printenv       stty
bbconfig       echo           iostat         mknod          ps             su
busybox        ed             ipcalc         mktemp         pwd            sync
cat            egrep          kbd_mode       more           reformime      tar
chattr         false          kill           mount          rev            touch
chgrp          fatattr        link           mountpoint     rm             true
chmod          fdflush        linux32        mpstat         rmdir          umount
chown          fgrep          linux64        mv             run-parts      uname
cp             fsync          ln             netstat        sed            usleep
date           getopt         login          nice           setpriv        watch
dd             grep           ls             pidof          setserial      zcat
df             gunzip         lsattr         ping           sh
/bin # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a             
CONTAINER ID   IMAGE                               COMMAND                  CREATED              STATUS                      PORTS                    NAMES
4c5b43de15d7   alpine                              "ash"                    About a minute ago   Exited (0) 3 seconds ago                             xenodochial_hopper
9e547603c005   nginx                               "/docker-entrypoint.…"   6 minutes ago        Exited (0) 4 minutes ago                             focused_chaum
6c2fd75d504a   nginx                               "/docker-entrypoint.…"   9 minutes ago        Exited (0) 4 minutes ago                             vigorous_gagarin
7faa411b344a   nginx                               "/docker-entrypoint.…"   14 minutes ago       Exited (0) 12 minutes ago                            my_container
c86868ab33ca   hello-world                         "/hello"                 22 minutes ago       Exited (0) 22 minutes ago                            goofy_wescoff
04a56205fd96   hello-world                         "/hello"                 20 hours ago         Exited (0) 20 hours ago                              magical_zhukovsky
7f1e95d39b58   hello-world                         "/hello"                 20 hours ago         Exited (0) 20 hours ago                              gallant_jang
cb02c38efa91   bradsimpson213/tuesday_taco_react   "docker-entrypoint.s…"   3 weeks ago          Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   zen_curie
dbada9136a38   postgres                            "docker-entrypoint.s…"   3 weeks ago          Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -p 8080:80 -d nginx
7e1f906b8157c9f19694b03bb8c0e604868d73fec4098f0f8932abbf76092dfa
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
7e1f906b8157   nginx     "/docker-entrypoint.…"   7 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container run --name test -it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container ls                           
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
7e1f906b8157   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS                      PORTS                    NAMES
84c19e5bb66a   alpine                              "sh"                     2 minutes ago    Exited (0) 2 minutes ago                             test
7e1f906b8157   nginx                               "/docker-entrypoint.…"   3 minutes ago    Up 3 minutes                0.0.0.0:8080->80/tcp     dazzling_napier
4c5b43de15d7   alpine                              "ash"                    7 minutes ago    Exited (0) 6 minutes ago                             xenodochial_hopper
9e547603c005   nginx                               "/docker-entrypoint.…"   12 minutes ago   Exited (0) 10 minutes ago                            focused_chaum
6c2fd75d504a   nginx                               "/docker-entrypoint.…"   15 minutes ago   Exited (0) 10 minutes ago                            vigorous_gagarin
7faa411b344a   nginx                               "/docker-entrypoint.…"   20 minutes ago   Exited (0) 18 minutes ago                            my_container
c86868ab33ca   hello-world                         "/hello"                 28 minutes ago   Exited (0) 28 minutes ago                            goofy_wescoff
04a56205fd96   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              magical_zhukovsky
7f1e95d39b58   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              gallant_jang
cb02c38efa91   bradsimpson213/tuesday_taco_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   zen_curie
dbada9136a38   postgres                            "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c86868ab33ca 
[
    {
        "Id": "c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9",
        "Created": "2023-12-12T16:06:23.801356962Z",
        "Path": "/hello",
        "Args": [],
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-12T16:06:23.998895212Z",
            "FinishedAt": "2023-12-12T16:06:23.998456004Z"
        },
        "Image": "sha256:b038788ddb222cb7d6025b411759e4f5abe9910486c8f98534ead97befd77dd7",
        "ResolvConfPath": "/var/lib/docker/containers/c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9/hostname",
        "HostsPath": "/var/lib/docker/containers/c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9/hosts",
        "LogPath": "/var/lib/docker/containers/c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9/c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9-json.log",
        "Name": "/goofy_wescoff",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                55,
                89
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/105853ca0618776c224a74d28ba9fb43ee3e4c2a14add8a398060f04a40dccef-init/diff:/var/lib/docker/overlay2/a1ea418060fc3bd2ad5b3c7337ffe56403b1161ac77de78d59f13330dd645d4f/diff",
                "MergedDir": "/var/lib/docker/overlay2/105853ca0618776c224a74d28ba9fb43ee3e4c2a14add8a398060f04a40dccef/merged",
                "UpperDir": "/var/lib/docker/overlay2/105853ca0618776c224a74d28ba9fb43ee3e4c2a14add8a398060f04a40dccef/diff",
                "WorkDir": "/var/lib/docker/overlay2/105853ca0618776c224a74d28ba9fb43ee3e4c2a14add8a398060f04a40dccef/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "c86868ab33ca",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/hello"
            ],
            "Image": "hello-world",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "f0166910648965e282e9846330ceee86cf894bbbf5e7caf0b6aec34045a26d5b",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/f01669106489",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "1ad5daf32a128aaae87a0bb86874cbaa7b06195bb6499ce85434fc95e94c4b16",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a                
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS                      PORTS                    NAMES
84c19e5bb66a   alpine                              "sh"                     4 minutes ago    Exited (0) 4 minutes ago                             test
7e1f906b8157   nginx                               "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:8080->80/tcp     dazzling_napier
4c5b43de15d7   alpine                              "ash"                    9 minutes ago    Exited (0) 8 minutes ago                             xenodochial_hopper
9e547603c005   nginx                               "/docker-entrypoint.…"   14 minutes ago   Exited (0) 13 minutes ago                            focused_chaum
6c2fd75d504a   nginx                               "/docker-entrypoint.…"   18 minutes ago   Exited (0) 13 minutes ago                            vigorous_gagarin
7faa411b344a   nginx                               "/docker-entrypoint.…"   22 minutes ago   Exited (0) 20 minutes ago                            my_container
c86868ab33ca   hello-world                         "/hello"                 31 minutes ago   Exited (0) 31 minutes ago                            goofy_wescoff
04a56205fd96   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              magical_zhukovsky
7f1e95d39b58   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              gallant_jang
cb02c38efa91   bradsimpson213/tuesday_taco_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   zen_curie
dbada9136a38   postgres                            "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container inspect 7faa411b344a
[
    {
        "Id": "7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6",
        "Created": "2023-12-12T16:14:50.020769375Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "exited",
            "Running": false,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 0,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-12T16:14:52.400484333Z",
            "FinishedAt": "2023-12-12T16:16:30.179707504Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6/hostname",
        "HostsPath": "/var/lib/docker/containers/7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6/hosts",
        "LogPath": "/var/lib/docker/containers/7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6/7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6-json.log",
        "Name": "/my_container",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "8000"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                55,
                89
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0853d45381ecd6194d475d8d7b7432a28a5ff2094c9d256470ed5696c83d2c2b-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/0853d45381ecd6194d475d8d7b7432a28a5ff2094c9d256470ed5696c83d2c2b/merged",
                "UpperDir": "/var/lib/docker/overlay2/0853d45381ecd6194d475d8d7b7432a28a5ff2094c9d256470ed5696c83d2c2b/diff",
                "WorkDir": "/var/lib/docker/overlay2/0853d45381ecd6194d475d8d7b7432a28a5ff2094c9d256470ed5696c83d2c2b/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "7faa411b344a",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.1",
                "NJS_VERSION=0.7.12",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers \u003cdocker-maint@nginx.com\u003e"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "3c17898713c4eb3bf4bdf1e445640e26a3b6ec9a610287645c8e9803fad73824",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/3c17898713c4",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "deb45aeeea980e379012d5cd8ca5e38da184601b27c461cd2679e907a6304248",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@Brads-MacBook-Air ~ % docker image inspect nginx
[
    {
        "Id": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:593dac25b7733ffb7afe1a72649a43e574778bf025ad60514ef40f6b5d606247"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-06-14T03:47:04.608168367Z",
        "Container": "3d692c6bf8c27f8927a126f64dda01db9513712ef8b2f6e606dfb22e2bfba211",
        "ContainerConfig": {
            "Hostname": "3d692c6bf8c2",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.1",
                "NJS_VERSION=0.7.12",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:5b0110e5e828098bdd36b1f65802bd907a1bc04091213fb8b78645cc69f72ead",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "DockerVersion": "20.10.23",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.1",
                "NJS_VERSION=0.7.12",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:5b0110e5e828098bdd36b1f65802bd907a1bc04091213fb8b78645cc69f72ead",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "Architecture": "arm64",
        "Variant": "v8",
        "Os": "linux",
        "Size": 192298817,
        "VirtualSize": 192298817,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/merged",
                "UpperDir": "/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff",
                "WorkDir": "/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:28729e4ae0abb44b42af819e47380bb8cc20e05d94c9f241f52122a1144a4401",
                "sha256:9778a1e5c8724bdaa5f17fb130a6fd055ca7fce663f8ebeddf755b2025c0bb42",
                "sha256:a02619bcaf18f97f71e9b3cb04e78a76be5b67d00510b3dab523cd1f5f6f6245",
                "sha256:ef823dda6d4f6348b36eb5a0cecfbb9dc52a7d05dc9c52116bee854cdfc6be88",
                "sha256:e97ed8d349b812fc7726ecb304d237653bf8e495f7d2e2d3031d71f7a64e74d7",
                "sha256:79b41f6a1b71bf2da50e101be580edd14fc614dcb78d3636a6bfbfd6602318a4",
                "sha256:0f024290dd085b43aa4e75ee57598636d88ff4d02920bffc05b528051495d0be"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
7e1f906b8157   nginx     "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container stop 7e1f906b8157
7e1f906b8157
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS                      PORTS                    NAMES
84c19e5bb66a   alpine                              "sh"                     7 minutes ago    Exited (0) 7 minutes ago                             test
7e1f906b8157   nginx                               "/docker-entrypoint.…"   8 minutes ago    Exited (0) 10 seconds ago                            dazzling_napier
4c5b43de15d7   alpine                              "ash"                    12 minutes ago   Exited (0) 11 minutes ago                            xenodochial_hopper
9e547603c005   nginx                               "/docker-entrypoint.…"   17 minutes ago   Exited (0) 15 minutes ago                            focused_chaum
6c2fd75d504a   nginx                               "/docker-entrypoint.…"   21 minutes ago   Exited (0) 15 minutes ago                            vigorous_gagarin
7faa411b344a   nginx                               "/docker-entrypoint.…"   25 minutes ago   Exited (0) 23 minutes ago                            my_container
c86868ab33ca   hello-world                         "/hello"                 33 minutes ago   Exited (0) 33 minutes ago                            goofy_wescoff
04a56205fd96   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              magical_zhukovsky
7f1e95d39b58   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              gallant_jang
cb02c38efa91   bradsimpson213/tuesday_taco_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   zen_curie
dbada9136a38   postgres                            "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container start dazzling_napier
dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
7e1f906b8157   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 8 seconds   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container rm 84c19e5bb66a magical_zhukovsky
84c19e5bb66a
magical_zhukovsky
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a                            
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS                      PORTS                    NAMES
7e1f906b8157   nginx                               "/docker-entrypoint.…"   11 minutes ago   Up About a minute           0.0.0.0:8080->80/tcp     dazzling_napier
4c5b43de15d7   alpine                              "ash"                    15 minutes ago   Exited (0) 13 minutes ago                            xenodochial_hopper
9e547603c005   nginx                               "/docker-entrypoint.…"   20 minutes ago   Exited (0) 18 minutes ago                            focused_chaum
6c2fd75d504a   nginx                               "/docker-entrypoint.…"   23 minutes ago   Exited (0) 18 minutes ago                            vigorous_gagarin
7faa411b344a   nginx                               "/docker-entrypoint.…"   27 minutes ago   Exited (0) 26 minutes ago                            my_container
c86868ab33ca   hello-world                         "/hello"                 36 minutes ago   Exited (0) 36 minutes ago                            goofy_wescoff
7f1e95d39b58   hello-world                         "/hello"                 20 hours ago     Exited (0) 20 hours ago                              gallant_jang
cb02c38efa91   bradsimpson213/tuesday_taco_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   zen_curie
dbada9136a38   postgres                            "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
4c5b43de15d78d08c36488d70646a2bfa3fbf7d69686249ad16af512ca7fdd00
9e547603c005eebace4ad64075128110fcfb063fc6a4b025b68a2a341bccdec0
6c2fd75d504a37dedc6df6eefb44b9f02fb971f5af62fed482f776fe6559bf44
7faa411b344a1609b3d8af429fca8cf1acbc5bd522f5190e23f1e1fab0fda3f6
c86868ab33caddb7bd32a6a62d7c11c767426909f721a862903e149c79a653c9
7f1e95d39b58a373a9a5d68dd4c949b656534591bf5013b9105db3b1bb60964c
cb02c38efa915ae66ceef37e23dc8db47800082ea1977f1ff24ea4f737eecad8
dbada9136a3896984946e47a462493fdadc3552c3cc2b74e10e5df01bb9b66a9

Total reclaimed space: 48.54MB
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7e1f906b8157   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it dazzling_napier sh
# \lsz
sh: 1: lsz: not found
# \ls
bin   dev		   docker-entrypoint.sh  home  media  opt   root  sbin	sys  usr
boot  docker-entrypoint.d  etc			 lib   mnt    proc  run   srv	tmp  var
# cd usr
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share
# \ls
X11		 common-licenses  dpkg	      java	   man	       pam-configs  terminfo
base-files	 debconf	  fontconfig  keyrings	   maven-repo  perl5	    util-linux
base-passwd	 debianutils	  fonts       libc-bin	   menu        pixmaps	    xml
bash-completion  dict		  gcc	      libgcrypt20  misc        polkit-1     zoneinfo
bug		 doc		  gdb	      lintian	   nginx       readline     zsh
ca-certificates  doc-base	  info	      locale	   pam	       tabset
# cd nginx
# \ls
html
# cd html	
# \ls
50x.html  index.html
# nano index.html
sh: 11: nano: not found
# apk add nano
sh: 12: apk: not found
# exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7e1f906b8157   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container run -p 5000:80 -d nginx:alpine 
267a68afa13603c75aaf88da795371ed4ffec2c274e68418e8aaefc6398513b2
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS         PORTS                  NAMES
267a68afa136   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago    Up 4 seconds   0.0.0.0:5000->80/tcp   nice_austin
7e1f906b8157   nginx          "/docker-entrypoint.…"   16 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it nice_austin sh
/ # \ls
bin                   home                  proc                  sys
dev                   lib                   root                  tmp
docker-entrypoint.d   media                 run                   usr
docker-entrypoint.sh  mnt                   sbin                  var
etc                   opt                   srv
/ # cd usr/
/usr # \ls
bin    lib    local  sbin   share
/usr # cd share
/usr/share # \ls
GeoIP            ca-certificates  licenses         nginx            zoneinfo
X11              doc              man              udhcpc
apk              fontconfig       misc             xml
/usr/share # cd nginx
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
50x.html    index.html
/usr/share/nginx/html # apk add nanop
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/aarch64/APKINDEX.tar.gz
ERROR: unable to select packages:
  nanop (no such package):
    required by: world[nanop]
/usr/share/nginx/html # apk add nano
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 44 MiB in 63 packages
/usr/share/nginx/html # \ls
50x.html    index.html
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS         PORTS                  NAMES
267a68afa136   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes   0.0.0.0:5000->80/tcp   nice_austin
7e1f906b8157   nginx          "/docker-entrypoint.…"   19 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container stop nice_austin

nice_austin
bradsimpson@Brads-MacBook-Air ~ % 


## NETWORKING


  import      Import the contents from a tarball to create a filesystem image
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Global Options:
      --config string      Location of client config files (default
                           "/Users/bradsimpson/.docker")
  -c, --context string     Name of the context to use to connect to the daemon
                           (overrides DOCKER_HOST env var and default context set with
                           "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket to connect to
  -l, --log-level string   Set the logging level ("debug", "info", "warn", "error",
                           "fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/Users/bradsimpson/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "/Users/bradsimpson/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default
                           "/Users/bradsimpson/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Run 'docker COMMAND --help' for more information on a command.

For more help on how to use Docker, head to https://docs.docker.com/go/guides/

bradsimpson@Brads-MacBook-Air ~ % docker network create --driver bridge my_new_network
255e708645d925710b4561afac301bd8ac6558e5bd40f0b79b6918bf9d1a309b
bradsimpson@Brads-MacBook-Air ~ % docker network ls                                   
NETWORK ID     NAME             DRIVER    SCOPE
1fe36a735ac1   bridge           bridge    local
0c4794c37db6   host             host      local
255e708645d9   my_new_network   bridge    local
61b3161ebf7d   none             null      local
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c1 --network my_new_network nginx:alpine
64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c2 --network my_new_network nginx:alpine 
be5f664a76a6298f9faac93a46c83179a498f064cb30d60e6046efe3511951da
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c2 nginx:alpine 
docker: Error response from daemon: Conflict. The container name "/c2" is already in use by container "be5f664a76a6298f9faac93a46c83179a498f064cb30d60e6046efe3511951da". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c3 nginx:alpine
e59ac71a58a63598728174f2c2e6da54df4c1d9853df23c83b2925736009740b
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c4 nginx:alpine 
4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
4ef68dd237e4   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago    Up 5 seconds    80/tcp                 c4
e59ac71a58a6   nginx:alpine   "/docker-entrypoint.…"   11 seconds ago   Up 11 seconds   80/tcp                 c3
be5f664a76a6   nginx:alpine   "/docker-entrypoint.…"   37 seconds ago   Up 36 seconds   80/tcp                 c2
64ee70e1abe0   nginx:alpine   "/docker-entrypoint.…"   47 seconds ago   Up 46 seconds   80/tcp                 c1
7e1f906b8157   nginx          "/docker-entrypoint.…"   46 minutes ago   Up 36 minutes   0.0.0.0:8080->80/tcp   dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container stop dazzling_napier
dazzling_napier
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c1
[
    {
        "Id": "64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889",
        "Created": "2023-12-12T17:16:48.545634551Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 6575,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-12T17:16:48.728717968Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889/hostname",
        "HostsPath": "/var/lib/docker/containers/64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889/hosts",
        "LogPath": "/var/lib/docker/containers/64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889/64ee70e1abe05dc66e9edec2a276f17d0311429bb73bf2222a8c9ede871e4889-json.log",
        "Name": "/c1",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "my_new_network",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                55,
                93
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/1974f352bc1c8eead27c4464e42e32855b0651d6b04210288429a575ba3373c9-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/1974f352bc1c8eead27c4464e42e32855b0651d6b04210288429a575ba3373c9/merged",
                "UpperDir": "/var/lib/docker/overlay2/1974f352bc1c8eead27c4464e42e32855b0651d6b04210288429a575ba3373c9/diff",
                "WorkDir": "/var/lib/docker/overlay2/1974f352bc1c8eead27c4464e42e32855b0651d6b04210288429a575ba3373c9/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "64ee70e1abe0",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.1",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.12"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx:alpine",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers \u003cdocker-maint@nginx.com\u003e"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "6ddf3b77d8b6f36308e10b6c279196e5a9d76c705c8f7d163a69f9ce14e34f87",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/6ddf3b77d8b6",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "",
            "Gateway": "",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "",
            "IPPrefixLen": 0,
            "IPv6Gateway": "",
            "MacAddress": "",
            "Networks": {
                "my_new_network": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "64ee70e1abe0"
                    ],
                    "NetworkID": "255e708645d925710b4561afac301bd8ac6558e5bd40f0b79b6918bf9d1a309b",
                    "EndpointID": "cc1ff168986f76a99bc7d834b5ced603e0eb8c2a2c30527c815254d88ff79538",
                    "Gateway": "172.18.0.1",
                    "IPAddress": "172.18.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:12:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c4 
[
    {
        "Id": "4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e",
        "Created": "2023-12-12T17:17:29.950858876Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 7009,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-12T17:17:30.108888751Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e/hostname",
        "HostsPath": "/var/lib/docker/containers/4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e/hosts",
        "LogPath": "/var/lib/docker/containers/4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e/4ef68dd237e405bbb0fa357d280c480b508edaf8ec2b3a2b4ba5328f39d4236e-json.log",
        "Name": "/c4",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                55,
                93
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/eb75dea6504ff201adb50edd82fe539543ff52505f1b229e0576a2ab8cb76eee-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/eb75dea6504ff201adb50edd82fe539543ff52505f1b229e0576a2ab8cb76eee/merged",
                "UpperDir": "/var/lib/docker/overlay2/eb75dea6504ff201adb50edd82fe539543ff52505f1b229e0576a2ab8cb76eee/diff",
                "WorkDir": "/var/lib/docker/overlay2/eb75dea6504ff201adb50edd82fe539543ff52505f1b229e0576a2ab8cb76eee/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "4ef68dd237e4",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.1",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.12"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx:alpine",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers \u003cdocker-maint@nginx.com\u003e"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "65fea267f5bf340d75537b8e96c6313d8c6456c899c236c4d046a123c65026a0",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/65fea267f5bf",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "99523d37a313bf1d68b2a71f314504f4325f7b56608166d9e9c436a8c93dde62",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.4",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:04",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "1fe36a735ac1b8211c6d2fe70ca0fb026e29ec7ac3bc4d8093d41539058eb43a",
                    "EndpointID": "99523d37a313bf1d68b2a71f314504f4325f7b56608166d9e9c436a8c93dde62",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.4",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:04",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 ash
/ # ping c2 -c 3
PING c2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.265 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.117 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.166 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.117/0.182/0.265 ms
/ # ping c3 -c 3
ping: bad address 'c3'
/ # ping c4 -c 3
ping: bad address 'c4'
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c3 ash 
/ # ping c4 -c 4
ping: bad address 'c4'
/ # ping c1 -c 4
ping: bad address 'c1'
/ # ping c2 -c 4
ping: bad address 'c2'
/ # ping 172.17.0.4 -c 4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.450 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.169 ms
64 bytes from 172.17.0.4: seq=2 ttl=64 time=0.192 ms
64 bytes from 172.17.0.4: seq=3 ttl=64 time=0.162 ms

--- 172.17.0.4 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.162/0.243/0.450 ms
/ # exit
bradsimpson@Brads-MacBook-Air ~ % 


## VOLUMES & BIND MOUNTS

441b370d59019178746eecc897887/diff:/var/lib/docker/overlay2/098e106cd4ce7d71eea1122353cfa08e6521f041a813df4e610aaa7db533fd44/diff:/var/lib/docker/overlay2/b524502fc40aece8a126f52872ffccdf33c8fd18eeb9896a73bbd37015162ce5/diff:/var/lib/docker/overlay2/82809c2f97a7559d2fc6bdd9ed979c89ddb5c62f689ca8dd8434aad7640f3cef/diff:/var/lib/docker/overlay2/2fd26a6716c4892966fdd7caf05ae2642c03c3e2c9cbc5afab58dd380bd5c4ee/diff:/var/lib/docker/overlay2/7651afd27ca6e197a766ffec66f5b77825ff7a28995c07ae0c878b9c3adde831/diff:/var/lib/docker/overlay2/033e377d2a69f2b5d8db1c9d16b65c47942292f658e8f72e06acf41007c25880/diff:/var/lib/docker/overlay2/494c1f85e9803b52bc30144d2937350c16dd654a3006dbe4a5d729497e0f72f6/diff:/var/lib/docker/overlay2/c18e7cdc5c90c2494b09769891c51c5f39fc475fc11a79c21493f1baa3beb564/diff:/var/lib/docker/overlay2/b0b9235892d66406d3e465349a8d3bb35f2f913af34c6ee5b5ea35da390ceb0c/diff",
                "MergedDir": "/var/lib/docker/overlay2/20fbafa167fcf3207196a945fa86cd01387bc47d52e362b965e6ff1c89058887/merged",
                "UpperDir": "/var/lib/docker/overlay2/20fbafa167fcf3207196a945fa86cd01387bc47d52e362b965e6ff1c89058887/diff",
                "WorkDir": "/var/lib/docker/overlay2/20fbafa167fcf3207196a945fa86cd01387bc47d52e362b965e6ff1c89058887/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:1c3daa06574284614db07a23682ab6d1c344f09f8093ee10e5de4152a51677a1",
                "sha256:310729fcb068da6941441d9627a3d8979e7dbd015c220324331e34af28b7e20c",
                "sha256:6cc6868915f4c4d399ec0026fd321acfd0b92e84cd2a51076e89041b3e3118b6",
                "sha256:10e10c831ae45343e95ad309a6e12d4248559f9dcffe3ca5b099044dfb1ced6e",
                "sha256:efeb668f57b52b8fe563c95296cd13a75431ab67e7a3b557b72ba4ef8d66e5de",
                "sha256:7df7b7f4d502154fb5a18da05456d5c74d9f70248a33112213c9469bb297470c",
                "sha256:79f05f53fceaaeffa6f88270b63f5b50d8359b7f66d6fb99a7ae2ebface34634",
                "sha256:f051436a55899d9ef6c1f7a74e487575a9d27e6046c0938ac49825972ada314e",
                "sha256:7cfa7dde137d5b682278bc5a0a6b5bec23ae142ddcec996d86faa2eec65ddaa3",
                "sha256:5bcc055db6d18a9f0252d404cecccfdb200a0124f510082bd6a95bb11e9ab5ae",
                "sha256:41961c2bd4aabfda25d4260d75f79052fd1f5a0c1645df7c43f3c2b3c711c794",
                "sha256:0e77db6aa900fe556e68e07ae83c1ba2008cd4a33b50e7f2898153731df0a104",
                "sha256:2a315bcee097176f1ba5a2916416eb2e40ef7348eba15212d3d95494af541b2e"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@Brads-MacBook-Air app % docker volume ls
DRIVER    VOLUME NAME
local     my_taco_tues
local     tuesday_taco
bradsimpson@Brads-MacBook-Air app % docker volume create taco_tuesday 
taco_tuesday
bradsimpson@Brads-MacBook-Air app % docker volume ls
DRIVER    VOLUME NAME
local     my_taco_tues
local     taco_tuesday
local     tuesday_taco
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker container run -d -e POSTGRES_PASSWORD=password --name postgres1 --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data postgres
e0ccc066dac869c15cb9a9e46dd505ed8f8fa3036cfd538afa004c77fee1f0bb
bradsimpson@Brads-MacBook-Air app % dpcker container ls
zsh: command not found: dpcker
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
e0ccc066dac8   postgres       "docker-entrypoint.s…"   14 seconds ago   Up 13 seconds   5432/tcp               postgres1
776f929aa366   nginx:alpine   "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   0.0.0.0:8000->80/tcp   infallible_swartz
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres1 sh
# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |  
 Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+--
---------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =
c/postgres          +
           |          |          |            |            |            |                 | p
ostgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =
c/postgres          +
           |          |          |            |            |            |                 | p
ostgres=CTc/postgres
(3 rows)







































postgres=# CREATE DATABASE test_taco WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |  
 Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+--
---------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =
c/postgres          +
           |          |          |            |            |            |                 | p
ostgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =
c/postgres          +
           |          |          |            |            |            |                 | p
ostgres=CTc/postgres
 test_taco | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
(4 rows)






































postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
e0ccc066dac8   postgres       "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    5432/tcp               postgres1
776f929aa366   nginx:alpine   "/docker-entrypoint.…"   12 minutes ago   Up 12 minutes   0.0.0.0:8000->80/tcp   infallible_swartz
bradsimpson@Brads-MacBook-Air app % docker container stop postgres1
postgres1
bradsimpson@Brads-MacBook-Air app % docker container ls =a
zsh: a not found
bradsimpson@Brads-MacBook-Air app % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS                  NAMES
e0ccc066dac8   postgres       "docker-entrypoint.s…"   3 minutes ago       Exited (0) 12 seconds ago                             postgres1
776f929aa366   nginx:alpine   "/docker-entrypoint.…"   13 minutes ago      Up 13 minutes                  0.0.0.0:8000->80/tcp   infallible_swartz
4ef68dd237e4   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 11 minutes ago                             c4
e59ac71a58a6   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 11 minutes ago                             c3
be5f664a76a6   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 11 minutes ago                             c2
64ee70e1abe0   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 11 minutes ago                             c1
267a68afa136   nginx:alpine   "/docker-entrypoint.…"   2 hours ago         Exited (0) 2 hours ago                                nice_austin
7e1f906b8157   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago                          dazzling_napier
bradsimpson@Brads-MacBook-Air app % docker container rm postgres1
postgres1
bradsimpson@Brads-MacBook-Air app % docker container run -d -e POSTGRES_PASSWORD=password --name postgres2 --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data postgres 
c278df35d9875a24e81057f1192cfe047ba6fd2d8473b77c0fa823caee1f616d
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres2 sh 
# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |  
 Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+--
---------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =
c/postgres          +
           |          |          |            |            |            |                 | p
ostgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =
c/postgres          +
           |          |          |            |            |            |                 | p
ostgres=CTc/postgres
 test_taco | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
(4 rows)






































postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % 

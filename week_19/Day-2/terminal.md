# DOCKER CLI TERMINAL 

bradsimpson@ ~:docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@ ~:docker container run hello-world
docker: Error response from daemon: dial unix docker.raw.sock: connect: connection refused.
See 'docker run --help'.
bradsimpson@ ~:docker container run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

bradsimpson@ ~:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_masterpiece   latest    68bd75289968   4 weeks ago     433MB
postgres                           latest    4c6b3cc10e6b   5 weeks ago     379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   3 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   4 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   6 months ago    377MB
ubuntu                             latest    27941809078c   7 months ago    77.8MB
nginx                              latest    0e901e68141f   7 months ago    142MB
alpine                             latest    e66264b98777   7 months ago    5.53MB
nginx                              alpine    b1c3acb28882   7 months ago    23.4MB
hello-world                        latest    feb5d9fea6a5   15 months ago   13.3kB
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
0422db406676   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     6b769352eb31a01b3fe6410a71a0dc6ff2994240bce8653a2c8ecd0f6616acaa
local     a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     new_taco_tues
local     postgres-data
local     taco_not_sandwich
local     taco_tuesday
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run --name cool_container -p 8080:80 -d nginx
f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af
bradsimpson@ ~:dcoker container ls
-bash: dcoker: command not found
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   22 seconds ago   Up 20 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container inspect
"docker container inspect" requires at least 1 argument.
See 'docker container inspect --help'.

Usage:  docker container inspect [OPTIONS] CONTAINER [CONTAINER...]

Display detailed information on one or more containers
bradsimpson@ ~:docker container inspect cool_container
[
    {
        "Id": "f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af",
        "Created": "2023-01-10T16:39:56.681565802Z",
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
            "Pid": 2666,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-10T16:39:58.159432601Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af/hostname",
        "HostsPath": "/var/lib/docker/containers/f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af/hosts",
        "LogPath": "/var/lib/docker/containers/f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af/f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af-json.log",
        "Name": "/cool_container",
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
                        "HostPort": "8080"
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
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
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
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
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
                "LowerDir": "/var/lib/docker/overlay2/c673e2886c3ee637d4e3620c8d51efb0d242ceabb6714daf74f940e9e1a2f9f8-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/c673e2886c3ee637d4e3620c8d51efb0d242ceabb6714daf74f940e9e1a2f9f8/merged",
                "UpperDir": "/var/lib/docker/overlay2/c673e2886c3ee637d4e3620c8d51efb0d242ceabb6714daf74f940e9e1a2f9f8/diff",
                "WorkDir": "/var/lib/docker/overlay2/c673e2886c3ee637d4e3620c8d51efb0d242ceabb6714daf74f940e9e1a2f9f8/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f74c6892e9d1",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1~bullseye"
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
            "SandboxID": "94008187a9015135ed31fa76c430bd2625fd4cd0d23d79485c6394f6420c5f9d",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8080"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "8080"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/94008187a901",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "7ff82da958a0c915f12eb129b2840994cdf6a95803100d18006f9439d53fdff1",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "0422db4066766f20b731404a02f06a59b9eec74f74992eb595c148bcbaae6eee",
                    "EndpointID": "7ff82da958a0c915f12eb129b2840994cdf6a95803100d18006f9439d53fdff1",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:docker image inspect nginx
[
    {
        "Id": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-05-28T05:41:03.228946845Z",
        "Container": "0a702bec7d2ceb935c6501ae3dfc1ab850f9ea46b9296eb1323b2b826595f954",
        "ContainerConfig": {
            "Hostname": "0a702bec7d2c",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1~bullseye"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:84a2e27303200422deb89ae538dbbc442ac0ffa72c7be4d6f1d3b4bd32dcd451",
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
        "DockerVersion": "20.10.12",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1~bullseye"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:84a2e27303200422deb89ae538dbbc442ac0ffa72c7be4d6f1d3b4bd32dcd451",
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
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 141526528,
        "VirtualSize": 141526528,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/merged",
                "UpperDir": "/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff",
                "WorkDir": "/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ad6562704f3759fb50f0d3de5f80a38f65a85e709b77fd24491253990f30b6be",
                "sha256:58354abe5f0e9e8cf3849a697cd86bfefb8448b9deb74e3d13aa3e4c98dd3665",
                "sha256:53ae81198b641f2911dfc469313edde2fe690bf230efaa823a4aa836d08336e0",
                "sha256:57d3fc88cb3f95fe3daac8591dabe1c161af0fcfd4cf099aa3f994c888ac7877",
                "sha256:747b7a567071ddb822a072c4dadc2ef50ef6d1bf35ce477e9a559f1df1b7c571",
                "sha256:33e3df466e11254954ba3b06301c93c066a1f699e2ddd80f0214340236d57935"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 21 minutes ago   Exited (0) 21 minutes ago                                               laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago   0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago   0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:docker container run --rm hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes               0.0.0.0:8080->80/tcp, :::8080->80/tcp       cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 22 minutes ago   Exited (0) 22 minutes ago                                               laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago   0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago   0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -p 8000:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/01/10 16:52:02 [notice] 1#1: using the "epoll" event method
2023/01/10 16:52:02 [notice] 1#1: nginx/1.21.6
2023/01/10 16:52:02 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/01/10 16:52:02 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2023/01/10 16:52:02 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/01/10 16:52:02 [notice] 1#1: start worker processes
2023/01/10 16:52:02 [notice] 1#1: start worker process 32
2023/01/10 16:52:02 [notice] 1#1: start worker process 33
172.17.0.1 - - [10/Jan/2023:16:52:21 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [10/Jan/2023:16:52:34 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [10/Jan/2023:16:52:35 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [10/Jan/2023:16:52:36 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [10/Jan/2023:16:52:36 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [10/Jan/2023:16:52:37 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
^C2023/01/10 16:53:18 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/01/10 16:53:18 [notice] 32#32: exiting
2023/01/10 16:53:18 [notice] 33#33: exiting
2023/01/10 16:53:18 [notice] 32#32: exit
2023/01/10 16:53:18 [notice] 33#33: exit
2023/01/10 16:53:18 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2023/01/10 16:53:18 [notice] 1#1: worker process 33 exited with code 0
2023/01/10 16:53:18 [notice] 1#1: signal 29 (SIGIO) received
2023/01/10 16:53:18 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/01/10 16:53:18 [notice] 1#1: worker process 32 exited with code 0
2023/01/10 16:53:18 [notice] 1#1: exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED              STATUS                      PORTS                                       NAMES
24a2889ca159   nginx                              "/docker-entrypoint.…"   About a minute ago   Exited (0) 27 seconds ago                                               confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   13 minutes ago       Up 13 minutes               0.0.0.0:8080->80/tcp, :::8080->80/tcp       cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 25 minutes ago       Exited (0) 25 minutes ago                                               laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago          Exited (255) 20 hours ago   0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago          Exited (255) 20 hours ago   0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -d alpine
unknown shorthand flag: 'd' in -d
See 'docker container ls --help'.
bradsimpson@ ~:docker container run -d alpine
f11c5241e18ad575d3f9831a5494d1309247c9dc9c007c71d8c6e015a6dc9d74
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                          PORTS                                       NAMES
f11c5241e18a   alpine                             "/bin/sh"                16 seconds ago   Exited (0) 14 seconds ago                                                   crazy_varahamihira
24a2889ca159   nginx                              "/docker-entrypoint.…"   2 minutes ago    Exited (0) About a minute ago                                               confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   15 minutes ago   Up 14 minutes                   0.0.0.0:8080->80/tcp, :::8080->80/tcp       cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 26 minutes ago   Exited (0) 26 minutes ago                                                   laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago       0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago       0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_masterpiece   latest    68bd75289968   4 weeks ago     433MB
postgres                           latest    4c6b3cc10e6b   5 weeks ago     379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   3 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   4 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   6 months ago    377MB
ubuntu                             latest    27941809078c   7 months ago    77.8MB
nginx                              latest    0e901e68141f   7 months ago    142MB
alpine                             latest    e66264b98777   7 months ago    5.53MB
nginx                              alpine    b1c3acb28882   7 months ago    23.4MB
hello-world                        latest    feb5d9fea6a5   15 months ago   13.3kB
bradsimpson@ ~:docker container run -it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd lib
/lib # \ls
apk                    libapk.so.3.12.0       libssl.so.1.1          mdev
firmware               libc.musl-x86_64.so.1  libz.so.1              modules-load.d
ld-musl-x86_64.so.1    libcrypto.so.1.1       libz.so.1.2.12         sysctl.d
/lib # cd ..
/ # cd bin
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
/bin # ^C
/bin # ^C
/bin # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                        PORTS                                       NAMES
435de5c690b0   alpine                             "sh"                     2 minutes ago    Exited (130) 24 seconds ago                                               angry_dhawan
f11c5241e18a   alpine                             "/bin/sh"                8 minutes ago    Exited (0) 8 minutes ago                                                  crazy_varahamihira
24a2889ca159   nginx                              "/docker-entrypoint.…"   11 minutes ago   Exited (0) 10 minutes ago                                                 confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes                 0.0.0.0:8080->80/tcp, :::8080->80/tcp       cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 35 minutes ago   Exited (0) 35 minutes ago                                                 laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago     0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago     0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -p 8080:80 -d nginx
f8d5bb36b6bc1a6e80b0f7effd301026c8de22f56cd613ea0048d50219566684
docker: Error response from daemon: driver failed programming external connectivity on endpoint busy_fermi (ad81b376d4d4d63de5feafda1fb8da90cb26ce24f3eccdbd10c0779ac17d00f3): Bind for 0.0.0.0:8080 failed: port is already allocated.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   26 minutes ago   Up 26 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container run -it --name test alpine sh
/ # exit
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   30 minutes ago   Up 30 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED              STATUS                          PORTS                                       NAMES
faec852fc054   alpine                             "sh"                     About a minute ago   Exited (0) About a minute ago                                               test
f8d5bb36b6bc   nginx                              "/docker-entrypoint.…"   4 minutes ago        Created                                                                     busy_fermi
435de5c690b0   alpine                             "sh"                     9 minutes ago        Exited (130) 7 minutes ago                                                  angry_dhawan
f11c5241e18a   alpine                             "/bin/sh"                16 minutes ago       Exited (0) 16 minutes ago                                                   crazy_varahamihira
24a2889ca159   nginx                              "/docker-entrypoint.…"   18 minutes ago       Exited (0) 17 minutes ago                                                   confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   30 minutes ago       Up 30 minutes                   0.0.0.0:8080->80/tcp, :::8080->80/tcp       cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 42 minutes ago       Exited (0) 42 minutes ago                                                   laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago          Exited (255) 20 hours ago       0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago          Exited (255) 20 hours ago       0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f74c6892e9d1   nginx     "/docker-entrypoint.…"   32 minutes ago   Up 32 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   cool_container
bradsimpson@ ~:docker container stop f74c6892e9d1 
f74c6892e9d1
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear

bradsimpson@ ~:docker contains ls -a
unknown shorthand flag: 'a' in -a
See 'docker --help'.

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "/Users/bradsimpson/.docker")
  -c, --context string     Name of the context to use to connect to the daemon
                           (overrides DOCKER_HOST env var and default context set with
                           "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal")
                           (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default
                           "/Users/bradsimpson/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default
                           "/Users/bradsimpson/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default
                           "/Users/bradsimpson/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Build with BuildKit (Docker Inc., v0.5.1-docker)
  compose*    Docker Compose (Docker Inc., v2.0.0-beta.6)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  scan*       Docker Scan (Docker Inc., v0.8.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker COMMAND --help' for more information on a command.

To get more help with docker, check out our guides at https://docs.docker.com/go/guides/

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                        PORTS                                       NAMES
faec852fc054   alpine                             "sh"                     4 minutes ago    Exited (0) 4 minutes ago                                                  test
f8d5bb36b6bc   nginx                              "/docker-entrypoint.…"   7 minutes ago    Created                                                                   busy_fermi
435de5c690b0   alpine                             "sh"                     12 minutes ago   Exited (130) 10 minutes ago                                               angry_dhawan
f11c5241e18a   alpine                             "/bin/sh"                19 minutes ago   Exited (0) 18 minutes ago                                                 crazy_varahamihira
24a2889ca159   nginx                              "/docker-entrypoint.…"   21 minutes ago   Exited (0) 20 minutes ago                                                 confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   33 minutes ago   Exited (0) 42 seconds ago                                                 cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 45 minutes ago   Exited (0) 45 minutes ago                                                 laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago     0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 20 hours ago     0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:docker container start 24a2889ca159 
24a2889ca159
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
24a2889ca159   nginx     "/docker-entrypoint.…"   23 minutes ago   Up 34 seconds   0.0.0.0:8000->80/tcp, :::8000->80/tcp   confident_lumiere
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                        PORTS                                       NAMES
faec852fc054   alpine                             "sh"                     6 minutes ago    Exited (0) 6 minutes ago                                                  test
f8d5bb36b6bc   nginx                              "/docker-entrypoint.…"   9 minutes ago    Created                                                                   busy_fermi
435de5c690b0   alpine                             "sh"                     15 minutes ago   Exited (130) 12 minutes ago                                               angry_dhawan
f11c5241e18a   alpine                             "/bin/sh"                21 minutes ago   Exited (0) 21 minutes ago                                                 crazy_varahamihira
24a2889ca159   nginx                              "/docker-entrypoint.…"   24 minutes ago   Up About a minute             0.0.0.0:8000->80/tcp, :::8000->80/tcp       confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   36 minutes ago   Exited (0) 3 minutes ago                                                  cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 47 minutes ago   Exited (0) 47 minutes ago                                                 laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 21 hours ago     0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 21 hours ago     0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:docker container rm 435de5c690b0 
435de5c690b0
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
faec852fc054   alpine                             "sh"                     7 minutes ago    Exited (0) 7 minutes ago                                                test
f8d5bb36b6bc   nginx                              "/docker-entrypoint.…"   10 minutes ago   Created                                                                 busy_fermi
f11c5241e18a   alpine                             "/bin/sh"                22 minutes ago   Exited (0) 22 minutes ago                                               crazy_varahamihira
24a2889ca159   nginx                              "/docker-entrypoint.…"   24 minutes ago   Up About a minute           0.0.0.0:8000->80/tcp, :::8000->80/tcp       confident_lumiere
f74c6892e9d1   nginx                              "/docker-entrypoint.…"   36 minutes ago   Exited (0) 3 minutes ago                                                cool_container
c3a0b7d5d5f5   hello-world                        "/hello"                 48 minutes ago   Exited (0) 48 minutes ago                                               laughing_einstein
fbbeba89e581   bradsimpson213/react_masterpiece   "docker-entrypoint.s…"   4 weeks ago      Exited (255) 21 hours ago   0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   peaceful_gauss
88754df26a8a   postgres                           "docker-entrypoint.s…"   4 weeks ago      Exited (255) 21 hours ago   0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ ~:docker container prune 
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
faec852fc054ef4c928de8ca8114a17c2ec108adb4071e8dd19189ec953b8763
f8d5bb36b6bc1a6e80b0f7effd301026c8de22f56cd613ea0048d50219566684
f11c5241e18ad575d3f9831a5494d1309247c9dc9c007c71d8c6e015a6dc9d74
f74c6892e9d12ae328df3ba6c39de72a6b0b9e9d977dc922c9fc5112370fc1af
c3a0b7d5d5f57cddb9f561a39f4ddfee50f56899f451d2c30398791715397127
fbbeba89e58124d9d0bca2973658a0abb9b3e73aafcf174c794adb04ea8160a1
88754df26a8ac9eeeacc7ced182bfa9fcae8b24e532284cc470c559389283dc2

Total reclaimed space: 47.95MB
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
24a2889ca159   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 4 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   confident_lumiere
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
24a2889ca159   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 4 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   confident_lumiere
bradsimpson@ ~:docker container exec -it confident_lumiere
"docker container exec" requires at least 2 arguments.
See 'docker container exec --help'.

Usage:  docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container
bradsimpson@ ~:docker container exec -it confident_lumiere sh
# \ls
bin   dev		   docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
boot  docker-entrypoint.d  etc			 lib   media  opt  root  sbin  sys  usr
# cd usr
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share
# \ls
X11		 ca-certificates  doc-base    info	man	    pam-configs     tabset
adduser		 common-licenses  dpkg	      java	maven-repo  perl5	    terminfo
base-files	 debconf	  fontconfig  keyrings	menu	    pixmaps	    ucf
base-passwd	 debianutils	  fonts       libc-bin	misc	    polkit-1	    xml
bash-completion  dict		  gcc	      lintian	nginx	    readline	    zoneinfo
bug		 doc		  gdb	      locale	pam	    sensible-utils  zsh
# cd nginx
# \ls
html
# cd html 	
# \ls
50x.html  index.html
# nano index.html
sh: 10: nano: not found
# apk add nano
sh: 11: apk: not found
# exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
24a2889ca159   nginx     "/docker-entrypoint.…"   31 minutes ago   Up 8 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   confident_lumiere


# NETWORKING SECTION!!!

bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
0422db406676   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
24a2889ca159   nginx     "/docker-entrypoint.…"   49 minutes ago   Up 26 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   confident_lumiere
bradsimpson@ ~:docker container inspect confident_lumiere
[
    {
        "Id": "24a2889ca1598490dee27a3ee17d4b272eb71e019a9dc65f652e899a6b91cf58",
        "Created": "2023-01-10T16:52:01.093722381Z",
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
            "Pid": 3613,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-10T17:15:02.168581274Z",
            "FinishedAt": "2023-01-10T16:53:18.355904976Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/24a2889ca1598490dee27a3ee17d4b272eb71e019a9dc65f652e899a6b91cf58/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/24a2889ca1598490dee27a3ee17d4b272eb71e019a9dc65f652e899a6b91cf58/hostname",
        "HostsPath": "/var/lib/docker/containers/24a2889ca1598490dee27a3ee17d4b272eb71e019a9dc65f652e899a6b91cf58/hosts",
        "LogPath": "/var/lib/docker/containers/24a2889ca1598490dee27a3ee17d4b272eb71e019a9dc65f652e899a6b91cf58/24a2889ca1598490dee27a3ee17d4b272eb71e019a9dc65f652e899a6b91cf58-json.log",
        "Name": "/confident_lumiere",
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
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
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
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
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
                "LowerDir": "/var/lib/docker/overlay2/932d13ec80a617ff369d655dd340e9e4d17c09a8cd28769d4e130a8bf8520bc4-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/932d13ec80a617ff369d655dd340e9e4d17c09a8cd28769d4e130a8bf8520bc4/merged",
                "UpperDir": "/var/lib/docker/overlay2/932d13ec80a617ff369d655dd340e9e4d17c09a8cd28769d4e130a8bf8520bc4/diff",
                "WorkDir": "/var/lib/docker/overlay2/932d13ec80a617ff369d655dd340e9e4d17c09a8cd28769d4e130a8bf8520bc4/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "24a2889ca159",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1~bullseye"
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
            "SandboxID": "d0fe37f5ef36fb125018e07a303c5ace9ec9b8313c814bab06ba0ad6a0da0bbf",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8000"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "8000"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/d0fe37f5ef36",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "d7f734e228c77d1ded57ed493c2737c67ca295b0c8f108d448938d5d48cf48ab",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "0422db4066766f20b731404a02f06a59b9eec74f74992eb595c148bcbaae6eee",
                    "EndpointID": "d7f734e228c77d1ded57ed493c2737c67ca295b0c8f108d448938d5d48cf48ab",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
0422db406676   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
0422db406676   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker network create --driver bridge my_network3
5a5cc332e83047ccf66fe2fddb5cb24a1858feb79381488a10466c6e1271d24c
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
0422db406676   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
5a5cc332e830   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
24a2889ca159   nginx     "/docker-entrypoint.…"   55 minutes ago   Up 32 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   confident_lumiere
bradsimpson@ ~:docker container stop 24a2889ca159
24a2889ca159
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run -d --name c1 --network my_network3 nginx:alpine
efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38
^[[Abradsimpson@ ~:docker container run -d --name c2 --network my_network3 nginx:alpine
3dad1a94ca8427a93e23778fa1965f3f97ba1798988af6de537cf82ef20c0604
dbradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
3dad1a94ca84   nginx:alpine   "/docker-entrypoint.…"   12 seconds ago   Up 6 seconds    80/tcp    c2
efa8c2d8f56e   nginx:alpine   "/docker-entrypoint.…"   25 seconds ago   Up 23 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c3 nginx:alpine
3b5f7ba05598dec91d858159e6838f41ae154bb34507ef904b2c645cf0d9d2df
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine
800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
800396a9e204   nginx:alpine   "/docker-entrypoint.…"   9 seconds ago        Up 7 seconds        80/tcp    c4
3b5f7ba05598   nginx:alpine   "/docker-entrypoint.…"   15 seconds ago       Up 13 seconds       80/tcp    c3
3dad1a94ca84   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up 59 seconds       80/tcp    c2
efa8c2d8f56e   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
800396a9e204   nginx:alpine   "/docker-entrypoint.…"   17 seconds ago       Up 16 seconds       80/tcp    c4
3b5f7ba05598   nginx:alpine   "/docker-entrypoint.…"   23 seconds ago       Up 22 seconds       80/tcp    c3
3dad1a94ca84   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
efa8c2d8f56e   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38",
        "Created": "2023-01-10T17:49:14.362454024Z",
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
            "Pid": 3958,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-10T17:49:16.456739893Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38/hostname",
        "HostsPath": "/var/lib/docker/containers/efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38/hosts",
        "LogPath": "/var/lib/docker/containers/efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38/efa8c2d8f56e0ea1ad3055479389a968869231f50b7e697356fb06a9d3104c38-json.log",
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
            "NetworkMode": "my_network3",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
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
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
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
                "LowerDir": "/var/lib/docker/overlay2/b9c123e3bd9293d8a49f334777379af5922e255d1383f5f92e3e40e02d580060-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/b9c123e3bd9293d8a49f334777379af5922e255d1383f5f92e3e40e02d580060/merged",
                "UpperDir": "/var/lib/docker/overlay2/b9c123e3bd9293d8a49f334777379af5922e255d1383f5f92e3e40e02d580060/diff",
                "WorkDir": "/var/lib/docker/overlay2/b9c123e3bd9293d8a49f334777379af5922e255d1383f5f92e3e40e02d580060/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "efa8c2d8f56e",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1"
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
            "SandboxID": "cbd82d6ec522b387e3c2a65043fa8e087de551ff0e68d66c627834905c38bd4e",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/cbd82d6ec522",
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
                "my_network3": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "efa8c2d8f56e"
                    ],
                    "NetworkID": "5a5cc332e83047ccf66fe2fddb5cb24a1858feb79381488a10466c6e1271d24c",
                    "EndpointID": "148c579cdce1a81b01347ffd4e73d2ccabed72c098fda78163e3b9ecf294b5a5",
                    "Gateway": "172.20.0.1",
                    "IPAddress": "172.20.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:14:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49",
        "Created": "2023-01-10T17:50:24.564893595Z",
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
            "Pid": 4425,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-01-10T17:50:25.515975872Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49/hostname",
        "HostsPath": "/var/lib/docker/containers/800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49/hosts",
        "LogPath": "/var/lib/docker/containers/800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49/800396a9e2045d8dec6a0e54e9d17a53a952d9270d37c8449012a9c447956c49-json.log",
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
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
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
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
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
                "LowerDir": "/var/lib/docker/overlay2/b44ddf6a5a7f3f5ae292bce8cac1d0fad4c3efeccbf731b293188663868cb331-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/b44ddf6a5a7f3f5ae292bce8cac1d0fad4c3efeccbf731b293188663868cb331/merged",
                "UpperDir": "/var/lib/docker/overlay2/b44ddf6a5a7f3f5ae292bce8cac1d0fad4c3efeccbf731b293188663868cb331/diff",
                "WorkDir": "/var/lib/docker/overlay2/b44ddf6a5a7f3f5ae292bce8cac1d0fad4c3efeccbf731b293188663868cb331/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "800396a9e204",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1"
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
            "SandboxID": "cae6e26a0f7bfc018902bcb0ff46a12b2513f48e4413066bd33ca74898dd0cef",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/cae6e26a0f7b",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "d76143d45d426d36b109b5de21b17acd9a761940894ffdf961bc5f399689e624",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "0422db4066766f20b731404a02f06a59b9eec74f74992eb595c148bcbaae6eee",
                    "EndpointID": "d76143d45d426d36b109b5de21b17acd9a761940894ffdf961bc5f399689e624",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
800396a9e204   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
3b5f7ba05598   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
3dad1a94ca84   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
efa8c2d8f56e   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 sh
/ # ping -c 3 c2
PING c2 (172.20.0.3): 56 data bytes
64 bytes from 172.20.0.3: seq=0 ttl=64 time=0.326 ms
64 bytes from 172.20.0.3: seq=1 ttl=64 time=0.106 ms
64 bytes from 172.20.0.3: seq=2 ttl=64 time=0.113 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.106/0.181/0.326 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
    
--- 172.17.0.3 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
/ # ping -c 3 c4
ping: bad address 'c4'
/ # exit
bradsimpson@ ~:docker container exec -it c3 sh
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.214 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.279 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.119 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.096 ms

--- 172.17.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.096/0.177/0.279 ms
/ # exit
bradsimpson@ ~:



# VOLUMES & BIND MOUNTS

Last login: Tue Jan 10 12:27:19 on ttys006

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\clear










































bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:\clear







































bradsimpson@ app:docker container run --mount type=bind,source=/absolute/path/to/local/folder,target=absolute/path/in/container
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ app:docker image inspect nginx
[
    {
        "Id": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:2bcabc23b45489fb0885d69a06ba1d648aeda973fae7bb981bafbb884165e514"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-05-28T05:41:03.228946845Z",
        "Container": "0a702bec7d2ceb935c6501ae3dfc1ab850f9ea46b9296eb1323b2b826595f954",
        "ContainerConfig": {
            "Hostname": "0a702bec7d2c",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1~bullseye"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:84a2e27303200422deb89ae538dbbc442ac0ffa72c7be4d6f1d3b4bd32dcd451",
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
        "DockerVersion": "20.10.12",
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
                "NGINX_VERSION=1.21.6",
                "NJS_VERSION=0.7.3",
                "PKG_RELEASE=1~bullseye"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:84a2e27303200422deb89ae538dbbc442ac0ffa72c7be4d6f1d3b4bd32dcd451",
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
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 141526528,
        "VirtualSize": 141526528,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/merged",
                "UpperDir": "/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff",
                "WorkDir": "/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ad6562704f3759fb50f0d3de5f80a38f65a85e709b77fd24491253990f30b6be",
                "sha256:58354abe5f0e9e8cf3849a697cd86bfefb8448b9deb74e3d13aa3e4c98dd3665",
                "sha256:53ae81198b641f2911dfc469313edde2fe690bf230efaa823a4aa836d08336e0",
                "sha256:57d3fc88cb3f95fe3daac8591dabe1c161af0fcfd4cf099aa3f994c888ac7877",
                "sha256:747b7a567071ddb822a072c4dadc2ef50ef6d1bf35ce477e9a559f1df1b7c571",
                "sha256:33e3df466e11254954ba3b06301c93c066a1f699e2ddd80f0214340236d57935"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:\ls
index.html
bradsimpson@ app:cd..
-bash: cd..: command not found
bradsimpson@ app:cd ..
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app/
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container run -d -p 8000:80 --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html nginx:alpine 
628a3b89738a8428b647a5e4f4328fc5185b95e8a9bf051c5d9a089da035100c
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
628a3b89738a   nginx:alpine   "/docker-entrypoint.…"   7 seconds ago    Up 5 seconds    0.0.0.0:8000->80/tcp, :::8000->80/tcp   loving_edison
800396a9e204   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago   Up 50 minutes   80/tcp                                  c4
3b5f7ba05598   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago   Up 50 minutes   80/tcp                                  c3
3dad1a94ca84   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp                                  c2
efa8c2d8f56e   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp                                  c1
bradsimpson@ ~:docker container exec -it loving_edison sh
/ # \ls
bin                   home                  proc                  sys
dev                   lib                   root                  tmp
docker-entrypoint.d   media                 run                   usr
docker-entrypoint.sh  mnt                   sbin                  var
etc                   opt                   srv
/ # cd usr
/usr # cd share
/usr/share # cd nginx/html
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
sh: nano: not found
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (5.9-r0)
Executing busybox-1.34.1-r5.trigger
OK: 26 MiB in 43 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ ~:cd app
bradsimpson@ app:nano index.html 
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
628a3b89738a   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8000->80/tcp, :::8000->80/tcp   loving_edison
800396a9e204   nginx:alpine   "/docker-entrypoint.…"   55 minutes ago   Up 55 minutes   80/tcp                                  c4
3b5f7ba05598   nginx:alpine   "/docker-entrypoint.…"   55 minutes ago   Up 55 minutes   80/tcp                                  c3
3dad1a94ca84   nginx:alpine   "/docker-entrypoint.…"   56 minutes ago   Up 56 minutes   80/tcp                                  c2
efa8c2d8f56e   nginx:alpine   "/docker-entrypoint.…"   56 minutes ago   Up 56 minutes   80/tcp                                  c1
bradsimpson@ app:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
628a3b89738a   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   loving_edison
bradsimpson@ app:docker container stop loving_edison
loving_edison
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:\clear




















bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     6b769352eb31a01b3fe6410a71a0dc6ff2994240bce8653a2c8ecd0f6616acaa
local     a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     new_taco_tues
local     postgres-data
local     taco_not_sandwich
local     taco_tuesday
bradsimpson@ app:docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
my_volume2
new_taco_tues
postgres-data
taco_not_sandwich
6b769352eb31a01b3fe6410a71a0dc6ff2994240bce8653a2c8ecd0f6616acaa
a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a
my_volume3
taco_tuesday
my_new_volume
my_volume

Total reclaimed space: 296.4MB
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_masterpiece   latest    68bd75289968   4 weeks ago     433MB
postgres                           latest    4c6b3cc10e6b   5 weeks ago     379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   3 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   4 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   6 months ago    377MB
ubuntu                             latest    27941809078c   7 months ago    77.8MB
nginx                              latest    0e901e68141f   7 months ago    142MB
alpine                             latest    e66264b98777   7 months ago    5.53MB
nginx                              alpine    b1c3acb28882   7 months ago    23.4MB
hello-world                        latest    feb5d9fea6a5   15 months ago   13.3kB
bradsimpson@ app:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:10d6e725f9b2f5531617d93164f4fc85b1739e04cab62cbfbfb81ccd866513b8
Deleted: sha256:4c6b3cc10e6bbb2afd68caa44a3eb6cef12caf483e60b28c6de2c56e8f1b99bc
Deleted: sha256:44539258acdf19c71f0d6c6f7c5981a280279925a21beb5e3e7fa946084e59cb
Deleted: sha256:41c9043a8c33d5c4eadb00346caaffa29f9a842d4f964d202968cf2ed0760cf6
Deleted: sha256:4445e5e3df8235ad2fbc67bda297a70b21e9bbde4e1527952e6abe0c02cc783d
Deleted: sha256:ed4b17599a658595847f4221020903501c46b475efe1223175cbe1d49ca44093
Deleted: sha256:db43c165e4829bc0ca2d71234849bcbed38f2482ea284efc59e66f1e39af294c
Deleted: sha256:e8c74768d3763096399ff71f13d735fc79224a3e8a4703629b0931c64e304d7e
Deleted: sha256:cb993bb1ec397175d29e14e72998b710f6fb1047a63ae3b55ade1bf2cf580987
Deleted: sha256:cec53686f926af2a1020462b5a72f311288c2b71f69997b1fea499f57fe88a4b
Deleted: sha256:981eca4ea122c675176da92a6a910c9f64bc488d4626c3cc3832f5c9306631d2
Deleted: sha256:39d7dafd74f851a61d4a890194667e3c662a0b23ae43ca14f985dc2b05959eaf
Deleted: sha256:a9f9a0eebd255a4cf59e3b2565a277e093cd9a91e6a04fdc0e7ae451a00784b0
Deleted: sha256:9594f6cf408b247f8e2fa1982f45ce6ba09ac289879c45e6cc8493deb64d8ee8
Deleted: sha256:b5ebffba54d3e3f7fd80435fcdc34c4a96fdb2ecab0f0a298fe08f74c2f69d29
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_masterpiece   latest    68bd75289968   4 weeks ago     433MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   3 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   4 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   6 months ago    377MB
ubuntu                             latest    27941809078c   7 months ago    77.8MB
nginx                              latest    0e901e68141f   7 months ago    142MB
alpine                             latest    e66264b98777   7 months ago    5.53MB
nginx                              alpine    b1c3acb28882   7 months ago    23.4MB
hello-world                        latest    feb5d9fea6a5   15 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
3f4ca61aafcd: Pull complete 
048d3078d446: Pull complete 
c6d23b4fe6c1: Pull complete 
d846f6946dd5: Pull complete 
76f7157f330d: Pull complete 
4eacfb0464b2: Pull complete 
5c197e2b597b: Pull complete 
2c4576649951: Pull complete 
1ae267d32d50: Pull complete 
03048c1132b5: Pull complete 
bdee410b6909: Pull complete 
d3354a8bfb14: Pull complete 
0105a87d8ff9: Pull complete 
Digest: sha256:f4cd32e7a418d9c9ba043e7d561243388202b654c740bcc85ca40b41d9fb4f1e
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
postgres                           latest    a26eb6069868   2 weeks ago     379MB
bradsimpson213/react_masterpiece   latest    68bd75289968   4 weeks ago     433MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   3 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   4 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   6 months ago    377MB
ubuntu                             latest    27941809078c   7 months ago    77.8MB
nginx                              latest    0e901e68141f   7 months ago    142MB
alpine                             latest    e66264b98777   7 months ago    5.53MB
nginx                              alpine    b1c3acb28882   7 months ago    23.4MB
hello-world                        latest    feb5d9fea6a5   15 months ago   13.3kB
bradsimpson@ app:\clear

bradsimpson@ app:docker image inspect postgres
[
    {
        "Id": "sha256:a26eb6069868e4bfd0095788e541bb40711861bdfb2a8252103dea85cc0758aa",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:f4cd32e7a418d9c9ba043e7d561243388202b654c740bcc85ca40b41d9fb4f1e"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-12-22T23:19:59.856808957Z",
        "Container": "938c729969fbf6312f6563590395ed0bb4cbc982b039598c38ffa539c86a5df5",
        "ContainerConfig": {
            "Hostname": "938c729969fb",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "5432/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/15/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=15",
                "PG_VERSION=15.1-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:69682b3d7cb168ec6269a7e9cf4e1e0e26210173e223211c20302ca93733dd64",
            "Volumes": {
                "/var/lib/postgresql/data": {}
            },
            "WorkingDir": "",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {},
            "StopSignal": "SIGINT"
        },
        "DockerVersion": "20.10.12",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "5432/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/15/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=15",
                "PG_VERSION=15.1-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:69682b3d7cb168ec6269a7e9cf4e1e0e26210173e223211c20302ca93733dd64",
            "Volumes": {
                "/var/lib/postgresql/data": {}
            },
            "WorkingDir": "",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": null,
            "StopSignal": "SIGINT"
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 378594789,
        "VirtualSize": 378594789,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/515ca55757c8ef8d52cef8936758b88443a06e21fe2d35f6f902839d0463fe6b/diff:/var/lib/docker/overlay2/bc0b9112f384eee2a89831c053c27d541fed77ef3ecd44bf52ac3998d12bff99/diff:/var/lib/docker/overlay2/4044ef27ecd6eef746cf4dfdd137c3e913b7567a1e71a5fe469b87df10819373/diff:/var/lib/docker/overlay2/11040f9c1f68b7b91f90fad6a6d19f565635b95ab6eb936ba99a6b273a510342/diff:/var/lib/docker/overlay2/3e82917566bc96fc2eb2163f33d5ee441450dab3f4c8e71f3d4a3cfa7466be42/diff:/var/lib/docker/overlay2/b3a757b01cb6a1e7226b9310199cbedd78232c1af723459f95a6f54750721610/diff:/var/lib/docker/overlay2/9ec4f387ea7187a633d2774eeba641264f6cf5157ec9abdcb70edca19d75daa5/diff:/var/lib/docker/overlay2/6af6853aa89cbb6cb55f1f72f704d3e0d11cdc7712759c5c4f6415c2274fd6d9/diff:/var/lib/docker/overlay2/c9eae3b32b26b05fc4df8c70665d5c525f5870d7a1621a1c3167ed731115eab5/diff:/var/lib/docker/overlay2/8ce8f21ba79f3f4c1405cf6c8b4228850b08737f28f5fa13952233a4790d78b5/diff:/var/lib/docker/overlay2/b61a01191104b44f475de2ad4205e6f92907fbb43d5af11f1f09908eccc731df/diff:/var/lib/docker/overlay2/80c5ace99c229d7afb4a30d2ee6935863d2c2efd87aaa0a90a145635ff4bb68a/diff",
                "MergedDir": "/var/lib/docker/overlay2/30a9405d720b8adc0b744fcfed137063f5b048fc5904411e9bb781c74bad62a9/merged",
                "UpperDir": "/var/lib/docker/overlay2/30a9405d720b8adc0b744fcfed137063f5b048fc5904411e9bb781c74bad62a9/diff",
                "WorkDir": "/var/lib/docker/overlay2/30a9405d720b8adc0b744fcfed137063f5b048fc5904411e9bb781c74bad62a9/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:8a70d251b65364698f195f5a0b424e0d67de81307b79afbe662abd797068a069",
                "sha256:258bf5ba2a242526a2436c6e0f2859c25a4bef657f7ba51c4e554009199cb2af",
                "sha256:328a9a322b848900668bd671bfec1b5357a0d616a248a0c370fc82de7fd7aae6",
                "sha256:0cc0ab5b848db7e72098ee62919e314188b204a716a61a74f81c46fed983aadd",
                "sha256:9e0f91636dfe2d069c9be6c79a84a19ac936cc1c566e6775cbeb7f6c81c048d4",
                "sha256:3969eb3b2a7a9196e43a7fee44b1fe85d8573292d48cc0f495e0250f9605f1a1",
                "sha256:66e1238f31e2484f816cb9bb206ed4105d45f82d3932b1b6129e94b94b1e1ee0",
                "sha256:25b9e54de726d30366b4894db0d029ddc942c89aa461b07aff98ca90a792cbb9",
                "sha256:93d46c1155513a0baa1d9ff24527d48cddaa58e436b790f2562985c77b40d3e9",
                "sha256:31094a71264f8e92a352057c36d77266e639eda3abb9708637ff3de1d4e7d79b",
                "sha256:0d5a36a7c9ea2425d4c24b0fd0296eb3184118a4a62b385af53edabdfb8bde14",
                "sha256:f24412f2c9ffc6a030df00031e1acf386b6322693333e5c778f6e078d6b7624e",
                "sha256:eca32511a241ebe0148580a9a190b80dcd446976c552206f0a743efac82387f3"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
bradsimpson@ app:docker volume create taco_tuesday
taco_tuesday
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     taco_tuesday
bradsimpson@ app:docker container run -p 5431:5432 --name postgres5431 -e POSTGRES_PASSWORD=password --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data -d postgres
1373429aa1b24d5df0b05bcfeccea97658e440d59dc01f1440c133d16aae901b
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
1373429aa1b2   postgres   "docker-entrypoint.s…"   8 seconds ago   Up 7 seconds   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

postgres=# CREATE DATABASE wing_wednesday WITH OWNER postgres
postgres-# ;
CREATE DATABASE
postgres=# \l
                                   List of databases
      Name      |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
----------------+----------+----------+------------+------------+-----------------------
 postgres       | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                |          |          |            |            | postgres=CTc/postgres
 template1      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                |          |          |            |            | postgres=CTc/postgres
 wing_wednesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres=# exit
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
1373429aa1b2   postgres   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
bradsimpson@ app:docker container stop postgres5431
postgres5431
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container run -p 5430:5432 --name postgres5430 -e POSTGRES_PASSWORD=password --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data -d postgres
ea6c421a3be9878b43f4cebaf6f30d3656d941fc9a9d94dd8e9d036a76c805c2
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
ea6c421a3be9   postgres   "docker-entrypoint.s…"   6 seconds ago   Up 4 seconds   0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   postgres5430
bradsimpson@ app:psql -p 5430 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                   List of databases
      Name      |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
----------------+----------+----------+------------+------------+-----------------------
 postgres       | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                |          |          |            |            | postgres=CTc/postgres
 template1      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                |          |          |            |            | postgres=CTc/postgres
 wing_wednesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres=# exit
bradsimpson@ app:

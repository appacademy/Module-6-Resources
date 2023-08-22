# Container CLI

Last login: Mon Aug 21 17:22:31 on ttys074
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                         COMMAND                  CREATED              STATUS                      PORTS     NAMES
0fe734686379   bradsimpson213/patchstagram   "flask run"              About a minute ago   Exited (0) 24 seconds ago             thirsty_bardeen
394ef7ba3467   2a5eb398bf5e                  "/bin/sh -c 'gunicor…"   5 minutes ago        Exited (3) 5 minutes ago              elegant_blackburn
0eb39ef68891   9dcd6c2141ad                  "/bin/sh -c 'gunicor…"   10 minutes ago       Exited (0) 6 minutes ago              peaceful_hellman
642de2c74d22   41cff62e047c                  "/bin/sh -c 'gunicor…"   13 minutes ago       Exited (0) 12 minutes ago             quizzical_chaplygin
bee0311a6bb3   bba8d2ee8f69                  "/bin/sh -c 'gunicor…"   14 minutes ago       Exited (0) 13 minutes ago             optimistic_wiles
b06b4bd3e8ba   bba8d2ee8f69                  "/bin/sh -c 'gunicor…"   15 minutes ago       Exited (0) 14 minutes ago             vigilant_rubin
67b1925bd665   a34109ecd6d4                  "/bin/sh -c 'gunicor…"   16 minutes ago       Exited (0) 15 minutes ago             brave_ptolemy
fc0b9d4eb5c2   25496cc28d2e                  "/bin/sh -c 'gunicor…"   18 minutes ago       Exited (3) 18 minutes ago             dazzling_nightingale
74d1d619c750   1cee8b9a9b1f                  "flask run"              22 minutes ago       Exited (0) 19 minutes ago             stoic_darwin
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
0fe7346863791c53fa1f1b6d181057d88a73a34a49f6524ced2a4a4ffc5fbddc
394ef7ba34670134c78c9e53cfdae53bf12728a1f9fff700fb5d6988c2d76e88
0eb39ef688918243abb4f7b93d48ec2571b66ae84979582d8074ace7d7e267bb
642de2c74d22043464cc91112958b82bc19db0e06115d9f2a841026c3b451f43
bee0311a6bb3c34992940a89492f59b0a7c2daf522376e48754b413c8eaedf14
b06b4bd3e8ba26e2d020e8d1d1d05603ad995dffce9c497e6ff5f0c07906722c
67b1925bd6657457f0f6828d994b185c9ea9ed42fc121d2faf7d2c9e5dc62ad8
fc0b9d4eb5c2597a88b573d7fb9155559e92266e78dd02918aa236d8b80d56a8
74d1d619c75012563fd67ebb16fde1793689fcd4ac76b9040663a241dfba9493

Total reclaimed space: 5.008MB
bradsimpson@Brads-MacBook-Air ~ % \clear






bradsimpson@Brads-MacBook-Air ~ % 












































bradsimpson@Brads-MacBook-Air ~ % docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
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

bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patchstagram   latest    6277c82a8b27   2 hours ago    113MB
<none>                        <none>    2a5eb398bf5e   2 hours ago    113MB
<none>                        <none>    1f5a7525d4a7   2 hours ago    113MB
<none>                        <none>    9dcd6c2141ad   2 hours ago    113MB
<none>                        <none>    41cff62e047c   2 hours ago    113MB
<none>                        <none>    bba8d2ee8f69   2 hours ago    113MB
<none>                        <none>    a34109ecd6d4   2 hours ago    113MB
<none>                        <none>    0de177ebe3ba   2 hours ago    113MB
<none>                        <none>    25496cc28d2e   2 hours ago    113MB
<none>                        <none>    1cee8b9a9b1f   2 hours ago    113MB
bradsimpson213/my_react_app   latest    0e6d1fad2b08   3 weeks ago    451MB
postgres                      latest    0344b98f56a6   7 weeks ago    433MB
bradsimpson213/taco_react     latest    aea6ddf0f44b   7 weeks ago    569MB
<none>                        <none>    df9580143a75   8 weeks ago    1.59GB
nginx                         alpine    66bf2c914bf4   2 months ago   41MB
alpine                        latest    5053b247d78b   2 months ago   7.66MB
nginx                         latest    2d21d843073b   2 months ago   192MB
ubuntu                        latest    cfb01e8e3121   2 months ago   69.2MB
hello-world                   latest    b038788ddb22   3 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run [-flags] image_name [commands]
zsh: no matches found: [-flags]
bradsimpson@Brads-MacBook-Air ~ % docker container run --name cool_container -p 8000:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/08/22 15:18:49 [notice] 1#1: using the "epoll" event method
2023/08/22 15:18:49 [notice] 1#1: nginx/1.25.1
2023/08/22 15:18:49 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2023/08/22 15:18:49 [notice] 1#1: OS: Linux 5.15.49-linuxkit-pr
2023/08/22 15:18:49 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/08/22 15:18:49 [notice] 1#1: start worker processes
2023/08/22 15:18:49 [notice] 1#1: start worker process 29
2023/08/22 15:18:49 [notice] 1#1: start worker process 30
2023/08/22 15:18:49 [notice] 1#1: start worker process 31
2023/08/22 15:18:49 [notice] 1#1: start worker process 32
172.17.0.1 - - [22/Aug/2023:15:19:18 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [22/Aug/2023:15:19:18 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
2023/08/22 15:19:18 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
172.17.0.1 - - [22/Aug/2023:15:19:37 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [22/Aug/2023:15:19:37 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [22/Aug/2023:15:19:38 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [22/Aug/2023:15:19:39 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [22/Aug/2023:15:19:39 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [22/Aug/2023:15:19:40 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
^C2023/08/22 15:20:06 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/08/22 15:20:06 [notice] 29#29: exiting
2023/08/22 15:20:06 [notice] 32#32: exiting
2023/08/22 15:20:06 [notice] 30#30: exiting
2023/08/22 15:20:06 [notice] 29#29: exit
2023/08/22 15:20:06 [notice] 30#30: exit
2023/08/22 15:20:06 [notice] 32#32: exit
2023/08/22 15:20:06 [notice] 31#31: exiting
2023/08/22 15:20:06 [notice] 31#31: exit
2023/08/22 15:20:06 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/08/22 15:20:06 [notice] 1#1: worker process 30 exited with code 0
2023/08/22 15:20:06 [notice] 1#1: worker process 31 exited with code 0
2023/08/22 15:20:06 [notice] 1#1: signal 29 (SIGIO) received
2023/08/22 15:20:06 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/08/22 15:20:06 [notice] 1#1: worker process 32 exited with code 0
2023/08/22 15:20:06 [notice] 1#1: signal 29 (SIGIO) received
2023/08/22 15:20:06 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2023/08/22 15:20:06 [notice] 1#1: worker process 29 exited with code 0
2023/08/22 15:20:06 [notice] 1#1: exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                      PORTS     NAMES
c8955f28c0c4   nginx         "/docker-entrypoint.…"   About a minute ago   Exited (0) 27 seconds ago             cool_container
7ee28eef80e7   hello-world   "/hello"                 14 minutes ago       Exited (0) 14 minutes ago             happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % \clear

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
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
c8955f28c0c4   nginx         "/docker-entrypoint.…"   5 minutes ago    Exited (0) 4 minutes ago              cool_container
7ee28eef80e7   hello-world   "/hello"                 18 minutes ago   Exited (0) 18 minutes ago             happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % docker container inspect cool_container
[
    {
        "Id": "c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4",
        "Created": "2023-08-22T15:18:48.98347375Z",
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
            "StartedAt": "2023-08-22T15:18:49.235885167Z",
            "FinishedAt": "2023-08-22T15:20:06.991604551Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4/hostname",
        "HostsPath": "/var/lib/docker/containers/c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4/hosts",
        "LogPath": "/var/lib/docker/containers/c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4/c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4-json.log",
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
                45,
                96
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
                "LowerDir": "/var/lib/docker/overlay2/3fabe1b2a8deb87f9ae677621b0374c847212b0ef5bcd784236ae7d323cafa82-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/3fabe1b2a8deb87f9ae677621b0374c847212b0ef5bcd784236ae7d323cafa82/merged",
                "UpperDir": "/var/lib/docker/overlay2/3fabe1b2a8deb87f9ae677621b0374c847212b0ef5bcd784236ae7d323cafa82/diff",
                "WorkDir": "/var/lib/docker/overlay2/3fabe1b2a8deb87f9ae677621b0374c847212b0ef5bcd784236ae7d323cafa82/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "c8955f28c0c4",
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
            "SandboxID": "4e195ac9f74cf934db4ae18dad3ab32d97d2d92d8b65925bccba69baa45d8278",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/4e195ac9f74c",
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
                    "NetworkID": "2e300c43b871ee0ba16d7e97ea70f7eb7898bfd1b6a9e89b1812169e81b74cf4",
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
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 5000:80 nginx
6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
6ebc7f23386b   nginx     "/docker-entrypoint.…"   17 seconds ago   Up 16 seconds   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container run --rm -it alpine ash
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd lib
/lib # \ls
apk                     libc.musl-aarch64.so.1  libz.so.1.2.13
firmware                libcrypto.so.3          mdev
ld-musl-aarch64.so.1    libssl.so.3             modules-load.d
libapk.so.2.14.0        libz.so.1               sysctl.d
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
/bin # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
6ebc7f23386b   nginx     "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
6ebc7f23386b   nginx         "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:5000->80/tcp   admiring_blackburn
c8955f28c0c4   nginx         "/docker-entrypoint.…"   12 minutes ago   Exited (0) 11 minutes ago                          cool_container
7ee28eef80e7   hello-world   "/hello"                 25 minutes ago   Exited (0) 25 minutes ago                          happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 8080:80 nginx
678ba78568e3c1fc77b511dc007f905feb37b222ad1ac0f845ef46ae90c9d4ac
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container run -it --name test alpine sh
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                      PORTS                  NAMES
d7bed0836e86   alpine        "sh"                     13 seconds ago       Exited (0) 7 seconds ago                           test
678ba78568e3   nginx         "/docker-entrypoint.…"   About a minute ago   Up About a minute           0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx         "/docker-entrypoint.…"   8 minutes ago        Up 8 minutes                0.0.0.0:5000->80/tcp   admiring_blackburn
c8955f28c0c4   nginx         "/docker-entrypoint.…"   16 minutes ago       Exited (0) 15 minutes ago                          cool_container
7ee28eef80e7   hello-world   "/hello"                 29 minutes ago       Exited (0) 29 minutes ago                          happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                          PORTS                  NAMES
d7bed0836e86   alpine        "sh"                     About a minute ago   Exited (0) About a minute ago                          test
678ba78568e3   nginx         "/docker-entrypoint.…"   3 minutes ago        Up 3 minutes                    0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx         "/docker-entrypoint.…"   10 minutes ago       Up 10 minutes                   0.0.0.0:5000->80/tcp   admiring_blackburn
c8955f28c0c4   nginx         "/docker-entrypoint.…"   18 minutes ago       Exited (0) 16 minutes ago                              cool_container
7ee28eef80e7   hello-world   "/hello"                 31 minutes ago       Exited (0) 31 minutes ago                              happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % \clear




bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
d7bed0836e86   alpine        "sh"                     2 minutes ago    Exited (0) 2 minutes ago                           test
678ba78568e3   nginx         "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx         "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes               0.0.0.0:5000->80/tcp   admiring_blackburn
c8955f28c0c4   nginx         "/docker-entrypoint.…"   19 minutes ago   Exited (0) 18 minutes ago                          cool_container
7ee28eef80e7   hello-world   "/hello"                 32 minutes ago   Exited (0) 32 minutes ago                          happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container stop admiring_blackburn 678ba78568e3
admiring_blackburn
678ba78568e3
bradsimpson@Brads-MacBook-Air ~ % docker container ls                                  
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
d7bed0836e86   alpine        "sh"                     4 minutes ago    Exited (0) 4 minutes ago              test
678ba78568e3   nginx         "/docker-entrypoint.…"   5 minutes ago    Exited (0) 20 seconds ago             condescending_gagarin
6ebc7f23386b   nginx         "/docker-entrypoint.…"   12 minutes ago   Exited (0) 20 seconds ago             admiring_blackburn
c8955f28c0c4   nginx         "/docker-entrypoint.…"   20 minutes ago   Exited (0) 19 minutes ago             cool_container
7ee28eef80e7   hello-world   "/hello"                 33 minutes ago   Exited (0) 33 minutes ago             happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % docker container start 678ba78568e3 admiring_blackburn
678ba78568e3
admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   6 minutes ago    Up 6 seconds   0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 6 seconds   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
d7bed0836e86   alpine        "sh"                     6 minutes ago    Exited (0) 5 minutes ago                           test
678ba78568e3   nginx         "/docker-entrypoint.…"   7 minutes ago    Up About a minute           0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx         "/docker-entrypoint.…"   14 minutes ago   Up About a minute           0.0.0.0:5000->80/tcp   admiring_blackburn
c8955f28c0c4   nginx         "/docker-entrypoint.…"   22 minutes ago   Exited (0) 21 minutes ago                          cool_container
7ee28eef80e7   hello-world   "/hello"                 35 minutes ago   Exited (0) 35 minutes ago                          happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % docker container rm happy_lumiere
happy_lumiere
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a           
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS                  NAMES
d7bed0836e86   alpine    "sh"                     6 minutes ago    Exited (0) 6 minutes ago                           test
678ba78568e3   nginx     "/docker-entrypoint.…"   7 minutes ago    Up About a minute           0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   15 minutes ago   Up About a minute           0.0.0.0:5000->80/tcp   admiring_blackburn
c8955f28c0c4   nginx     "/docker-entrypoint.…"   22 minutes ago   Exited (0) 21 minutes ago                          cool_container
bradsimpson@Brads-MacBook-Air ~ % docker container prune 
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
d7bed0836e865ea26f4aa299b1bf342374f7c038f1200037e90c4d0de3443cb6
c8955f28c0c4df3c538ab133ee3ea080665a633bf9e60afc5356219e22c937a4

Total reclaimed space: 1.098kB
bradsimpson@Brads-MacBook-Air ~ % docker image ls 
REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patchstagram   latest    6277c82a8b27   2 hours ago    113MB
<none>                        <none>    2a5eb398bf5e   2 hours ago    113MB
<none>                        <none>    1f5a7525d4a7   2 hours ago    113MB
<none>                        <none>    9dcd6c2141ad   2 hours ago    113MB
<none>                        <none>    41cff62e047c   2 hours ago    113MB
<none>                        <none>    bba8d2ee8f69   2 hours ago    113MB
<none>                        <none>    a34109ecd6d4   2 hours ago    113MB
<none>                        <none>    0de177ebe3ba   2 hours ago    113MB
<none>                        <none>    25496cc28d2e   2 hours ago    113MB
<none>                        <none>    1cee8b9a9b1f   3 hours ago    113MB
bradsimpson213/my_react_app   latest    0e6d1fad2b08   3 weeks ago    451MB
postgres                      latest    0344b98f56a6   7 weeks ago    433MB
bradsimpson213/taco_react     latest    aea6ddf0f44b   7 weeks ago    569MB
<none>                        <none>    df9580143a75   8 weeks ago    1.59GB
nginx                         alpine    66bf2c914bf4   2 months ago   41MB
alpine                        latest    5053b247d78b   2 months ago   7.66MB
nginx                         latest    2d21d843073b   2 months ago   192MB
ubuntu                        latest    cfb01e8e3121   2 months ago   69.2MB
hello-world                   latest    b038788ddb22   3 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker image prune 
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Deleted Images:
deleted: sha256:1cee8b9a9b1fcb98037ddc715f8621055b287ac855938b95aa968253808a6364
deleted: sha256:df9580143a753581b04a2a701b3eb3c78ba5baa20b7a178e9ebb81239cee2060
deleted: sha256:9dcd6c2141adcd3967d705b49717314d8ce941c07248760e59c9e2d1dbcee0ad
deleted: sha256:41cff62e047c0782cb4f33bdff25f37a287d1c7f2d9cdd635cd5c954556c1e27
deleted: sha256:2a5eb398bf5e0640bbb4f51ac387c308ec9824419b7680c0d542bfcb1fe4e47b
deleted: sha256:a34109ecd6d448906ee4976d9d6c5fd6565ea75a20fecdce6c3d1826bc39cabb
deleted: sha256:1f5a7525d4a719c4c0a780c15602e1b1cb2f09afc7968de1e3f4ccf2ef27cafb
deleted: sha256:bba8d2ee8f6976260ede36af614c1cf78db5de2461360f22960694c01e86b11e
deleted: sha256:25496cc28d2eb6173184365a30c449a4c3cfc8cd8a4b0a024d785c29ccc68005
deleted: sha256:0de177ebe3ba9b2315527fed900dadab1dbd8dc36fb5f04acb4a74ba61268103

Total reclaimed space: 0B
bradsimpson@Brads-MacBook-Air ~ % docker image ls    
REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patchstagram   latest    6277c82a8b27   2 hours ago    113MB
bradsimpson213/my_react_app   latest    0e6d1fad2b08   3 weeks ago    451MB
postgres                      latest    0344b98f56a6   7 weeks ago    433MB
bradsimpson213/taco_react     latest    aea6ddf0f44b   7 weeks ago    569MB
nginx                         alpine    66bf2c914bf4   2 months ago   41MB
alpine                        latest    5053b247d78b   2 months ago   7.66MB
nginx                         latest    2d21d843073b   2 months ago   192MB
ubuntu                        latest    cfb01e8e3121   2 months ago   69.2MB
hello-world                   latest    b038788ddb22   3 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker image prune 
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   17 minutes ago   Up 3 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it admiring_blackburn sh
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
# exit
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
2e300c43b871   bridge       bridge    local
0c4794c37db6   host         host      local
2be63f87cace   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % 


# NETWORKING

Last login: Tue Aug 22 11:49:49 on ttys076
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
2e300c43b871   bridge       bridge    local
0c4794c37db6   host         host      local
2be63f87cace   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 21 minutes   0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   34 minutes ago   Up 21 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container inspect  admiring_blackburn
[
    {
        "Id": "6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6",
        "Created": "2023-08-22T15:26:36.393606717Z",
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
            "Pid": 7118,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-08-22T15:40:09.320345593Z",
            "FinishedAt": "2023-08-22T15:38:57.645717213Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6/hostname",
        "HostsPath": "/var/lib/docker/containers/6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6/hosts",
        "LogPath": "/var/lib/docker/containers/6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6/6ebc7f23386b50f4316a817474c654231a91ce3a4106e55ec1f12d9518e608f6-json.log",
        "Name": "/admiring_blackburn",
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
                        "HostPort": "5000"
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
                45,
                96
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
                "LowerDir": "/var/lib/docker/overlay2/33f7be3b4ff2cfd50693a1f220a1894a8376a3342b51209eeebc8b2d7c15caa3-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/33f7be3b4ff2cfd50693a1f220a1894a8376a3342b51209eeebc8b2d7c15caa3/merged",
                "UpperDir": "/var/lib/docker/overlay2/33f7be3b4ff2cfd50693a1f220a1894a8376a3342b51209eeebc8b2d7c15caa3/diff",
                "WorkDir": "/var/lib/docker/overlay2/33f7be3b4ff2cfd50693a1f220a1894a8376a3342b51209eeebc8b2d7c15caa3/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "6ebc7f23386b",
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
            "SandboxID": "34cb130828ac69c0be238406839b8d44c9dfebdd972810468bb56e6c6175a68c",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5000"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/34cb130828ac",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "536f07788086f1369d742a9b320a16f980381d7f3f1eb80641475a5c56f7cc72",
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
                    "NetworkID": "2e300c43b871ee0ba16d7e97ea70f7eb7898bfd1b6a9e89b1812169e81b74cf4",
                    "EndpointID": "536f07788086f1369d742a9b320a16f980381d7f3f1eb80641475a5c56f7cc72",
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
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
2e300c43b871   bridge       bridge    local
0c4794c37db6   host         host      local
2be63f87cace   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
2e300c43b871   bridge       bridge    local
0c4794c37db6   host         host      local
2be63f87cace   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % docker network create --driver bridge taco_network
5bd45a71ad7349c1e15b22e54fe893b07cf3bb649debfc103e441ce454a09a64
bradsimpson@Brads-MacBook-Air ~ % docker network ls                                 
NETWORK ID     NAME           DRIVER    SCOPE
2e300c43b871   bridge         bridge    local
0c4794c37db6   host           host      local
2be63f87cace   my_network     bridge    local
61b3161ebf7d   none           null      local
5bd45a71ad73   taco_network   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
678ba78568e3   nginx     "/docker-entrypoint.…"   32 minutes ago   Up 25 minutes   0.0.0.0:8080->80/tcp   condescending_gagarin
6ebc7f23386b   nginx     "/docker-entrypoint.…"   39 minutes ago   Up 25 minutes   0.0.0.0:5000->80/tcp   admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container stop condescending_gagarin admiring_blackburn
condescending_gagarin
admiring_blackburn
bradsimpson@Brads-MacBook-Air ~ % docker container run --name c1 --network taco_network -d nginx:alpine
91eeb2088717ed2c33c88a94f173a32fc585a6c6ce2f287123ca66d8a98a9061
bradsimpson@Brads-MacBook-Air ~ % docker container run --name c2 --network taco_network -d nginx:alpine 
3ec4762a0b9f31e015627660afa88b9e93345b60b010fceb9555bdc493bf4275
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago    Up 3 seconds    80/tcp    c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   16 seconds ago   Up 15 seconds   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container run --name c3 -d nginx:alpine 
17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655
bradsimpson@Brads-MacBook-Air ~ % docker container run --name c4 -d nginx:alpine 
2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
2c54eda5fbf9   nginx:alpine   "/docker-entrypoint.…"   9 seconds ago    Up 7 seconds    80/tcp    c4
17eb423a61a7   nginx:alpine   "/docker-entrypoint.…"   15 seconds ago   Up 14 seconds   80/tcp    c3
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   42 seconds ago   Up 41 seconds   80/tcp    c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   54 seconds ago   Up 53 seconds   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c4
[
    {
        "Id": "2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890",
        "Created": "2023-08-22T16:09:03.867702716Z",
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
            "Pid": 11418,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-08-22T16:09:04.056676216Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/hostname",
        "HostsPath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/hosts",
        "LogPath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890-json.log",
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
                46,
                99
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
                "LowerDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7/merged",
                "UpperDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7/diff",
                "WorkDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "2c54eda5fbf9",
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
            "SandboxID": "2d9035c17c60eed02051ef9dc70fefd62d169276fa6e08f6dc14891e5ab5c7d9",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/2d9035c17c60",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "8a0277efb46bb6a8024acb7bdc229b1c6ce470500d50f9ba701ef7cb8a740939",
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
                    "NetworkID": "2e300c43b871ee0ba16d7e97ea70f7eb7898bfd1b6a9e89b1812169e81b74cf4",
                    "EndpointID": "8a0277efb46bb6a8024acb7bdc229b1c6ce470500d50f9ba701ef7cb8a740939",
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
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
2c54eda5fbf9   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
17eb423a61a7   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 ash
/ # ping -c 4 c2
PING c2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.531 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.190 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.259 ms
64 bytes from 172.18.0.3: seq=3 ttl=64 time=0.147 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.147/0.281/0.531 ms
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c3 ash 
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 172.17.0.3
ping: invalid number '172.17.0.3'
/ # ping -c 172.17.0.3
ping: invalid number '172.17.0.3'
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
2c54eda5fbf9   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c4
17eb423a61a7   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c3
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c3
[
    {
        "Id": "17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655",
        "Created": "2023-08-22T16:08:57.289262421Z",
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
            "Pid": 11296,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-08-22T16:08:57.478147838Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655/hostname",
        "HostsPath": "/var/lib/docker/containers/17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655/hosts",
        "LogPath": "/var/lib/docker/containers/17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655/17eb423a61a7678005f00c994eec32a62d9bfa032ed22333b9d61f7f2e566655-json.log",
        "Name": "/c3",
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
                46,
                99
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
                "LowerDir": "/var/lib/docker/overlay2/4ece3bae5e98f9b1530c636c6f51d3e514c58e7d24a953cb9cd9691d922c7067-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/4ece3bae5e98f9b1530c636c6f51d3e514c58e7d24a953cb9cd9691d922c7067/merged",
                "UpperDir": "/var/lib/docker/overlay2/4ece3bae5e98f9b1530c636c6f51d3e514c58e7d24a953cb9cd9691d922c7067/diff",
                "WorkDir": "/var/lib/docker/overlay2/4ece3bae5e98f9b1530c636c6f51d3e514c58e7d24a953cb9cd9691d922c7067/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "17eb423a61a7",
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
            "SandboxID": "26310ba9a6acdee7b794a087ac244e9737ebf680f362cb49f42edfa564310d76",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/26310ba9a6ac",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "0721d6b7d20e7914311f93b773cd3a5ac8a3c02c716d2a942dbd3812a40d880f",
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
                    "NetworkID": "2e300c43b871ee0ba16d7e97ea70f7eb7898bfd1b6a9e89b1812169e81b74cf4",
                    "EndpointID": "0721d6b7d20e7914311f93b773cd3a5ac8a3c02c716d2a942dbd3812a40d880f",
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
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c4 ash 
/ # ping -c 4 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.348 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.146 ms
64 bytes from 172.17.0.2: seq=2 ttl=64 time=0.134 ms
64 bytes from 172.17.0.2: seq=3 ttl=64 time=0.166 ms

--- 172.17.0.2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.134/0.198/0.348 ms
/ # ping -c 4 c3
ping: bad address 'c3'
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c4
[
    {
        "Id": "2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890",
        "Created": "2023-08-22T16:09:03.867702716Z",
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
            "Pid": 11418,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-08-22T16:09:04.056676216Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/hostname",
        "HostsPath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/hosts",
        "LogPath": "/var/lib/docker/containers/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890/2c54eda5fbf967f01e996353a8c6806461cee4954b0ee5251604dac41ebc3890-json.log",
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
                46,
                99
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
                "LowerDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7/merged",
                "UpperDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7/diff",
                "WorkDir": "/var/lib/docker/overlay2/2d1ad824f64c858b4983a8e823172149e7db494a3224a785056c1993cf0965e7/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "2c54eda5fbf9",
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
            "SandboxID": "2d9035c17c60eed02051ef9dc70fefd62d169276fa6e08f6dc14891e5ab5c7d9",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {

# BIND MOUNTS

/ # --mount type=bind/volume,source=path/to/folder or volume, target=path/in/container
ash: --mount: not found
/ # docker volume ls
ash: docker: not found
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker volume ls
DRIVER    VOLUME NAME
local     my_volume
local     taco_tuesday
bradsimpson@Brads-MacBook-Air ~ % docker volume prune
WARNING! This will remove anonymous local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B
bradsimpson@Brads-MacBook-Air ~ % docker volume ls   
DRIVER    VOLUME NAME
local     my_volume
local     taco_tuesday
bradsimpson@Brads-MacBook-Air ~ % docker volume rm taco_tuesday
taco_tuesday
bradsimpson@Brads-MacBook-Air ~ % docker volume ls             
DRIVER    VOLUME NAME
local     my_volume
bradsimpson@Brads-MacBook-Air ~ % docker volume rm my_volume   
my_volume
bradsimpson@Brads-MacBook-Air ~ % docker volume ls          
DRIVER    VOLUME NAME
bradsimpson@Brads-MacBook-Air ~ % docker volume create taco_tues
taco_tues
bradsimpson@Brads-MacBook-Air ~ % docker volume ls              
DRIVER    VOLUME NAME
local     taco_tues
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Library			Pictures		requirements.txt
Documents		Movies			Public
Downloads		Music			app
bradsimpson@Brads-MacBook-Air ~ % cd app
bradsimpson@Brads-MacBook-Air app % \ls     
index.html
bradsimpson@Brads-MacBook-Air app % nano index.html
bradsimpson@Brads-MacBook-Air app % cd ..
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Library			Pictures		requirements.txt
Documents		Movies			Public
Downloads		Music			app
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -d --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8000:80 nginx:alpine
f3687ce94ba8fa6b6ed4a5b791be909a371b71a7977ac902f203b161eb1a3963
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
f3687ce94ba8   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 5 seconds    0.0.0.0:8000->80/tcp   serene_darwin
2c54eda5fbf9   nginx:alpine   "/docker-entrypoint.…"   32 minutes ago   Up 32 minutes   80/tcp                 c4
17eb423a61a7   nginx:alpine   "/docker-entrypoint.…"   33 minutes ago   Up 33 minutes   80/tcp                 c3
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   33 minutes ago   Up 33 minutes   80/tcp                 c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   33 minutes ago   Up 33 minutes   80/tcp                 c1
bradsimpson@Brads-MacBook-Air ~ % docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@Brads-MacBook-Air ~ % docker container ls              
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
f3687ce94ba8   nginx:alpine   "/docker-entrypoint.…"   18 seconds ago   Up 17 seconds   0.0.0.0:8000->80/tcp   serene_darwin
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it serene_darwin ash
/ # \ls
bin                   home                  proc                  sys
dev                   lib                   root                  tmp
docker-entrypoint.d   media                 run                   usr
docker-entrypoint.sh  mnt                   sbin                  var
etc                   opt                   srv
/ # cd usr
/usr # \ls
bin    lib    local  sbin   share
/usr # cd share
/usr/share # cd nginx
/usr/share/nginx # cd html
/usr/share/nginx/html # \la
ash: la: not found
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index/html
ash: nano: not found
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/aarch64/APKINDEX.tar.gz
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 44 MiB in 63 packages
/usr/share/nginx/html # nano index/html
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
f3687ce94ba8   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   serene_darwin
bradsimpson@Brads-MacBook-Air ~ % cd app 
bradsimpson@Brads-MacBook-Air app % nano index.html
bradsimpson@Brads-MacBook-Air app % 
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
f3687ce94ba8   nginx:alpine   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:8000->80/tcp   serene_darwin
bradsimpson@Brads-MacBook-Air app % docker container stop serene_darwin
serene_darwin
bradsimpson@Brads-MacBook-Air app % docker container ls                
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % \clear

# VOLUMES


bradsimpson@Brads-MacBook-Air app % docker image ls
REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patchstagram   latest    6277c82a8b27   3 hours ago    113MB
bradsimpson213/my_react_app   latest    0e6d1fad2b08   3 weeks ago    451MB
postgres                      latest    0344b98f56a6   7 weeks ago    433MB
bradsimpson213/taco_react     latest    aea6ddf0f44b   7 weeks ago    569MB
nginx                         alpine    66bf2c914bf4   2 months ago   41MB
alpine                        latest    5053b247d78b   2 months ago   7.66MB
nginx                         latest    2d21d843073b   2 months ago   192MB
ubuntu                        latest    cfb01e8e3121   2 months ago   69.2MB
hello-world                   latest    b038788ddb22   3 months ago   9.14kB
bradsimpson@Brads-MacBook-Air app % docker image rm postgres  
Untagged: postgres:latest
Untagged: postgres@sha256:362a63cb1e864195ea2bc29b5066bdb222bc9a4461bfaff2418f63a06e56bce0
Deleted: sha256:0344b98f56a6e17873f7e37ee5cdc90d51bc172b2cbf7768419509ca3cce8d14
Deleted: sha256:3c587faf268cebef075306b661259e1d522435813e52672d8879ce968373df1e
Deleted: sha256:b9ec775547eff70d603477e5197461c8dd8f966d1809ae494880f6587324cd02
Deleted: sha256:49bf9c21272528ce846888241739eee9fdaf1c6af6a06e70b050b37b9ec49165
Deleted: sha256:a40f8ed8a245683cc01fb208c92c4a8aa1fe049d85db392a0c8871d9501de0fe
Deleted: sha256:2fbcdacd5e0106e44ee809f0d46d607e6f7a3fff876e2294dbe328f69163fa1d
Deleted: sha256:70d8f900c1da18418398dc50fc4ee718b8f4d9d28b6ee8587fc2fcee6175b1d2
Deleted: sha256:d5fa27a4f01480a15c7f267824a258d04c393b60325f7a691eb7f49109f14950
Deleted: sha256:cf375d1e4d034ccdaddfb8da181ce937cf0ad2b0717fc66a2165dc78ef7f0864
Deleted: sha256:69cfc0ef48a7251a291c2d9d070d9fc7a3f59a2e54a28984a503ffa7f8537e2e
Deleted: sha256:be5524e8ee45c8e932e42367b0d276f235a6b03825cb79202a1adf1600c0f3e4
Deleted: sha256:991985db7d9bee3b37c7f53250c57c53388af49019a8861abe61d72a3d3a3f0e
Deleted: sha256:ad1d6d47ecad672fe218db22529462c12fd8c540862dcff960a524db5454cf24
Deleted: sha256:efd1965f1684506744544d66c57387a60bd89607480e2dbc89bf3e8a30081bc1
bradsimpson@Brads-MacBook-Air app % docker image ls         
REPOSITORY                    TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patchstagram   latest    6277c82a8b27   3 hours ago    113MB
bradsimpson213/my_react_app   latest    0e6d1fad2b08   3 weeks ago    451MB
bradsimpson213/taco_react     latest    aea6ddf0f44b   7 weeks ago    569MB
nginx                         alpine    66bf2c914bf4   2 months ago   41MB
alpine                        latest    5053b247d78b   2 months ago   7.66MB
nginx                         latest    2d21d843073b   2 months ago   192MB
ubuntu                        latest    cfb01e8e3121   2 months ago   69.2MB
hello-world                   latest    b038788ddb22   3 months ago   9.14kB
bradsimpson@Brads-MacBook-Air app % docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
4ee097f9a366: Pull complete 
76feac26ff4c: Pull complete 
cd38eeb1c7ed: Pull complete 
c5a6aa48270c: Pull complete 
8400a13ec8f7: Pull complete 
0bddf18c4a6e: Pull complete 
287cdab72fa1: Pull complete 
d55736c8451f: Pull complete 
d84639c1fc9e: Pull complete 
a7a76ec02575: Pull complete 
b0c360759201: Pull complete 
118910365168: Pull complete 
f6a1c2f3f6a0: Pull complete 
Digest: sha256:a5e89e5f2679863bedef929c4a7ec5d1a2cb3c045f13b47680d86f8701144ed7
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@Brads-MacBook-Air app % docker image inspect postgres
[
    {
        "Id": "sha256:ee56d70bcdf1aeca472a9899de653eb4d72f4a3ac31d9b0b95e677488ce766f3",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:a5e89e5f2679863bedef929c4a7ec5d1a2cb3c045f13b47680d86f8701144ed7"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-08-16T06:40:57.929475525Z",
        "Container": "850331b21eb942e9dad178c06146950af0dbe9b0794213e3fa9306637db74286",
        "ContainerConfig": {
            "Hostname": "850331b21eb9",
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
                "GOSU_VERSION=1.16",
                "LANG=en_US.utf8",
                "PG_MAJOR=15",
                "PG_VERSION=15.4-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:92c6e333aa36edb1932ac4198c20f986e32ad86ebd3c71bac7005ce622a6412c",
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
                "5432/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/15/bin",
                "GOSU_VERSION=1.16",
                "LANG=en_US.utf8",
                "PG_MAJOR=15",
                "PG_VERSION=15.4-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:92c6e333aa36edb1932ac4198c20f986e32ad86ebd3c71bac7005ce622a6412c",
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
        "Architecture": "arm64",
        "Variant": "v8",
        "Os": "linux",
        "Size": 433237434,
        "VirtualSize": 433237434,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/19c2c0fd488f257ec64ccf2debc443f8d7b2fb51b6b424507b12dad8ceced5a2/diff:/var/lib/docker/overlay2/720cfe7bbf41f9167a5fd897387c047d1bd0b0788cbc76be818c124b40b9a2fc/diff:/var/lib/docker/overlay2/9ef2f2492f5d7b33f6842bcaa73544a5827441b370d59019178746eecc897887/diff:/var/lib/docker/overlay2/098e106cd4ce7d71eea1122353cfa08e6521f041a813df4e610aaa7db533fd44/diff:/var/lib/docker/overlay2/b524502fc40aece8a126f52872ffccdf33c8fd18eeb9896a73bbd37015162ce5/diff:/var/lib/docker/overlay2/82809c2f97a7559d2fc6bdd9ed979c89ddb5c62f689ca8dd8434aad7640f3cef/diff:/var/lib/docker/overlay2/2fd26a6716c4892966fdd7caf05ae2642c03c3e2c9cbc5afab58dd380bd5c4ee/diff:/var/lib/docker/overlay2/7651afd27ca6e197a766ffec66f5b77825ff7a28995c07ae0c878b9c3adde831/diff:/var/lib/docker/overlay2/033e377d2a69f2b5d8db1c9d16b65c47942292f658e8f72e06acf41007c25880/diff:/var/lib/docker/overlay2/494c1f85e9803b52bc30144d2937350c16dd654a3006dbe4a5d729497e0f72f6/diff:/var/lib/docker/overlay2/c18e7cdc5c90c2494b09769891c51c5f39fc475fc11a79c21493f1baa3beb564/diff:/var/lib/docker/overlay2/b0b9235892d66406d3e465349a8d3bb35f2f913af34c6ee5b5ea35da390ceb0c/diff",
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
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % 
bradsimpson@Brads-MacBook-Air app % docker container run --name postgres1 -d --mount type=volume,source=taco_tues,target=/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres 
970f2b0173315d53d911598e1a7dcb3c8602a601d082b16b632590d5597c427d
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS      NAMES
970f2b017331   postgres   "docker-entrypoint.s…"   5 seconds ago   Up 4 seconds   5432/tcp   postgres1
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres1 ash
OCI runtime exec failed: exec failed: unable to start container process: exec: "ash": executable file not found in $PATH: unknown
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres1    
"docker container exec" requires at least 2 arguments.
See 'docker container exec --help'.

Usage:  docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]

Execute a command in a running container
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres1 sh  
# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access p
rivileges   
-----------+----------+----------+------------+------------+------------+-----------------+-----------
------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgre
s          +
           |          |          |            |            |            |                 | postgres=C
Tc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgre
s          +
           |          |          |            |            |            |                 | postgres=C
Tc/postgres
(3 rows)






























postgres=# CREATE DATABASE taco_tuesday WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                                  List of databases
     Name     |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Acces
s privileges   
--------------+----------+----------+------------+------------+------------+-----------------+--------
---------------
 postgres     | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/post
gres          +
              |          |          |            |            |            |                 | postgre
s=CTc/postgres
 template1    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/post
gres          +
              |          |          |            |            |            |                 | postgre
s=CTc/postgres
(4 rows)





























postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS      NAMES
970f2b017331   postgres   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   5432/tcp   postgres1
bradsimpson@Brads-MacBook-Air app % docker container stop postgres1
postgres1
bradsimpson@Brads-MacBook-Air app % docker container ls            
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                      PORTS     NAMES
970f2b017331   postgres       "docker-entrypoint.s…"   3 minutes ago       Exited (0) 7 seconds ago              postgres1
f3687ce94ba8   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago      Exited (0) 10 minutes ago             serene_darwin
2c54eda5fbf9   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 16 minutes ago             c4
17eb423a61a7   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 16 minutes ago             c3
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 16 minutes ago             c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 16 minutes ago             c1
678ba78568e3   nginx          "/docker-entrypoint.…"   About an hour ago   Exited (0) 52 minutes ago             condescending_gagarin
6ebc7f23386b   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) 52 minutes ago             admiring_blackburn
bradsimpson@Brads-MacBook-Air app % docker container rm postgres1
postgres1
bradsimpson@Brads-MacBook-Air app % docker container ls -a       
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                      PORTS     NAMES
f3687ce94ba8   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago      Exited (0) 10 minutes ago             serene_darwin
2c54eda5fbf9   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 17 minutes ago             c4
17eb423a61a7   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 17 minutes ago             c3
3ec4762a0b9f   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago      Exited (0) 17 minutes ago             c2
91eeb2088717   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago      Exited (0) 17 minutes ago             c1
678ba78568e3   nginx          "/docker-entrypoint.…"   About an hour ago   Exited (0) 53 minutes ago             condescending_gagarin
6ebc7f23386b   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) 53 minutes ago             admiring_blackburn
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker container run --name postgres2 -d --mount type=volume,source=taco_tues,target=/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres
5a34dd6b17070964ec561967ecc6886de462746c5e4e01e125a7d2a1cc24ecb8
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS      NAMES
5a34dd6b1707   postgres   "docker-entrypoint.s…"   4 seconds ago   Up 4 seconds   5432/tcp   postgres2
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres2 sh
# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                  List of databases
     Name     |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Acces
s privileges   
--------------+----------+----------+------------+------------+------------+-----------------+--------
---------------
 postgres     | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/post
gres          +
              |          |          |            |            |            |                 | postgre
s=CTc/postgres
 template1    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/post
gres          +
              |          |          |            |            |            |                 | postgre
s=CTc/postgres
(4 rows)





























postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % 

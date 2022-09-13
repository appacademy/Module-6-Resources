Last login: Tue Sep 13 09:55:52 on ttys008

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
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

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
e6246a6e7570   hello-world   "/hello"   2 minutes ago   Exited (0) 2 minutes ago             stoic_sinoussi

impson@ ~:docker container run --name my_nginx -d -p 8000:80 nginx 
9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
9029dde2a87c   nginx     "/docker-entrypoint.…"   9 seconds ago   Up 8 seconds   0.0.0.0:8000->80/tcp, :::8000->80/tcp   my_nginx
bradsimpson@ ~:docker container stop 9029dde2a87c
9029dde2a87c
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
9029dde2a87c   nginx         "/docker-entrypoint.…"   2 minutes ago    Exited (0) 42 seconds ago             my_nginx
e6246a6e7570   hello-world   "/hello"                 31 minutes ago   Exited (0) 31 minutes ago             stoic_sinoussi
bradsimpson@ ~:docker container run -p 8000:80 --rm nginx 
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2022/09/13 15:37:32 [notice] 1#1: using the "epoll" event method
2022/09/13 15:37:32 [notice] 1#1: nginx/1.21.6
2022/09/13 15:37:32 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2022/09/13 15:37:32 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2022/09/13 15:37:32 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/09/13 15:37:32 [notice] 1#1: start worker processes
2022/09/13 15:37:32 [notice] 1#1: start worker process 32
2022/09/13 15:37:32 [notice] 1#1: start worker process 33
172.17.0.1 - - [13/Sep/2022:15:38:12 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [13/Sep/2022:15:38:21 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
2022/09/13 15:39:07 [notice] 1#1: signal 3 (SIGQUIT) received, shutting down
2022/09/13 15:39:07 [notice] 33#33: gracefully shutting down
2022/09/13 15:39:07 [notice] 32#32: gracefully shutting down
2022/09/13 15:39:07 [notice] 32#32: exiting
2022/09/13 15:39:07 [notice] 32#32: exit
2022/09/13 15:39:07 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2022/09/13 15:39:07 [notice] 1#1: worker process 32 exited with code 0
2022/09/13 15:39:07 [notice] 1#1: signal 29 (SIGIO) received
2022/09/13 15:39:12 [notice] 33#33: exiting
2022/09/13 15:39:12 [notice] 33#33: exit
2022/09/13 15:39:12 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2022/09/13 15:39:12 [notice] 1#1: worker process 33 exited with code 0
2022/09/13 15:39:12 [notice] 1#1: exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
9029dde2a87c   nginx         "/docker-entrypoint.…"   8 minutes ago    Exited (0) 6 minutes ago              my_nginx
e6246a6e7570   hello-world   "/hello"                 37 minutes ago   Exited (0) 37 minutes ago             stoic_sinoussi
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:docker container run -it --name test_it alpine sh
/ # ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd bin
/bin # \ls
arch           echo           kill           mv             setserial
ash            ed             link           netstat        sh
base64         egrep          linux32        nice           sleep
bbconfig       false          linux64        pidof          stat
busybox        fatattr        ln             ping           stty
cat            fdflush        login          ping6          su
chattr         fgrep          ls             pipe_progress  sync
chgrp          fsync          lsattr         printenv       tar
chmod          getopt         lzop           ps             touch
chown          grep           makemime       pwd            true
cp             gunzip         mkdir          reformime      umount
date           gzip           mknod          rev            uname
dd             hostname       mktemp         rm             usleep
df             ionice         more           rmdir          watch
dmesg          iostat         mount          run-parts      zcat
dnsdomainname  ipcalc         mountpoint     sed
dumpkmap       kbd_mode       mpstat         setpriv
/bin # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
c6e2e667baef   alpine        "sh"                     2 minutes ago    Exited (0) 39 seconds ago             test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   13 minutes ago   Exited (0) 11 minutes ago             my_nginx
e6246a6e7570   hello-world   "/hello"                 42 minutes ago   Exited (0) 42 minutes ago             stoic_sinoussi
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
c6e2e667baef   alpine        "sh"                     3 minutes ago    Exited (0) 46 seconds ago             test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   13 minutes ago   Exited (0) 11 minutes ago             my_nginx
e6246a6e7570   hello-world   "/hello"                 42 minutes ago   Exited (0) 42 minutes ago             stoic_sinoussi
bradsimpson@ ~:docker container inspect test_it
[
    {
        "Id": "c6e2e667baef226d589d66d25dc30570b99854b2d78696749630cdd5852e5c49",
        "Created": "2022-09-13T15:42:53.690783536Z",
        "Path": "sh",
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
            "StartedAt": "2022-09-13T15:42:54.374451192Z",
            "FinishedAt": "2022-09-13T15:45:09.128708806Z"
        },
        "Image": "sha256:e66264b98777e12192600bf9b4d663655c98a090072e1bab49e233d7531d1294",
        "ResolvConfPath": "/var/lib/docker/containers/c6e2e667baef226d589d66d25dc30570b99854b2d78696749630cdd5852e5c49/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/c6e2e667baef226d589d66d25dc30570b99854b2d78696749630cdd5852e5c49/hostname",
        "HostsPath": "/var/lib/docker/containers/c6e2e667baef226d589d66d25dc30570b99854b2d78696749630cdd5852e5c49/hosts",
        "LogPath": "/var/lib/docker/containers/c6e2e667baef226d589d66d25dc30570b99854b2d78696749630cdd5852e5c49/c6e2e667baef226d589d66d25dc30570b99854b2d78696749630cdd5852e5c49-json.log",
        "Name": "/test_it",
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
                "LowerDir": "/var/lib/docker/overlay2/791af53be7f479b5156a0a43a20c586c0faaf4c7ba73841feb2ae94aa81eaf64-init/diff:/var/lib/docker/overlay2/3f1c8d74fe34fa48885ff511520a5e51ccf48761b02fea56d929b5dc00893e7c/diff",
                "MergedDir": "/var/lib/docker/overlay2/791af53be7f479b5156a0a43a20c586c0faaf4c7ba73841feb2ae94aa81eaf64/merged",
                "UpperDir": "/var/lib/docker/overlay2/791af53be7f479b5156a0a43a20c586c0faaf4c7ba73841feb2ae94aa81eaf64/diff",
                "WorkDir": "/var/lib/docker/overlay2/791af53be7f479b5156a0a43a20c586c0faaf4c7ba73841feb2ae94aa81eaf64/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "c6e2e667baef",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "sh"
            ],
            "Image": "alpine",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "61b5f92cc33efa797a5d3709bc804679371e5935361cc711e4894cd49662bf40",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/61b5f92cc33e",
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
                    "NetworkID": "282442d7b6e8b14588afc2eeaf0a0831ae4949db117e3401da0bed7da63e1851",
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
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
c6e2e667baef   alpine        "sh"                     7 minutes ago    Exited (0) 5 minutes ago              test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   18 minutes ago   Exited (0) 16 minutes ago             my_nginx
e6246a6e7570   hello-world   "/hello"                 47 minutes ago   Exited (0) 47 minutes ago             stoic_sinoussi
bradsimpson@ ~:docker container inspect my_nginx
[
    {
        "Id": "9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be",
        "Created": "2022-09-13T15:32:27.222588658Z",
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
            "StartedAt": "2022-09-13T15:32:28.378685516Z",
            "FinishedAt": "2022-09-13T15:34:06.500337337Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be/hostname",
        "HostsPath": "/var/lib/docker/containers/9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be/hosts",
        "LogPath": "/var/lib/docker/containers/9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be/9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be-json.log",
        "Name": "/my_nginx",
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
                "LowerDir": "/var/lib/docker/overlay2/45b6d22184b7943760117ac328bc08f462375e4b7eaf44885864a0ba7d5fa2bf-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/45b6d22184b7943760117ac328bc08f462375e4b7eaf44885864a0ba7d5fa2bf/merged",
                "UpperDir": "/var/lib/docker/overlay2/45b6d22184b7943760117ac328bc08f462375e4b7eaf44885864a0ba7d5fa2bf/diff",
                "WorkDir": "/var/lib/docker/overlay2/45b6d22184b7943760117ac328bc08f462375e4b7eaf44885864a0ba7d5fa2bf/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "9029dde2a87c",
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
            "SandboxID": "3a4bd42fbb23cc8533c3591827d30267cdf07ffac3b164628831ed24bb91a973",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/3a4bd42fbb23",
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
                    "NetworkID": "282442d7b6e8b14588afc2eeaf0a0831ae4949db117e3401da0bed7da63e1851",
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
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
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

bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:docker image inspect postgres
[
    {
        "Id": "sha256:5b21e2e86aab1630251ecfb5d0d715634c0965931e8f5ab5d2dc6bce3aeb92fa",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:2d1e636f07781d4799b3f2edbff78a0a5494f24c4512cb56a83ebfd0e04ec074"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-05-28T11:51:18.200535542Z",
        "Container": "7a9823308ba16b9130ca8fad574ed79edbfa4f8713671bb6eae81983195c02ca",
        "ContainerConfig": {
            "Hostname": "7a9823308ba1",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.3-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:906a82f7fa1bd09c76b61109cdb36b7595d6322952cae6be8b5ea3fa887ee303",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.3-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:906a82f7fa1bd09c76b61109cdb36b7595d6322952cae6be8b5ea3fa887ee303",
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
        "Size": 376123192,
        "VirtualSize": 376123192,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/b642eb8696e4e27eb0bb0d12f52a4eea2ad1fdb16f686051d027b9eb16a3b63c/diff:/var/lib/docker/overlay2/77a63f3f4ee039a568146d6a9434532507fe315f821f81f143f8f089300ded0e/diff:/var/lib/docker/overlay2/0886ea31cb0054e29f26aa85d54bdbf0d46b9cc4dadfb1cf3910f36fb5574f45/diff:/var/lib/docker/overlay2/28e11608521227763164316ab06300958fd21a416134ceb40ffd437e5636fb1d/diff:/var/lib/docker/overlay2/1faf7363256b6ff44fb5b0c7b1b4ea74f24680000accca8ba098ebdc5cd2267f/diff:/var/lib/docker/overlay2/9d1037fda7fe805571f54031a2613f8f5e23c80aa2542b697523ee8cd44595a0/diff:/var/lib/docker/overlay2/3991c0b8cc10bf3a2f41bb8f9783d1227c235a4a3a6c47ddd12312fdb9a3bb83/diff:/var/lib/docker/overlay2/9696cf2539d58ee0228008050c1f30ff5f6776f582e1e4034ebb8dc44ae365ae/diff:/var/lib/docker/overlay2/88f713a38a34f2055b2b4d42e93f058de3e99ebc683b5a1aaa4ce933334fc578/diff:/var/lib/docker/overlay2/6407585b7c5e83b411bb15d8f9e65f00caeea5a55580d3e59f3a190f7b589a78/diff:/var/lib/docker/overlay2/9cbf8941166293e7b9a1b66844eecaa477fc9c2ebb7d74c4a6949759fd4f6f81/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/8a262f13606e4c24ba394895d96c9960873aeca5b1ce7ec15ff04d74d0135bdf/merged",
                "UpperDir": "/var/lib/docker/overlay2/8a262f13606e4c24ba394895d96c9960873aeca5b1ce7ec15ff04d74d0135bdf/diff",
                "WorkDir": "/var/lib/docker/overlay2/8a262f13606e4c24ba394895d96c9960873aeca5b1ce7ec15ff04d74d0135bdf/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ad6562704f3759fb50f0d3de5f80a38f65a85e709b77fd24491253990f30b6be",
                "sha256:8fa5e671e66543c8b567bb6c76364322fddf4fff0daa487178a8caefc61f52f4",
                "sha256:81c2fe13a1f0bde53c09587480446c5b38cb33064beef504215d394799107dae",
                "sha256:287d777006b9b6673406327c7099b0b20cc5f5421db91663a4bea0c1fd23a98a",
                "sha256:69feeba6d5b01eea6edc5fe0dcae6ab79935f7428d42143c7bb25552eb06c33b",
                "sha256:1b67a9cd52150ec147f84bc854737f12868081f76791dac23114f3a254c18580",
                "sha256:1ff3ceb3f41434dbf6b5beef16ce094242663ac5ddc5b92a3fd73a0d44eafead",
                "sha256:32e442eaf90910f2f058de7e6ff4148361407dc59034a8410f26ea54af19af01",
                "sha256:5cad0059a27d804a2cfd5ce5af4163e5ad85f81817222489177d38de12859f41",
                "sha256:88e235c6b97504282831b44d9e69a79e88fcb4c72b73f38e5f31eeb9df47f56e",
                "sha256:edf7a92c1e15438484ad490543a86936a2b94f14624364ec4a189bfadc408fb8",
                "sha256:8e43b491d5d4c69edb04aa526487a358afb3b51d805ca4bc059ab05411050af1",
                "sha256:8b44e3129736d85abec3a86be4807b2ca3f4a5b35d4da41403a6f07e89567ae6"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run --name nginx_alec -p 8080:80 -d nginx
81a751d149c88960b4136971a4e1983aad1b130886074684a97ea0dc691c004b
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
81a751d149c8   nginx     "/docker-entrypoint.…"   20 seconds ago   Up 18 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container run -it --name test_jason alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS              PORTS                                   NAMES
81a751d149c8   nginx     "/docker-entrypoint.…"   2 minutes ago   Up About a minute   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                                   NAMES
e98c726244fb   alpine        "sh"                     15 seconds ago   Exited (0) 6 seconds ago                                            test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
c6e2e667baef   alpine        "sh"                     16 minutes ago   Exited (0) 14 minutes ago                                           test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   27 minutes ago   Exited (0) 25 minutes ago                                           my_nginx
e6246a6e7570   hello-world   "/hello"                 56 minutes ago   Exited (0) 56 minutes ago                                           stoic_sinoussi
bradsimpson@ ~:docker container run --rm --name great_me_tyler ubuntu echo hello world
hello world
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                                   NAMES
e98c726244fb   alpine        "sh"                     3 minutes ago    Exited (0) 3 minutes ago                                            test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
c6e2e667baef   alpine        "sh"                     19 minutes ago   Exited (0) 17 minutes ago                                           test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   30 minutes ago   Exited (0) 28 minutes ago                                           my_nginx
e6246a6e7570   hello-world   "/hello"                 59 minutes ago   Exited (0) 59 minutes ago                                           stoic_sinoussi
bradsimpson@ ~:docker container run --name great_me_tyler ubuntu echo hello world
hello world
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                                   NAMES
308afa9fe77c   ubuntu        "echo hello world"       17 seconds ago   Exited (0) 16 seconds ago                                           great_me_tyler
e98c726244fb   alpine        "sh"                     4 minutes ago    Exited (0) 4 minutes ago                                            test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
c6e2e667baef   alpine        "sh"                     20 minutes ago   Exited (0) 18 minutes ago                                           test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   30 minutes ago   Exited (0) 29 minutes ago                                           my_nginx
e6246a6e7570   hello-world   "/hello"                 59 minutes ago   Exited (0) 59 minutes ago                                           stoic_sinoussi
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
81a751d149c8   nginx     "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                          PORTS                                   NAMES
308afa9fe77c   ubuntu        "echo hello world"       About a minute ago   Exited (0) About a minute ago                                           great_me_tyler
e98c726244fb   alpine        "sh"                     5 minutes ago        Exited (0) 5 minutes ago                                                test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   7 minutes ago        Up 7 minutes                    0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
c6e2e667baef   alpine        "sh"                     21 minutes ago       Exited (0) 19 minutes ago                                               test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   32 minutes ago       Exited (0) 30 minutes ago                                               my_nginx
e6246a6e7570   hello-world   "/hello"                 About an hour ago    Exited (0) About an hour ago                                            stoic_sinoussi
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:\clear



bradsimpson@ ~:docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
282442d7b6e8   bridge    bridge    local
7318efe60d0f   host      host      local
475754f27665   none      null      local
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS                                   NAMES
308afa9fe77c   ubuntu        "echo hello world"       3 minutes ago       Exited (0) 3 minutes ago                                               great_me_tyler
e98c726244fb   alpine        "sh"                     6 minutes ago       Exited (0) 6 minutes ago                                               test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   8 minutes ago       Up 8 minutes                   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
c6e2e667baef   alpine        "sh"                     23 minutes ago      Exited (0) 20 minutes ago                                              test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   33 minutes ago      Exited (0) 32 minutes ago                                              my_nginx
e6246a6e7570   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago                                           stoic_sinoussi
bradsimpson@ ~:echo hey all
hey all
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
81a751d149c8   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container stop nginx_alec
nginx_alec
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear












bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS     NAMES
308afa9fe77c   ubuntu        "echo hello world"       4 minutes ago       Exited (0) 4 minutes ago                 great_me_tyler
e98c726244fb   alpine        "sh"                     8 minutes ago       Exited (0) 8 minutes ago                 test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   10 minutes ago      Exited (0) 14 seconds ago                nginx_alec
c6e2e667baef   alpine        "sh"                     24 minutes ago      Exited (0) 22 minutes ago                test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   35 minutes ago      Exited (0) 33 minutes ago                my_nginx
e6246a6e7570   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago             stoic_sinoussi
bradsimpson@ ~:docker container start great_me_tyler
great_me_tyler
bradsimpson@ ~:docker container start nginx_alec
nginx_alec
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
81a751d149c8   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 8 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container stop nginx_alec
nginx_alec
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS     NAMES
308afa9fe77c   ubuntu        "echo hello world"       8 minutes ago       Exited (0) 3 minutes ago                 great_me_tyler
e98c726244fb   alpine        "sh"                     12 minutes ago      Exited (0) 12 minutes ago                test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   14 minutes ago      Exited (0) 6 seconds ago                 nginx_alec
c6e2e667baef   alpine        "sh"                     28 minutes ago      Exited (0) 26 minutes ago                test_it
9029dde2a87c   nginx         "/docker-entrypoint.…"   39 minutes ago      Exited (0) 37 minutes ago                my_nginx
e6246a6e7570   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago             stoic_sinoussi
bradsimpson@ ~:docker container remove test_it

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  inspect     Display detailed information on one or more containers
  kill        Kill one or more running containers
  logs        Fetch the logs of a container
  ls          List containers
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all stopped containers
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  run         Run a command in a new container
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
bradsimpson@ ~:docker container re\clear

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  inspect     Display detailed information on one or more containers
  kill        Kill one or more running containers
  logs        Fetch the logs of a container
  ls          List containers
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all stopped containers
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  run         Run a command in a new container
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container rm test_it
test_it
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                          PORTS     NAMES
308afa9fe77c   ubuntu        "echo hello world"       9 minutes ago       Exited (0) 4 minutes ago                  great_me_tyler
e98c726244fb   alpine        "sh"                     13 minutes ago      Exited (0) 13 minutes ago                 test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   15 minutes ago      Exited (0) About a minute ago             nginx_alec
9029dde2a87c   nginx         "/docker-entrypoint.…"   40 minutes ago      Exited (0) 38 minutes ago                 my_nginx
e6246a6e7570   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago              stoic_sinoussi
bradsimpson@ ~:docker container inspect test_jason
[
    {
        "Id": "e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9",
        "Created": "2022-09-13T15:59:15.180538821Z",
        "Path": "sh",
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
            "StartedAt": "2022-09-13T15:59:15.820511249Z",
            "FinishedAt": "2022-09-13T15:59:24.319563597Z"
        },
        "Image": "sha256:e66264b98777e12192600bf9b4d663655c98a090072e1bab49e233d7531d1294",
        "ResolvConfPath": "/var/lib/docker/containers/e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9/hostname",
        "HostsPath": "/var/lib/docker/containers/e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9/hosts",
        "LogPath": "/var/lib/docker/containers/e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9/e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9-json.log",
        "Name": "/test_jason",
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
                "LowerDir": "/var/lib/docker/overlay2/2e14a62bda047e5c6b825070d0d9a48637f353cac824a1d1f661463885149800-init/diff:/var/lib/docker/overlay2/3f1c8d74fe34fa48885ff511520a5e51ccf48761b02fea56d929b5dc00893e7c/diff",
                "MergedDir": "/var/lib/docker/overlay2/2e14a62bda047e5c6b825070d0d9a48637f353cac824a1d1f661463885149800/merged",
                "UpperDir": "/var/lib/docker/overlay2/2e14a62bda047e5c6b825070d0d9a48637f353cac824a1d1f661463885149800/diff",
                "WorkDir": "/var/lib/docker/overlay2/2e14a62bda047e5c6b825070d0d9a48637f353cac824a1d1f661463885149800/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "e98c726244fb",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "sh"
            ],
            "Image": "alpine",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "de1424bc42cefeff0495bb1cd9ac7ee3b1e7598b3e7fd276b38f1bbc7d381652",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/de1424bc42ce",
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
                    "NetworkID": "282442d7b6e8b14588afc2eeaf0a0831ae4949db117e3401da0bed7da63e1851",
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
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS     NAMES
308afa9fe77c   ubuntu        "echo hello world"       11 minutes ago      Exited (0) 6 minutes ago                 great_me_tyler
e98c726244fb   alpine        "sh"                     15 minutes ago      Exited (0) 15 minutes ago                test_jason
81a751d149c8   nginx         "/docker-entrypoint.…"   17 minutes ago      Exited (0) 2 minutes ago                 nginx_alec
9029dde2a87c   nginx         "/docker-entrypoint.…"   42 minutes ago      Exited (0) 40 minutes ago                my_nginx
e6246a6e7570   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago             stoic_sinoussi
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
308afa9fe77c1dbbc92f638ec8c81af8636f38da22df5087676de6f0062c084b
e98c726244fbdd5780c3998e1eac982cee58dc3893170595edd14dd9282646d9
81a751d149c88960b4136971a4e1983aad1b130886074684a97ea0dc691c004b
9029dde2a87cc96b6f0dafadf56ea218dc327dff7e596fbea0768ac8a805c7be
e6246a6e75703b904024caaf7c250c5d52c27a271bacecd50511f64c6a935306

Total reclaimed space: 2.195kB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run --name nginx_alec -p 8080:80 -d nginx
39f7e15821430ca40db0765ad2266be746860bb90049fbf8673940147710cdc0
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
39f7e1582143   nginx     "/docker-entrypoint.…"   7 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container exec -it nginx_alec
"docker container exec" requires at least 2 arguments.
See 'docker container exec --help'.

Usage:  docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container
bradsimpson@ ~:docker container exec -it nginx_alec sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# exit

Last login: Tue Sep 13 11:38:02 on ttys009

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\clear











































bradsimpson@ ~:docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
282442d7b6e8   bridge    bridge    local
7318efe60d0f   host      host      local
475754f27665   none      null      local
bradsimpson@ ~:docker network create --driver bridge my_network
1a584f63c88c0ec2e6cac2118a00164789037a534529282e1bad9260e2c7f754
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
282442d7b6e8   bridge       bridge    local
7318efe60d0f   host         host      local
1a584f63c88c   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker network create my_network2
39816ba14919dab70bcf70b080451407612a4df1294324df9e350b0d34cbfdc7
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
282442d7b6e8   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker container run -d --name c1 --network my_network nginx:alpine0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
0e07ed388aa7   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago    Up 4 seconds    80/tcp                                  c1
39f7e1582143   nginx          "/docker-entrypoint.…"   24 minutes ago   Up 24 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   nginx_alec
bradsimpson@ ~:docker container stop nginx_alec
nginx_alec
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
0e07ed388aa7   nginx:alpine   "/docker-entrypoint.…"   23 seconds ago   Up 21 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c2 --network my_network nginx:alpine 
df23cab697d2794f045ecd379914f32a9321136f09625f23b5d2d2ae3ae41631
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
df23cab697d2   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 3 seconds    80/tcp    c2
0e07ed388aa7   nginx:alpine   "/docker-entrypoint.…"   38 seconds ago   Up 36 seconds   80/tcp    c1
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d --name c3  nginx:alpine
13908dd5fcc91726712131bccc51cc73fb8b7d6343be7d2afa74f6c5614dc6c0
bradsimpson@ ~:docker container run -d --name c4  nginx:alpine
b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
b84b82c0d9a8   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago        Up 4 seconds        80/tcp    c4
13908dd5fcc9   nginx:alpine   "/docker-entrypoint.…"   11 seconds ago       Up 10 seconds       80/tcp    c3
df23cab697d2   nginx:alpine   "/docker-entrypoint.…"   37 seconds ago       Up 35 seconds       80/tcp    c2
0e07ed388aa7   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 4 c2
PING c2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.184 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.095 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.220 ms
64 bytes from 172.18.0.3: seq=3 ttl=64 time=0.104 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.095/0.150/0.220 ms
/ # ping -c 4 c3
ping: bad address 'c3'
/ # ping -c 4 c4
ping: bad address 'c4'
/ # exit
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949",
        "Created": "2022-09-13T16:54:30.977201717Z",
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
            "Pid": 4730,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-09-13T16:54:31.708851867Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/hostname",
        "HostsPath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/hosts",
        "LogPath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238/merged",
                "UpperDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238/diff",
                "WorkDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b84b82c0d9a8",
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
            "SandboxID": "8ee45a06305057ec55cbe3d2eafc815e772508953eb8844e4bbd84d72d8d7fd6",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/8ee45a063050",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "5e86eccdf87c080f6fb39cbf7ab80d17f342dada9bce45f40724652dc1739c7e",
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
                    "NetworkID": "282442d7b6e8b14588afc2eeaf0a0831ae4949db117e3401da0bed7da63e1851",
                    "EndpointID": "5e86eccdf87c080f6fb39cbf7ab80d17f342dada9bce45f40724652dc1739c7e",
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

bradsimpson@ ~:docker container exec -it c3 ash
/ # ping -c 3 c4
ping: bad address 'c4'
/ # ping -c 3 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.192 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.098 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.150 ms

--- 172.17.0.3 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.098/0.146/0.192 ms
/ # exit
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949",
        "Created": "2022-09-13T16:54:30.977201717Z",
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
            "Pid": 4730,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-09-13T16:54:31.708851867Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/hostname",
        "HostsPath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/hosts",
        "LogPath": "/var/lib/docker/containers/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949/b84b82c0d9a87d24d440eabe4ec0e16ef3f2e3c0e6465d9721bf536eb5209949-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238/merged",
                "UpperDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238/diff",
                "WorkDir": "/var/lib/docker/overlay2/d7a39c4a686778b57ce362697cb8a9e24f33521a94aeb6a46a2fc16024077238/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b84b82c0d9a8",
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
            "SandboxID": "8ee45a06305057ec55cbe3d2eafc815e772508953eb8844e4bbd84d72d8d7fd6",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/8ee45a063050",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "5e86eccdf87c080f6fb39cbf7ab80d17f342dada9bce45f40724652dc1739c7e",
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
                    "NetworkID": "282442d7b6e8b14588afc2eeaf0a0831ae4949db117e3401da0bed7da63e1851",
                    "EndpointID": "5e86eccdf87c080f6fb39cbf7ab80d17f342dada9bce45f40724652dc1739c7e",
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
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914",
        "Created": "2022-09-13T16:53:26.800771806Z",
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
            "Pid": 4200,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-09-13T16:53:27.89172598Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914/hostname",
        "HostsPath": "/var/lib/docker/containers/0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914/hosts",
        "LogPath": "/var/lib/docker/containers/0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914/0e07ed388aa7334cb837a4c6a9a55cf3059de94b804fc20d5ed15f0d57621914-json.log",
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
            "NetworkMode": "my_network",
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
                "LowerDir": "/var/lib/docker/overlay2/e1362ba56cbddaf0fd9257c12c9ed964d8e830066df5df8e7906e1282835ddbd-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/e1362ba56cbddaf0fd9257c12c9ed964d8e830066df5df8e7906e1282835ddbd/merged",
                "UpperDir": "/var/lib/docker/overlay2/e1362ba56cbddaf0fd9257c12c9ed964d8e830066df5df8e7906e1282835ddbd/diff",
                "WorkDir": "/var/lib/docker/overlay2/e1362ba56cbddaf0fd9257c12c9ed964d8e830066df5df8e7906e1282835ddbd/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0e07ed388aa7",
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
            "SandboxID": "954114e9a37faeddfdef2d81f13a868cf2d9aaabdd75bf084a3091d8d27e4124",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/954114e9a37f",
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
                "my_network": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "0e07ed388aa7"
                    ],
                    "NetworkID": "1a584f63c88c0ec2e6cac2118a00164789037a534529282e1bad9260e2c7f754",
                    "EndpointID": "75aaeb7b9944c903c2de75c134d9075a677f25e2698808226d5816a4a65cf9ed",
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
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
282442d7b6e8   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd tmp
/tmp # \ls
/tmp # touch index.html
/tmp # \ls
index.html
/tmp # exit
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                     PORTS     NAMES
6d01e80a251d   alpine         "sh"                     33 seconds ago   Exited (0) 9 seconds ago             laughing_noether
b84b82c0d9a8   nginx:alpine   "/docker-entrypoint.…"   8 minutes ago    Up 8 minutes               80/tcp    c4
13908dd5fcc9   nginx:alpine   "/docker-entrypoint.…"   8 minutes ago    Up 8 minutes               80/tcp    c3
df23cab697d2   nginx:alpine   "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes               80/tcp    c2
0e07ed388aa7   nginx:alpine   "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes               80/tcp    c1
39f7e1582143   nginx          "/docker-entrypoint.…"   34 minutes ago   Exited (0) 9 minutes ago             nginx_alec

bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker volume inspect postgres-data
[
    {
        "CreatedAt": "2022-08-16T20:07:04Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/postgres-data/_data",
        "Name": "postgres-data",
        "Options": {},
        "Scope": "local"
    }
]
bradsimpson@ ~:docker volume inspect my_volume2
[
    {
        "CreatedAt": "2022-06-21T17:38:54Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/my_volume2/_data",
        "Name": "my_volume2",
        "Options": {},
        "Scope": "local"
    }
]
bradsimpson@ ~:\clear

















bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker container run --mount type=bind/volume source=/absolute/path/on/local/filesystem,target=absolute/path/in/container
invalid argument "type=bind/volume" for "--mount" flag: target is required
See 'docker container run --help'.
bradsimpson@ ~:
bradsimpson@ ~:docker container run --mount type=volume source=name_of_volume,target=absolute/path/in/container
invalid argument "type=volume" for "--mount" flag: target is required
See 'docker container run --help'.
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:docker image inspect b1c3acb28882
[
    {
        "Id": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "RepoTags": [
            "nginx:alpine"
        ],
        "RepoDigests": [
            "nginx@sha256:a74534e76ee1121d418fa7394ca930eb67440deda413848bc67c68138535b989"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-05-17T22:36:41.590296646Z",
        "Container": "6267b0b64513d649f62fdcba05446c4f24d94ea820fbc80f41705a44df47915f",
        "ContainerConfig": {
            "Hostname": "6267b0b64513",
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
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:ebc24bc17c5a0e526e658e2473222556f40588eaf8b65995fd0eade2365602dc",
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
                "PKG_RELEASE=1"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:ebc24bc17c5a0e526e658e2473222556f40588eaf8b65995fd0eade2365602dc",
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
        "Size": 23421875,
        "VirtualSize": 23421875,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/merged",
                "UpperDir": "/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff",
                "WorkDir": "/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:4fc242d58285699eca05db3cc7c7122a2b8e014d9481f323bd9277baacfa0628",
                "sha256:4721bfafc708dfeaa56a501848081b91415899e5b9f0d26612be42a8ff43e8e2",
                "sha256:45b275e8a06dd152de9b17143ad936aa971fb8abaa0f6d977f7d822c61604abc",
                "sha256:a43749efe4ecc3db4ca41063def5021c8567743c5ea13865d2e620beab1017ea",
                "sha256:d6dd885da0bbd4268a39c7f79fc0e87c8de6641ba4ea33e5ef7e1caa64f8429d",
                "sha256:c0e7c94aefd832d1ee1c565ddcac257ca7851f41c3ef6f079722c69f14f0662b"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:docker image inspect postgres
[
    {
        "Id": "sha256:5b21e2e86aab1630251ecfb5d0d715634c0965931e8f5ab5d2dc6bce3aeb92fa",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:2d1e636f07781d4799b3f2edbff78a0a5494f24c4512cb56a83ebfd0e04ec074"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-05-28T11:51:18.200535542Z",
        "Container": "7a9823308ba16b9130ca8fad574ed79edbfa4f8713671bb6eae81983195c02ca",
        "ContainerConfig": {
            "Hostname": "7a9823308ba1",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.3-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:906a82f7fa1bd09c76b61109cdb36b7595d6322952cae6be8b5ea3fa887ee303",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.3-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:906a82f7fa1bd09c76b61109cdb36b7595d6322952cae6be8b5ea3fa887ee303",
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
        "Size": 376123192,
        "VirtualSize": 376123192,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/b642eb8696e4e27eb0bb0d12f52a4eea2ad1fdb16f686051d027b9eb16a3b63c/diff:/var/lib/docker/overlay2/77a63f3f4ee039a568146d6a9434532507fe315f821f81f143f8f089300ded0e/diff:/var/lib/docker/overlay2/0886ea31cb0054e29f26aa85d54bdbf0d46b9cc4dadfb1cf3910f36fb5574f45/diff:/var/lib/docker/overlay2/28e11608521227763164316ab06300958fd21a416134ceb40ffd437e5636fb1d/diff:/var/lib/docker/overlay2/1faf7363256b6ff44fb5b0c7b1b4ea74f24680000accca8ba098ebdc5cd2267f/diff:/var/lib/docker/overlay2/9d1037fda7fe805571f54031a2613f8f5e23c80aa2542b697523ee8cd44595a0/diff:/var/lib/docker/overlay2/3991c0b8cc10bf3a2f41bb8f9783d1227c235a4a3a6c47ddd12312fdb9a3bb83/diff:/var/lib/docker/overlay2/9696cf2539d58ee0228008050c1f30ff5f6776f582e1e4034ebb8dc44ae365ae/diff:/var/lib/docker/overlay2/88f713a38a34f2055b2b4d42e93f058de3e99ebc683b5a1aaa4ce933334fc578/diff:/var/lib/docker/overlay2/6407585b7c5e83b411bb15d8f9e65f00caeea5a55580d3e59f3a190f7b589a78/diff:/var/lib/docker/overlay2/9cbf8941166293e7b9a1b66844eecaa477fc9c2ebb7d74c4a6949759fd4f6f81/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/8a262f13606e4c24ba394895d96c9960873aeca5b1ce7ec15ff04d74d0135bdf/merged",
                "UpperDir": "/var/lib/docker/overlay2/8a262f13606e4c24ba394895d96c9960873aeca5b1ce7ec15ff04d74d0135bdf/diff",
                "WorkDir": "/var/lib/docker/overlay2/8a262f13606e4c24ba394895d96c9960873aeca5b1ce7ec15ff04d74d0135bdf/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:ad6562704f3759fb50f0d3de5f80a38f65a85e709b77fd24491253990f30b6be",
                "sha256:8fa5e671e66543c8b567bb6c76364322fddf4fff0daa487178a8caefc61f52f4",
                "sha256:81c2fe13a1f0bde53c09587480446c5b38cb33064beef504215d394799107dae",
                "sha256:287d777006b9b6673406327c7099b0b20cc5f5421db91663a4bea0c1fd23a98a",
                "sha256:69feeba6d5b01eea6edc5fe0dcae6ab79935f7428d42143c7bb25552eb06c33b",
                "sha256:1b67a9cd52150ec147f84bc854737f12868081f76791dac23114f3a254c18580",
                "sha256:1ff3ceb3f41434dbf6b5beef16ce094242663ac5ddc5b92a3fd73a0d44eafead",
                "sha256:32e442eaf90910f2f058de7e6ff4148361407dc59034a8410f26ea54af19af01",
                "sha256:5cad0059a27d804a2cfd5ce5af4163e5ad85f81817222489177d38de12859f41",
                "sha256:88e235c6b97504282831b44d9e69a79e88fcb4c72b73f38e5f31eeb9df47f56e",
                "sha256:edf7a92c1e15438484ad490543a86936a2b94f14624364ec4a189bfadc408fb8",
                "sha256:8e43b491d5d4c69edb04aa526487a358afb3b51d805ca4bc059ab05411050af1",
                "sha256:8b44e3129736d85abec3a86be4807b2ca3f4a5b35d4da41403a6f07e89567ae6"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		docker
Desktop		Library		Pictures	app		opt
Documents	Movies		Postman		app.index.html
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
dec.db		index.html
bradsimpson@ app:cd ..
bradsimpson@ ~:mkdir app2
bradsimpson@ ~:cd app2/
bradsimpson@ app2:touch index.html
bradsimpson@ app2:nano index.html
bradsimpson@ app2:cd ..
bradsimpson@ ~:docker container run -d --mount type=bind,source=$(pwd)/app2, target=/usr/share/nginx/html -p 8000:80 nginx:alpine 
invalid argument "type=bind,source=/Users/bradsimpson/app2," for "--mount" flag: invalid field '' must be a key=value pair
See 'docker container run --help'.
bradsimpson@ ~:docker container run -d --mount type=bind,source="$(pwd)/app2",target=/usr/share/nginx/html -p 8000:80 nginx:alpine 
6d1c1814a7a5a99d860913c63470fa41cfc9d89094e820fa0aaf53c96bbdb499
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
6d1c1814a7a5   nginx:alpine   "/docker-entrypoint.…"   8 seconds ago   Up 6 seconds   0.0.0.0:8000->80/tcp, :::8000->80/tcp   blissful_hypatia
bradsimpson@ ~:docker container exec -it blissful_hypatia ash
/ # ls
bin                   media                 srv
dev                   mnt                   sys
docker-entrypoint.d   opt                   tmp
docker-entrypoint.sh  proc                  usr
etc                   root                  var
home                  run
lib                   sbin
/ # cd usr
/usr # \ls
bin    lib    local  sbin   share
/usr # cd share
/usr/share # \ls
GeoIP            doc              misc             zoneinfo
apk              licenses         nginx
ca-certificates  man              udhcpc
/usr/share # cd nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
ash: nano: not found
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (5.9-r0)
Executing busybox-1.34.1-r5.trigger
OK: 26 MiB in 43 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ ~:\clear

bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		app2
Desktop		Library		Pictures	app		docker
Documents	Movies		Postman		app.index.html	opt
bradsimpson@ ~:cd app2
bradsimpson@ app2:\ls
index.html
bradsimpson@ app2:nano index.html 
bradsimpson@ app2:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
6d1c1814a7a5   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   blissful_hypatia
bradsimpson@ app2:docker container stop blissful_hypatia
blissful_hypatia
bradsimpson@ app2:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app2:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ app2:docker volume create my_volume3
my_volume3
bradsimpson@ app2:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     postgres-data
bradsimpson@ app2:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
postgres                    latest    5b21e2e86aab   3 months ago    376MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ app2:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:2d1e636f07781d4799b3f2edbff78a0a5494f24c4512cb56a83ebfd0e04ec074
Deleted: sha256:5b21e2e86aab1630251ecfb5d0d715634c0965931e8f5ab5d2dc6bce3aeb92fa
Deleted: sha256:dc2b1e2f79ea4ed5d1191d313dc4e02fef000b7d78125068b69ab0bd81fff50d
Deleted: sha256:bf0d659b5b33b2555d614903750c58e41e32245aac657d7adf881bb18beff947
Deleted: sha256:7ea3bc7834357d0f3e8fc6e1bb97443863939252b1a7704a4e0324168052dd57
Deleted: sha256:7aaacf887c0ed90858ab16c6cf805b3bc13c262728083365a0325ae50215a207
Deleted: sha256:b95563591a3dcec4a730bcbb93ce2a3273668adf6455ad4acdd39af979a819fd
Deleted: sha256:3a70523d280c8b4996fcd744fdaf78947a893379e2a66a55b8cb521904a415f7
Deleted: sha256:951723d537e46a68c0d9c3481fcf2da76a802c699325d009f81e4eb554781369
Deleted: sha256:15a422d5cc439b961bdbad7a20049b16da206906f1b38f81d86f7f0bc078a2fd
Deleted: sha256:3459c51d6882b970b575d6df53336641ed64dfc6d6bee42ddaf788c46a361726
Deleted: sha256:90545f9646db23cd2e9759e9665888744623cd83a98e93aca9538c172ea8b3cf
Deleted: sha256:1370822ddffdc745b805d3997c59b4ccc299ab1bbf60a06a89c58a1ec81f145a
Deleted: sha256:e9195a0ed2fc9be10687915094405116ad3d04563436d7cb15117babf3c3e466
bradsimpson@ app2:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ app2:\clear

bradsimpson@ app2:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
31b3f1ad4ce1: Pull complete 
dc97844d0cd5: Pull complete 
9ad9b1166fde: Pull complete 
286c4682b24d: Pull complete 
1d3679a4a1a1: Pull complete 
5f2e6cdc8503: Pull complete 
0f7dc70f54e8: Pull complete 
a090c7442692: Pull complete 
81bfe40fd0f6: Pull complete 
8ac8c22bbb38: Pull complete 
96e51d1d3c6e: Pull complete 
667bd4154fa2: Pull complete 
87267fb600a9: Pull complete 
Digest: sha256:e71e4f897079e9e2efea20b3d181e400f502887cbe1fc0b65c7135b6455aef09
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app2:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
postgres                    latest    75993dd36176   6 hours ago     376MB
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ app2:docker image inspect postgres
[
    {
        "Id": "sha256:75993dd36176c7d4be8c1e6d88a115f1fb35a85451088699dbdc80659ad688ed",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:e71e4f897079e9e2efea20b3d181e400f502887cbe1fc0b65c7135b6455aef09"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-09-13T11:44:43.764321338Z",
        "Container": "81312c45847316210986993661c43b636141f7718b74c42ece966d1440f2d6bd",
        "ContainerConfig": {
            "Hostname": "81312c458473",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.5-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:0e94bdc97cd1d0111bf8dc753b90e7bffac68f166396af8e5e01d1590da49bed",
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
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/14/bin",
                "GOSU_VERSION=1.14",
                "LANG=en_US.utf8",
                "PG_MAJOR=14",
                "PG_VERSION=14.5-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:0e94bdc97cd1d0111bf8dc753b90e7bffac68f166396af8e5e01d1590da49bed",
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
        "Size": 376259946,
        "VirtualSize": 376259946,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/e7f508a58774c73d6df32f0f37f46c39f2e3f63cf00b453538cb301a2c1d7442/diff:/var/lib/docker/overlay2/03e8e91bd5208c6cc99f51dd0bcf71fe39b61aeecf6fee6e7766058b61f0c107/diff:/var/lib/docker/overlay2/f6653b4b0d550e4989b3790d4da6b01edc37bca8e38deb7795b8a00e502728ee/diff:/var/lib/docker/overlay2/2cb734de10b4a17b225d6795fcb4ca3534476b143bca364a9c08da45bf5e6ca9/diff:/var/lib/docker/overlay2/809934c3cc8322af8f42437a9f903b7349e75c86496a22b9ba08a1ed64ee6d65/diff:/var/lib/docker/overlay2/0989c1d53da4f464b88e722598087e2175c9b2287c16e672a700dd0e46fec18e/diff:/var/lib/docker/overlay2/b5f798142cacb2400fef74d59153816323d67f7517941e9668fab5d80d3ed7de/diff:/var/lib/docker/overlay2/668b87112c8abce231d28eeb13f352411e56a18690895b7c2c0290bd2b181d5b/diff:/var/lib/docker/overlay2/eeaf575184da7d2ce75012e111cb873efde129aca2915ed0b4cb14d0a7e7203b/diff:/var/lib/docker/overlay2/7ce7106ccb89561fc35102d9734d544194ed0e9c7508d63bd19385586cf9fc8f/diff:/var/lib/docker/overlay2/63987f9914de8be4aab20762b9617cbf8e7f615ca65697be15cc83a00fd37c77/diff:/var/lib/docker/overlay2/3005069fb555dd88278cf4a79b176c285746177e690f4f0ccea848adefa8f5ce/diff",
                "MergedDir": "/var/lib/docker/overlay2/e5e9cf5be2c23d7c2240e5b7e31dd9f260dc6e3046a6519a635739517d136982/merged",
                "UpperDir": "/var/lib/docker/overlay2/e5e9cf5be2c23d7c2240e5b7e31dd9f260dc6e3046a6519a635739517d136982/diff",
                "WorkDir": "/var/lib/docker/overlay2/e5e9cf5be2c23d7c2240e5b7e31dd9f260dc6e3046a6519a635739517d136982/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:b45078e74ec97c5e600f6d5de8ce6254094fb3cb4dc5e1cc8335fb31664af66e",
                "sha256:38c22c30b0ada83ef94a815ca842970eef78663dbbe071b370a9081bf598e65d",
                "sha256:198bac2d459b1958d8a505bea77d1fa941026722340bd1cd46d79abd3230b497",
                "sha256:d4d16d23c3fd11b343adbfe0ad467ba5a6ee2ae40df582bd09f6659d0c0a0cf2",
                "sha256:0c768903c915c6faa0aaf2f33416fead0b1a46b73ffd039aadc983c85eb6cfd6",
                "sha256:98fc89d04d4fa98ee17726dd33de253b9131defacb1da03284995fa8226f75fe",
                "sha256:039f1b2f32f02cbeb64f8c0afcfc36b98e1c34374f5ecdc4eaf205cfc8edcb5d",
                "sha256:f0af0bfea71055f628f8cb1d5ddf517ee90d6ebe113cdd9112f5644f24a535f0",
                "sha256:0dce2b9841fdf752ec4a471170f868a0485b5f6716900be65636dc61d16edee1",
                "sha256:bbb8548e11e4831562c4b68a992ebf290f60f0217669273b9d9aa5b21eb3a5ae",
                "sha256:557544342c621aa698a93d04ded5af6ff5d1c55873cd1e050d307e270b36ab7f",
                "sha256:0ee3d3df28d4d0c0a3029b5e3ebdda5656a402fc43abbf0b9d12ef565e092933",
                "sha256:d64f00c56a9dc3ca0e04c6a22d83987d19c06c618a2f1e36ae84791a7d140b33"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app2:\clear

bradsimpson@ app2:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgres5431 -d --mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres
970f3551861db4b74e1921841d0d5af47ddd6dafd481d4ec23c71908d0c41584
bradsimpson@ app2:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
970f3551861d   postgres   "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
bradsimpson@ app2:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 14.5 (Debian 14.5-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
Type "help" for help.

postgres=# d
postgres-# \d
Did not find any relations.
postgres-# \l
                                 List of databases
   Name    |   Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+-----------+----------+------------+------------+-----------------------
 postgres  | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |           |          |            |            | postgres=CTc/postgres
 template1 | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |           |          |            |            | postgres=CTc/postgres
 test_db   | test_user | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres-# CREATE DATABASE new_test WITH OWNER postgres;
ERROR:  syntax error at or near "d"
LINE 1: d
        ^
postgres=# CREATE DATABASE new_test WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                 List of databases
   Name    |   Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+-----------+----------+------------+------------+-----------------------
 new_test  | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |           |          |            |            | postgres=CTc/postgres
 template1 | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |           |          |            |            | postgres=CTc/postgres
 test_db   | test_user | UTF8     | en_US.utf8 | en_US.utf8 | 
(5 rows)

postgres=# exit
bradsimpson@ app2:\clear

bradsimpson@ app2:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
970f3551861d   postgres   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
bradsimpson@ app2:docker container stop postgres5431
postgres5431
bradsimpson@ app2:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app2:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgresnew -d --mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres
81eb438f379b59b4b9a35b0ea129e8c7d827e9bc0279ddcb2abad50a61e3faeb
bradsimpson@ app2:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
81eb438f379b   postgres   "docker-entrypoint.s…"   5 seconds ago   Up 4 seconds   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgresnew
bradsimpson@ app2:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 14.5 (Debian 14.5-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |   Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+-----------+----------+------------+------------+-----------------------
 new_test  | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |           |          |            |            | postgres=CTc/postgres
 template1 | postgres  | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |           |          |            |            | postgres=CTc/postgres
 test_db   | test_user | UTF8     | en_US.utf8 | en_US.utf8 | 
(5 rows)

postgres=# exit
bradsimpson@ app2:


















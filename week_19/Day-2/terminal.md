# CLI Section

Last login: Tue Feb  7 11:28:53 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
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
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/revisited_react   latest    303fa668755c   3 weeks ago     568MB
my_project                       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/new_project         latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/react_project       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimpson213/my_project        latest    ae74e957ba0d   3 weeks ago     568MB
bradsimpson213/react_project     latest    ae74e957ba0d   3 weeks ago     568MB
postgres                         latest    a26eb6069868   6 weeks ago     379MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2         <none>    8edeca523aef   4 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   5 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   7 months ago    377MB
ubuntu                           latest    27941809078c   8 months ago    77.8MB
nginx                            latest    0e901e68141f   8 months ago    142MB
alpine                           latest    e66264b98777   8 months ago    5.53MB
nginx                            alpine    b1c3acb28882   8 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   16 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run [options/flags] image name [commands]
docker: invalid reference format.
See 'docker run --help'.
bradsimpson@ ~:docker container run --name cool_container -p 5000:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/02/07 16:56:08 [notice] 1#1: using the "epoll" event method
2023/02/07 16:56:08 [notice] 1#1: nginx/1.21.6
2023/02/07 16:56:08 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/02/07 16:56:08 [notice] 1#1: OS: Linux 5.15.49-linuxkit
2023/02/07 16:56:08 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/02/07 16:56:08 [notice] 1#1: start worker processes
2023/02/07 16:56:08 [notice] 1#1: start worker process 31
2023/02/07 16:56:08 [notice] 1#1: start worker process 32
172.17.0.1 - - [07/Feb/2023:16:56:39 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" "-"
2023/02/07 16:56:40 [error] 32#32: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:5000", referrer: "http://localhost:5000/"
172.17.0.1 - - [07/Feb/2023:16:56:40 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:5000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [07/Feb/2023:16:57:01 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [07/Feb/2023:16:57:02 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [07/Feb/2023:16:57:04 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" "-"
^C2023/02/07 16:57:29 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/02/07 16:57:29 [notice] 31#31: exiting
2023/02/07 16:57:29 [notice] 31#31: exit
2023/02/07 16:57:29 [notice] 32#32: exiting
2023/02/07 16:57:29 [notice] 32#32: exit
2023/02/07 16:57:29 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/02/07 16:57:29 [notice] 1#1: worker process 31 exited with code 0
2023/02/07 16:57:29 [notice] 1#1: signal 29 (SIGIO) received
2023/02/07 16:57:29 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/02/07 16:57:29 [notice] 1#1: worker process 32 exited with code 0
2023/02/07 16:57:29 [notice] 1#1: exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS                      PORTS     NAMES
28daacce32f9   nginx     "/docker-entrypoint.…"   About a minute ago   Exited (0) 24 seconds ago             cool_container
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -p 8000:80 -d nginx
4df077909c4c4fd63448477317a41be6759bae7c38f36e325f4ba6116a040c62
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS          PORTS                  NAMES
4df077909c4c   nginx     "/docker-entrypoint.…"   About a minute ago   Up 58 seconds   0.0.0.0:8000->80/tcp   funny_mclaren
bradsimpson@ ~:docker container run --rm -it alpine ash  
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd lib/
/lib # \ls
apk                    libc.musl-x86_64.so.1  libz.so.1.2.12
firmware               libcrypto.so.1.1       mdev
ld-musl-x86_64.so.1    libssl.so.1.1          modules-load.d
libapk.so.3.12.0       libz.so.1              sysctl.d
/lib # cd ..
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
/bin # ^C
/bin # quit
ash: quit: not found
/bin # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
4df077909c4c   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->80/tcp   funny_mclaren
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
4df077909c4c   nginx     "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:8000->80/tcp   funny_mclaren
bradsimpson@ ~:docker container run -it alpine ash  
/ # exit
bradsimpson@ ~:docker container ls =la
"docker container ls" accepts no arguments.
See 'docker container ls --help'.

Usage:  docker container ls [OPTIONS]

List containers
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                      PORTS     NAMES
a3f5eb0afdbc   alpine    "ash"     18 seconds ago   Exited (0) 12 seconds ago             laughing_ellis
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx
b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959
bradsimpson@ ~:docker container run --name test -it alpine sh
/ # exit
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello worldhello world
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
52b50160154b   alpine    "sh"      2 minutes ago   Exited (0) 2 minutes ago             test
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:8080->80/tcp   zen_neumann
4df077909c4c   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:8000->80/tcp   funny_mclaren
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
52b50160154b   alpine    "sh"      2 minutes ago   Exited (0) 2 minutes ago             test
bradsimpson@ ~:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/revisited_react   latest    303fa668755c   3 weeks ago     568MB
bradsimpson213/react_project     latest    ae74e957ba0d   3 weeks ago     568MB
my_project                       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/new_project         latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/react_project       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimpson213/my_project        latest    ae74e957ba0d   3 weeks ago     568MB
postgres                         latest    a26eb6069868   6 weeks ago     379MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2         <none>    8edeca523aef   4 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   5 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   7 months ago    377MB
ubuntu                           latest    27941809078c   8 months ago    77.8MB
nginx                            latest    0e901e68141f   8 months ago    142MB
alpine                           latest    e66264b98777   8 months ago    5.53MB
nginx                            alpine    b1c3acb28882   8 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   16 months ago   13.3kB
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
133072a02e44   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
5a5cc332e830   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     taco_tuesday
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8080->80/tcp   zen_neumann
4df077909c4c   nginx     "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp   funny_mclaren
bradsimpson@ ~:docker container stop funny_mclaren b78442678f56
funny_mclaren
b78442678f56
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
52b50160154b   alpine    "sh"      4 minutes ago   Exited (0) 4 minutes ago             test
bradsimpson@ ~:docker container ls -l
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
52b50160154b   alpine    "sh"      5 minutes ago   Exited (0) 5 minutes ago             test
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
52b50160154b   alpine        "sh"                     5 minutes ago    Exited (0) 5 minutes ago              test
b78442678f56   nginx         "/docker-entrypoint.…"   7 minutes ago    Exited (0) 48 seconds ago             zen_neumann
a3f5eb0afdbc   alpine        "ash"                    11 minutes ago   Exited (0) 10 minutes ago             laughing_ellis
4df077909c4c   nginx         "/docker-entrypoint.…"   17 minutes ago   Exited (0) 48 seconds ago             funny_mclaren
28daacce32f9   nginx         "/docker-entrypoint.…"   21 minutes ago   Exited (0) 20 minutes ago             cool_container
edba253135a8   hello-world   "/hello"                 35 minutes ago   Exited (0) 35 minutes ago             upbeat_bassi
bradsimpson@ ~:docker container start upbeat_bassi b78442678f56
upbeat_bassi
b78442678f56
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   8 minutes ago   Up 7 seconds   0.0.0.0:8080->80/tcp   zen_neumann
bradsimpson@ ~:\clear


bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
52b50160154b   alpine        "sh"                     7 minutes ago    Exited (0) 7 minutes ago                           test
b78442678f56   nginx         "/docker-entrypoint.…"   9 minutes ago    Up 58 seconds               0.0.0.0:8080->80/tcp   zen_neumann
a3f5eb0afdbc   alpine        "ash"                    13 minutes ago   Exited (0) 13 minutes ago                          laughing_ellis
4df077909c4c   nginx         "/docker-entrypoint.…"   19 minutes ago   Exited (0) 3 minutes ago                           funny_mclaren
28daacce32f9   nginx         "/docker-entrypoint.…"   24 minutes ago   Exited (0) 22 minutes ago                          cool_container
edba253135a8   hello-world   "/hello"                 37 minutes ago   Exited (0) 59 seconds ago                          upbeat_bassi
bradsimpson@ ~:docker comtainer rm upbeat_bassi
docker: 'comtainer' is not a docker command.
See 'docker --help'
bradsimpson@ ~:docker container rm upbeat_bassi
upbeat_bassi
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS                  NAMES
52b50160154b   alpine    "sh"                     8 minutes ago    Exited (0) 7 minutes ago                           test
b78442678f56   nginx     "/docker-entrypoint.…"   10 minutes ago   Up About a minute           0.0.0.0:8080->80/tcp   zen_neumann
a3f5eb0afdbc   alpine    "ash"                    13 minutes ago   Exited (0) 13 minutes ago                          laughing_ellis
4df077909c4c   nginx     "/docker-entrypoint.…"   20 minutes ago   Exited (0) 3 minutes ago                           funny_mclaren
28daacce32f9   nginx     "/docker-entrypoint.…"   24 minutes ago   Exited (0) 23 minutes ago                          cool_container
bradsimpson@ ~:docker container prune 
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
52b50160154b19787127c2e4399ffda3b2b560387179b81e8ad65cc9b9686025
a3f5eb0afdbce277db47b561200106aa9d5ebcd3f39366320dbbaa20e913e800
4df077909c4c4fd63448477317a41be6759bae7c38f36e325f4ba6116a040c62
28daacce32f9d49435d2098f49976abfebfe75e12370d2676a7458c46891a407

Total reclaimed space: 2.196kB
bradsimpson@ ~:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/revisited_react   latest    303fa668755c   3 weeks ago     568MB
bradsimpson213/react_project     latest    ae74e957ba0d   3 weeks ago     568MB
my_project                       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/new_project         latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/react_project       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimpson213/my_project        latest    ae74e957ba0d   3 weeks ago     568MB
postgres                         latest    a26eb6069868   6 weeks ago     379MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2         <none>    8edeca523aef   4 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   5 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   7 months ago    377MB
ubuntu                           latest    27941809078c   8 months ago    77.8MB
nginx                            latest    0e901e68141f   8 months ago    142MB
alpine                           latest    e66264b98777   8 months ago    5.53MB
nginx                            alpine    b1c3acb28882   8 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   16 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   zen_neumann
bradsimpson@ ~:docker container exec -it zen_neumann
"docker container exec" requires at least 2 arguments.
See 'docker container exec --help'.

Usage:  docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container
bradsimpson@ ~:docker container exec -it zen_neumann sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp   zen_neumann
bradsimpson@ ~:docker container inspect zen_neumann
[
    {
        "Id": "b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959",
        "Created": "2023-02-07T17:10:46.96630167Z",
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
            "Pid": 3176,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-02-07T17:19:24.206339757Z",
            "FinishedAt": "2023-02-07T17:17:17.055229163Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/hostname",
        "HostsPath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/hosts",
        "LogPath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959-json.log",
        "Name": "/zen_neumann",
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
                "LowerDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858/merged",
                "UpperDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858/diff",
                "WorkDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b78442678f56",
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
            "SandboxID": "e699a20a0804e6b9cacd042a3364af5e236092f4cb54b1d7879457c495efcc1a",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8080"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/e699a20a0804",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "7f67fa8f1d634b01cc8e0404d4138a0e5bcbab06ebcc9674bd9e335166a2d8cb",
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
                    "NetworkID": "133072a02e44e727f41e2334ff5aa01214e0519e66a10231435ff9af0be6886f",
                    "EndpointID": "7f67fa8f1d634b01cc8e0404d4138a0e5bcbab06ebcc9674bd9e335166a2d8cb",
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
bradsimpson@ ~:


# Networking Section

Last login: Tue Feb  7 11:29:01 on ttys001

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
133072a02e44   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
5a5cc332e830   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   42 minutes ago   Up 34 minutes   0.0.0.0:8080->80/tcp   zen_neumann
bradsimpson@ ~:docker container inspect zen_neumann
[
    {
        "Id": "b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959",
        "Created": "2023-02-07T17:10:46.96630167Z",
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
            "Pid": 3176,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-02-07T17:19:24.206339757Z",
            "FinishedAt": "2023-02-07T17:17:17.055229163Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/hostname",
        "HostsPath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/hosts",
        "LogPath": "/var/lib/docker/containers/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959/b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959-json.log",
        "Name": "/zen_neumann",
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
                "LowerDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858/merged",
                "UpperDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858/diff",
                "WorkDir": "/var/lib/docker/overlay2/e414eea75678b6320a712127765c276d3b337731fca06eff48961eb68b3c2858/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b78442678f56",
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
            "SandboxID": "e699a20a0804e6b9cacd042a3364af5e236092f4cb54b1d7879457c495efcc1a",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8080"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/e699a20a0804",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "7f67fa8f1d634b01cc8e0404d4138a0e5bcbab06ebcc9674bd9e335166a2d8cb",
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
                    "NetworkID": "133072a02e44e727f41e2334ff5aa01214e0519e66a10231435ff9af0be6886f",
                    "EndpointID": "7f67fa8f1d634b01cc8e0404d4138a0e5bcbab06ebcc9674bd9e335166a2d8cb",
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
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
133072a02e44   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
5a5cc332e830   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker network create --driver bridge taco_tuesday
6000c9f47f196b461f18d83c6aa89dc6969aa11d3eba69803de7c31dde59c64f
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
133072a02e44   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
ef43db5a14d2   my_network2    bridge    local
5a5cc332e830   my_network3    bridge    local
475754f27665   none           null      local
6000c9f47f19   taco_tuesday   bridge    local
bradsimpson@ ~:docker network rm 5a5cc332e830
5a5cc332e830
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
133072a02e44   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
ef43db5a14d2   my_network2    bridge    local
475754f27665   none           null      local
6000c9f47f19   taco_tuesday   bridge    local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
b78442678f56   nginx     "/docker-entrypoint.…"   49 minutes ago   Up 41 minutes   0.0.0.0:8080->80/tcp   zen_neumann
bradsimpson@ ~:docker container stop zen_neumann
zen_neumann
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
133072a02e44   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
ef43db5a14d2   my_network2    bridge    local
475754f27665   none           null      local
6000c9f47f19   taco_tuesday   bridge    local
bradsimpson@ ~:docker container run -d --name c1 --network taco_tuesday nginx:alpine
2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
2dc8b0387af2   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago   Up 3 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c2 --network taco_tuesday nginx:alpine
920bf88a190382b45d9af3ca80ad4f9260bd6b2c4551484e195911a00c4c1114
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
920bf88a1903   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 4 seconds    80/tcp    c2
2dc8b0387af2   nginx:alpine   "/docker-entrypoint.…"   22 seconds ago   Up 20 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c3 nginx:alpine
1e72d96d1cbcc6820a2b5423ec4f37f598bf2ab83b42058f68688e85858e3219
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine
a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS          PORTS     NAMES
a9cf78790ed8   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago        Up 5 seconds    80/tcp    c4
1e72d96d1cbc   nginx:alpine   "/docker-entrypoint.…"   13 seconds ago       Up 11 seconds   80/tcp    c3
920bf88a1903   nginx:alpine   "/docker-entrypoint.…"   43 seconds ago       Up 42 seconds   80/tcp    c2
2dc8b0387af2   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up 58 seconds   80/tcp    c1
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796",
        "Created": "2023-02-07T18:02:34.703462046Z",
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
            "Pid": 3399,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-02-07T18:02:35.636103396Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796/hostname",
        "HostsPath": "/var/lib/docker/containers/2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796/hosts",
        "LogPath": "/var/lib/docker/containers/2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796/2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796-json.log",
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
            "NetworkMode": "taco_tuesday",
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
                "LowerDir": "/var/lib/docker/overlay2/3b02c34a264de90b872d3f66d512a6100fb7c39cc0ea250908508a2622b52882-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/3b02c34a264de90b872d3f66d512a6100fb7c39cc0ea250908508a2622b52882/merged",
                "UpperDir": "/var/lib/docker/overlay2/3b02c34a264de90b872d3f66d512a6100fb7c39cc0ea250908508a2622b52882/diff",
                "WorkDir": "/var/lib/docker/overlay2/3b02c34a264de90b872d3f66d512a6100fb7c39cc0ea250908508a2622b52882/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "2dc8b0387af2",
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
            "SandboxID": "4b6eb2ebc715afe7edab354cdccc65ea7705592f9094d1d2f92ff986f00e3739",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/4b6eb2ebc715",
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
                "taco_tuesday": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "2dc8b0387af2"
                    ],
                    "NetworkID": "6000c9f47f196b461f18d83c6aa89dc6969aa11d3eba69803de7c31dde59c64f",
                    "EndpointID": "cc0712434c625498afae3f89802e0bdd8b1e1dfae82d7829d060cd292e68ee5d",
                    "Gateway": "172.21.0.1",
                    "IPAddress": "172.21.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:15:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76",
        "Created": "2023-02-07T18:03:28.103721381Z",
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
            "Pid": 3752,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-02-07T18:03:28.809531506Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76/hostname",
        "HostsPath": "/var/lib/docker/containers/a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76/hosts",
        "LogPath": "/var/lib/docker/containers/a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76/a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/986e237c81ccef49dcef81e258b2c23d2cca0ada97b8cb2783c2c3036a22b126-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/986e237c81ccef49dcef81e258b2c23d2cca0ada97b8cb2783c2c3036a22b126/merged",
                "UpperDir": "/var/lib/docker/overlay2/986e237c81ccef49dcef81e258b2c23d2cca0ada97b8cb2783c2c3036a22b126/diff",
                "WorkDir": "/var/lib/docker/overlay2/986e237c81ccef49dcef81e258b2c23d2cca0ada97b8cb2783c2c3036a22b126/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "a9cf78790ed8",
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
            "SandboxID": "42cba407fdab0cb3a8ac60ebf3290b6498ddf785b49a46e93f7ddba33ec7bd41",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/42cba407fdab",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "d287e2e0038ff40a2dde8e65f6064b69ae93a50181ba188acf1e7d4116acc0cd",
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
                    "NetworkID": "133072a02e44e727f41e2334ff5aa01214e0519e66a10231435ff9af0be6886f",
                    "EndpointID": "d287e2e0038ff40a2dde8e65f6064b69ae93a50181ba188acf1e7d4116acc0cd",
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
a9cf78790ed8   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
1e72d96d1cbc   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
920bf88a1903   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
2dc8b0387af2   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 3 c2
PING c2 (172.21.0.3): 56 data bytes
64 bytes from 172.21.0.3: seq=0 ttl=64 time=1.355 ms
64 bytes from 172.21.0.3: seq=1 ttl=64 time=0.087 ms
64 bytes from 172.21.0.3: seq=2 ttl=64 time=0.085 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.085/0.509/1.355 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 c4
ping: bad address 'c4'
/ # exit
bradsimpson@ ~:docker container exec -it c3 ash
/ # ping -c 4 c1
ping: bad address 'c1'
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.232 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.102 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.386 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.310 ms

--- 172.17.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.102/0.257/0.386 ms
/ # exit
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
133072a02e44   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
ef43db5a14d2   my_network2    bridge    local
475754f27665   none           null      local
6000c9f47f19   taco_tuesday   bridge    local
bradsimpson@ ~:\clear


# Bind Mounts and Volumes

Last login: Tue Feb  7 12:35:03 on ttys002

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html 
bradsimpson@ app:\clear










bradsimpson@ app:\clear























bradsimpson@ app:cd..
-bash: cd..: command not found
bradsimpson@ app:cd ..
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		docker
bradsimpson@ ~:\clear








































bradsimpson@ ~:docker container run --mount type=bind,source=/path/to/shared/folder,target=path/to/location/in/container
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
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

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
a9cf78790ed8   nginx:alpine   "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   80/tcp    c4
1e72d96d1cbc   nginx:alpine   "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   80/tcp    c3
920bf88a1903   nginx:alpine   "/docker-entrypoint.…"   49 minutes ago   Up 49 minutes   80/tcp    c2
2dc8b0387af2   nginx:alpine   "/docker-entrypoint.…"   49 minutes ago   Up 49 minutes   80/tcp    c1
bradsimpson@ app:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ app:docker contains ls -a
unknown shorthand flag: 'a' in -a
See 'docker --help'.

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "/Users/bradsimpson/.docker")
  -c, --context string     Name of the context to use to connect to the
                           daemon (overrides DOCKER_HOST env var and
                           default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal")
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
  buildx*     Docker Buildx (Docker Inc., v0.9.1)
  compose*    Docker Compose (Docker Inc., v2.13.0)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  dev*        Docker Dev Environments (Docker Inc., v0.0.5)
  extension*  Manages Docker extensions (Docker Inc., v0.2.16)
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
  scan*       Docker Scan (Docker Inc., v0.22.0)
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

bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS     NAMES
a9cf78790ed8   nginx:alpine   "/docker-entrypoint.…"   49 minutes ago   Exited (0) 17 seconds ago             c4
1e72d96d1cbc   nginx:alpine   "/docker-entrypoint.…"   49 minutes ago   Exited (0) 17 seconds ago             c3
920bf88a1903   nginx:alpine   "/docker-entrypoint.…"   49 minutes ago   Exited (0) 17 seconds ago             c2
2dc8b0387af2   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago   Exited (0) 17 seconds ago             c1
b78442678f56   nginx          "/docker-entrypoint.…"   2 hours ago      Exited (0) 51 minutes ago             zen_neumann
bradsimpson@ app:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
a9cf78790ed8d4db031d69da944d454fc3a1f3bf9101e1b85ef77e78e517ca76
1e72d96d1cbcc6820a2b5423ec4f37f598bf2ab83b42058f68688e85858e3219
920bf88a190382b45d9af3ca80ad4f9260bd6b2c4551484e195911a00c4c1114
2dc8b0387af2b13f5a39747ae3c98e52a1db8a556e7622945c87ab6162216796
b78442678f564f9a755ebb08a2dd6303710e260eac63c34c87f11b8be681d959

Total reclaimed space: 5.561kB
bradsimpson@ app:\clear

bradsimpson@ app:cd ..
bradsimpson@ ~:docker container run --mount type=bind,source="($pwd)/app",target=/usr/share/nginx/html -d -p 8000:80 nginx:alpine
docker: Error response from daemon: invalid mount config for type "bind": invalid mount path: '()/app' mount path must be absolute.
See 'docker run --help'.
bradsimpson@ ~:docker container run --mount type=bind,source=/app,target=/usr/share/nginx/html -d -p 8000:80 nginx:alpine
docker: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: /app.
See 'docker run --help'.
bradsimpson@ ~:docker container run --mount type=bind,source=($pwd)/app,target=/usr/share/nginx/html -d -p 8000:80 nginx:alpine
-bash: syntax error near unexpected token `('
bradsimpson@ ~:docker container run --mount type=bind,source=$(pwd)/app,target=/usr/share/nginx/html -d -p 8000:80 nginx:alpine
78190c434fbe5a4b4fa71340a6183dab5cbffbe6f97019863b8e2176142b9a9e
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
78190c434fbe   nginx:alpine   "/docker-entrypoint.…"   52 seconds ago   Up 50 seconds   0.0.0.0:8000->80/tcp   keen_swirles
bradsimpson@ ~:docker container exec -it keen_swirles sh
/ # \ls
bin                   media                 srv
dev                   mnt                   sys
docker-entrypoint.d   opt                   tmp
docker-entrypoint.sh  proc                  usr
etc                   root                  var
home                  run
lib                   sbin
/ # cd usr/
/usr # cd share/
/usr/share # cd nginx/
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html
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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
78190c434fbe   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   keen_swirles
bradsimpson@ ~:\clear

bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html 
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
78190c434fbe   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8000->80/tcp   keen_swirles
bradsimpson@ app:docker container stop keen_swirles
keen_swirles
bradsimpson@ app:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/revisited_react   latest    303fa668755c   3 weeks ago     568MB
my_project                       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/new_project         latest    ae74e957ba0d   3 weeks ago     568MB
bradsimps213/react_project       latest    ae74e957ba0d   3 weeks ago     568MB
bradsimpson213/my_project        latest    ae74e957ba0d   3 weeks ago     568MB
bradsimpson213/react_project     latest    ae74e957ba0d   3 weeks ago     568MB
postgres                         latest    a26eb6069868   6 weeks ago     379MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   3 months ago    560MB
bradsimpson213/test_app2         <none>    8edeca523aef   4 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   5 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   7 months ago    377MB
ubuntu                           latest    27941809078c   8 months ago    77.8MB
nginx                            latest    0e901e68141f   8 months ago    142MB
alpine                           latest    e66264b98777   8 months ago    5.53MB
nginx                            alpine    b1c3acb28882   8 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   16 months ago   13.3kB
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
local     taco_tuesday
bradsimpson@ app:docker volume create new_test_volume
new_test_volume
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     new_test_volume
local     taco_tuesday
bradsimpson@ app:docker container run -p 5431:5432 --name postgres5431 -d --mount type=volume,source=new_test_volume,target=/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres
cd6f5cd44761f4db1e6a72d55594a2977655ebc3035dac7fca5530312b04f7ce
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
cd6f5cd44761   postgres   "docker-entrypoint.s…"   6 seconds ago   Up 4 seconds   0.0.0.0:5431->5432/tcp   postgres5431
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \d
Did not find any relations.
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

postgres=# CREATE DATABASE taco_tesday WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                  List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-------------+----------+----------+------------+------------+-----------------------
 postgres    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 taco_tesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS              PORTS                    NAMES
cd6f5cd44761   postgres   "docker-entrypoint.s…"   2 minutes ago   Up About a minute   0.0.0.0:5431->5432/tcp   postgres5431
bradsimpson@ app:docker container stop postgres5431
postgres5431
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                       PORTS     NAMES
cd6f5cd44761   postgres       "docker-entrypoint.s…"   2 minutes ago    Exited (0) 11 seconds ago              postgres5431
78190c434fbe   nginx:alpine   "/docker-entrypoint.…"   14 minutes ago   Exited (137) 9 minutes ago             keen_swirles
bradsimpson@ app:docker container rm postgres5431
postgres5431
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                       PORTS     NAMES
78190c434fbe   nginx:alpine   "/docker-entrypoint.…"   14 minutes ago   Exited (137) 9 minutes ago             keen_swirles
bradsimpson@ app:\clear
























bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     new_test_volume
local     taco_tuesday
bradsimpson@ app:docker container run -p 5430:5432 -d --mount type=volume,source=new_test_volume,target=/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres
e5e4bb3d49266475940ab7c0b859d8b1c365b1684c0075c520cea92491ef869b
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
e5e4bb3d4926   postgres   "docker-entrypoint.s…"   5 seconds ago   Up 3 seconds   0.0.0.0:5430->5432/tcp   exciting_burnell
bradsimpson@ app:psql -p 5430 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                  List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-------------+----------+----------+------------+------------+-----------------------
 postgres    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 taco_tesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit

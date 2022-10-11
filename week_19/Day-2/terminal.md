Last login: Tue Oct  4 17:39:05 on ttys004

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

bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/test_app2    latest    0c74730ce62a   3 weeks ago     376MB
bradsimpson213/test_app2    <none>    8edeca523aef   3 weeks ago     432MB
postgres                    latest    75993dd36176   4 weeks ago     376MB
bradsimpson213/react_test   latest    4de311ebce05   7 weeks ago     545MB
bradsimpson213/test_react   latest    93489609ef4b   3 months ago    377MB
ubuntu                      latest    27941809078c   4 months ago    77.8MB
nginx                       latest    0e901e68141f   4 months ago    142MB
alpine                      latest    e66264b98777   4 months ago    5.53MB
nginx                       alpine    b1c3acb28882   4 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   12 months ago   13.3kB
bradsimpson@ ~:\clear




bradsimpson@ ~:docker container run nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2022/10/11 15:30:48 [notice] 1#1: using the "epoll" event method
2022/10/11 15:30:48 [notice] 1#1: nginx/1.21.6
2022/10/11 15:30:48 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2022/10/11 15:30:48 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2022/10/11 15:30:48 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/10/11 15:30:48 [notice] 1#1: start worker processes
2022/10/11 15:30:48 [notice] 1#1: start worker process 31
2022/10/11 15:30:48 [notice] 1#1: start worker process 32
^C2022/10/11 15:31:35 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/10/11 15:31:35 [notice] 32#32: exiting
2022/10/11 15:31:35 [notice] 32#32: exit
2022/10/11 15:31:35 [notice] 31#31: exiting
2022/10/11 15:31:35 [notice] 31#31: exit
2022/10/11 15:31:35 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2022/10/11 15:31:35 [notice] 1#1: worker process 32 exited with code 0
2022/10/11 15:31:35 [notice] 1#1: signal 29 (SIGIO) received
2022/10/11 15:31:35 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2022/10/11 15:31:35 [notice] 1#1: worker process 31 exited with code 0
2022/10/11 15:31:35 [notice] 1#1: exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                      PORTS     NAMES
fbe230b977f1   nginx         "/docker-entrypoint.…"   About a minute ago   Exited (0) 55 seconds ago             vigorous_gould
b213e920e9e5   hello-world   "/hello"                 28 minutes ago       Exited (0) 28 minutes ago             xenodochial_cannon
bradsimpson@ ~:\clear




bradsimpson@ ~:docker container run --name my_nginx -p 8000:80 -d nginx
bfe6cebaa3cca13abce37a95f966251439b8f5be9fff2e741df1b3208fa0f5a0
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
bfe6cebaa3cc   nginx     "/docker-entrypoint.…"   9 seconds ago   Up 8 seconds   0.0.0.0:8000->80/tcp, :::8000->80/tcp   my_nginx
bradsimpson@ ~:docker container stop my_ngnix
Error response from daemon: No such container: my_ngnix
bradsimpson@ ~:docker container stop my_nginx
my_nginx
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   2 minutes ago    Exited (0) 9 seconds ago              my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   14 minutes ago   Exited (0) 13 minutes ago             vigorous_gould
b213e920e9e5   hello-world   "/hello"                 41 minutes ago   Exited (0) 41 minutes ago             xenodochial_cannon
bradsimpson@ ~:docker container run -it --name teat_it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd home
/home # \ls
/home # cd ..
/ # cd lib
/lib # \ls
apk                    libc.musl-x86_64.so.1  libz.so.1.2.12
firmware               libcrypto.so.1.1       mdev
ld-musl-x86_64.so.1    libssl.so.1.1          modules-load.d
libapk.so.3.12.0       libz.so.1              sysctl.d
/lib # cd ..
/ # cd sys
/sys # \ls
block       class       devices     fs          kernel      power
bus         dev         firmware    hypervisor  module
/sys # cd ..
/ # ^C
/ # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                        PORTS     NAMES
7f2dfbbed90f   alpine        "sh"                     About a minute ago   Exited (130) 24 seconds ago             teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   8 minutes ago        Exited (0) 6 minutes ago                my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   20 minutes ago       Exited (0) 19 minutes ago               vigorous_gould
b213e920e9e5   hello-world   "/hello"                 47 minutes ago       Exited (0) 47 minutes ago               xenodochial_cannon
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -p 8080:80 -d nginx
e61508e091b73ca43be14bfdcfdd412501442c0033aaf93d8c62c765d2cc1128
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
e61508e091b7   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
bradsimpson@ ~:docker container run -it --name test alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                       PORTS                                   NAMES
8fe5ca4061fe   alpine        "sh"                     22 seconds ago   Exited (0) 13 seconds ago                                            test
e61508e091b7   nginx         "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes                 0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
7f2dfbbed90f   alpine        "sh"                     7 minutes ago    Exited (130) 6 minutes ago                                           teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   15 minutes ago   Exited (0) 12 minutes ago                                            my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   26 minutes ago   Exited (0) 25 minutes ago                                            vigorous_gould
b213e920e9e5   hello-world   "/hello"                 53 minutes ago   Exited (0) 53 minutes ago                                            xenodochial_cannon
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello worldhello world
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                       PORTS                                   NAMES
8fe5ca4061fe   alpine        "sh"                     3 minutes ago    Exited (0) 3 minutes ago                                             test
e61508e091b7   nginx         "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                 0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
7f2dfbbed90f   alpine        "sh"                     10 minutes ago   Exited (130) 9 minutes ago                                           teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   17 minutes ago   Exited (0) 15 minutes ago                                            my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   29 minutes ago   Exited (0) 28 minutes ago                                            vigorous_gould
b213e920e9e5   hello-world   "/hello"                 56 minutes ago   Exited (0) 56 minutes ago                                            xenodochial_cannon
bradsimpson@ ~:\clear




bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
e61508e091b7   nginx     "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                        PORTS                                   NAMES
8fe5ca4061fe   alpine        "sh"                     4 minutes ago    Exited (0) 4 minutes ago                                              test
e61508e091b7   nginx         "/docker-entrypoint.…"   7 minutes ago    Up 6 minutes                  0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
7f2dfbbed90f   alpine        "sh"                     12 minutes ago   Exited (130) 10 minutes ago                                           teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   19 minutes ago   Exited (0) 16 minutes ago                                             my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   30 minutes ago   Exited (0) 29 minutes ago                                             vigorous_gould
b213e920e9e5   hello-world   "/hello"                 57 minutes ago   Exited (0) 57 minutes ago                                             xenodochial_cannon
bradsimpson@ ~:dpcker container stop e61508e091b7
-bash: dpcker: command not found
bradsimpson@ ~:docker container stop e61508e091b7
e61508e091b7
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container start e61508e091b7
e61508e091b7
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
e61508e091b7   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 6 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/test_app2    latest    0c74730ce62a   3 weeks ago     376MB
bradsimpson213/test_app2    <none>    8edeca523aef   3 weeks ago     432MB
postgres                    latest    75993dd36176   4 weeks ago     376MB
bradsimpson213/react_test   latest    4de311ebce05   7 weeks ago     545MB
bradsimpson213/test_react   latest    93489609ef4b   3 months ago    377MB
ubuntu                      latest    27941809078c   4 months ago    77.8MB
nginx                       latest    0e901e68141f   4 months ago    142MB
alpine                      latest    e66264b98777   4 months ago    5.53MB
nginx                       alpine    b1c3acb28882   4 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   12 months ago   13.3kB
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
fc46591dd794   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     postgres-data
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
e61508e091b7   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS                                   NAMES
8fe5ca4061fe   alpine        "sh"                     11 minutes ago      Exited (0) 11 minutes ago                                              test
e61508e091b7   nginx         "/docker-entrypoint.…"   14 minutes ago      Up 3 minutes                   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
7f2dfbbed90f   alpine        "sh"                     19 minutes ago      Exited (130) 18 minutes ago                                            teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   26 minutes ago      Exited (0) 23 minutes ago                                              my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   37 minutes ago      Exited (0) 36 minutes ago                                              vigorous_gould
b213e920e9e5   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago                                           xenodochial_cannon
bradsimpson@ ~:docker container start 8fe5ca4061fe b213e920e9e5
8fe5ca4061fe
b213e920e9e5
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
8fe5ca4061fe   alpine    "sh"                     12 minutes ago   Up 11 seconds                                           test
e61508e091b7   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 5 minutes    0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_khorana
bradsimpson@ ~:docker container stop 8fe5ca4061fe e61508e091b7
8fe5ca4061fe
e61508e091b7
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                          PORTS     NAMES
8fe5ca4061fe   alpine        "sh"                     14 minutes ago      Exited (137) 56 seconds ago               test
e61508e091b7   nginx         "/docker-entrypoint.…"   16 minutes ago      Exited (0) About a minute ago             hardcore_khorana
7f2dfbbed90f   alpine        "sh"                     22 minutes ago      Exited (130) 20 minutes ago               teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   29 minutes ago      Exited (0) 26 minutes ago                 my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   40 minutes ago      Exited (0) 39 minutes ago                 vigorous_gould
b213e920e9e5   hello-world   "/hello"                 About an hour ago   Exited (0) About a minute ago             xenodochial_cannon
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                            PORTS     NAMES
8fe5ca4061fe   alpine        "sh"                     14 minutes ago      Exited (137) About a minute ago             test
e61508e091b7   nginx         "/docker-entrypoint.…"   17 minutes ago      Exited (0) About a minute ago               hardcore_khorana
7f2dfbbed90f   alpine        "sh"                     22 minutes ago      Exited (130) 20 minutes ago                 teat_it
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   29 minutes ago      Exited (0) 26 minutes ago                   my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   40 minutes ago      Exited (0) 39 minutes ago                   vigorous_gould
b213e920e9e5   hello-world   "/hello"                 About an hour ago   Exited (0) 2 minutes ago                    xenodochial_cannon
bradsimpson@ ~:docker container rm teat_it
teat_it
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                            PORTS     NAMES
8fe5ca4061fe   alpine        "sh"                     15 minutes ago      Exited (137) About a minute ago             test
e61508e091b7   nginx         "/docker-entrypoint.…"   17 minutes ago      Exited (0) About a minute ago               hardcore_khorana
bfe6cebaa3cc   nginx         "/docker-entrypoint.…"   29 minutes ago      Exited (0) 27 minutes ago                   my_nginx
fbe230b977f1   nginx         "/docker-entrypoint.…"   41 minutes ago      Exited (0) 40 minutes ago                   vigorous_gould
b213e920e9e5   hello-world   "/hello"                 About an hour ago   Exited (0) 2 minutes ago                    xenodochial_cannon
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
8fe5ca4061fecdca1af6c3f69f7cf66ea6efe62ae6dbf6d2dd9c3526d6ede773
e61508e091b73ca43be14bfdcfdd412501442c0033aaf93d8c62c765d2cc1128
bfe6cebaa3cca13abce37a95f966251439b8f5be9fff2e741df1b3208fa0f5a0
fbe230b977f1532311073627159415dcfbb25cb138fa54dd4fb4ca9b310dbbeb
b213e920e9e5b19611b3bf2e7a7f1aa8c36745a3b75a93fa5282a3d1c85501ab

Total reclaimed space: 3.288kB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear





bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run -d -p 8080:80 nginx
bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
bac4a14681c1   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 3 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   confident_gauss
bradsimpson@ ~:docker container exec -it confident_gauss sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# echo hello world
hello world
# exit 
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
bac4a14681c1   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   confident_gauss
bradsimpson@ ~:docker container inspect confident_gauss
[
    {
        "Id": "bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2",
        "Created": "2022-10-11T16:14:46.322083215Z",
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
            "Pid": 3963,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-10-11T16:14:47.204618863Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2/hostname",
        "HostsPath": "/var/lib/docker/containers/bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2/hosts",
        "LogPath": "/var/lib/docker/containers/bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2/bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2-json.log",
        "Name": "/confident_gauss",
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
                "LowerDir": "/var/lib/docker/overlay2/aee34234fee9e95f3eddfeb556839e2cef37f1bc7ec830ba3297f4a49f9282bb-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/aee34234fee9e95f3eddfeb556839e2cef37f1bc7ec830ba3297f4a49f9282bb/merged",
                "UpperDir": "/var/lib/docker/overlay2/aee34234fee9e95f3eddfeb556839e2cef37f1bc7ec830ba3297f4a49f9282bb/diff",
                "WorkDir": "/var/lib/docker/overlay2/aee34234fee9e95f3eddfeb556839e2cef37f1bc7ec830ba3297f4a49f9282bb/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "bac4a14681c1",
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
            "SandboxID": "3fb1075170850b1872a411f6dff8b7d55545327dacb2a6494256112c9bfd44e0",
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
            "SandboxKey": "/var/run/docker/netns/3fb107517085",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "12935f15599376daa7cf4653493b5362f32744ccac262295c22c0416126e4766",
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
                    "NetworkID": "fc46591dd7948b44e344e826196d98d0487cb7a3e349e83e87b05dcbd79948e3",
                    "EndpointID": "12935f15599376daa7cf4653493b5362f32744ccac262295c22c0416126e4766",
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







bradsimpson@ ~:docker container COMMAND

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











bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
fc46591dd794   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker network create my_network3
7775a70e761db18e8841c7635f06dbc939355fcdc607d2ebb5543a066ed87ecb
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
fc46591dd794   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
7775a70e761d   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:
bradsimpson@ ~:docker container run -d --name c1 --network my_network3 nginx:alpine
0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 3 seconds    80/tcp                                  c1
bac4a14681c1   nginx          "/docker-entrypoint.…"   38 minutes ago   Up 38 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   confident_gauss
bradsimpson@ ~:docker container stop confident)gauss
-bash: syntax error near unexpected token `)'
bradsimpson@ ~:docker container stop confident_gauss
confident_gauss
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   31 seconds ago   Up 29 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c2 --network my_network3 nginx:alpine
7b406bdf47f133d0ca497dc2784a7feafc813e30bbd990ed6d474166820a6404
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago    Up 2 seconds    80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   52 seconds ago   Up 50 seconds   80/tcp    c1
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   9 seconds ago    Up 7 seconds    80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   57 seconds ago   Up 55 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c3 nginx:alpine
f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine
2c1ddb833c1ae14c643205fd71a1a68912f9ba01c94c5a02c063fc2301b4adc1
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
2c1ddb833c1a   nginx:alpine   "/docker-entrypoint.…"   3 seconds ago        Up 2 seconds        80/tcp    c4
f8e1904b753b   nginx:alpine   "/docker-entrypoint.…"   12 seconds ago       Up 11 seconds       80/tcp    c3
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   44 seconds ago       Up 43 seconds       80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container inspect c3
[
    {
        "Id": "f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1",
        "Created": "2022-10-11T16:54:12.454756376Z",
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
            "Pid": 4670,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-10-11T16:54:13.090113809Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/hostname",
        "HostsPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/hosts",
        "LogPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/merged",
                "UpperDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/diff",
                "WorkDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f8e1904b753b",
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
            "SandboxID": "deef974daa9296d92344bc60275b04b086e5e5c3a04f7453642466ff013e31de",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/deef974daa92",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "404d092216c5b335d2a02ce7a7d708ff53a33e406a4298e6870755120c02c46f",
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
                    "NetworkID": "fc46591dd7948b44e344e826196d98d0487cb7a3e349e83e87b05dcbd79948e3",
                    "EndpointID": "404d092216c5b335d2a02ce7a7d708ff53a33e406a4298e6870755120c02c46f",
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
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container inspect c3
[
    {
        "Id": "f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1",
        "Created": "2022-10-11T16:54:12.454756376Z",
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
            "Pid": 4670,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-10-11T16:54:13.090113809Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/hostname",
        "HostsPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/hosts",
        "LogPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/merged",
                "UpperDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/diff",
                "WorkDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f8e1904b753b",
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
            "SandboxID": "deef974daa9296d92344bc60275b04b086e5e5c3a04f7453642466ff013e31de",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/deef974daa92",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "404d092216c5b335d2a02ce7a7d708ff53a33e406a4298e6870755120c02c46f",
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
                    "NetworkID": "fc46591dd7948b44e344e826196d98d0487cb7a3e349e83e87b05dcbd79948e3",
                    "EndpointID": "404d092216c5b335d2a02ce7a7d708ff53a33e406a4298e6870755120c02c46f",
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
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
2c1ddb833c1a   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
f8e1904b753b   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago        Up 3 minutes        80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 3 c2
PING c2 (172.20.0.3): 56 data bytes
64 bytes from 172.20.0.3: seq=0 ttl=64 time=2.334 ms
64 bytes from 172.20.0.3: seq=1 ttl=64 time=0.163 ms
64 bytes from 172.20.0.3: seq=2 ttl=64 time=0.091 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.091/0.862/2.334 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 c4
ping: bad address 'c4'
/ # ping -c 3 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes

--- 172.17.0.2 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
/ # ^C
/ # exit
bradsimpson@ ~:docker container exec -it c4 ash
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.193 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.078 ms
64 bytes from 172.17.0.2: seq=2 ttl=64 time=0.120 ms

--- 172.17.0.2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.078/0.130/0.193 ms
/ # exit
bradsimpson@ ~:\clear



bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
2c1ddb833c1a   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c4
f8e1904b753b   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c3
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   80/tcp    c1
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82",
        "Created": "2022-10-11T16:52:52.006844351Z",
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
            "Pid": 4245,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-10-11T16:52:53.666379288Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82/hostname",
        "HostsPath": "/var/lib/docker/containers/0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82/hosts",
        "LogPath": "/var/lib/docker/containers/0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82/0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/b4e1c1a1684667ce31a3b1b76d231965a0278d251281f47b09763079e37ff93e-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/b4e1c1a1684667ce31a3b1b76d231965a0278d251281f47b09763079e37ff93e/merged",
                "UpperDir": "/var/lib/docker/overlay2/b4e1c1a1684667ce31a3b1b76d231965a0278d251281f47b09763079e37ff93e/diff",
                "WorkDir": "/var/lib/docker/overlay2/b4e1c1a1684667ce31a3b1b76d231965a0278d251281f47b09763079e37ff93e/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0a3395fe752e",
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
            "SandboxID": "d3882a0d0fb2527d93c621675d95ea8a7f29924c99080d5df68cebcde79ce8e6",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/d3882a0d0fb2",
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
                        "0a3395fe752e"
                    ],
                    "NetworkID": "7775a70e761db18e8841c7635f06dbc939355fcdc607d2ebb5543a066ed87ecb",
                    "EndpointID": "a4d22050cb8e2f03fc3525d6d8cd29878f49853e68927136780812eeaf789d7b",
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
bradsimpson@ ~:docker container inspect c3
[
    {
        "Id": "f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1",
        "Created": "2022-10-11T16:54:12.454756376Z",
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
            "Pid": 4670,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-10-11T16:54:13.090113809Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/hostname",
        "HostsPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/hosts",
        "LogPath": "/var/lib/docker/containers/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1/f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/merged",
                "UpperDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/diff",
                "WorkDir": "/var/lib/docker/overlay2/d8029239c1c0511ab9a58dfe0f872257e195012d141a73bfab93ffeba561748d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f8e1904b753b",
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
            "SandboxID": "deef974daa9296d92344bc60275b04b086e5e5c3a04f7453642466ff013e31de",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/deef974daa92",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "404d092216c5b335d2a02ce7a7d708ff53a33e406a4298e6870755120c02c46f",
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
                    "NetworkID": "fc46591dd7948b44e344e826196d98d0487cb7a3e349e83e87b05dcbd79948e3",
                    "EndpointID": "404d092216c5b335d2a02ce7a7d708ff53a33e406a4298e6870755120c02c46f",
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
fc46591dd794   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
7775a70e761d   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     postgres-data
bradsimpson@ ~:

bradsimpson@ ~:docker container run --mount type=bind/volume, source=users/bradsimpson/app2, target=/usr/share/nginx/html
invalid argument "type=bind/volume," for "--mount" flag: invalid field '' must be a key=value pair
See 'docker container run --help'.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
2c1ddb833c1a   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c4
f8e1904b753b   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c3
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Up 45 minutes   80/tcp    c1
bradsimpson@ ~:docker container exec -it c2 ash
/ # \ls
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
/usr/share/nginx # \sl
ash: sl: not found
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html
/usr/share/nginx/html # \ls
50x.html    index.html
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

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
2c1ddb833c1a   nginx:alpine   "/docker-entrypoint.…"   46 minutes ago   Up 46 minutes   80/tcp    c4
f8e1904b753b   nginx:alpine   "/docker-entrypoint.…"   46 minutes ago   Up 46 minutes   80/tcp    c3
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp    c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   80/tcp    c1
bradsimpson@ ~:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ ~:\clear































bradsimpson@ ~:\ls
Applications	Library		Pipfile		app		opt
Desktop		Movies		Pipfile.lock	app.index.html
Documents	Music		Postman		app2
Downloads	Pictures	Public		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
dec.db		index.html
bradsimpson@ app:nano index.html 
bradsimpson@ app:cd .. 
bradsimpson@ ~:docker container run -d -p 8000:80 --mount type=bind, source="$(pwd)/app", target=/usr/share/nginx/html nginx:alpine
invalid argument "type=bind," for "--mount" flag: invalid field '' must be a key=value pair
See 'docker container run --help'.
bradsimpson@ ~:docker container run -d -p 8000:80 --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html nginx:alpine
a7ef8cf06d0afee8fae7ffc389cc34e8ae44113efece6d0cea7caa391665a4bb
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
a7ef8cf06d0a   nginx:alpine   "/docker-entrypoint.…"   7 seconds ago   Up 6 seconds   0.0.0.0:8000->80/tcp, :::8000->80/tcp   crazy_wozniak
bradsimpson@ ~:docker container exec -it crazy_wozniak ash 
/ # \ls
bin                   media                 srv
dev                   mnt                   sys
docker-entrypoint.d   opt                   tmp
docker-entrypoint.sh  proc                  usr
etc                   root                  var
home                  run
lib                   sbin
/ # cd usr
/usr # cd share/nginx/html
/usr/share/nginx/html # \ls
dec.db      index.html
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (5.9-r0)
Executing busybox-1.34.1-r5.trigger
OK: 26 MiB in 43 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
dec.db		index.html
bradsimpson@ app:nano index.html 
bradsimpson@ app:\ls
dec.db		index.html
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container l

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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
a7ef8cf06d0a   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   crazy_wozniak
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                   NAMES
a7ef8cf06d0a   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   crazy_wozniak
bradsimpson@ ~:docker container stop crazy_wozniak
crazy_wozniak
bradsimpson@ ~:\clear








































bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     postgres-data
bradsimpson@ ~:docker volume create taco_tuesday
taco_tuesday
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     postgres-data
local     taco_tuesday
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/test_app2    latest    0c74730ce62a   3 weeks ago     376MB
bradsimpson213/test_app2    <none>    8edeca523aef   3 weeks ago     432MB
postgres                    latest    75993dd36176   4 weeks ago     376MB
bradsimpson213/react_test   latest    4de311ebce05   7 weeks ago     545MB
bradsimpson213/test_react   latest    93489609ef4b   3 months ago    377MB
ubuntu                      latest    27941809078c   4 months ago    77.8MB
nginx                       latest    0e901e68141f   4 months ago    142MB
alpine                      latest    e66264b98777   4 months ago    5.53MB
nginx                       alpine    b1c3acb28882   4 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   12 months ago   13.3kB
bradsimpson@ ~:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:e71e4f897079e9e2efea20b3d181e400f502887cbe1fc0b65c7135b6455aef09
Deleted: sha256:75993dd36176c7d4be8c1e6d88a115f1fb35a85451088699dbdc80659ad688ed
Deleted: sha256:c7c46d892ab03c575798d792c78b3a59f580f20e2dfc83efcceb2942420a1b89
Deleted: sha256:0a028c3187e5c4d5b4e75f5f89c4726b8dae72550e3a34071fbdf9db19ff9d14
Deleted: sha256:e44d4f50c963163e8a54219acca05ba01ebaf4df0a7fd344d1ae054e5b453203
Deleted: sha256:b60726f52baafec96184868879944ea86894d445746bdaaf138a2fa38e756849
Deleted: sha256:6192509d9485332e30e5f40eef5f0c96c74b91c81c423cd0d6849268916d9347
Deleted: sha256:4896f2332587807947e808c449c3157412292e6bc001592f07cd24fe9cd24517
Deleted: sha256:2070401e45e168ea76c6cd27d1dc7664a7a2cbc3315d9265f71081dee9f9fc4c
Deleted: sha256:4828ef329129f389154ce6e76d0835ffe96742c35f6e0c65ac43e6e5cacde97d
Deleted: sha256:49d905bbd7e4f2eb98bf8b08fc719a08eec194f159ad295fec4fc82dbdc4691d
Deleted: sha256:cabc4e0e1d534df58105e8274c40744cd24b188516b4d94177e263005a67bb98
Deleted: sha256:741715b3a5e3671b8790a10d0794f781065e1b39532c64e585f1fd0ab304b397
Deleted: sha256:a813d1a2587f9b8bad58fd9d6b598bd0c8f8db5ace833d58f1f76c3e5df973d8
Deleted: sha256:b45078e74ec97c5e600f6d5de8ce6254094fb3cb4dc5e1cc8335fb31664af66e
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/test_app2    latest    0c74730ce62a   3 weeks ago     376MB
bradsimpson213/test_app2    <none>    8edeca523aef   3 weeks ago     432MB
bradsimpson213/react_test   latest    4de311ebce05   7 weeks ago     545MB
bradsimpson213/test_react   latest    93489609ef4b   3 months ago    377MB
ubuntu                      latest    27941809078c   4 months ago    77.8MB
nginx                       latest    0e901e68141f   4 months ago    142MB
alpine                      latest    e66264b98777   4 months ago    5.53MB
nginx                       alpine    b1c3acb28882   4 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   12 months ago   13.3kB
bradsimpson@ ~:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
bd159e379b3b: Pull complete 
b955aac8d5e0: Pull complete 
922fe4565b9a: Pull complete 
c39aa91943e9: Pull complete 
59e6d12f4c90: Pull complete 
d058e68b8750: Pull complete 
03549096a058: Pull complete 
c941aeed5670: Pull complete 
de6ada71681e: Pull complete 
05fe2d19a511: Pull complete 
4d05d65606f6: Pull complete 
da6c2869b374: Pull complete 
57577a098de9: Pull complete 
Digest: sha256:640fa552e4f0e71f2bd369ad615779385442f7d447d1600f8f2c385b51edb336
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
postgres                    latest    e270a11b9c8a   6 days ago      376MB
bradsimpson213/test_app2    latest    0c74730ce62a   3 weeks ago     376MB
bradsimpson213/test_app2    <none>    8edeca523aef   3 weeks ago     432MB
bradsimpson213/react_test   latest    4de311ebce05   7 weeks ago     545MB
bradsimpson213/test_react   latest    93489609ef4b   3 months ago    377MB
ubuntu                      latest    27941809078c   4 months ago    77.8MB
nginx                       latest    0e901e68141f   4 months ago    142MB
alpine                      latest    e66264b98777   4 months ago    5.53MB
nginx                       alpine    b1c3acb28882   4 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   12 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker image inspect postgres
[
    {
        "Id": "sha256:e270a11b9c8a719c4f501c34f1fccf7de89cda4d95e6e6ec9cadc73bdb1ae6d5",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:640fa552e4f0e71f2bd369ad615779385442f7d447d1600f8f2c385b51edb336"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-10-05T09:06:10.117054765Z",
        "Container": "0ccf364d28f7599ca58061633310d3f89f98f464b607fad4c9c0c6d7d548817c",
        "ContainerConfig": {
            "Hostname": "0ccf364d28f7",
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
            "Image": "sha256:3e12da8c65baee371b95506277f721b75db51ee8797cc8040f4690c618034551",
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
            "Image": "sha256:3e12da8c65baee371b95506277f721b75db51ee8797cc8040f4690c618034551",
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
        "Size": 376282245,
        "VirtualSize": 376282245,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/3501367acaf10cc0947665be29dfc6b1ba807465a1a4d38692dfabfd488d68ab/diff:/var/lib/docker/overlay2/d5a08c91e9f4832c4273406d7330ff1cbbbe08baa641c0fe42e0f917adeb26a8/diff:/var/lib/docker/overlay2/d0a55235ca9ff46416284ba8c8c13a2b3cdc09f49e9f8612daf0caffc7691375/diff:/var/lib/docker/overlay2/a9001690a3ba4d45a2add33d62c7e11f4434d82a9f7f72b172c21a1332d1307f/diff:/var/lib/docker/overlay2/8e8d7ce857158f3998ccde9d996b1218f332d5a26964712baa4af1c52090e46f/diff:/var/lib/docker/overlay2/7713d9894f69441e391c724b86334929e854833e3890f1669cb0b1aefe15025a/diff:/var/lib/docker/overlay2/b9aba1dc2747e9ca8d6766a71909593a8e9c7135159987bda957d78da5616d43/diff:/var/lib/docker/overlay2/8549dc16db5eef70a196cd5bb00b50f799e42d092e6bb390ba319bb67dec0039/diff:/var/lib/docker/overlay2/754dca284523641f4da0ab1461398c2fa0628d6ff3810a803b497b08c8b9ea11/diff:/var/lib/docker/overlay2/b0d300387b7a9dbd185b1e591c294a07454bc072dfd3afb4c660153a258e89f3/diff:/var/lib/docker/overlay2/f7cef0a38d826dd7cbeca547149d1be5498505e5106024884c0b14e37ffe942c/diff:/var/lib/docker/overlay2/7dc50721e3f741cf54dbc9845b5b3385694ab98ceac9298d46d3604c6fb13241/diff",
                "MergedDir": "/var/lib/docker/overlay2/bd76e7fd5bbc1b83b21f2ec60059de57d6f1d4a7140aa777d1f05b37f929f3ba/merged",
                "UpperDir": "/var/lib/docker/overlay2/bd76e7fd5bbc1b83b21f2ec60059de57d6f1d4a7140aa777d1f05b37f929f3ba/diff",
                "WorkDir": "/var/lib/docker/overlay2/bd76e7fd5bbc1b83b21f2ec60059de57d6f1d4a7140aa777d1f05b37f929f3ba/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:fe7b1e9bf7922fbc22281bcc6b4f5ac8f1a7b4278929880940978c42fc9d0229",
                "sha256:cf1c1d4e7b970cff84425af42b2cb4ba5e635ffcb97000925e8022264df934d4",
                "sha256:a560084a04efa3e75519796d24a4b9c2db8b594dbd043f537e9e350907d9d05c",
                "sha256:596139a369da06580f5bb60799cd821af643580440dc3c864aa6e88dad9069da",
                "sha256:8b56e06d2fd794bd063ba61618e29679aa303b62a5259212fc7690ac059402b6",
                "sha256:afa3537bdcd4a91804325ecbac0c15502041d394bd11a94c6bedb77deef24863",
                "sha256:421ac1c18bca65072f73db57a5f2fc249a364c594f75f4e1e4a521f2a9d4dced",
                "sha256:89be899c57c887d655d5c768926a091f335d47dbf3276819974c10ce375b081b",
                "sha256:ea711c00598891e0115c5a169ec18ea56d0043c011dfdfdae2d0afed0fb43ae7",
                "sha256:acdde886f333248d2c3ec6d876dbae8e76bc17655fdcfdb0f9ae1694458cb273",
                "sha256:0dfa4efd26e64f5598a9e4702114807d9c89dba5b0893e976c62661d7890ef13",
                "sha256:3f5562cabc06ce4ebcc0b5d8c0facd44335eb8744c0546a8efa6f5c3e43e493f",
                "sha256:8eb479c4888d212b5a5c652ea159ddcd198b13f836a6896c7c7eda16d2d00120"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgres5431 -d --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data postgres
8b984c29c43df249ef2cc7104a8e852ed6c4620a2e664ebd4b508d21ec33ce3e
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
8b984c29c43d   postgres   "docker-entrypoint.s…"   6 seconds ago   Up 4 seconds   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
bradsimpson@ ~:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 14.5 (Debian 14.5-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
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

...skipping...
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
postgres=# CREATE DATABASE tacos_yum WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 tacos_yum | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
8b984c29c43d   postgres   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
bradsimpson@ ~:docker container stop postgres5431
postgres5431
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS     NAMES
8b984c29c43d   postgres       "docker-entrypoint.s…"   2 minutes ago       Exited (0) 8 seconds ago                 postgres5431
a7ef8cf06d0a   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago      Exited (0) 12 minutes ago                crazy_wozniak
2c1ddb833c1a   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 22 minutes ago                c4
f8e1904b753b   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 22 minutes ago                c3
7b406bdf47f1   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 22 minutes ago                c2
0a3395fe752e   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 22 minutes ago                c1
bac4a14681c1   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago             confident_gauss
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
8b984c29c43df249ef2cc7104a8e852ed6c4620a2e664ebd4b508d21ec33ce3e
a7ef8cf06d0afee8fae7ffc389cc34e8ae44113efece6d0cea7caa391665a4bb
2c1ddb833c1ae14c643205fd71a1a68912f9ba01c94c5a02c063fc2301b4adc1
f8e1904b753ba818a31b1a64ca6fdf36e33b3b7450e59bba88b1a400b88281e1
7b406bdf47f133d0ca497dc2784a7feafc813e30bbd990ed6d474166820a6404
0a3395fe752e3ed59dc91a2ebe71a815f448f298aa7d4f6b2a31b3df0fec6d82
bac4a14681c1f4bf45b9e5f4aab664778ea2639cc82c21be46a8608b3076dcf2

Total reclaimed space: 8.138MB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear






bradsimpson@ ~:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name taco_for_lunch -d --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data postgres
e323bd36d51b3a9dbd2a4535b2776bf81ef94336ec60ce60cb4e9ca9ab5d8102
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
e323bd36d51b   postgres   "docker-entrypoint.s…"   6 seconds ago   Up 5 seconds   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 14.5 (Debian 14.5-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 tacos_yum | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# 
postgres=# exit
bradsimpson@ ~:


# CONTAINER CLI

Last login: Wed May 31 10:32:14 on ttys004

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
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
postgres      latest    ceccf204404e   7 weeks ago     379MB
nginx         alpine    2bc7edbc3cf2   3 months ago    40.7MB
ubuntu        latest    27941809078c   11 months ago   77.8MB
nginx         latest    0e901e68141f   12 months ago   142MB
alpine        latest    e66264b98777   12 months ago   5.53MB
hello-world   latest    feb5d9fea6a5   20 months ago   13.3kB
bradsimpson@ ~:\clear









bradsimpson@ ~:docker container run [options or flags] image-name [commands/parameters]
docker: invalid reference format.
See 'docker run --help'.
bradsimpson@ ~:docker container run --name cool_container -p 8000:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/05/31 15:14:43 [notice] 1#1: using the "epoll" event method
2023/05/31 15:14:43 [notice] 1#1: nginx/1.21.6
2023/05/31 15:14:43 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/05/31 15:14:43 [notice] 1#1: OS: Linux 5.15.49-linuxkit
2023/05/31 15:14:43 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/05/31 15:14:43 [notice] 1#1: start worker processes
2023/05/31 15:14:43 [notice] 1#1: start worker process 30
2023/05/31 15:14:43 [notice] 1#1: start worker process 31
172.17.0.1 - - [31/May/2023:15:15:16 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
2023/05/31 15:15:17 [error] 31#31: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
172.17.0.1 - - [31/May/2023:15:15:17 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [31/May/2023:15:15:43 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
^C2023/05/31 15:16:02 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/05/31 15:16:02 [notice] 31#31: exiting
2023/05/31 15:16:02 [notice] 31#31: exit
2023/05/31 15:16:02 [notice] 30#30: exiting
2023/05/31 15:16:02 [notice] 30#30: exit
2023/05/31 15:16:02 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2023/05/31 15:16:02 [notice] 1#1: worker process 30 exited with code 0
2023/05/31 15:16:02 [notice] 1#1: signal 29 (SIGIO) received
2023/05/31 15:16:02 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/05/31 15:16:02 [notice] 1#1: worker process 31 exited with code 0
2023/05/31 15:16:02 [notice] 1#1: exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
6a16bb633c6c   nginx     "/docker-entrypoint.…"   2 minutes ago   Exited (0) 50 seconds ago             cool_container
bradsimpson@ ~:docker container run -p 8000:80 -d nginx
7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   40 seconds ago   Up 38 seconds   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container run -it --rm alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd lib
/lib # \ls
apk                    libc.musl-x86_64.so.1  libz.so.1.2.12
firmware               libcrypto.so.1.1       mdev
ld-musl-x86_64.so.1    libssl.so.1.1          modules-load.d
libapk.so.3.12.0       libz.so.1              sysctl.d
/lib # cd ..
/ # \ls
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
/bin # ^C
/bin # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
7891a299d4e9   nginx         "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:8000->80/tcp   funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   7 minutes ago    Exited (0) 6 minutes ago                           cool_container
e82e618eebf6   hello-world   "/hello"                 16 minutes ago   Exited (0) 16 minutes ago                          wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago                            awesome_swanson
bradsimpson@ ~:docker container run -it alpine sh
/ # exit
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
80aaa925575e   alpine        "sh"                     6 seconds ago    Exited (0) 2 seconds ago                           cranky_gagarin
7891a299d4e9   nginx         "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8000->80/tcp   funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   8 minutes ago    Exited (0) 6 minutes ago                           cool_container
e82e618eebf6   hello-world   "/hello"                 16 minutes ago   Exited (0) 16 minutes ago                          wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago                            awesome_swanson
bradsimpson@ ~:docker container run -p 8080:80 -d nginx 
2554f45a6028696869211d9d6c98e9149d425b0ab51fcfc362f0d12c805e4dfd
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
2554f45a6028   nginx     "/docker-entrypoint.…"   20 seconds ago   Up 19 seconds   0.0.0.0:8080->80/tcp   strange_lederberg
7891a299d4e9   nginx     "/docker-entrypoint.…"   7 minutes ago    Up 7 minutes    0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container run --name test -it alpine sh
/ # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                  NAMES
2554f45a6028   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp   strange_lederberg
7891a299d4e9   nginx     "/docker-entrypoint.…"   9 minutes ago        Up 9 minutes        0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
6d88665df235   alpine        "sh"                     20 seconds ago   Exited (0) 16 seconds ago                          test
2554f45a6028   nginx         "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes                0.0.0.0:8080->80/tcp   strange_lederberg
80aaa925575e   alpine        "sh"                     4 minutes ago    Exited (0) 4 minutes ago                           cranky_gagarin
7891a299d4e9   nginx         "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes                0.0.0.0:8000->80/tcp   funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   12 minutes ago   Exited (0) 11 minutes ago                          cool_container
e82e618eebf6   hello-world   "/hello"                 20 minutes ago   Exited (0) 20 minutes ago                          wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago                            awesome_swanson
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run --name greet_me -rm ubuntu echo hello world
unknown shorthand flag: 'r' in -rm
See 'docker container run --help'.
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@ ~:echo hello world
hello world
bradsimpson@ ~:docker container ls 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
2554f45a6028   nginx     "/docker-entrypoint.…"   3 minutes ago    Up 3 minutes    0.0.0.0:8080->80/tcp   strange_lederberg
7891a299d4e9   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
6d88665df235   alpine        "sh"                     2 minutes ago    Exited (0) 2 minutes ago                           test
2554f45a6028   nginx         "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:8080->80/tcp   strange_lederberg
80aaa925575e   alpine        "sh"                     6 minutes ago    Exited (0) 6 minutes ago                           cranky_gagarin
7891a299d4e9   nginx         "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes               0.0.0.0:8000->80/tcp   funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   14 minutes ago   Exited (0) 12 minutes ago                          cool_container
e82e618eebf6   hello-world   "/hello"                 22 minutes ago   Exited (0) 22 minutes ago                          wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago                            awesome_swanson
bradsimpson@ ~:\clear


















bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
2554f45a6028   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8080->80/tcp   strange_lederberg
7891a299d4e9   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 12 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container stop strange_lederberg 7891a299d4e9
strange_lederberg
7891a299d4e9
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
6d88665df235   alpine        "sh"                     4 minutes ago    Exited (0) 4 minutes ago              test
2554f45a6028   nginx         "/docker-entrypoint.…"   5 minutes ago    Exited (0) 16 seconds ago             strange_lederberg
80aaa925575e   alpine        "sh"                     8 minutes ago    Exited (0) 8 minutes ago              cranky_gagarin
7891a299d4e9   nginx         "/docker-entrypoint.…"   13 minutes ago   Exited (0) 16 seconds ago             funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   16 minutes ago   Exited (0) 14 minutes ago             cool_container
e82e618eebf6   hello-world   "/hello"                 24 minutes ago   Exited (0) 24 minutes ago             wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago               awesome_swanson
bradsimpson@ ~:docker container start -d -p 5000:80 funny_dewdney
unknown shorthand flag: 'd' in -d
See 'docker container start --help'.
bradsimpson@ ~:docker container start funny_dewdney
funny_dewdney
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 6 seconds   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container rm test
test
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
2554f45a6028   nginx         "/docker-entrypoint.…"   8 minutes ago    Exited (0) 2 minutes ago                           strange_lederberg
80aaa925575e   alpine        "sh"                     10 minutes ago   Exited (0) 10 minutes ago                          cranky_gagarin
7891a299d4e9   nginx         "/docker-entrypoint.…"   15 minutes ago   Up 59 seconds               0.0.0.0:8000->80/tcp   funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   18 minutes ago   Exited (0) 17 minutes ago                          cool_container
e82e618eebf6   hello-world   "/hello"                 27 minutes ago   Exited (0) 27 minutes ago                          wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago                            awesome_swanson
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS              PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   16 minutes ago   Up About a minute   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
2554f45a6028   nginx         "/docker-entrypoint.…"   8 minutes ago    Exited (0) 3 minutes ago                           strange_lederberg
80aaa925575e   alpine        "sh"                     11 minutes ago   Exited (0) 11 minutes ago                          cranky_gagarin
7891a299d4e9   nginx         "/docker-entrypoint.…"   16 minutes ago   Up About a minute           0.0.0.0:8000->80/tcp   funny_dewdney
6a16bb633c6c   nginx         "/docker-entrypoint.…"   19 minutes ago   Exited (0) 17 minutes ago                          cool_container
e82e618eebf6   hello-world   "/hello"                 27 minutes ago   Exited (0) 27 minutes ago                          wizardly_thompson
28ce98007e83   hello-world   "/hello"                 19 hours ago     Exited (0) 19 hours ago                            awesome_swanson
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
2554f45a6028696869211d9d6c98e9149d425b0ab51fcfc362f0d12c805e4dfd
80aaa925575ed36af29268623aa6ee8564641c0802e1ca185e2cdf93a563d0dc
6a16bb633c6c9f6b78a8b5575b48c4f0b3d713886fabf93ac1ef18fdb9f9cd98
e82e618eebf6f4aa79d0896d4064d8f97cc80cc0c22b958baba63c460866e899
28ce98007e830e33a9c7c8a76ea4acea3ddce82a0f853a574056ff047069b2f2

Total reclaimed space: 2.191kB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS              PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   16 minutes ago   Up About a minute   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   16 minutes ago   Up 2 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   17 minutes ago   Up 2 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:\clear



bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   17 minutes ago   Up 2 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container exec -it funny_dewdney sh
# \ls   
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# cd usr	
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share
# \ls
X11		 debianutils  info	  misc		  tabset
adduser		 dict	      java	  nginx		  terminfo
base-files	 doc	      keyrings	  pam		  ucf
base-passwd	 doc-base     libc-bin	  pam-configs	  xml
bash-completion  dpkg	      lintian	  perl5		  zoneinfo
bug		 fontconfig   locale	  pixmaps	  zsh
ca-certificates  fonts	      man	  polkit-1
common-licenses  gcc	      maven-repo  readline
debconf		 gdb	      menu	  sensible-utils
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
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   20 minutes ago   Up 6 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:

# NETWORKING

Last login: Wed May 31 11:39:34 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
2ee89bb0bf95   bridge         bridge    local
7318efe60d0f   host           host      local
e462f118fac6   my_network     bridge    local
475754f27665   none           null      local
0d6561636bf9   taco_network   bridge    local
bradsimpson@ ~:docker conatainer ls
docker: 'conatainer' is not a docker command.
See 'docker --help'
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   29 minutes ago   Up 14 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container inspect funny_dewdney
[
    {
        "Id": "7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794",
        "Created": "2023-05-31T15:17:28.982082673Z",
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
            "Pid": 2917,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-31T15:32:23.492579525Z",
            "FinishedAt": "2023-05-31T15:30:34.355101047Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794/hostname",
        "HostsPath": "/var/lib/docker/containers/7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794/hosts",
        "LogPath": "/var/lib/docker/containers/7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794/7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794-json.log",
        "Name": "/funny_dewdney",
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
                "LowerDir": "/var/lib/docker/overlay2/8cb49aec41871feb620fd96da2e41dddfcd5252b72a42a8b7b14cfbd57da4fbc-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/8cb49aec41871feb620fd96da2e41dddfcd5252b72a42a8b7b14cfbd57da4fbc/merged",
                "UpperDir": "/var/lib/docker/overlay2/8cb49aec41871feb620fd96da2e41dddfcd5252b72a42a8b7b14cfbd57da4fbc/diff",
                "WorkDir": "/var/lib/docker/overlay2/8cb49aec41871feb620fd96da2e41dddfcd5252b72a42a8b7b14cfbd57da4fbc/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "7891a299d4e9",
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
            "SandboxID": "f600b557101bc7fe99a08598d8fc71787e7a831a7ea18a291e36a7db385edc88",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "8000"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/f600b557101b",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "56cf83652458846e095631da669f0253442dff8d273a7ba7677eebad601db372",
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
                    "NetworkID": "2ee89bb0bf95f5b810a9dd0b4256a272f6e7b9178fc3bce5151d97e07262371e",
                    "EndpointID": "56cf83652458846e095631da669f0253442dff8d273a7ba7677eebad601db372",
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
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
2ee89bb0bf95   bridge         bridge    local
7318efe60d0f   host           host      local
e462f118fac6   my_network     bridge    local
475754f27665   none           null      local
0d6561636bf9   taco_network   bridge    local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
7891a299d4e9   nginx     "/docker-entrypoint.…"   49 minutes ago   Up 34 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
2ee89bb0bf95   bridge         bridge    local
7318efe60d0f   host           host      local
e462f118fac6   my_network     bridge    local
475754f27665   none           null      local
0d6561636bf9   taco_network   bridge    local
bradsimpson@ ~:docker network create wing_wednesday
fac97caaa0e3d3b751006d1c37f54b60effefbb3cdbd528156e45925e4fda58b
bradsimpson@ ~:docker network ls
NETWORK ID     NAME             DRIVER    SCOPE
2ee89bb0bf95   bridge           bridge    local
7318efe60d0f   host             host      local
e462f118fac6   my_network       bridge    local
475754f27665   none             null      local
0d6561636bf9   taco_network     bridge    local
fac97caaa0e3   wing_wednesday   bridge    local
bradsimpson@ ~:docker container run -d --name c1 --network wing_wednesday nginx:alpine
92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7
bradsimpson@ ~:docker container run -d --name c2 --network wing_wednesday nginx:alpine
83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
83f63fef1efd   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago    Up 3 seconds    80/tcp                 c2
92f3e94b48b2   nginx:alpine   "/docker-entrypoint.…"   12 seconds ago   Up 11 seconds   80/tcp                 c1
7891a299d4e9   nginx          "/docker-entrypoint.…"   52 minutes ago   Up 37 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container run -d --name c3 nginx:alpine
1d8851b84df0a014a37574ae4afd01c69772d278fc9d5e58106f347647ea9863
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine
132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
132253a7b7f4   nginx:alpine   "/docker-entrypoint.…"   7 seconds ago    Up 6 seconds    80/tcp                 c4
1d8851b84df0   nginx:alpine   "/docker-entrypoint.…"   13 seconds ago   Up 12 seconds   80/tcp                 c3
83f63fef1efd   nginx:alpine   "/docker-entrypoint.…"   33 seconds ago   Up 32 seconds   80/tcp                 c2
92f3e94b48b2   nginx:alpine   "/docker-entrypoint.…"   41 seconds ago   Up 40 seconds   80/tcp                 c1
7891a299d4e9   nginx          "/docker-entrypoint.…"   52 minutes ago   Up 37 minutes   0.0.0.0:8000->80/tcp   funny_dewdney
bradsimpson@ ~:docker container stop funny_dewdney
funny_dewdney
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
132253a7b7f4   nginx:alpine   "/docker-entrypoint.…"   32 seconds ago       Up 32 seconds       80/tcp    c4
1d8851b84df0   nginx:alpine   "/docker-entrypoint.…"   38 seconds ago       Up 38 seconds       80/tcp    c3
83f63fef1efd   nginx:alpine   "/docker-entrypoint.…"   58 seconds ago       Up 57 seconds       80/tcp    c2
92f3e94b48b2   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc",
        "Created": "2023-05-31T16:09:58.007871379Z",
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
            "Pid": 3421,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-31T16:09:58.616665507Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc/hostname",
        "HostsPath": "/var/lib/docker/containers/132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc/hosts",
        "LogPath": "/var/lib/docker/containers/132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc/132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/de26261c89bf958ccb08689ba4b7674083e2a568bbd4bb3e594a82827047b6bc-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/de26261c89bf958ccb08689ba4b7674083e2a568bbd4bb3e594a82827047b6bc/merged",
                "UpperDir": "/var/lib/docker/overlay2/de26261c89bf958ccb08689ba4b7674083e2a568bbd4bb3e594a82827047b6bc/diff",
                "WorkDir": "/var/lib/docker/overlay2/de26261c89bf958ccb08689ba4b7674083e2a568bbd4bb3e594a82827047b6bc/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "132253a7b7f4",
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
                "NGINX_VERSION=1.23.3",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.9"
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
            "SandboxID": "dd0608209959dc66572d16992db849a6971cb80557442fb96311f62e90de3bc4",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/dd0608209959",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "c0fa49e974264bc24236c081faba5173814ae8b00ceb71fd60fffd3bf2dcd5b5",
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
                    "NetworkID": "2ee89bb0bf95f5b810a9dd0b4256a272f6e7b9178fc3bce5151d97e07262371e",
                    "EndpointID": "c0fa49e974264bc24236c081faba5173814ae8b00ceb71fd60fffd3bf2dcd5b5",
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
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
132253a7b7f4   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
1d8851b84df0   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
83f63fef1efd   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
92f3e94b48b2   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 4 c2
PING c2 (172.20.0.3): 56 data bytes
64 bytes from 172.20.0.3: seq=0 ttl=64 time=0.960 ms
64 bytes from 172.20.0.3: seq=1 ttl=64 time=0.124 ms
64 bytes from 172.20.0.3: seq=2 ttl=64 time=0.089 ms
64 bytes from 172.20.0.3: seq=3 ttl=64 time=0.083 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.083/0.314/0.960 ms
/ # exit
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7",
        "Created": "2023-05-31T16:09:24.117234496Z",
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
            "Pid": 3069,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-31T16:09:24.888064391Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7/hostname",
        "HostsPath": "/var/lib/docker/containers/92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7/hosts",
        "LogPath": "/var/lib/docker/containers/92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7/92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7-json.log",
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
            "NetworkMode": "wing_wednesday",
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
                "LowerDir": "/var/lib/docker/overlay2/0effd801e64a2214067f157bb5a41dda371e4c39dca918be18cf274640cc186d-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/0effd801e64a2214067f157bb5a41dda371e4c39dca918be18cf274640cc186d/merged",
                "UpperDir": "/var/lib/docker/overlay2/0effd801e64a2214067f157bb5a41dda371e4c39dca918be18cf274640cc186d/diff",
                "WorkDir": "/var/lib/docker/overlay2/0effd801e64a2214067f157bb5a41dda371e4c39dca918be18cf274640cc186d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "92f3e94b48b2",
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
                "NGINX_VERSION=1.23.3",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.9"
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
            "SandboxID": "9a374d1841e385bf0508bb8dca160648f0da48724ab5a88629c46ddf281db315",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/9a374d1841e3",
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
                "wing_wednesday": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "92f3e94b48b2"
                    ],
                    "NetworkID": "fac97caaa0e3d3b751006d1c37f54b60effefbb3cdbd528156e45925e4fda58b",
                    "EndpointID": "03e0c4e08fcc04cc626c20670b7cf2dcf8b5f64d577cb90cd0604418df075204",
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
bradsimpson@ ~:docker container inspect c2
[
    {
        "Id": "83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968",
        "Created": "2023-05-31T16:09:32.341695902Z",
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
            "Pid": 3195,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-31T16:09:33.034646904Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968/hostname",
        "HostsPath": "/var/lib/docker/containers/83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968/hosts",
        "LogPath": "/var/lib/docker/containers/83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968/83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968-json.log",
        "Name": "/c2",
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
            "NetworkMode": "wing_wednesday",
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
                "LowerDir": "/var/lib/docker/overlay2/30fcab63238b60190affca94c29768125ae34b8b7053ab6373122e07efaf6275-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/30fcab63238b60190affca94c29768125ae34b8b7053ab6373122e07efaf6275/merged",
                "UpperDir": "/var/lib/docker/overlay2/30fcab63238b60190affca94c29768125ae34b8b7053ab6373122e07efaf6275/diff",
                "WorkDir": "/var/lib/docker/overlay2/30fcab63238b60190affca94c29768125ae34b8b7053ab6373122e07efaf6275/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "83f63fef1efd",
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
                "NGINX_VERSION=1.23.3",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.9"
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
            "SandboxID": "265a3718ec68923669495c80305798a15654eeff363b4244ec4c95086a9ef6d5",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/265a3718ec68",
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
                "wing_wednesday": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "83f63fef1efd"
                    ],
                    "NetworkID": "fac97caaa0e3d3b751006d1c37f54b60effefbb3cdbd528156e45925e4fda58b",
                    "EndpointID": "0a6585724fcb057e432b1c3c79739acacef63e6c973252a2c2ea9b8721439070",
                    "Gateway": "172.20.0.1",
                    "IPAddress": "172.20.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:14:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container exec -it c3 ash
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.403 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.101 ms
64 bytes from 172.17.0.4: seq=2 ttl=64 time=0.088 ms
64 bytes from 172.17.0.4: seq=3 ttl=64 time=0.207 ms

--- 172.17.0.4 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.088/0.199/0.403 ms
/ # exit
bradsimpson@ ~:



# BIND MOUNTS & VOLUMES

Last login: Wed May 31 11:41:11 on ttys005

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
132253a7b7f4   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c4
1d8851b84df0   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c3
83f63fef1efd   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c2
92f3e94b48b2   nginx:alpine   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   80/tcp    c1
bradsimpson@ ~:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ ~:\clear


























bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     even_more_tacos
local     tuesday_taco
bradsimpson@ ~:--mount type=bind,source=/path/to/folder,target=/path/in/container
-bash: --mount: command not found
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		oct-starter
Desktop		Library		Pictures	app		opt
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:ls
index.html
bradsimpson@ app:nano index/html
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

bradsimpson@ app:docker container run -d -p 8000:80 --mount type=bind,source="$(pwd)",target=/usr/share/nginx/html nginx:alpine
1d942f3002b16d692da70e3ee2c559661434bf752f43c7deb31b158ec1cb4237
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
1d942f3002b1   nginx:alpine   "/docker-entrypoint.…"   18 seconds ago   Up 17 seconds   0.0.0.0:8000->80/tcp   thirsty_heisenberg
bradsimpson@ app:docker container exec -it thirsty_heisenberg ash
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
/usr/share # \ls
GeoIP            ca-certificates  licenses         nginx            zoneinfo
X11              doc              man              udhcpc
apk              fontconfig       misc             xml
/usr/share # cd nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html/
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 43 MiB in 63 packages
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ app:nano index.html 
bradsimpson@ app:docker volume inspect
"docker volume inspect" requires at least 1 argument.
See 'docker volume inspect --help'.

Usage:  docker volume inspect [OPTIONS] VOLUME [VOLUME...]

Display detailed information on one or more volumes
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     even_more_tacos
local     tuesday_taco
bradsimpson@ app:docker volume create wing_wednesday
wing_wednesday
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     even_more_tacos
local     tuesday_taco
local     wing_wednesday
bradsimpson@ app:docker volume inspect tuesday_taco
[
    {
        "CreatedAt": "2023-04-04T17:54:03Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/tuesday_taco/_data",
        "Name": "tuesday_taco",
        "Options": {},
        "Scope": "local"
    }
]
bradsimpson@ app:docker volume rm even_more_tacos
even_more_tacos
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     tuesday_taco
local     wing_wednesday
bradsimpson@ app:docker image inspect
"docker image inspect" requires at least 1 argument.
See 'docker image inspect --help'.

Usage:  docker image inspect [OPTIONS] IMAGE [IMAGE...]

Display detailed information on one or more images
bradsimpson@ app:docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
postgres      latest    ceccf204404e   7 weeks ago     379MB
nginx         alpine    2bc7edbc3cf2   3 months ago    40.7MB
ubuntu        latest    27941809078c   11 months ago   77.8MB
nginx         latest    0e901e68141f   12 months ago   142MB
alpine        latest    e66264b98777   12 months ago   5.53MB
hello-world   latest    feb5d9fea6a5   20 months ago   13.3kB
bradsimpson@ app:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:6cc97262444f1c45171081bc5a1d4c28b883ea46a6e0d1a45a8eac4a7f4767ab
Deleted: sha256:ceccf204404e5efe764f2d4d97e6977db04062579d525d9cb445cf93e0f0fef4
Deleted: sha256:5581e2a0252cdb4f2b1847cfd9300122841787cd0a9ba13e095425b22c08bb05
Deleted: sha256:b8d9a959ce0f6039bf4061ddedb320c05b9b049b5bd8dabb2b5f9d697fdc4e0e
Deleted: sha256:d426781ae8413908a52d86fb8f28319b834625c5c6b194e3d122d1b1eb179d87
Deleted: sha256:ee6f16055bfd3ad8bcc92a9af3567c69c0bb499cbc2c2b9a2f2ccafa3538504b
Deleted: sha256:42c973890245849bff76e03def91ceacb87da92a19fa5aa7eab58975a811c683
Deleted: sha256:179015cc5c69fea24583ca7a52a8ba75dd363310d17461b6eb9b430c0d69a37e
Deleted: sha256:9362c3f758a9916eb7e2262af8e63d7f1b0a45818e7ac033c9152ecf049933d0
Deleted: sha256:b47ed6c8bc9fa1548ed586316aa7a0e27b34937efb1b3c4ad5742ae3a5d63f8c
Deleted: sha256:a603ddfeb1e19bb984a56b96e96cc987d8e27621390a9bc1b11f7003ff357e7d
Deleted: sha256:ca073f3da5fc959ed40fff93ae9a550ddb14916b3f8bd620235d306f5e9d3d64
Deleted: sha256:fd2d7bb88deba0351caf0ee032dac84272a04e489fd055407cddd740009e329c
Deleted: sha256:2c3cc0e91a94c04e5446f3a8061970073053850ce8093a46ba819b8e59af1dee
Deleted: sha256:ed7b0ef3bf5bbec74379c3ae3d5339e666a314223e863c70644f7522a7527461
bradsimpson@ app:docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
nginx         alpine    2bc7edbc3cf2   3 months ago    40.7MB
ubuntu        latest    27941809078c   11 months ago   77.8MB
nginx         latest    0e901e68141f   12 months ago   142MB
alpine        latest    e66264b98777   12 months ago   5.53MB
hello-world   latest    feb5d9fea6a5   20 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
f03b40093957: Pull complete 
9d674c93414d: Pull complete 
de781e8e259a: Pull complete 
5ea6efaf51f6: Pull complete 
b078d5f4ac82: Pull complete 
97f84fb2a918: Pull complete 
5a6bf2f43fb8: Pull complete 
f1a40e88fea4: Pull complete 
4be673794a1a: Pull complete 
9d72f84fb861: Pull complete 
5d52569da92e: Pull complete 
5d48fbe991ff: Pull complete 
4ae692d11ad3: Pull complete 
Digest: sha256:31c9342603866f29206a06b77c8fed48b3c3f70d710a4be4e8216b134f92d0df
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:docker image inspect postgres
[
    {
        "Id": "sha256:0c88fbae765e8bcdb4c8974c73279e9c00b3bb5ab7e23131e40706430ef2bb2a",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:31c9342603866f29206a06b77c8fed48b3c3f70d710a4be4e8216b134f92d0df"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-05-23T09:17:39.893824651Z",
        "Container": "2ff1cc92ff5e509752282e1bd3e520450b829282d0dc0b166fff5f93df2699f7",
        "ContainerConfig": {
            "Hostname": "2ff1cc92ff5e",
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
                "PG_VERSION=15.3-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:7400ee22cae48f653c4ab2322494dd129e608673c32d53ee2a53c2e6667c7881",
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
                "PG_VERSION=15.3-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:7400ee22cae48f653c4ab2322494dd129e608673c32d53ee2a53c2e6667c7881",
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
        "Size": 379110293,
        "VirtualSize": 379110293,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/c80431971e3464f88280b4cd16edd0e6475fd5a28a1062b8cc0c034a0f43a4bc/diff:/var/lib/docker/overlay2/de7af92050196145a728586d293813e67b44d3cb3bfa792e250e57843b0079f7/diff:/var/lib/docker/overlay2/fd60e63656541e1155358c706c4c488fb3a25eec1d85186260910ebcda484fd9/diff:/var/lib/docker/overlay2/8b27677420116a1774a9931c955a309b0180ce00d213560d2c60b314f6c66350/diff:/var/lib/docker/overlay2/1cd68dd744843bcd70af8787350613d958798ea2f54c159bb0876b7fed478569/diff:/var/lib/docker/overlay2/c8ee39d52b5b95560570f3ca60095849396e5edb23efdb7d6ab55a4477824a14/diff:/var/lib/docker/overlay2/3048f115d7b0611769bd71a1a17944817e2f1b934db67a4230b332c11c287e89/diff:/var/lib/docker/overlay2/1f63c7d86b96824fdfd9ffbcfc2e111ae5192b543c5e40f74348cae5e3ed4dcf/diff:/var/lib/docker/overlay2/40f367b57fa34d5cf00c43b7f7cadf224b4a9d92c309735486f73eca929204c4/diff:/var/lib/docker/overlay2/6631f476f377f6c68cb9ff0a34d73c8121fb64b89594dd215808be40112dd492/diff:/var/lib/docker/overlay2/31c555852c96ff704f04ab8133608dbd404f8d6e4c98097da704512ebbdc037f/diff:/var/lib/docker/overlay2/36253db8313454c3efd5f2653406dc9a71a4f91c4b8722597f898ec30656c20d/diff",
                "MergedDir": "/var/lib/docker/overlay2/1965c4541c16f2d876e50e02d0b9e4c53167b2ffa05c50e2ab2d888b19fd5f92/merged",
                "UpperDir": "/var/lib/docker/overlay2/1965c4541c16f2d876e50e02d0b9e4c53167b2ffa05c50e2ab2d888b19fd5f92/diff",
                "WorkDir": "/var/lib/docker/overlay2/1965c4541c16f2d876e50e02d0b9e4c53167b2ffa05c50e2ab2d888b19fd5f92/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:8cbe4b54fa88d8fc0198ea0cc3a5432aea41573e6a0ee26eca8c79f9fbfa40e3",
                "sha256:f8004b9cc781c88f973abf709a5c01e3df02bb0af11a7db3a328c0973bffd687",
                "sha256:322bc795fc019d1b5610f6816812621470e189d7bad29d5ebce318b4dfc433d7",
                "sha256:8f1ffee792b8d702c635e10431f8a6b723675f6919d8750bd84578a3e7dbbbc1",
                "sha256:3a6dd980caa17c5e2a1b3fa79eb86a893b112eb020a2fedeefaf242c4cf13f8c",
                "sha256:3b4d053c7446d4544eac3b45213b3b3229b5cdcefc25dd4cf07529042451c351",
                "sha256:aa8832a5dfbf0bf3a5c218a5f1253144013b3945ef8055e024f411ff6a6ec2e9",
                "sha256:8b3ae80f8cb80bdc6e0aa92ec1269d50cdcbcd69bc452930eaa65e42cc8bc47f",
                "sha256:d3759839e302cc2eb3b3dc8e69f966a1067b73d192711d6d9aaa84b6df5e53a3",
                "sha256:aef5e99594f1902de6fae3dff1a8ba9150192a6daf9d8742332baa307f38ee84",
                "sha256:b94637ca0ff77ec2d4f5b2606421c69ef0fe39763d244e00b53c6065b4b0e928",
                "sha256:c930589cdeb13abc8f9b6d1697e19de4e5058cd8eab780fe1a3cc9b0e9d67ee6",
                "sha256:36578bc8bfaa28b80855a2a36c8c684ee55803dac6cf17d9e4d10fe56db7b4b5"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgres1 -d --mount type=volume,source=wing_wednesday,target=/var/lib/postgresql/data postgres
f510c0c0a5798b25201d6b373a3035ae1034cf4bad8c0f7f8d48c26802647966
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
f510c0c0a579   postgres       "docker-entrypoint.s…"   4 seconds ago    Up 3 seconds    0.0.0.0:5431->5432/tcp   postgres1
1d942f3002b1   nginx:alpine   "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8000->80/tcp     thirsty_heisenberg
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.3 (Debian 15.3-1.pgdg110+1))
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

postgres=# CREATE DATABASE wednesday_wing WITH OWNER postgres;
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
 wednesday_wing | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres=# exit
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                    NAMES
f510c0c0a579   postgres       "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5431->5432/tcp   postgres1
1d942f3002b1   nginx:alpine   "/docker-entrypoint.…"   15 minutes ago       Up 15 minutes       0.0.0.0:8000->80/tcp     thirsty_heisenberg
bradsimpson@ app:docker container stop postgres1
postgres1
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                      PORTS                  NAMES
f510c0c0a579   postgres       "docker-entrypoint.s…"   2 minutes ago       Exited (0) 5 seconds ago                           postgres1
1d942f3002b1   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago      Up 16 minutes               0.0.0.0:8000->80/tcp   thirsty_heisenberg
132253a7b7f4   nginx:alpine   "/docker-entrypoint.…"   32 minutes ago      Exited (0) 26 minutes ago                          c4
1d8851b84df0   nginx:alpine   "/docker-entrypoint.…"   32 minutes ago      Exited (0) 26 minutes ago                          c3
83f63fef1efd   nginx:alpine   "/docker-entrypoint.…"   33 minutes ago      Exited (0) 26 minutes ago                          c2
92f3e94b48b2   nginx:alpine   "/docker-entrypoint.…"   33 minutes ago      Exited (0) 26 minutes ago                          c1
7891a299d4e9   nginx          "/docker-entrypoint.…"   About an hour ago   Exited (0) 32 minutes ago                          funny_dewdney
bradsimpson@ app:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
f510c0c0a5798b25201d6b373a3035ae1034cf4bad8c0f7f8d48c26802647966
132253a7b7f45760425ab323ed44b777530c488b0f7db9c723e4161fb456a0bc
1d8851b84df0a014a37574ae4afd01c69772d278fc9d5e58106f347647ea9863
83f63fef1efd16526ab108efebfabfd84ad012fb2b492fe3591d76f6b0f36968
92f3e94b48b238199f7854b7d2e88e753f540a44d74ce9d7bcbb9dbea6acd5e7
7891a299d4e9029bf85680770fe4abf40e71e5739d663d422325510267491794

Total reclaimed space: 5.522kB
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgres2 -d --mount type=volume,source=wing_wednesday,target=/var/lib/postgresql/data postgres
b00d62bbbafdc9b4cf314c2291ba686754447fcbef1a93ba4de598b3d0daeae8
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
b00d62bbbafd   postgres       "docker-entrypoint.s…"   4 seconds ago    Up 3 seconds    0.0.0.0:5431->5432/tcp   postgres2
1d942f3002b1   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp     thirsty_heisenberg
bradsimpson@ app:psql -p 5431 0h localhost -U postgres
psql: warning: extra command-line argument "localhost" ignored
psql: error: could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket "/tmp/.s.PGSQL.5431"?
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.3 (Debian 15.3-1.pgdg110+1))
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
 wednesday_wing | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
(4 rows)

postgres=# exit
bradsimpson@ app:

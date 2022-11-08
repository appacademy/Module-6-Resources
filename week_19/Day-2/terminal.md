Last login: Tue Nov  8 10:39:53 on ttys007

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container ls
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
bradsimpson@ ~:\clear


bradsimpson@ ~:docker container ls
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED       STATUS                    PORTS                                       NAMES
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago   Exited (255) 3 days ago   0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago   Exited (255) 3 days ago   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:\clear

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
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wing_wednesday   latest    09dccc5d2562   3 weeks ago     560MB
postgres                        latest    e270a11b9c8a   4 weeks ago     376MB
bradsimpson213/test_app2        <none>    8edeca523aef   7 weeks ago     432MB
bradsimpson213/react_test       latest    4de311ebce05   2 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   4 months ago    377MB
ubuntu                          latest    27941809078c   5 months ago    77.8MB
nginx                           latest    0e901e68141f   5 months ago    142MB
alpine                          latest    e66264b98777   5 months ago    5.53MB
nginx                           alpine    b1c3acb28882   5 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   13 months ago   13.3kB
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED         STATUS                     PORTS                                       NAMES
431a08b9fb86   hello-world                     "/hello"                 4 minutes ago   Exited (0) 4 minutes ago                                               relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago     Exited (255) 4 days ago    0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago     Exited (255) 4 days ago    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:\clear


bradsimpson@ ~:docker container run [OPTIONS] image-name [Commands]
docker: invalid reference format: repository name must be lowercase.
See 'docker run --help'.
bradsimpson@ ~:docker container run --name cool_container -p 8080:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2022/11/08 16:35:23 [notice] 1#1: using the "epoll" event method
2022/11/08 16:35:23 [notice] 1#1: nginx/1.21.6
2022/11/08 16:35:23 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2022/11/08 16:35:23 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2022/11/08 16:35:23 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/11/08 16:35:23 [notice] 1#1: start worker processes
2022/11/08 16:35:23 [notice] 1#1: start worker process 32
2022/11/08 16:35:23 [notice] 1#1: start worker process 33
172.17.0.1 - - [08/Nov/2022:16:36:04 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
^C2022/11/08 16:36:50 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/11/08 16:36:50 [notice] 33#33: exiting
2022/11/08 16:36:50 [notice] 32#32: exiting
2022/11/08 16:36:50 [notice] 33#33: exit
2022/11/08 16:36:50 [notice] 32#32: exit
2022/11/08 16:36:50 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2022/11/08 16:36:50 [notice] 1#1: worker process 33 exited with code 0
2022/11/08 16:36:50 [notice] 1#1: signal 29 (SIGIO) received
2022/11/08 16:36:50 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2022/11/08 16:36:50 [notice] 1#1: worker process 32 exited with code 0
2022/11/08 16:36:50 [notice] 1#1: exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
bc54106c05dd   nginx                           "/docker-entrypoint.…"   2 minutes ago    Exited (0) 33 seconds ago                                               cool_container
431a08b9fb86   hello-world                     "/hello"                 11 minutes ago   Exited (0) 11 minutes ago                                               relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago     0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago     0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx
8556bdfccfa6b78e06e026adc61d829e6f5be61acc8dac5a70d16b2d68708997
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   13 seconds ago   Up 12 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container run --rm alpine
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   7 minutes ago    Exited (0) 6 minutes ago                                                cool_container
431a08b9fb86   hello-world                     "/hello"                 17 minutes ago   Exited (0) 17 minutes ago                                               relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago     0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago     0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:docker container run alpine
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
45480654907e   alpine                          "/bin/sh"                4 seconds ago    Exited (0) 2 seconds ago                                                happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   8 minutes ago    Exited (0) 7 minutes ago                                                cool_container
431a08b9fb86   hello-world                     "/hello"                 18 minutes ago   Exited (0) 18 minutes ago                                               relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago     0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago     0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -it alpine sh
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
/bin # nano
sh: nano: not found
/bin # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                        PORTS                                       NAMES
ab5973275aa9   alpine                          "sh"                     About a minute ago   Exited (127) 18 seconds ago                                               dreamy_darwin
45480654907e   alpine                          "/bin/sh"                3 minutes ago        Exited (0) 3 minutes ago                                                  happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   5 minutes ago        Up 5 minutes                  0.0.0.0:8080->80/tcp, :::8080->80/tcp       agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   11 minutes ago       Exited (0) 10 minutes ago                                                 cool_container
431a08b9fb86   hello-world                     "/hello"                 21 minutes ago       Exited (0) 21 minutes ago                                                 relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago          Exited (255) 4 days ago       0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago          Exited (255) 4 days ago       0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:\clear

bradsimpson@ ~:docker image ls
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wing_wednesday   latest    09dccc5d2562   3 weeks ago     560MB
postgres                        latest    e270a11b9c8a   4 weeks ago     376MB
bradsimpson213/test_app2        <none>    8edeca523aef   7 weeks ago     432MB
bradsimpson213/react_test       latest    4de311ebce05   2 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   4 months ago    377MB
ubuntu                          latest    27941809078c   5 months ago    77.8MB
nginx                           latest    0e901e68141f   5 months ago    142MB
alpine                          latest    e66264b98777   5 months ago    5.53MB
nginx                           alpine    b1c3acb28882   5 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   13 months ago   13.3kB
bradsimpson@ ~:\clear


bradsimpson@ ~:docker container run -d -p 8080:80 nginx
8808c5db803903a25f55e646230245d28405e8971358929e0281e58f5d2576ce
docker: Error response from daemon: driver failed programming external connectivity on endpoint recursing_blackwell (c639b60fe3d8a03ebe5f78b30412fbbd29a7e56a6dda101ef4a315f9c9a73190): Bind for 0.0.0.0:8080 failed: port is already allocated.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container run --name test -it alpine sh
/ # echo hello world
hello world
/ # exit
bradsimpson@ ~:docker container run --rm --name greet_me ubuntu echo hello world
hello world
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                          PORTS                                       NAMES
4701a5fdf6a4   alpine                          "sh"                     About a minute ago   Exited (0) About a minute ago                                               test
8808c5db8039   nginx                           "/docker-entrypoint.…"   4 minutes ago        Created                                                                     recursing_blackwell
ab5973275aa9   alpine                          "sh"                     9 minutes ago        Exited (127) 8 minutes ago                                                  dreamy_darwin
45480654907e   alpine                          "/bin/sh"                10 minutes ago       Exited (0) 10 minutes ago                                                   happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   13 minutes ago       Up 13 minutes                   0.0.0.0:8080->80/tcp, :::8080->80/tcp       agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   19 minutes ago       Exited (0) 17 minutes ago                                                   cool_container
431a08b9fb86   hello-world                     "/hello"                 29 minutes ago       Exited (0) 29 minutes ago                                                   relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago          Exited (255) 4 days ago         0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago          Exited (255) 4 days ago         0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:\clear





bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                       PORTS                                       NAMES
4701a5fdf6a4   alpine                          "sh"                     2 minutes ago    Exited (0) 2 minutes ago                                                 test
8808c5db8039   nginx                           "/docker-entrypoint.…"   5 minutes ago    Created                                                                  recursing_blackwell
ab5973275aa9   alpine                          "sh"                     10 minutes ago   Exited (127) 9 minutes ago                                               dreamy_darwin
45480654907e   alpine                          "/bin/sh"                11 minutes ago   Exited (0) 11 minutes ago                                                happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   20 minutes ago   Exited (0) 18 minutes ago                                                cool_container
431a08b9fb86   hello-world                     "/hello"                 30 minutes ago   Exited (0) 30 minutes ago                                                relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago      0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago      0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
d0a7ac21caa0   bridge        bridge    local
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
local     taco_tuesday
bradsimpson@ ~:\clear






bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
8556bdfccfa6   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   agitated_jones
bradsimpson@ ~:docker container stop agitated_jones
agitated_jones
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                        PORTS                                       NAMES
4701a5fdf6a4   alpine                          "sh"                     4 minutes ago    Exited (0) 4 minutes ago                                                  test
8808c5db8039   nginx                           "/docker-entrypoint.…"   7 minutes ago    Created                                                                   recursing_blackwell
ab5973275aa9   alpine                          "sh"                     12 minutes ago   Exited (127) 11 minutes ago                                               dreamy_darwin
45480654907e   alpine                          "/bin/sh"                14 minutes ago   Exited (0) 14 minutes ago                                                 happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   16 minutes ago   Exited (0) 41 seconds ago                                                 agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   22 minutes ago   Exited (0) 21 minutes ago                                                 cool_container
431a08b9fb86   hello-world                     "/hello"                 32 minutes ago   Exited (0) 32 minutes ago                                                 relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago       0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago       0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:docker container start 4701a5fdf6a4
4701a5fdf6a4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS         PORTS     NAMES
4701a5fdf6a4   alpine    "sh"      5 minutes ago   Up 6 seconds             test
bradsimpson@ ~:docker container stop 4701a5fdf6a4
4701a5fdf6a4
bradsimpson@ ~:\clear











bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                        PORTS                                       NAMES
4701a5fdf6a4   alpine                          "sh"                     6 minutes ago    Exited (137) 53 seconds ago                                               test
8808c5db8039   nginx                           "/docker-entrypoint.…"   9 minutes ago    Created                                                                   recursing_blackwell
ab5973275aa9   alpine                          "sh"                     14 minutes ago   Exited (127) 13 minutes ago                                               dreamy_darwin
45480654907e   alpine                          "/bin/sh"                16 minutes ago   Exited (0) 15 minutes ago                                                 happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   18 minutes ago   Exited (0) 2 minutes ago                                                  agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   24 minutes ago   Exited (0) 23 minutes ago                                                 cool_container
431a08b9fb86   hello-world                     "/hello"                 34 minutes ago   Exited (0) 34 minutes ago                                                 relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago       0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago       0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:docker container rm dreamy_darwin
dreamy_darwin
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS                            PORTS                                       NAMES
4701a5fdf6a4   alpine                          "sh"                     7 minutes ago    Exited (137) About a minute ago                                               test
8808c5db8039   nginx                           "/docker-entrypoint.…"   9 minutes ago    Created                                                                       recursing_blackwell
45480654907e   alpine                          "/bin/sh"                16 minutes ago   Exited (0) 16 minutes ago                                                     happy_lumiere
8556bdfccfa6   nginx                           "/docker-entrypoint.…"   19 minutes ago   Exited (0) 3 minutes ago                                                      agitated_jones
bc54106c05dd   nginx                           "/docker-entrypoint.…"   24 minutes ago   Exited (0) 23 minutes ago                                                     cool_container
431a08b9fb86   hello-world                     "/hello"                 34 minutes ago   Exited (0) 34 minutes ago                                                     relaxed_bohr
25a9bdb01435   bradsimpson213/wing_wednesday   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago           0.0.0.0:3001->3000/tcp, :::3001->3000/tcp   react_demo
e323bd36d51b   postgres                        "docker-entrypoint.s…"   3 weeks ago      Exited (255) 4 days ago           0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   taco_for_lunch
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
4701a5fdf6a41474cc32c58545c1ce0fc374bb0f29d78546028c4d0f987aa57b
8808c5db803903a25f55e646230245d28405e8971358929e0281e58f5d2576ce
45480654907ea172f6e481e5379fc927803e54741b7a4265bd18d7b515b9682f
8556bdfccfa6b78e06e026adc61d829e6f5be61acc8dac5a70d16b2d68708997
bc54106c05dd3e29b840e87ad8a4e15bce437dbb6772056cc42f4324159a5c3f
431a08b9fb8600eb84a2f5323014fd3a2c2b0043d1066d532c0f15c4781d9584
25a9bdb01435f7dff477bbc65510c79efdf50e217fae0e4a82db61a275bdb3a4
e323bd36d51b3a9dbd2a4535b2776bf81ef94336ec60ce60cb4e9ca9ab5d8102

Total reclaimed space: 48.03MB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx 
8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
8dc6ce7ec8ff   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   vibrant_leavitt
bradsimpson@ ~:docker container exec -it vibrant_leavitt sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                   NAMES
8dc6ce7ec8ff   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, :::8080->80/tcp   vibrant_leavitt
bradsimpson@ ~:docker container inspect vibrant_leavitt
[
    {
        "Id": "8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92",
        "Created": "2022-11-08T17:03:29.251020997Z",
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
            "Pid": 3856,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-11-08T17:03:30.041146768Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92/hostname",
        "HostsPath": "/var/lib/docker/containers/8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92/hosts",
        "LogPath": "/var/lib/docker/containers/8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92/8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92-json.log",
        "Name": "/vibrant_leavitt",
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
                "LowerDir": "/var/lib/docker/overlay2/39414e60c45442d159f5e8a3579611281ec4a065e04584fea610664593a8c393-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/39414e60c45442d159f5e8a3579611281ec4a065e04584fea610664593a8c393/merged",
                "UpperDir": "/var/lib/docker/overlay2/39414e60c45442d159f5e8a3579611281ec4a065e04584fea610664593a8c393/diff",
                "WorkDir": "/var/lib/docker/overlay2/39414e60c45442d159f5e8a3579611281ec4a065e04584fea610664593a8c393/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "8dc6ce7ec8ff",
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
            "SandboxID": "631fa67102f1b864aea2c477b53d0694719007fb21b9a6b7a91cf751c4ec2334",
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
            "SandboxKey": "/var/run/docker/netns/631fa67102f1",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "92fc38b0aaa63d7f2ca5f8fcb7a9f210a3bc4e387c8b62205af4d81abc793a8e",
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
                    "NetworkID": "d0a7ac21caa0a7cfcb723265e3d744dedfba98a5163411c1c5119db70e5b9d55",
                    "EndpointID": "92fc38b0aaa63d7f2ca5f8fcb7a9f210a3bc4e387c8b62205af4d81abc793a8e",
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
NETWORK ID     NAME           DRIVER    SCOPE
d0a7ac21caa0   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
39816ba14919   my_network2    bridge    local
7775a70e761d   my_network3    bridge    local
475754f27665   none           null      local
ef178e0d46c8   taco_tuesday   bridge    local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
c9250f4d688a   nginx:alpine   "/docker-entrypoint.…"   57 seconds ago       Up 56 seconds       80/tcp    c4
89616095146f   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
44af67958573   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
d2ae5fc87277   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1


bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 3 c2
PING c2 (172.21.0.3): 56 data bytes
64 bytes from 172.21.0.3: seq=0 ttl=64 time=0.290 ms
64 bytes from 172.21.0.3: seq=1 ttl=64 time=0.148 ms
64 bytes from 172.21.0.3: seq=2 ttl=64 time=0.097 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.097/0.178/0.290 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 c4
ping: bad address 'c4'
/ # exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789",
        "Created": "2022-11-08T17:35:08.869809822Z",
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
            "Pid": 4659,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-11-08T17:35:09.592790293Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789/hostname",
        "HostsPath": "/var/lib/docker/containers/c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789/hosts",
        "LogPath": "/var/lib/docker/containers/c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789/c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/0adca840ae375d6dbb88eaf6f340b6e18e613fda2c64b5e9482f77a637fc687c-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/0adca840ae375d6dbb88eaf6f340b6e18e613fda2c64b5e9482f77a637fc687c/merged",
                "UpperDir": "/var/lib/docker/overlay2/0adca840ae375d6dbb88eaf6f340b6e18e613fda2c64b5e9482f77a637fc687c/diff",
                "WorkDir": "/var/lib/docker/overlay2/0adca840ae375d6dbb88eaf6f340b6e18e613fda2c64b5e9482f77a637fc687c/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "c9250f4d688a",
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
            "SandboxID": "c4b8a576f9a3f33b0be663af849d0859e3dfe5949667045ff7de7a2cbafe36a8",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/c4b8a576f9a3",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "ef15e34299ef4687545fefa4a995e59f97894c2817c623926b0214def92cd7e3",
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
                    "NetworkID": "d0a7ac21caa0a7cfcb723265e3d744dedfba98a5163411c1c5119db70e5b9d55",
                    "EndpointID": "ef15e34299ef4687545fefa4a995e59f97894c2817c623926b0214def92cd7e3",
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
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.688 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.250 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.095 ms

--- 172.17.0.3 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.095/0.344/0.688 ms
/ # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
c9250f4d688a   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c4
89616095146f   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c3
44af67958573   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c2
d2ae5fc87277   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c1
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
d0a7ac21caa0   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
39816ba14919   my_network2    bridge    local
7775a70e761d   my_network3    bridge    local
475754f27665   none           null      local
ef178e0d46c8   taco_tuesday   bridge    local
bradsimpson@ ~:docker volumes ls
docker: 'volumes' is not a docker command.
See 'docker --help'
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     postgres-data
local     taco_tuesday
bradsimpson@ ~:



bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
c9250f4d688a   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp    c4
89616095146f   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp    c3
44af67958573   nginx:alpine   "/docker-entrypoint.…"   52 minutes ago   Up 52 minutes   80/tcp    c2
d2ae5fc87277   nginx:alpine   "/docker-entrypoint.…"   52 minutes ago   Up 52 minutes   80/tcp    c1
bradsimpson@ app:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container start c1
c1
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS         PORTS     NAMES
d2ae5fc87277   nginx:alpine   "/docker-entrypoint.…"   53 minutes ago   Up 4 seconds   80/tcp    c1
bradsimpson@ app:docker container exec -it c1 sh
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
/usr/share # \ls
GeoIP            ca-certificates  licenses         misc             udhcpc
apk              doc              man              nginx            zoneinfo
/usr/share # cd nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html
/usr/share/nginx/html # \ls
50x.html    index.html
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
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS         PORTS     NAMES
d2ae5fc87277   nginx:alpine   "/docker-entrypoint.…"   55 minutes ago   Up 2 minutes   80/tcp    c1
bradsimpson@ app:docker container stop c1
c1
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -d -p 8080:80 --mount type=bind,source="$(pwd)",target=/usr/share/nginx/html nginx:alpine 
6ac39a0815ecd594bb4b5b64eb154f0b42b23f8116388c85b355fa9a1cd2493f
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   34 seconds ago   Up 32 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ecstatic_engelbart
bradsimpson@ app:docker container exec -it ecstatic_engelbart sh
/ # \ls
bin                   home                  proc                  sys
dev                   lib                   root                  tmp
docker-entrypoint.d   media                 run                   usr
docker-entrypoint.sh  mnt                   sbin                  var
etc                   opt                   srv
/ # cd usr
/usr # cd share
/usr/share # cd nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
sh: nano: not found
/usr/share/nginx/html # apk app nano
ERROR: 'app' is not an apk command. See 'apk --help'.
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (5.9-r0)
Executing busybox-1.34.1-r5.trigger
OK: 26 MiB in 43 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:\clear









bradsimpson@ app:docker image inspect
"docker image inspect" requires at least 1 argument.
See 'docker image inspect --help'.

Usage:  docker image inspect [OPTIONS] IMAGE [IMAGE...]

Display detailed information on one or more images
bradsimpson@ app:docker image ls
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wing_wednesday   latest    09dccc5d2562   3 weeks ago     560MB
postgres                        latest    e270a11b9c8a   4 weeks ago     376MB
bradsimpson213/test_app2        <none>    8edeca523aef   7 weeks ago     432MB
bradsimpson213/react_test       latest    4de311ebce05   2 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   4 months ago    377MB
ubuntu                          latest    27941809078c   5 months ago    77.8MB
nginx                           latest    0e901e68141f   5 months ago    142MB
alpine                          latest    e66264b98777   5 months ago    5.53MB
nginx                           alpine    b1c3acb28882   5 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   13 months ago   13.3kB
bradsimpson@ app:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:640fa552e4f0e71f2bd369ad615779385442f7d447d1600f8f2c385b51edb336
Deleted: sha256:e270a11b9c8a719c4f501c34f1fccf7de89cda4d95e6e6ec9cadc73bdb1ae6d5
Deleted: sha256:dadd44e6170bdc3a18f2d98e15dcbe284dd28cffb038a564812dd654ca9d54ac
Deleted: sha256:fef2d970279fd9eb6c3cdbbbfd562b740252ef4cc3dab62bb2bb1cb1c5576800
Deleted: sha256:1ccc514d3842cc87ac95e899dbf012915fe30d436871c3efbc771fdb784a39b9
Deleted: sha256:85f3af45b61b35e9119e65803d0359d26ccf704305dfd4d977bdfb5194e251ea
Deleted: sha256:92971262ecef4d4d3947ddc0e19febf56ecbbfe69be0839d5f01cae4003b26db
Deleted: sha256:1b30a3eddf2d59246b7ea201e9587552417c657b5519aff31f13a5c6337bc7b6
Deleted: sha256:8dcd955e4894f78939196e160993768f9a2674d2846a17d14ad15e891af9e9af
Deleted: sha256:6fcc528ead19dec936ebedfa4f406db66c6f96d9b183f8ff6a741c8da17d185f
Deleted: sha256:0d521080d6242086fc36247bbdbb578780f1060e8816e686922831f754c9fb34
Deleted: sha256:b0dfc592122cc2d21b2a6d4a9dfb42ed792a7d006db39619c96a80b1772ae96d
Deleted: sha256:922c2bb14e7ff03f6773cec59ba73f5fcbec1b02f5c0d9b7f81b9a59f4ce7748
Deleted: sha256:d96a14d07d56076ed528e05c970067c77920a8e564c042044b37f241f349239c
Deleted: sha256:fe7b1e9bf7922fbc22281bcc6b4f5ac8f1a7b4278929880940978c42fc9d0229
bradsimpson@ app:docker image ls
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wing_wednesday   latest    09dccc5d2562   3 weeks ago     560MB
bradsimpson213/test_app2        <none>    8edeca523aef   7 weeks ago     432MB
bradsimpson213/react_test       latest    4de311ebce05   2 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   4 months ago    377MB
ubuntu                          latest    27941809078c   5 months ago    77.8MB
nginx                           latest    0e901e68141f   5 months ago    142MB
alpine                          latest    e66264b98777   5 months ago    5.53MB
nginx                           alpine    b1c3acb28882   5 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   13 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
e9995326b091: Pull complete 
a0cb03f17886: Pull complete 
bb26f7e78134: Pull complete 
c8e073b7ae91: Pull complete 
99b5b1679915: Pull complete 
55c520fc03c5: Pull complete 
d0ac84d6672c: Pull complete 
4effb95d5849: Pull complete 
f4c3677d4414: Pull complete 
6707712b5af7: Pull complete 
896a00668d28: Pull complete 
50b8050f9af6: Pull complete 
203e0ce1e9da: Pull complete 
Digest: sha256:bab8d7be6466e029f7fa1e69ff6aa0082704db330572638fd01f2791824774d8
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:\clear

bradsimpson@ app:docker image ls
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
postgres                        latest    027eba2e8939   2 weeks ago     377MB
bradsimpson213/wing_wednesday   latest    09dccc5d2562   3 weeks ago     560MB
bradsimpson213/test_app2        <none>    8edeca523aef   7 weeks ago     432MB
bradsimpson213/react_test       latest    4de311ebce05   2 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   4 months ago    377MB
ubuntu                          latest    27941809078c   5 months ago    77.8MB
nginx                           latest    0e901e68141f   5 months ago    142MB
alpine                          latest    e66264b98777   5 months ago    5.53MB
nginx                           alpine    b1c3acb28882   5 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   13 months ago   13.3kB
bradsimpson@ app:docker image inspect postgres
[
    {
        "Id": "sha256:027eba2e89396946fd63dd69c919844b248c8b591c07545321de3006503cc974",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:bab8d7be6466e029f7fa1e69ff6aa0082704db330572638fd01f2791824774d8"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-10-25T13:24:17.200931106Z",
        "Container": "47005d1482bcc0d3b39a3979afb786038b7d317d09711c875d27018f7b103de6",
        "ContainerConfig": {
            "Hostname": "47005d1482bc",
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
                "PG_VERSION=15.0-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:23625f6b659ae02e2e26c50da945d68fd9a3e4f7344e86acf1b683c9a9af2975",
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
                "PG_VERSION=15.0-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:23625f6b659ae02e2e26c50da945d68fd9a3e4f7344e86acf1b683c9a9af2975",
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
        "Size": 377373840,
        "VirtualSize": 377373840,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/c94ccfb4aad007961c59686620bad768b1b33be6d7a9e756078306cc6a72bf31/diff:/var/lib/docker/overlay2/918dbd411aff47334dc1bc7880dd81ecb11ab33e441f80dfaa1b79c93bc34019/diff:/var/lib/docker/overlay2/44eb1489c0ebd3eb2e75807620711d0deebf66b0ec956e3fc235d7921058d3c5/diff:/var/lib/docker/overlay2/877faaec97d8bd56dc8dfbfc5ed190f279409715e3ade46110309471cda65846/diff:/var/lib/docker/overlay2/aeb04d341941d5d074cc1324d56bc6295398b7cc19d5cea11bc9da0e3f4adce7/diff:/var/lib/docker/overlay2/43ccb47e3f90cf658c16cac44c4226c3c369190a46f7945f2de052e67ccd936f/diff:/var/lib/docker/overlay2/987e6cff23ba26ff330f68421f2f33192ec5d6331f080deb9f774c70d5456cb1/diff:/var/lib/docker/overlay2/0faa0f9875e2d43481690ca093d04fe5bafd8689bbf6196e9ab91d95df7ab250/diff:/var/lib/docker/overlay2/a6d159e9bbf526af43a17c357dd63609066d9e6b4d5b5c4a9829a635a8fe5ba3/diff:/var/lib/docker/overlay2/8e29b38356f1b52a9ffed386ab650325953bbc84450055edee69268830882ed6/diff:/var/lib/docker/overlay2/af725479b1c62a3197f75bc7ef190a8a930ad51d0bcdddde9dc4db31f3b47203/diff:/var/lib/docker/overlay2/f21656dc94e73a0e737cd4a8e5bbe0455234a5db244ee5b39a52d3c7103fced1/diff",
                "MergedDir": "/var/lib/docker/overlay2/0463a1fccd6117cc1ae2a6c8a8a80307d2d65163888127173fc32ccf80c6e3bb/merged",
                "UpperDir": "/var/lib/docker/overlay2/0463a1fccd6117cc1ae2a6c8a8a80307d2d65163888127173fc32ccf80c6e3bb/diff",
                "WorkDir": "/var/lib/docker/overlay2/0463a1fccd6117cc1ae2a6c8a8a80307d2d65163888127173fc32ccf80c6e3bb/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:a12586ed027fafddcddcc63b31671f406c25e43342479fc92a330e7e30d65f2e",
                "sha256:e1a930a711c4174b1aab55dabffac5ec6aa1a56af884ba4b63a3f91d3a9cc759",
                "sha256:c7355294a3c32504739c688f1ed18aa099033508927c5594211b6427698e71f9",
                "sha256:e0d2bd2355aca78c3e8025d10b4558bb8ae8c0366244ad9be6ed0dbcf288e2ab",
                "sha256:c0f17a6a224dbb6f0af304676f30c29aeb7815546494c04d57c79faff1996990",
                "sha256:20eaa932cf88cac8355504a41cdb677b65fe2ca1fda86d51a99b45905713f6ca",
                "sha256:466e4e8c2b3ea554fe5dbfff4b66eb2703d581a2e09b50cd294a6f4b6e3b03f9",
                "sha256:4f9460380916cd7d5b96ae0e1eaac650f56c8abc2978f8f5ded88d22999a40f8",
                "sha256:76c336cb30a79288fdff415c25a072ebe9ea3117fa847fb47f72ad1180675be4",
                "sha256:5799d05a927952b302dc7fcd786e5a9cdb6638b680c8bcee3c13e7af38434003",
                "sha256:04224e468fec04940e21d98628a7e5710dcc6afe628b4bb646445bec907c84ea",
                "sha256:f0a132bbe8a8db48a9e4acdaae979bc8a3f98bdf2bd0edcc7ea3c8b4e1cba81d",
                "sha256:c0cea61d3ab60c5bb8e20122b9d2f63ac34f0095b2ef5017e59cb00d4b443aa4"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 -d -e POSTGRES_PASSWORD=password --name postgres5431 --mount type=volume,source=new_taco_tues,target=/var/lib/postgres/data postres
Unable to find image 'postres:latest' locally
docker: Error response from daemon: pull access denied for postres, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
bradsimpson@ app:docker container run -p 5431:5432 -d -e POSTGRES_PASSWORD=password --name postgres5431 --mount type=volume,source=new_taco_tues,target=/var/lib/postgres/data postgres
e7bf5506db48bdb6f6cdf51d2f5db5220113eba4554c902578d67ae04c08d30c
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e7bf5506db48   postgres       "docker-entrypoint.s…"   7 seconds ago    Up 6 seconds    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   12 minutes ago   Up 12 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:psql -p 4531 -h localhost -U postgres
psql: error: could not connect to server: Connection refused
	Is the server running on host "localhost" (::1) and accepting
	TCP/IP connections on port 4531?
could not connect to server: Connection refused
	Is the server running on host "localhost" (127.0.0.1) and accepting
	TCP/IP connections on port 4531?
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.0 (Debian 15.0-1.pgdg110+1))
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

postgres=# CREATE DATABASE taco_tuesday WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                  List of databases
     Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
--------------+----------+----------+------------+------------+-----------------------
 postgres     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 taco_tuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
              |          |          |            |            | postgres=CTc/postgres
 template1    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
              |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# quit
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e7bf5506db48   postgres       "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:docker container stop postgres5431
postgres5431
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ecstatic_engelbart
bradsimpson@ app:docker container run -p 5431:5432 -d -e POSTGRES_PASSWORD=password --name new_postgres5431 --mount type=volume,source=new_taco_tues,target=/var/lib/postgres/data postgres
e7d9cbf64f26de165e36ff6a1cb7ba26fc68b9895ffee4fd07249a95ad542ef3
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e7d9cbf64f26   postgres       "docker-entrypoint.s…"   5 seconds ago    Up 4 seconds    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   new_postgres5431
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.0 (Debian 15.0-1.pgdg110+1))
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

postgres=# exit
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e7d9cbf64f26   postgres       "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   new_postgres5431
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS                                       NAMES
e7d9cbf64f26   postgres       "docker-entrypoint.s…"   2 minutes ago       Up 2 minutes                   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   new_postgres5431
e7bf5506db48   postgres       "docker-entrypoint.s…"   6 minutes ago       Exited (0) 2 minutes ago                                                   postgres5431
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago      Up 19 minutes                  0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 24 minutes ago                                                  c4
89616095146f   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 24 minutes ago                                                  c3
44af67958573   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 24 minutes ago                                                  c2
d2ae5fc87277   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 21 minutes ago                                                  c1
8dc6ce7ec8ff   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago                                               vibrant_leavitt
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
local     taco_tuesday
bradsimpson@ app:docker volume inspect new_taco_tues
[
    {
        "CreatedAt": "2022-11-08T18:24:07Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/new_taco_tues/_data",
        "Name": "new_taco_tues",
        "Options": {},
        "Scope": "local"
    }
]
bradsimpson@ app:docker volume inspect a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a
[
    {
        "CreatedAt": "2022-11-08T18:48:40Z",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a/_data",
        "Name": "a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a",
        "Options": null,
        "Scope": "local"
    }
]
bradsimpson@ app:docker image inspect postgres
[
    {
        "Id": "sha256:027eba2e89396946fd63dd69c919844b248c8b591c07545321de3006503cc974",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:bab8d7be6466e029f7fa1e69ff6aa0082704db330572638fd01f2791824774d8"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-10-25T13:24:17.200931106Z",
        "Container": "47005d1482bcc0d3b39a3979afb786038b7d317d09711c875d27018f7b103de6",
        "ContainerConfig": {
            "Hostname": "47005d1482bc",
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
                "PG_VERSION=15.0-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:23625f6b659ae02e2e26c50da945d68fd9a3e4f7344e86acf1b683c9a9af2975",
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
                "PG_VERSION=15.0-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:23625f6b659ae02e2e26c50da945d68fd9a3e4f7344e86acf1b683c9a9af2975",
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
        "Size": 377373840,
        "VirtualSize": 377373840,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/c94ccfb4aad007961c59686620bad768b1b33be6d7a9e756078306cc6a72bf31/diff:/var/lib/docker/overlay2/918dbd411aff47334dc1bc7880dd81ecb11ab33e441f80dfaa1b79c93bc34019/diff:/var/lib/docker/overlay2/44eb1489c0ebd3eb2e75807620711d0deebf66b0ec956e3fc235d7921058d3c5/diff:/var/lib/docker/overlay2/877faaec97d8bd56dc8dfbfc5ed190f279409715e3ade46110309471cda65846/diff:/var/lib/docker/overlay2/aeb04d341941d5d074cc1324d56bc6295398b7cc19d5cea11bc9da0e3f4adce7/diff:/var/lib/docker/overlay2/43ccb47e3f90cf658c16cac44c4226c3c369190a46f7945f2de052e67ccd936f/diff:/var/lib/docker/overlay2/987e6cff23ba26ff330f68421f2f33192ec5d6331f080deb9f774c70d5456cb1/diff:/var/lib/docker/overlay2/0faa0f9875e2d43481690ca093d04fe5bafd8689bbf6196e9ab91d95df7ab250/diff:/var/lib/docker/overlay2/a6d159e9bbf526af43a17c357dd63609066d9e6b4d5b5c4a9829a635a8fe5ba3/diff:/var/lib/docker/overlay2/8e29b38356f1b52a9ffed386ab650325953bbc84450055edee69268830882ed6/diff:/var/lib/docker/overlay2/af725479b1c62a3197f75bc7ef190a8a930ad51d0bcdddde9dc4db31f3b47203/diff:/var/lib/docker/overlay2/f21656dc94e73a0e737cd4a8e5bbe0455234a5db244ee5b39a52d3c7103fced1/diff",
                "MergedDir": "/var/lib/docker/overlay2/0463a1fccd6117cc1ae2a6c8a8a80307d2d65163888127173fc32ccf80c6e3bb/merged",
                "UpperDir": "/var/lib/docker/overlay2/0463a1fccd6117cc1ae2a6c8a8a80307d2d65163888127173fc32ccf80c6e3bb/diff",
                "WorkDir": "/var/lib/docker/overlay2/0463a1fccd6117cc1ae2a6c8a8a80307d2d65163888127173fc32ccf80c6e3bb/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:a12586ed027fafddcddcc63b31671f406c25e43342479fc92a330e7e30d65f2e",
                "sha256:e1a930a711c4174b1aab55dabffac5ec6aa1a56af884ba4b63a3f91d3a9cc759",
                "sha256:c7355294a3c32504739c688f1ed18aa099033508927c5594211b6427698e71f9",
                "sha256:e0d2bd2355aca78c3e8025d10b4558bb8ae8c0366244ad9be6ed0dbcf288e2ab",
                "sha256:c0f17a6a224dbb6f0af304676f30c29aeb7815546494c04d57c79faff1996990",
                "sha256:20eaa932cf88cac8355504a41cdb677b65fe2ca1fda86d51a99b45905713f6ca",
                "sha256:466e4e8c2b3ea554fe5dbfff4b66eb2703d581a2e09b50cd294a6f4b6e3b03f9",
                "sha256:4f9460380916cd7d5b96ae0e1eaac650f56c8abc2978f8f5ded88d22999a40f8",
                "sha256:76c336cb30a79288fdff415c25a072ebe9ea3117fa847fb47f72ad1180675be4",
                "sha256:5799d05a927952b302dc7fcd786e5a9cdb6638b680c8bcee3c13e7af38434003",
                "sha256:04224e468fec04940e21d98628a7e5710dcc6afe628b4bb646445bec907c84ea",
                "sha256:f0a132bbe8a8db48a9e4acdaae979bc8a3f98bdf2bd0edcc7ea3c8b4e1cba81d",
                "sha256:c0cea61d3ab60c5bb8e20122b9d2f63ac34f0095b2ef5017e59cb00d4b443aa4"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
e7d9cbf64f26   postgres       "docker-entrypoint.s…"   5 minutes ago    Up 5 minutes    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   new_postgres5431
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   22 minutes ago   Up 22 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:docker container stop new_postgres5431
new_postgres5431
bradsimpson@ app:docker container run -p 5431:5432 -d -e POSTGRES_PASSWORD=password --name new_postgres5431 --mount type=volume,source=new_taco_tues,target=/var/lib/postgresql/data postgres
docker: Error response from daemon: Conflict. The container name "/new_postgres5431" is already in use by container "e7d9cbf64f26de165e36ff6a1cb7ba26fc68b9895ffee4fd07249a95ad542ef3". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ app:docker container run -p 5431:5432 -d -e POSTGRES_PASSWORD=password --name postgres5431_v2 --mount type=volume,source=new_taco_tues,target=/var/lib/postgresql/data postgres 
a0b207004d0982cea67f1ccdb534adf9a3c075c2b76a193875d4731091e1b5b1
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
a0b207004d09   postgres       "docker-entrypoint.s…"   5 seconds ago    Up 4 seconds    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v2
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.0 (Debian 15.0-1.pgdg110+1))
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

postgres=# CREATE DATABASE taco_tuesday WITH OWNER POSTGRES;
CREATE DATABASE
postgres=# \l
                                  List of databases
     Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
--------------+----------+----------+------------+------------+-----------------------
 postgres     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 taco_tuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
              |          |          |            |            | postgres=CTc/postgres
 template1    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
              |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS          PORTS                                       NAMES
a0b207004d09   postgres       "docker-entrypoint.s…"   About a minute ago   Up 59 seconds   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v2
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   24 minutes ago       Up 24 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:docker container stop postgres5431_v2
postgres5431_v2
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   24 minutes ago   Up 24 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   ecstatic_engelbart
bradsimpson@ app:docker container run -p 5431:5432 -d -e POSTGRES_PASSWORD=password --name postgres5431_v3 --mount type=volume,source=new_taco_tues,target=/var/lib/postgresql/data postgres 
1a3245dd9a7c0f40488c298390a92ce417c3b538ac5c51bbaf0f79a217bc424f
bradsimpson@ app:docker container sl

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
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
1a3245dd9a7c   postgres       "docker-entrypoint.s…"   8 seconds ago    Up 8 seconds    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
6ac39a0815ec   nginx:alpine   "/docker-entrypoint.…"   25 minutes ago   Up 25 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
bradsimpson@ app:\clear

bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.0 (Debian 15.0-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                  List of databases
     Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
--------------+----------+----------+------------+------------+-----------------------
 postgres     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 taco_tuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
              |          |          |            |            | postgres=CTc/postgres
 template1    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
              |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
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
local     taco_tuesday
bradsimpson@ app:

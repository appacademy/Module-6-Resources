Last login: Mon Dec  5 17:42:41 on ttys002

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@ ~:\clear






































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
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
postgres                         latest    027eba2e8939   6 weeks ago     377MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   7 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
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

bradsimpson@ ~:docker container run [options] image-name [command]
docker: invalid reference format.
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
2022/12/06 16:35:07 [notice] 1#1: using the "epoll" event method
2022/12/06 16:35:07 [notice] 1#1: nginx/1.21.6
2022/12/06 16:35:07 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2022/12/06 16:35:07 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2022/12/06 16:35:07 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/12/06 16:35:07 [notice] 1#1: start worker processes
2022/12/06 16:35:07 [notice] 1#1: start worker process 33
2022/12/06 16:35:07 [notice] 1#1: start worker process 34
172.17.0.1 - - [06/Dec/2022:16:35:29 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [06/Dec/2022:16:35:48 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [06/Dec/2022:16:35:50 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [06/Dec/2022:16:35:51 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [06/Dec/2022:16:35:52 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
^C2022/12/06 16:36:02 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/12/06 16:36:02 [notice] 33#33: exiting
2022/12/06 16:36:02 [notice] 33#33: exit
2022/12/06 16:36:02 [notice] 34#34: exiting
2022/12/06 16:36:02 [notice] 34#34: exit
2022/12/06 16:36:02 [notice] 1#1: signal 17 (SIGCHLD) received from 34
2022/12/06 16:36:02 [notice] 1#1: worker process 34 exited with code 0
2022/12/06 16:36:02 [notice] 1#1: signal 29 (SIGIO) received
2022/12/06 16:36:02 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2022/12/06 16:36:02 [notice] 1#1: worker process 33 exited with code 0
2022/12/06 16:36:02 [notice] 1#1: exit
bradsimpson@ ~:docker container run --name cool_container -p 8080:80 -d nginx
docker: Error response from daemon: Conflict. The container name "/cool_container" is already in use by container "46ccb04aa17148ae7b198478b78e2c53d9e9185545af9891fc390414608cc366". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED              STATUS                      PORTS                                       NAMES
46ccb04aa171   nginx                            "/docker-entrypoint.…"   About a minute ago   Exited (0) 31 seconds ago                                               cool_container
ff1ac8e19678   hello-world                      "/hello"                 5 minutes ago        Exited (0) 5 minutes ago                                                zealous_jones
5003d07f4b40   hello-world                      "/hello"                 31 minutes ago       Exited (0) 31 minutes ago                                               condescending_lichterman
8484dc3e0379   bradsimpson213/wacky_wed-react   "docker-entrypoint.s…"   3 weeks ago          Exited (1) 3 weeks ago                                                  react_demo
1a3245dd9a7c   postgres                         "docker-entrypoint.s…"   3 weeks ago          Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
a0b207004d09   postgres                         "docker-entrypoint.s…"   3 weeks ago          Exited (0) 3 weeks ago                                                  postgres5431_v2
e7d9cbf64f26   postgres                         "docker-entrypoint.s…"   3 weeks ago          Exited (0) 3 weeks ago                                                  new_postgres5431
e7bf5506db48   postgres                         "docker-entrypoint.s…"   3 weeks ago          Exited (0) 3 weeks ago                                                  postgres5431
6ac39a0815ec   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago          Exited (255) 3 weeks ago    0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago          Exited (0) 3 weeks ago                                                  c4
89616095146f   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago          Exited (0) 3 weeks ago                                                  c3
44af67958573   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago          Exited (0) 3 weeks ago                                                  c2
d2ae5fc87277   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago          Exited (0) 3 weeks ago                                                  c1
8dc6ce7ec8ff   nginx                            "/docker-entrypoint.…"   4 weeks ago          Exited (0) 3 weeks ago                                                  vibrant_leavitt
bradsimpson@ ~:docker container run -p 8080:80 -d nginx
2dd4a5e40c4a7f82286ce73b63b00199dda53f73de75cc79fdc8e83a92270288
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   11 seconds ago   Up 9 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -rm alpine echo howdy programmers
unknown shorthand flag: 'r' in -rm
See 'docker container run --help'.
bradsimpson@ ~:docker container run --rm alpine echo howdy programmers
howdy programmers
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                      PORTS                                       NAMES
2dd4a5e40c4a   nginx                            "/docker-entrypoint.…"   8 minutes ago    Up 8 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       gracious_nightingale
46ccb04aa171   nginx                            "/docker-entrypoint.…"   10 minutes ago   Exited (0) 9 minutes ago                                                cool_container
ff1ac8e19678   hello-world                      "/hello"                 14 minutes ago   Exited (0) 14 minutes ago                                               zealous_jones
5003d07f4b40   hello-world                      "/hello"                 40 minutes ago   Exited (0) 40 minutes ago                                               condescending_lichterman
8484dc3e0379   bradsimpson213/wacky_wed-react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                                  react_demo
1a3245dd9a7c   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
a0b207004d09   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                  postgres5431_v2
e7d9cbf64f26   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                  new_postgres5431
e7bf5506db48   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                  postgres5431
6ac39a0815ec   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                  c4
89616095146f   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                  c3
44af67958573   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                  c2
d2ae5fc87277   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                  c1
8dc6ce7ec8ff   nginx                            "/docker-entrypoint.…"   4 weeks ago      Exited (0) 3 weeks ago                                                  vibrant_leavitt
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -it alpine sh
/ # ls
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
/bin # nano
sh: nano: not found
/bin # ls
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
/bin # ^C
/bin # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8000:80 nginx
f886e5c6b024907918f64d2592cb13297de98842d7bc66430f047b7f76d3ffd5
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   7 seconds ago    Up 6 seconds    0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:docker container run -it --name test alpine sh 
/ # \la
sh: la: not found
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                       PORTS                                       NAMES
d653502966f9   alpine                           "sh"                     21 seconds ago   Exited (0) 7 seconds ago                                                 test
f886e5c6b024   nginx                            "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes                 0.0.0.0:8000->80/tcp, :::8000->80/tcp       gifted_shirley
da16b1219fad   alpine                           "sh"                     10 minutes ago   Exited (130) 6 minutes ago                                               hungry_curie
2dd4a5e40c4a   nginx                            "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       gracious_nightingale
46ccb04aa171   nginx                            "/docker-entrypoint.…"   21 minutes ago   Exited (0) 20 minutes ago                                                cool_container
ff1ac8e19678   hello-world                      "/hello"                 26 minutes ago   Exited (0) 25 minutes ago                                                zealous_jones
5003d07f4b40   hello-world                      "/hello"                 51 minutes ago   Exited (0) 51 minutes ago                                                condescending_lichterman
8484dc3e0379   bradsimpson213/wacky_wed-react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                                   react_demo
1a3245dd9a7c   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
a0b207004d09   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                   postgres5431_v2
e7d9cbf64f26   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                   new_postgres5431
e7bf5506db48   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                   postgres5431
6ac39a0815ec   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c4
89616095146f   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c3
44af67958573   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c2
d2ae5fc87277   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c1
8dc6ce7ec8ff   nginx                            "/docker-entrypoint.…"   4 weeks ago      Exited (0) 3 weeks ago                                                   vibrant_leavitt
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run --rm --name test ubuntu echo hello world 
docker: Error response from daemon: Conflict. The container name "/test" is already in use by container "d653502966f904fac632195f8603fa3d1d7d722a16dc023068ca6060b611ad61". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ ~:docker container run --rm --name test2 ubuntu echo hello world 
hello world
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   21 minutes ago   Up 21 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                       PORTS                                       NAMES
d653502966f9   alpine                           "sh"                     2 minutes ago    Exited (0) 2 minutes ago                                                 test
f886e5c6b024   nginx                            "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                 0.0.0.0:8000->80/tcp, :::8000->80/tcp       gifted_shirley
da16b1219fad   alpine                           "sh"                     12 minutes ago   Exited (130) 8 minutes ago                                               hungry_curie
2dd4a5e40c4a   nginx                            "/docker-entrypoint.…"   21 minutes ago   Up 21 minutes                0.0.0.0:8080->80/tcp, :::8080->80/tcp       gracious_nightingale
46ccb04aa171   nginx                            "/docker-entrypoint.…"   23 minutes ago   Exited (0) 22 minutes ago                                                cool_container
ff1ac8e19678   hello-world                      "/hello"                 28 minutes ago   Exited (0) 28 minutes ago                                                zealous_jones
5003d07f4b40   hello-world                      "/hello"                 53 minutes ago   Exited (0) 53 minutes ago                                                condescending_lichterman
8484dc3e0379   bradsimpson213/wacky_wed-react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                                   react_demo
1a3245dd9a7c   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
a0b207004d09   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                   postgres5431_v2
e7d9cbf64f26   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                   new_postgres5431
e7bf5506db48   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                   postgres5431
6ac39a0815ec   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c4
89616095146f   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c3
44af67958573   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c2
d2ae5fc87277   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                   c1
8dc6ce7ec8ff   nginx                            "/docker-entrypoint.…"   4 weeks ago      Exited (0) 3 weeks ago                                                   vibrant_leavitt
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   22 minutes ago   Up 22 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
postgres                         latest    027eba2e8939   6 weeks ago     377MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   7 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
888c44f3808b   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
39816ba14919   my_network2    bridge    local
7775a70e761d   my_network3    bridge    local
475754f27665   none           null      local
ef178e0d46c8   taco_tuesday   bridge    local
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
local     taco_tuesday
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                        PORTS                                       NAMES
d653502966f9   alpine                           "sh"                     4 minutes ago    Exited (0) 4 minutes ago                                                  test
f886e5c6b024   nginx                            "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                  0.0.0.0:8000->80/tcp, :::8000->80/tcp       gifted_shirley
da16b1219fad   alpine                           "sh"                     14 minutes ago   Exited (130) 10 minutes ago                                               hungry_curie
2dd4a5e40c4a   nginx                            "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes                 0.0.0.0:8080->80/tcp, :::8080->80/tcp       gracious_nightingale
46ccb04aa171   nginx                            "/docker-entrypoint.…"   25 minutes ago   Exited (0) 24 minutes ago                                                 cool_container
ff1ac8e19678   hello-world                      "/hello"                 30 minutes ago   Exited (0) 30 minutes ago                                                 zealous_jones
5003d07f4b40   hello-world                      "/hello"                 55 minutes ago   Exited (0) 55 minutes ago                                                 condescending_lichterman
8484dc3e0379   bradsimpson213/wacky_wed-react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                                    react_demo
1a3245dd9a7c   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago      0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
a0b207004d09   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                    postgres5431_v2
e7d9cbf64f26   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                    new_postgres5431
e7bf5506db48   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                                    postgres5431
6ac39a0815ec   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (255) 3 weeks ago      0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                    c4
89616095146f   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                    c3
44af67958573   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                    c2
d2ae5fc87277   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                                    c1
8dc6ce7ec8ff   nginx                            "/docker-entrypoint.…"   4 weeks ago      Exited (0) 3 weeks ago                                                    vibrant_leavitt
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   7 minutes ago    Up 7 minutes    0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
2dd4a5e40c4a   nginx     "/docker-entrypoint.…"   24 minutes ago   Up 24 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   gracious_nightingale
bradsimpson@ ~:docker container stop gracious_nightingale f886e5c6b024 
gracious_nightingale
f886e5c6b024
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container start gifted_shirley
gifted_shirley
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 3 seconds   0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
bradsimpson@ ~:docker container rm zealous_jones
zealous_jones
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED             STATUS                         PORTS                                       NAMES
d653502966f9   alpine                           "sh"                     9 minutes ago       Exited (0) 8 minutes ago                                                   test
f886e5c6b024   nginx                            "/docker-entrypoint.…"   11 minutes ago      Up 2 minutes                   0.0.0.0:8000->80/tcp, :::8000->80/tcp       gifted_shirley
da16b1219fad   alpine                           "sh"                     18 minutes ago      Exited (130) 14 minutes ago                                                hungry_curie
2dd4a5e40c4a   nginx                            "/docker-entrypoint.…"   28 minutes ago      Exited (0) 3 minutes ago                                                   gracious_nightingale
46ccb04aa171   nginx                            "/docker-entrypoint.…"   30 minutes ago      Exited (0) 29 minutes ago                                                  cool_container
5003d07f4b40   hello-world                      "/hello"                 About an hour ago   Exited (0) About an hour ago                                               condescending_lichterman
8484dc3e0379   bradsimpson213/wacky_wed-react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                                     react_demo
1a3245dd9a7c   postgres                         "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago       0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres5431_v3
a0b207004d09   postgres                         "docker-entrypoint.s…"   3 weeks ago         Exited (0) 3 weeks ago                                                     postgres5431_v2
e7d9cbf64f26   postgres                         "docker-entrypoint.s…"   3 weeks ago         Exited (0) 3 weeks ago                                                     new_postgres5431
e7bf5506db48   postgres                         "docker-entrypoint.s…"   3 weeks ago         Exited (0) 3 weeks ago                                                     postgres5431
6ac39a0815ec   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago         Exited (255) 3 weeks ago       0.0.0.0:8080->80/tcp, :::8080->80/tcp       ecstatic_engelbart
c9250f4d688a   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago         Exited (0) 3 weeks ago                                                     c4
89616095146f   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago         Exited (0) 3 weeks ago                                                     c3
44af67958573   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago         Exited (0) 3 weeks ago                                                     c2
d2ae5fc87277   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago         Exited (0) 3 weeks ago                                                     c1
8dc6ce7ec8ff   nginx                            "/docker-entrypoint.…"   4 weeks ago         Exited (0) 4 weeks ago                                                     vibrant_leavitt
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
d653502966f904fac632195f8603fa3d1d7d722a16dc023068ca6060b611ad61
da16b1219fadd3258d615b03f79b32f62924900bc2ba2dca9f5b652cd091ae0d
2dd4a5e40c4a7f82286ce73b63b00199dda53f73de75cc79fdc8e83a92270288
46ccb04aa17148ae7b198478b78e2c53d9e9185545af9891fc390414608cc366
5003d07f4b401bbe511349fc91af92940d2be1374b7b5f04d7cdeb2ca2298889
8484dc3e03794ad26d4a5c16d068f1f9b196e56b2d4dbd0e38edd08152c16984
1a3245dd9a7c0f40488c298390a92ce417c3b538ac5c51bbaf0f79a217bc424f
a0b207004d0982cea67f1ccdb534adf9a3c075c2b76a193875d4731091e1b5b1
e7d9cbf64f26de165e36ff6a1cb7ba26fc68b9895ffee4fd07249a95ad542ef3
e7bf5506db48bdb6f6cdf51d2f5db5220113eba4554c902578d67ae04c08d30c
6ac39a0815ecd594bb4b5b64eb154f0b42b23f8116388c85b355fa9a1cd2493f
c9250f4d688ab2a3f29e44ee169e8ecf83ed3dd541afdb3a75a6d27292f79789
89616095146ffb152e4aa64fb514d0f09f948fba38d6db36e87c8a5606853dc9
44af679585735667016eea1e1471fcee2098f0635d95f1a1b7f02bd52f2ef14d
d2ae5fc87277b7519579d134e8c9f93aba4e7d0a323ae9aed9354db2af7625f9
8dc6ce7ec8ff834da83eb7238b6a435b03b0a5c089fa247c56cdc7696a328f92

Total reclaimed space: 55.41MB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                                   NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp, :::8000->80/tcp   gifted_shirley
bradsimpson@ ~:docker container stop gifted_shirley
gifted_shirley
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
f886e5c6b024   nginx     "/docker-entrypoint.…"   13 minutes ago   Exited (0) 2 seconds ago             gifted_shirley
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx 
d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
d002001b3e45   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   upbeat_vaughan
bradsimpson@ ~:docker container exec -it upbeat_vaughan sh
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
bradsimpson@ ~:


Last login: Mon Dec  5 17:42:45 on ttys003

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\clear


















bradsimpson@ ~:
bradsimpson@ ~:\clear






















bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
888c44f3808b   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
39816ba14919   my_network2    bridge    local
7775a70e761d   my_network3    bridge    local
475754f27665   none           null      local
ef178e0d46c8   taco_tuesday   bridge    local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
d002001b3e45   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 27 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   upbeat_vaughan
bradsimpson@ ~:docker container inspect upbeat_vaughan
[
    {
        "Id": "d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4",
        "Created": "2022-12-06T17:08:23.330864333Z",
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
            "Pid": 4344,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-12-06T17:08:24.271774357Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4/hostname",
        "HostsPath": "/var/lib/docker/containers/d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4/hosts",
        "LogPath": "/var/lib/docker/containers/d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4/d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4-json.log",
        "Name": "/upbeat_vaughan",
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
                "LowerDir": "/var/lib/docker/overlay2/253c5768268cb33d6d34d2582a20602a8721db59313a6b3fddb70050ce49ec03-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/253c5768268cb33d6d34d2582a20602a8721db59313a6b3fddb70050ce49ec03/merged",
                "UpperDir": "/var/lib/docker/overlay2/253c5768268cb33d6d34d2582a20602a8721db59313a6b3fddb70050ce49ec03/diff",
                "WorkDir": "/var/lib/docker/overlay2/253c5768268cb33d6d34d2582a20602a8721db59313a6b3fddb70050ce49ec03/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "d002001b3e45",
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
            "SandboxID": "c672824a08ac8c9ca6b9c62075fdbc06a4592865de2a835528dce4c146bbd9a0",
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
            "SandboxKey": "/var/run/docker/netns/c672824a08ac",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "b8f38b72fc50c53351715a35c52b7e048d17aba9fbe3ce7c9c844fd1cfb4e4d2",
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
                    "NetworkID": "888c44f3808be44bba7de68b1689d52a794ae26b8ebfb2d27ec6ea1ee9bf1c41",
                    "EndpointID": "b8f38b72fc50c53351715a35c52b7e048d17aba9fbe3ce7c9c844fd1cfb4e4d2",
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
888c44f3808b   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
39816ba14919   my_network2    bridge    local
7775a70e761d   my_network3    bridge    local
475754f27665   none           null      local
ef178e0d46c8   taco_tuesday   bridge    local
bradsimpson@ ~:docker network rm taco_tuesday
taco_tuesday
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
888c44f3808b   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
39816ba14919   my_network2   bridge    local
7775a70e761d   my_network3   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker network 39816ba14919 7775a70e761d

Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
bradsimpson@ ~:docker network rm 39816ba14919 7775a70e761d
39816ba14919
7775a70e761d
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
888c44f3808b   bridge       bridge    local
7318efe60d0f   host         host      local
1a584f63c88c   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
888c44f3808b   bridge       bridge    local
7318efe60d0f   host         host      local
1a584f63c88c   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker network create --driver bridge my_network2
ef43db5a14d28bc9b09f3bf15aaf0aefe63441f833f730940925889696060ca6
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
888c44f3808b   bridge        bridge    local
7318efe60d0f   host          host      local
1a584f63c88c   my_network    bridge    local
ef43db5a14d2   my_network2   bridge    local
475754f27665   none          null      local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
d002001b3e45   nginx     "/docker-entrypoint.…"   35 minutes ago   Up 35 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   upbeat_vaughan
bradsimpson@ ~:docker container stop upbeat_vaughan
upbeat_vaughan
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run -d --name c1 --network my_network2
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ ~:docker container run -d --name c1 --network my_network2 nginx:alpine
aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago   Up 2 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c2 --network my_network2 nginx:alpine
854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9
bradsimpson@ ~:\clear





bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   10 seconds ago   Up 8 seconds    80/tcp    c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   30 seconds ago   Up 28 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c3 nginx:alpine
ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine
13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   3 seconds ago    Up 2 seconds    80/tcp    c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   10 seconds ago   Up 9 seconds    80/tcp    c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   35 seconds ago   Up 33 seconds   80/tcp    c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   55 seconds ago   Up 53 seconds   80/tcp    c1
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da",
        "Created": "2022-12-06T17:45:04.778845195Z",
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
            "Pid": 5004,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-12-06T17:45:06.722015001Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da/hostname",
        "HostsPath": "/var/lib/docker/containers/aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da/hosts",
        "LogPath": "/var/lib/docker/containers/aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da/aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da-json.log",
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
            "NetworkMode": "my_network2",
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
                "LowerDir": "/var/lib/docker/overlay2/e13902d2b28f3d2ffafa834658aeb0ddb0d3005afc67769607ab3fbe8281bdbb-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/e13902d2b28f3d2ffafa834658aeb0ddb0d3005afc67769607ab3fbe8281bdbb/merged",
                "UpperDir": "/var/lib/docker/overlay2/e13902d2b28f3d2ffafa834658aeb0ddb0d3005afc67769607ab3fbe8281bdbb/diff",
                "WorkDir": "/var/lib/docker/overlay2/e13902d2b28f3d2ffafa834658aeb0ddb0d3005afc67769607ab3fbe8281bdbb/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "aaba71b9fb26",
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
            "SandboxID": "fc09b2d463ebcee9ae974729a0ccd06be647c880c2622e764a9ca6ca5b9f17fa",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/fc09b2d463eb",
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
                "my_network2": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "aaba71b9fb26"
                    ],
                    "NetworkID": "ef43db5a14d28bc9b09f3bf15aaf0aefe63441f833f730940925889696060ca6",
                    "EndpointID": "4affa3ecf6a332f927c3aec83a410c4b22c41f2c457bf6b16f6ccbfe66c6d149",
                    "Gateway": "172.19.0.1",
                    "IPAddress": "172.19.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:13:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:docker container inspect c2
[
    {
        "Id": "854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9",
        "Created": "2022-12-06T17:45:24.940489386Z",
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
            "Pid": 5188,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-12-06T17:45:26.119937376Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9/hostname",
        "HostsPath": "/var/lib/docker/containers/854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9/hosts",
        "LogPath": "/var/lib/docker/containers/854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9/854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9-json.log",
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
            "NetworkMode": "my_network2",
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
                "LowerDir": "/var/lib/docker/overlay2/b588389478ff4316e00d13045e47486e7fc9275376c8f0b6974aeb525f300a2d-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/b588389478ff4316e00d13045e47486e7fc9275376c8f0b6974aeb525f300a2d/merged",
                "UpperDir": "/var/lib/docker/overlay2/b588389478ff4316e00d13045e47486e7fc9275376c8f0b6974aeb525f300a2d/diff",
                "WorkDir": "/var/lib/docker/overlay2/b588389478ff4316e00d13045e47486e7fc9275376c8f0b6974aeb525f300a2d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "854c47ab654e",
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
            "SandboxID": "8c0cec2fc977e38dc12062b4ae87893872a04aee8deb8d135dbbdcde127d3dca",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/8c0cec2fc977",
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
                "my_network2": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "854c47ab654e"
                    ],
                    "NetworkID": "ef43db5a14d28bc9b09f3bf15aaf0aefe63441f833f730940925889696060ca6",
                    "EndpointID": "1ea5d18540e5586d441ea0805704eb28daa5987b8e88e22939e7090fa78fe74a",
                    "Gateway": "172.19.0.1",
                    "IPAddress": "172.19.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:13:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
bradsimpson@ ~:docker container inspect c3
[
    {
        "Id": "ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a",
        "Created": "2022-12-06T17:45:49.403412749Z",
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
            "Pid": 5366,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-12-06T17:45:50.257758006Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a/hostname",
        "HostsPath": "/var/lib/docker/containers/ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a/hosts",
        "LogPath": "/var/lib/docker/containers/ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a/ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/adbc57f57c8623030f473303d76b7eea29ea8ee658f17384e207b24eb5644498-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/adbc57f57c8623030f473303d76b7eea29ea8ee658f17384e207b24eb5644498/merged",
                "UpperDir": "/var/lib/docker/overlay2/adbc57f57c8623030f473303d76b7eea29ea8ee658f17384e207b24eb5644498/diff",
                "WorkDir": "/var/lib/docker/overlay2/adbc57f57c8623030f473303d76b7eea29ea8ee658f17384e207b24eb5644498/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "ec8181220f09",
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
            "SandboxID": "9da9047c8a31820f431027100644928a18dc58d6a339ebb3f45e5fbdd5b05c3a",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/9da9047c8a31",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "bdef25bf9a075444f2c211070cec0438661ab5125a737f480b88062a9ff46b75",
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
                    "NetworkID": "888c44f3808be44bba7de68b1689d52a794ae26b8ebfb2d27ec6ea1ee9bf1c41",
                    "EndpointID": "bdef25bf9a075444f2c211070cec0438661ab5125a737f480b88062a9ff46b75",
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
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698",
        "Created": "2022-12-06T17:45:56.267643332Z",
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
            "Pid": 5470,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-12-06T17:45:57.063459113Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b1c3acb28882519cf6d3a4d7fe2b21d0ae20bde9cfd2c08a7de057f8cfccff15",
        "ResolvConfPath": "/var/lib/docker/containers/13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698/hostname",
        "HostsPath": "/var/lib/docker/containers/13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698/hosts",
        "LogPath": "/var/lib/docker/containers/13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698/13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/0e7c20a5441486958ea05234f88afe0b3ce959fc4ea1329311fa1d33ab0cc7b5-init/diff:/var/lib/docker/overlay2/8300ef7fc167f47e1ea49203a4d844bfed4978583b687b835fb3efe42544f1c0/diff:/var/lib/docker/overlay2/a75fcc1ee2c2f8b1f38349fc46e9443c4086ffb456680a96c7a54c1fdc668f02/diff:/var/lib/docker/overlay2/a33f814fd99234120273879e0be8400e6a42ee78a3d70e01171be165451ca1ec/diff:/var/lib/docker/overlay2/ffd737b698ba4590d1f08c0e36696d28ed297432113b295fdea237ce89ae2869/diff:/var/lib/docker/overlay2/d789de4827ccb4924ef58381dbc6fc5237b90a20a58061cbd0a18016685fff90/diff:/var/lib/docker/overlay2/794253c0d848bab2ec029f063423f339348a043c7402cf2c3aefed837abfde5c/diff",
                "MergedDir": "/var/lib/docker/overlay2/0e7c20a5441486958ea05234f88afe0b3ce959fc4ea1329311fa1d33ab0cc7b5/merged",
                "UpperDir": "/var/lib/docker/overlay2/0e7c20a5441486958ea05234f88afe0b3ce959fc4ea1329311fa1d33ab0cc7b5/diff",
                "WorkDir": "/var/lib/docker/overlay2/0e7c20a5441486958ea05234f88afe0b3ce959fc4ea1329311fa1d33ab0cc7b5/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "13aba8abea04",
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
            "SandboxID": "5592d8ae13be575878e45a3b5860a1b9744c6b953c5bd8b30f3a1575ad546122",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/5592d8ae13be",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "39045fed517ebe650a76b0eeaf4c12ebdd4adbac759804cd3b6ef629e335a9d0",
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
                    "NetworkID": "888c44f3808be44bba7de68b1689d52a794ae26b8ebfb2d27ec6ea1ee9bf1c41",
                    "EndpointID": "39045fed517ebe650a76b0eeaf4c12ebdd4adbac759804cd3b6ef629e335a9d0",
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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 3 c2
PING c2 (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: seq=0 ttl=64 time=2.808 ms
64 bytes from 172.19.0.3: seq=1 ttl=64 time=0.576 ms
64 bytes from 172.19.0.3: seq=2 ttl=64 time=0.082 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.082/1.155/2.808 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 c4
ping: bad address 'c4'
/ # ping -c 3 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes

--- 172.17.0.2 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss
/ # exit
bradsimpson@ ~:docker container exec -it c4 ash
/ # ping -c 3 c1
ping: bad address 'c1'
/ # ping -c 3 c2
ping: bad address 'c2'
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes
64 bytes from 172.17.0.2: seq=0 ttl=64 time=0.307 ms
64 bytes from 172.17.0.2: seq=1 ttl=64 time=0.095 ms
64 bytes from 172.17.0.2: seq=2 ttl=64 time=0.116 ms

--- 172.17.0.2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.095/0.172/0.307 ms
/ # exit
bradsimpson@ ~:docker network

Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
bradsimpson@ ~:docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
888c44f3808b   bridge        bridge    local
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
local     taco_tuesday
bradsimpson@ ~:

Last login: Tue Dec  6 12:15:57 on ttys003

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\clear


















bradsimpson@ ~:\clear
























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
local     taco_tuesday
bradsimpson@ ~:docker container run --mount type=bind/volume,source=/absolute/path/to/folder/name_of_volume,target=/absolute/path/in/container
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ ~:\ls
Applications	Downloads	Music		Pipfile.lock	app
Desktop		Library		Pictures	Postman		docker
Documents	Movies		Pipfile		Public		opt
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container run --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8080:80 nginx:alpine
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2022/12/06 18:31:53 [notice] 1#1: using the "epoll" event method
2022/12/06 18:31:53 [notice] 1#1: nginx/1.21.6
2022/12/06 18:31:53 [notice] 1#1: built by gcc 10.3.1 20211027 (Alpine 10.3.1_git20211027) 
2022/12/06 18:31:53 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2022/12/06 18:31:53 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/12/06 18:31:53 [notice] 1#1: start worker processes
2022/12/06 18:31:53 [notice] 1#1: start worker process 33
2022/12/06 18:31:53 [notice] 1#1: start worker process 34
172.17.0.1 - - [06/Dec/2022:18:32:09 +0000] "GET / HTTP/1.1" 200 123 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36" "-"
^C2022/12/06 18:32:28 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/12/06 18:32:28 [notice] 34#34: exiting
2022/12/06 18:32:28 [notice] 33#33: exiting
2022/12/06 18:32:28 [notice] 34#34: exit
2022/12/06 18:32:28 [notice] 33#33: exit
2022/12/06 18:32:28 [notice] 1#1: signal 17 (SIGCHLD) received from 33
2022/12/06 18:32:28 [notice] 1#1: worker process 33 exited with code 0
2022/12/06 18:32:28 [notice] 1#1: signal 29 (SIGIO) received
2022/12/06 18:32:28 [notice] 1#1: signal 17 (SIGCHLD) received from 34
2022/12/06 18:32:28 [notice] 1#1: worker process 34 exited with code 0
2022/12/06 18:32:28 [notice] 1#1: exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   46 minutes ago   Up 46 minutes   80/tcp    c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   46 minutes ago   Up 46 minutes   80/tcp    c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp    c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp    c1
bradsimpson@ ~:docker container run --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8080:80 -d nginx:alpine
52b1a5a73114d9e22044339ab6294d738fd4bce05baf14d097b13de10ac395a5
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
52b1a5a73114   nginx:alpine   "/docker-entrypoint.…"   20 seconds ago   Up 15 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   trusting_bouman
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp                                  c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp                                  c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp                                  c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   80/tcp                                  c1
bradsimpson@ ~:docker container exec -it trusting_bouman ash
/ # \lsd
ash: lsd: not found
/ # \ls
bin                   media                 srv
dev                   mnt                   sys
docker-entrypoint.d   opt                   tmp
docker-entrypoint.sh  proc                  usr
etc                   root                  var
home                  run
lib                   sbin
/ # cd usr
/usr # cd share
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
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:\clear

bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
52b1a5a73114   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago    Up 3 minutes    0.0.0.0:8080->80/tcp, :::8080->80/tcp   trusting_bouman
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   50 minutes ago   Up 50 minutes   80/tcp                                  c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp                                  c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp                                  c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   80/tcp                                  c1
bradsimpson@ app:docker container stop c1 c2 c3 c4 trusting_bouman
c1
c2
c3
c4
trusting_bouman
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                      PORTS     NAMES
52b1a5a73114   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago       Exited (0) 7 seconds ago              trusting_bouman
a1572282ef9f   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago       Exited (0) 4 minutes ago              jovial_torvalds
13aba8abea04   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago      Exited (0) 7 seconds ago              c4
ec8181220f09   nginx:alpine   "/docker-entrypoint.…"   51 minutes ago      Exited (0) 7 seconds ago              c3
854c47ab654e   nginx:alpine   "/docker-entrypoint.…"   52 minutes ago      Exited (0) 7 seconds ago              c2
aaba71b9fb26   nginx:alpine   "/docker-entrypoint.…"   52 minutes ago      Exited (0) 7 seconds ago              c1
d002001b3e45   nginx          "/docker-entrypoint.…"   About an hour ago   Exited (0) 53 minutes ago             upbeat_vaughan
f886e5c6b024   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) 2 hours ago                gifted_shirley
bradsimpson@ app:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
52b1a5a73114d9e22044339ab6294d738fd4bce05baf14d097b13de10ac395a5
a1572282ef9f2a9e389e97b7474191d187c760e6c4722d66d59941140aeba4fb
13aba8abea04b891c7c113181cf24725ecdc3493a69bac8fbb41be8d7e841698
ec8181220f0943bfc9795e75fd0df8de0ef52d3964afb05172f2e17fe1c8928a
854c47ab654e7eea5ec59b966673c6adf82a6e1b07ee2136abd642dbee34b9c9
aaba71b9fb26e16072435e7a5486b23977166375ee310511f7711778d4af20da
d002001b3e45a1eb7e36631069f7ca3bfbc4035c44170cd395a3fb19a25b96a4
f886e5c6b024907918f64d2592cb13297de98842d7bc66430f047b7f76d3ffd5

Total reclaimed space: 2.72MB
bradsimpson@ app:\clear

bradsimpson@ app:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
postgres                         latest    027eba2e8939   6 weeks ago     377MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   7 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ app:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:bab8d7be6466e029f7fa1e69ff6aa0082704db330572638fd01f2791824774d8
Deleted: sha256:027eba2e89396946fd63dd69c919844b248c8b591c07545321de3006503cc974
Deleted: sha256:db5225c78af25f6356fa95792483a93502c014455e51055dead78e4f08d8fdde
Deleted: sha256:2ca1ad5051c51b5d0f61005847c324072bd8bff45b54c7fb7f6d0b91fe073d1e
Deleted: sha256:76d9950cf76de383ac195c6f23ec97f4d410e85e775ae9a63c085311d3961063
Deleted: sha256:7bb8f2873db6ab2c5569057bb5c35620fd047f53fd6f50fa1d7f54bc78a080c4
Deleted: sha256:b78c2b5113c4583ee7cd70a5c52ce277634ae9f9f35b75451e3d4d49a3db3e11
Deleted: sha256:98c27c1180d875661001719e25771018691903f1a7e10f9c173bf7f7446a50b7
Deleted: sha256:ef0e8c9a121ddf7ded5e8d1d3fe484e573d9e28634215a4574842f724576dd2b
Deleted: sha256:9f92889e6abda3dfc419a2cf9c148955a2141b87da6582839f18c861c70eebcf
Deleted: sha256:2c3906fdeb1a5e619aa8d2b53e5735c3bf628be792939af75d9b626db276e422
Deleted: sha256:0ac2a847c23a8022fc3c4e08a7da997dfb61125cb1cb9e1dd619648452033d7d
Deleted: sha256:f8e20684b92bd01980738612e2a75c0f2a5804ded56729b202eeade15e845c97
Deleted: sha256:757f722c7c80d5e86dc04c390fbf2204d0e14bfaf81cd0337d6b915b5b97548f
Deleted: sha256:a12586ed027fafddcddcc63b31671f406c25e43342479fc92a330e7e30d65f2e
bradsimpson@ app:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   7 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
025c56f98b67: Pull complete 
26dc25c16f4e: Pull complete 
a032d8a894de: Pull complete 
40dba7d35750: Pull complete 
8ebb44a56070: Pull complete 
813fd6cf203b: Pull complete 
7024f61bf8f5: Pull complete 
23f986b322e8: Pull complete 
1fb05ff7a8d6: Pull complete 
74afc7d9bc5c: Pull complete 
7c2c7eebef2f: Pull complete 
bdd9df7f1d37: Pull complete 
33d269a3a052: Pull complete 
Digest: sha256:10d6e725f9b2f5531617d93164f4fc85b1739e04cab62cbfbfb81ccd866513b8
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
postgres                         latest    4c6b3cc10e6b   2 hours ago     379MB
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   7 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ app:docker image inspect postgres
[
    {
        "Id": "sha256:4c6b3cc10e6bbb2afd68caa44a3eb6cef12caf483e60b28c6de2c56e8f1b99bc",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:10d6e725f9b2f5531617d93164f4fc85b1739e04cab62cbfbfb81ccd866513b8"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-12-06T16:21:34.600185732Z",
        "Container": "dd061ec0d6e65efcba137b69e1e3e9b624b82f1cecd4f38c294a0f57b58fe233",
        "ContainerConfig": {
            "Hostname": "dd061ec0d6e6",
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
            "Image": "sha256:52f4b92bfbd970ff262f6fc4edfbc1ae754dea0a99f84d187fe4ee9fffbbac14",
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
            "Image": "sha256:52f4b92bfbd970ff262f6fc4edfbc1ae754dea0a99f84d187fe4ee9fffbbac14",
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
        "Size": 378636573,
        "VirtualSize": 378636573,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/329017f1bb12f7a00ceef40bc07385dc7fa95bede6728a6f321017439b97a71f/diff:/var/lib/docker/overlay2/3599746f2c5018e5828edab283c4c8b5d3aa43344a1564a4b0e6912fc90c14c0/diff:/var/lib/docker/overlay2/5c614fd13a0159070668f21be775f3656b80364f198446685a0e83a038187103/diff:/var/lib/docker/overlay2/c145e9457cedbdc5496c489790ca68edf58034b2be093e9e336089cdc3ff3ceb/diff:/var/lib/docker/overlay2/7bedb40e7d0b94ecfb87e0f2e816d18a1cd4fce6d94528796aa550695b72cb7b/diff:/var/lib/docker/overlay2/7d77b9f90fa9a58d415f7be7d43b23a904ba5589596be42db04b44de36f27d27/diff:/var/lib/docker/overlay2/6336bf9521e9224425085ecf6ce246c00791e6bb32edbc9d784caad2681bddac/diff:/var/lib/docker/overlay2/a8d90a317b1d38ddd724322cb074852b16391320b1c2a5ec4184203276b3c460/diff:/var/lib/docker/overlay2/230bf015722bea6930be31fd9f642e3d479862a07057de4e7cc79b4a6f20a20d/diff:/var/lib/docker/overlay2/e8e623f48f72b2f8ef537611f6d98f5940f1d1c646aef93c0b8509cc45ec9b99/diff:/var/lib/docker/overlay2/8bd55cc8c27e28ef6bb5c3fe1a86ee28916c80b347748f385021887af0478ee9/diff:/var/lib/docker/overlay2/3bb05f69f3b2fcce012ac51e60332f0a2b99db77f18c77068184cd0683cd716b/diff",
                "MergedDir": "/var/lib/docker/overlay2/6f46a1c752efc6fe3216d971254689800e6a88b40c74bcd1783cb1e568adccb1/merged",
                "UpperDir": "/var/lib/docker/overlay2/6f46a1c752efc6fe3216d971254689800e6a88b40c74bcd1783cb1e568adccb1/diff",
                "WorkDir": "/var/lib/docker/overlay2/6f46a1c752efc6fe3216d971254689800e6a88b40c74bcd1783cb1e568adccb1/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:b5ebffba54d3e3f7fd80435fcdc34c4a96fdb2ecab0f0a298fe08f74c2f69d29",
                "sha256:83ea585bd8d5e4e92e17e7a47b987674ddbdaa8fae3e5278d92a5e9f0bc95fa3",
                "sha256:348c05a139f2f94f4ca0250805f95a48e42cc8de4de5e27b735a782df14796d2",
                "sha256:18abf810e7046b9b016f9c841a08f06c30d7bae0aeb6f66395b275863b382535",
                "sha256:79674c8247be9f29fc7d017bfcdbd0d59363e195a7137a2f2d4a3fcb4a1e57da",
                "sha256:0843aa47049d40f0d98c3d5a1b019d162008c0d002fda1973a54e0cd4d75b4c5",
                "sha256:673ab51df9fa86d13ef7892f80559b7565b61267117b1970244080d0f2a4184a",
                "sha256:0cb0dda2ca2886b5589cdbd459732a7863143584bdb4d2708ee5bbda570a8827",
                "sha256:810b20c99b6739d1a2466cd70fa03cd2592c3465251c4408edd6e6f61ccd0328",
                "sha256:0f522f2c0565e8c0e4496f17785c509b533ba2ee3f9ee88b77ab75bd2659c337",
                "sha256:2192fa5f71ee165d42aa21ec9e16fb908ad8fdcb3eb2f522f1231847c73ec2cb",
                "sha256:cecf9c48543e14c59c007f730655385b3f94acabbe9a161c4c1b67d27e79c40a",
                "sha256:85604ecf5f86cd26eda59b255967a2bc8d4aa90937469f3ea55bbaf55a30fffe"
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
local     6b769352eb31a01b3fe6410a71a0dc6ff2994240bce8653a2c8ecd0f6616acaa
local     a9100dadfa006724a9145c0bf2951033ab3598680a14e4261cbfe1fae1239c1a
local     my_new_volume
local     my_volume
local     my_volume2
local     my_volume3
local     new_taco_tues
local     postgres-data
local     taco_tuesday
bradsimpson@ app:docker volume create taco_not_sandwich
taco_not_sandwich
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
bradsimpson@ app:docker container run -p 5431:5432 --name postgres5431 -d --mount type=volume,source=taco_not_sandwich,target=/var/lib/postgresql/data postgres
7a4406f9e2b4969ee223a4bdd16464699be6985ba30b55bf37ebac411a3e34cb
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS                      PORTS     NAMES
7a4406f9e2b4   postgres   "docker-entrypoint.s…"   20 seconds ago   Exited (1) 18 seconds ago             postgres5431
bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 -e POSTGRES_PASSWORD=password -d --mount type=volume,source=taco_not_sandwich,target=/var/lib/postgresql/data postgres
13f9a6126ef99117dff9ae8fb0fc67c823f416a61934e8161d33ad8bab204014
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \d
Did not find any relations.
postgres=# \u
invalid command \u
Try \? for help.
postgres=# \ls
invalid command \ls
Try \? for help.
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

postgres=# CREATE DATABASE hot_dog_not_sandwich WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                      List of databases
         Name         |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
----------------------+----------+----------+------------+------------+-----------------------
 hot_dog_not_sandwich | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres             | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0            | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                      |          |          |            |            | postgres=CTc/postgres
 template1            | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                      |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
13f9a6126ef9   postgres   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres1
bradsimpson@ app:docker container stop postgres1
postgres1
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS                     PORTS     NAMES
13f9a6126ef9   postgres   "docker-entrypoint.s…"   2 minutes ago   Exited (0) 8 seconds ago             postgres1
7a4406f9e2b4   postgres   "docker-entrypoint.s…"   4 minutes ago   Exited (1) 4 minutes ago             postgres5431
bradsimpson@ app:docker container prune 
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
13f9a6126ef99117dff9ae8fb0fc67c823f416a61934e8161d33ad8bab204014
7a4406f9e2b4969ee223a4bdd16464699be6985ba30b55bf37ebac411a3e34cb

Total reclaimed space: 0B
bradsimpson@ app:docker container ls -a
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
bradsimpson@ app:docker container run -p 5430:5432 --name post_sandwich -e POSTGRES_PASSWORD=password -d --mount type=volume,source=taco_not_sandwich,target=/var/lib/postgresql/data postgres
88754df26a8ac9eeeacc7ced182bfa9fcae8b24e532284cc470c559389283dc2
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                       NAMES
88754df26a8a   postgres   "docker-entrypoint.s…"   9 seconds ago   Up 8 seconds   0.0.0.0:5430->5432/tcp, :::5430->5432/tcp   post_sandwich
bradsimpson@ app:psql -p 5430 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                      List of databases
         Name         |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
----------------------+----------+----------+------------+------------+-----------------------
 hot_dog_not_sandwich | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres             | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0            | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                      |          |          |            |            | postgres=CTc/postgres
 template1            | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
                      |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:










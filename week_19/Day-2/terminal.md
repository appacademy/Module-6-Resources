Last login: Mon Apr  3 15:52:55 on ttys001

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
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/12345_react         latest    c63116090e8b   3 weeks ago     441MB
postgres                           latest    3b6645d2c145   4 weeks ago     379MB
nginx                              alpine    2bc7edbc3cf2   7 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   7 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   2 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   2 months ago    568MB
bradsimps213/react_project         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   2 months ago    568MB
my_project                         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   5 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   6 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   10 months ago   142MB
alpine                             latest    e66264b98777   10 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   18 months ago   13.3kB
bradsimpson@ ~:\clear



bradsimpson@ ~:docker container run [options] image-name [commands][ARG...]
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
2023/04/04 15:37:41 [notice] 1#1: using the "epoll" event method
2023/04/04 15:37:41 [notice] 1#1: nginx/1.21.6
2023/04/04 15:37:41 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/04/04 15:37:41 [notice] 1#1: OS: Linux 5.15.49-linuxkit
2023/04/04 15:37:41 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/04/04 15:37:41 [notice] 1#1: start worker processes
2023/04/04 15:37:41 [notice] 1#1: start worker process 31
2023/04/04 15:37:41 [notice] 1#1: start worker process 32
172.17.0.1 - - [04/Apr/2023:15:38:04 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:05 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8080/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
2023/04/04 15:38:05 [error] 32#32: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: "http://localhost:8080/"
172.17.0.1 - - [04/Apr/2023:15:38:39 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:41 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:42 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:43 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:43 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:44 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:45 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [04/Apr/2023:15:38:46 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36" "-"
^C2023/04/04 15:40:16 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/04/04 15:40:16 [notice] 31#31: exiting
2023/04/04 15:40:16 [notice] 31#31: exit
2023/04/04 15:40:16 [notice] 32#32: exiting
2023/04/04 15:40:16 [notice] 32#32: exit
2023/04/04 15:40:16 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/04/04 15:40:16 [notice] 1#1: worker process 31 exited with code 0
2023/04/04 15:40:16 [notice] 1#1: signal 29 (SIGIO) received
2023/04/04 15:40:16 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/04/04 15:40:16 [notice] 1#1: worker process 32 exited with code 0
2023/04/04 15:40:16 [notice] 1#1: exit
bradsimpson@ ~:\c;ear
-bash: c: command not found
-bash: ear: command not found
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
0c5c212e538b   nginx     "/docker-entrypoint.…"   3 minutes ago   Exited (0) 34 seconds ago             cool_container
bradsimpson@ ~:docker container run -d -p 8080:80 nginx
20c798aa3f32fb4f866c631f673647a7f8e7e97aab0ca1dbfe7d14b089f6ddff
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
20c798aa3f32   nginx     "/docker-entrypoint.…"   34 seconds ago   Up 33 seconds   0.0.0.0:8080->80/tcp   happy_morse
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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
20c798aa3f32   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp   happy_morse
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS                      PORTS     NAMES
f0d4100c1419   alpine    "sh"      About a minute ago   Exited (0) 30 seconds ago             reverent_bose
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
20c798aa3f32   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8080->80/tcp   happy_morse
bradsimpson@ ~:docker container run -it --rm alpine sh
/ # exit
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                          PORTS     NAMES
f0d4100c1419   alpine    "sh"      2 minutes ago   Exited (0) About a minute ago             reverent_bose
bradsimpson@ ~:docker container run -d -p 8080:80 nginx 
a4d1c8b12254ba4011bb9c2736e7d9c36b08d92a80ee901fcd2afed01de0c90a
docker: Error response from daemon: driver failed programming external connectivity on endpoint stupefied_chatelet (6c6f97ca037158177b034eaaf000a7acd5962f0db0b2420eaa39bbb742f4ae58): Bind for 0.0.0.0:8080 failed: port is already allocated.
bradsimpson@ ~:docker container run -d -p 8000:80 nginx 
f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   9 seconds ago   Up 8 seconds   0.0.0.0:8000->80/tcp   adoring_jennings
20c798aa3f32   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 9 minutes   0.0.0.0:8080->80/tcp   happy_morse
bradsimpson@ ~:docker container run -it --name test alpine sh
/ # exit
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                     PORTS     NAMES
cd2f7af1b2d0   alpine    "sh"      15 seconds ago   Exited (0) 8 seconds ago             test
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
cd2f7af1b2d0   alpine    "sh"      2 minutes ago   Exited (0) 2 minutes ago             test
bradsimpson@ ~:docker contains ls 
docker: 'contains' is not a docker command.
See 'docker --help'
bradsimpson@ ~:docker container ls 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8000->80/tcp   adoring_jennings
20c798aa3f32   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:8080->80/tcp   happy_morse
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                    NAMES
cd2f7af1b2d0   alpine                             "sh"                     3 minutes ago    Exited (0) 3 minutes ago                             test
f181e5f493a4   nginx                              "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8000->80/tcp     adoring_jennings
a4d1c8b12254   nginx                              "/docker-entrypoint.…"   6 minutes ago    Created                                              stupefied_chatelet
f0d4100c1419   alpine                             "sh"                     10 minutes ago   Exited (0) 9 minutes ago                             reverent_bose
20c798aa3f32   nginx                              "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes               0.0.0.0:8080->80/tcp     happy_morse
0c5c212e538b   nginx                              "/docker-entrypoint.…"   20 minutes ago   Exited (0) 17 minutes ago                            cool_container
a451f75be76a   hello-world                        "/hello"                 55 minutes ago   Exited (0) 55 minutes ago                            thirsty_heyrovsky
93b374550684   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                              stupefied_bose
d38e8c67a7b1   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               goofy_swirles
dd7ed9ebae5f   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               zealous_ellis
ff3cad67b0a6   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               thirsty_wilbur
f626f9ce95ec   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               peaceful_cray
d1f0d202fe1e   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               heuristic_taussig
c1f10ded956c   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               busy_ptolemy
38def1c4c065   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sad_keller
8f507596bb85   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sharp_mclean
7d2cbcc69117   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               ecstatic_raman
5e08488c5962   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               angry_driscoll
ac31950b4c99   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               elated_fermat
6b2c51319c02   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               eager_mirzakhani
576959c4cff4   postgres                           "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp   my_postgres2
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                     PORTS     NAMES
cd2f7af1b2d0   alpine    "sh"      3 minutes ago   Exited (0) 3 minutes ago             test
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8000->80/tcp   adoring_jennings
20c798aa3f32   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8080->80/tcp   happy_morse
bradsimpson@ ~:docker container stop happy_morse f181e5f493a4
happy_morse
f181e5f493a4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                    NAMES
cd2f7af1b2d0   alpine                             "sh"                     4 minutes ago    Exited (0) 4 minutes ago                             test
f181e5f493a4   nginx                              "/docker-entrypoint.…"   6 minutes ago    Exited (0) 36 seconds ago                            adoring_jennings
a4d1c8b12254   nginx                              "/docker-entrypoint.…"   7 minutes ago    Created                                              stupefied_chatelet
f0d4100c1419   alpine                             "sh"                     12 minutes ago   Exited (0) 11 minutes ago                            reverent_bose
20c798aa3f32   nginx                              "/docker-entrypoint.…"   16 minutes ago   Exited (0) 36 seconds ago                            happy_morse
0c5c212e538b   nginx                              "/docker-entrypoint.…"   21 minutes ago   Exited (0) 19 minutes ago                            cool_container
a451f75be76a   hello-world                        "/hello"                 56 minutes ago   Exited (0) 56 minutes ago                            thirsty_heyrovsky
93b374550684   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                              stupefied_bose
d38e8c67a7b1   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               goofy_swirles
dd7ed9ebae5f   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               zealous_ellis
ff3cad67b0a6   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               thirsty_wilbur
f626f9ce95ec   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               peaceful_cray
d1f0d202fe1e   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               heuristic_taussig
c1f10ded956c   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               busy_ptolemy
38def1c4c065   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sad_keller
8f507596bb85   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sharp_mclean
7d2cbcc69117   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               ecstatic_raman
5e08488c5962   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               angry_driscoll
ac31950b4c99   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               elated_fermat
6b2c51319c02   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               eager_mirzakhani
576959c4cff4   postgres                           "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp   my_postgres2
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container start adoring_jennings
adoring_jennings
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   7 minutes ago   Up 4 seconds   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                    NAMES
cd2f7af1b2d0   alpine                             "sh"                     6 minutes ago    Exited (0) 6 minutes ago                             test
f181e5f493a4   nginx                              "/docker-entrypoint.…"   8 minutes ago    Up 49 seconds               0.0.0.0:8000->80/tcp     adoring_jennings
a4d1c8b12254   nginx                              "/docker-entrypoint.…"   9 minutes ago    Created                                              stupefied_chatelet
f0d4100c1419   alpine                             "sh"                     14 minutes ago   Exited (0) 13 minutes ago                            reverent_bose
20c798aa3f32   nginx                              "/docker-entrypoint.…"   18 minutes ago   Exited (0) 2 minutes ago                             happy_morse
0c5c212e538b   nginx                              "/docker-entrypoint.…"   23 minutes ago   Exited (0) 20 minutes ago                            cool_container
a451f75be76a   hello-world                        "/hello"                 58 minutes ago   Exited (0) 58 minutes ago                            thirsty_heyrovsky
93b374550684   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                              stupefied_bose
d38e8c67a7b1   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               goofy_swirles
dd7ed9ebae5f   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               zealous_ellis
ff3cad67b0a6   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               thirsty_wilbur
f626f9ce95ec   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               peaceful_cray
d1f0d202fe1e   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               heuristic_taussig
c1f10ded956c   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               busy_ptolemy
38def1c4c065   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sad_keller
8f507596bb85   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sharp_mclean
7d2cbcc69117   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               ecstatic_raman
5e08488c5962   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               angry_driscoll
ac31950b4c99   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               elated_fermat
6b2c51319c02   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               eager_mirzakhani
576959c4cff4   postgres                           "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp   my_postgres2
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container rm 93b374550684
93b374550684
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                    NAMES
cd2f7af1b2d0   alpine                             "sh"                     6 minutes ago    Exited (0) 6 minutes ago                             test
f181e5f493a4   nginx                              "/docker-entrypoint.…"   8 minutes ago    Up About a minute           0.0.0.0:8000->80/tcp     adoring_jennings
a4d1c8b12254   nginx                              "/docker-entrypoint.…"   9 minutes ago    Created                                              stupefied_chatelet
f0d4100c1419   alpine                             "sh"                     14 minutes ago   Exited (0) 13 minutes ago                            reverent_bose
20c798aa3f32   nginx                              "/docker-entrypoint.…"   18 minutes ago   Exited (0) 2 minutes ago                             happy_morse
0c5c212e538b   nginx                              "/docker-entrypoint.…"   23 minutes ago   Exited (0) 21 minutes ago                            cool_container
a451f75be76a   hello-world                        "/hello"                 58 minutes ago   Exited (0) 58 minutes ago                            thirsty_heyrovsky
d38e8c67a7b1   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               goofy_swirles
dd7ed9ebae5f   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               zealous_ellis
ff3cad67b0a6   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               thirsty_wilbur
f626f9ce95ec   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               peaceful_cray
d1f0d202fe1e   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               heuristic_taussig
c1f10ded956c   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               busy_ptolemy
38def1c4c065   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sad_keller
8f507596bb85   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               sharp_mclean
7d2cbcc69117   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               ecstatic_raman
5e08488c5962   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               angry_driscoll
ac31950b4c99   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               elated_fermat
6b2c51319c02   bradsimpson213/12345_react         "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               eager_mirzakhani
576959c4cff4   postgres                           "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp   my_postgres2
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
cd2f7af1b2d0463f84b57e8aec39a744b7e6b98693362dc6aa238fdf1e4aa9b3
a4d1c8b12254ba4011bb9c2736e7d9c36b08d92a80ee901fcd2afed01de0c90a
f0d4100c1419e93b7beced9aded70bb2536c736c80e855254aab46b62f7ec85e
20c798aa3f32fb4f866c631f673647a7f8e7e97aab0ca1dbfe7d14b089f6ddff
0c5c212e538b7d01afe43648b3afcba6f23f886666e6672db9851865f598b9cc
a451f75be76a6dc7a43fb2d8d0802d678ccb0a2f7079b25f3670520e32503a9b
d38e8c67a7b11adf77b894406f321d1490e69941f41642b53bf094971f015c55
dd7ed9ebae5f029771b04e2b1d8abfe10f064db367bd69d454d24efdc828b94f
ff3cad67b0a69aa6e9278f95ff799807927112ef577febfcb4e85b0f1254976f
f626f9ce95ec0d4206c291e38ca8f11777563d4d4e5cf6e08e6bb4b9be4af781
d1f0d202fe1edcc60d2cf50e44bf7e38efde1404af16616db17bc251e4c2c760
c1f10ded956ca569235ee0354a4e445d248df1f153a33216f230cb93198e9139
38def1c4c0653c4f2c798f59e66ffb4e50adf5dbd12d931b08130f412e079968
8f507596bb85f8d3eed5717bfb6c9cfdc679045cfbe8b098ac41ad2bb20a4aeb
7d2cbcc6911745a9193c3bdd3d400ca87d8ef57a553279b251a551f09cd9e206
5e08488c5962b7a6e0bb07c45c94007bb1d99058b1aaf4647870f027e4deb7fb
ac31950b4c997aca40af2e0c7a0be29f36f61b5a663439ab44cb8db126345b46
6b2c51319c02b970ea03a747ef498c4c76fafc9b6cf353f7299c4191a46470c8
576959c4cff41aec0203942bb97567531d3c068cb7064828109d802d625c7a2b

Total reclaimed space: 298.3MB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker conatiner exec -it adoring_jennings sh
unknown shorthand flag: 'i' in -it
See 'docker --help'.

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default
                           "/Users/bradsimpson/.docker")
  -c, --context string     Name of the context to use to connect to the daemon
                           (overrides DOCKER_HOST env var and default context set
                           with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level
                           ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
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

bradsimpson@ ~:docker container exec -it adoring_jennings sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 6 minutes   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker container inspect adoring_jennings
[
    {
        "Id": "f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588",
        "Created": "2023-04-04T15:52:29.209127311Z",
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
            "Pid": 2972,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-04-04T16:00:04.287149241Z",
            "FinishedAt": "2023-04-04T15:58:42.251668786Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/hostname",
        "HostsPath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/hosts",
        "LogPath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588-json.log",
        "Name": "/adoring_jennings",
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
                "LowerDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09/merged",
                "UpperDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09/diff",
                "WorkDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f181e5f493a4",
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
            "SandboxID": "c4f27fe49e99888bdf32a57c91df8f2e9a9414c3ecd518a936f3988b7cea8cfb",
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
            "SandboxKey": "/var/run/docker/netns/c4f27fe49e99",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "25076dccce5309918271300bd15441b28054dece96fdd9d30edb7b9c53acb1a2",
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
                    "NetworkID": "d2273989e8433f932ff8c4189eec88367913b548d0722b809f7d0db94c5a6567",
                    "EndpointID": "25076dccce5309918271300bd15441b28054dece96fdd9d30edb7b9c53acb1a2",
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
bradsimpson@ ~:


# NETWORKING


Last login: Tue Apr  4 09:31:54 on ttys001

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker network ls
NETWORK ID     NAME                     DRIVER    SCOPE
d2273989e843   bridge                   bridge    local
2af1b34de9a0   even_more_taco_tuesday   bridge    local
7318efe60d0f   host                     host      local
1a584f63c88c   my_network               bridge    local
475754f27665   none                     null      local
6000c9f47f19   taco_tuesday             bridge    local
bradsimpson@ ~:docker network prune
WARNING! This will remove all custom networks not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Networks:
taco_tuesday
my_network
even_more_taco_tuesday

bradsimpson@ ~:docker network ls
^[[3~NETWORK ID     NAME      DRIVER    SCOPE
d2273989e843   bridge    bridge    local
7318efe60d0f   host      host      local
475754f27665   none      null      local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   37 minutes ago   Up 29 minutes   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker container inspect adoring_jennings
[
    {
        "Id": "f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588",
        "Created": "2023-04-04T15:52:29.209127311Z",
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
            "Pid": 2972,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-04-04T16:00:04.287149241Z",
            "FinishedAt": "2023-04-04T15:58:42.251668786Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/hostname",
        "HostsPath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/hosts",
        "LogPath": "/var/lib/docker/containers/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588/f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588-json.log",
        "Name": "/adoring_jennings",
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
                "LowerDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09/merged",
                "UpperDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09/diff",
                "WorkDir": "/var/lib/docker/overlay2/a6c76ea3507e0e2209224086bb301f99ca3154bf4be3724b80fd94be0ea6af09/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f181e5f493a4",
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
            "SandboxID": "c4f27fe49e99888bdf32a57c91df8f2e9a9414c3ecd518a936f3988b7cea8cfb",
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
            "SandboxKey": "/var/run/docker/netns/c4f27fe49e99",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "25076dccce5309918271300bd15441b28054dece96fdd9d30edb7b9c53acb1a2",
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
                    "NetworkID": "d2273989e8433f932ff8c4189eec88367913b548d0722b809f7d0db94c5a6567",
                    "EndpointID": "25076dccce5309918271300bd15441b28054dece96fdd9d30edb7b9c53acb1a2",
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
NETWORK ID     NAME      DRIVER    SCOPE
d2273989e843   bridge    bridge    local
7318efe60d0f   host      host      local
475754f27665   none      null      local
bradsimpson@ ~:docker network create --driver bridge my_network
cb48cd425fede48de923b505fbf13d9b16957b155e1a55cdcc41e68b1c51bf50
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
d2273989e843   bridge       bridge    local
7318efe60d0f   host         host      local
cb48cd425fed   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker network rm cb48cd425fed
cb48cd425fed
bradsimpson@ ~:docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
d2273989e843   bridge    bridge    local
7318efe60d0f   host      host      local
475754f27665   none      null      local
bradsimpson@ ~:docker network create --driver bridge my_network
e462f118fac6825ed248846f6868427c3b10a9369216d36a2e8b6f67ba1bcb5f
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
d2273989e843   bridge       bridge    local
7318efe60d0f   host         host      local
e462f118fac6   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
d2273989e843   bridge       bridge    local
7318efe60d0f   host         host      local
e462f118fac6   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker container run -d --name c1 --network my_netwwork nginx:alpine
14e06c0b72d75c798062924549f31c37e3b5772a251f77b0ca51f579efc0939b
docker: Error response from daemon: network my_netwwork not found.
bradsimpson@ ~:docker container run -d --name c1 --network my_network nginx:alpine
docker: Error response from daemon: Conflict. The container name "/c1" is already in use by container "14e06c0b72d75c798062924549f31c37e3b5772a251f77b0ca51f579efc0939b". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f181e5f493a4   nginx     "/docker-entrypoint.…"   43 minutes ago   Up 36 minutes   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
14e06c0b72d7   nginx:alpine   "/docker-entrypoint.…"   36 seconds ago   Created                                c1
f181e5f493a4   nginx          "/docker-entrypoint.…"   43 minutes ago   Up 36 minutes   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker container rm c1
c1
bradsimpson@ ~:docker container run -d --name c1 --network my_network nginx:alpinec88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 4 seconds    80/tcp                 c1
f181e5f493a4   nginx          "/docker-entrypoint.…"   44 minutes ago   Up 36 minutes   0.0.0.0:8000->80/tcp   adoring_jennings
bradsimpson@ ~:docker container stop adoring_jennings
adoring_jennings
bradsimpson@ ~:docker container run -d --name c2 --network my_network nginx:alpine
3e8a1e9aebd4a181df451e1adb39a8c407383a766ef63049e2762a5b6b8153a7
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
3e8a1e9aebd4   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 3 seconds    80/tcp    c2
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   32 seconds ago   Up 31 seconds   80/tcp    c1
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d --name c3 nginx:alpine
62757323dcf77adc3ba4bbd8b9179e130b439b5e9007625a41157f7725906cfc
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine
abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
abbec9031c21   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago        Up 3 seconds        80/tcp    c4
62757323dcf7   nginx:alpine   "/docker-entrypoint.…"   12 seconds ago       Up 10 seconds       80/tcp    c3
3e8a1e9aebd4   nginx:alpine   "/docker-entrypoint.…"   46 seconds ago       Up 44 seconds       80/tcp    c2
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b",
        "Created": "2023-04-04T16:36:48.152421886Z",
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
            "Pid": 3245,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-04-04T16:36:49.05374186Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b/hostname",
        "HostsPath": "/var/lib/docker/containers/c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b/hosts",
        "LogPath": "/var/lib/docker/containers/c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b/c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/4ae97c5793b2adc16fdb09e47cd940bab87b076b02ff6fed7e988786227822fa-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/4ae97c5793b2adc16fdb09e47cd940bab87b076b02ff6fed7e988786227822fa/merged",
                "UpperDir": "/var/lib/docker/overlay2/4ae97c5793b2adc16fdb09e47cd940bab87b076b02ff6fed7e988786227822fa/diff",
                "WorkDir": "/var/lib/docker/overlay2/4ae97c5793b2adc16fdb09e47cd940bab87b076b02ff6fed7e988786227822fa/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "c88e1e943c74",
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
            "SandboxID": "1fa8bbc9f7d751ce310fff3782b47415fe16ce35587fb41c49ebcd9e9844d589",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/1fa8bbc9f7d7",
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
                        "c88e1e943c74"
                    ],
                    "NetworkID": "e462f118fac6825ed248846f6868427c3b10a9369216d36a2e8b6f67ba1bcb5f",
                    "EndpointID": "662982a5ba44d236337d1486885b25b6901c09e8ecbdf1ba419c671b07628261",
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
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e",
        "Created": "2023-04-04T16:37:56.465409359Z",
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
            "Pid": 3633,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-04-04T16:37:57.227685516Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e/hostname",
        "HostsPath": "/var/lib/docker/containers/abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e/hosts",
        "LogPath": "/var/lib/docker/containers/abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e/abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/ff0d0ea64316b4615eadd7d3cfd433d41e17a2ed7b70b8aa43861fb9c3bba464-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/ff0d0ea64316b4615eadd7d3cfd433d41e17a2ed7b70b8aa43861fb9c3bba464/merged",
                "UpperDir": "/var/lib/docker/overlay2/ff0d0ea64316b4615eadd7d3cfd433d41e17a2ed7b70b8aa43861fb9c3bba464/diff",
                "WorkDir": "/var/lib/docker/overlay2/ff0d0ea64316b4615eadd7d3cfd433d41e17a2ed7b70b8aa43861fb9c3bba464/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "abbec9031c21",
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
            "SandboxID": "bb0adfc391549b0d83f83414a09812cab9c7d40589dfcc4e694a2315dff51eee",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/bb0adfc39154",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "b1ec9ef7d958448db64fe266a05f2aaf0c357c725bb2855b31e2faacac57a9a9",
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
                    "NetworkID": "d2273989e8433f932ff8c4189eec88367913b548d0722b809f7d0db94c5a6567",
                    "EndpointID": "b1ec9ef7d958448db64fe266a05f2aaf0c357c725bb2855b31e2faacac57a9a9",
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
abbec9031c21   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
62757323dcf7   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
3e8a1e9aebd4   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 3 c2
PING c2 (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: seq=0 ttl=64 time=2.421 ms
64 bytes from 172.19.0.3: seq=1 ttl=64 time=0.101 ms
64 bytes from 172.19.0.3: seq=2 ttl=64 time=0.144 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.101/0.888/2.421 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 c4
ping: bad address 'c4'
/ # exit
bradsimpson@ ~:docker container exec -it c3 ash
/ # ping -c 4 c1
ping: bad address 'c1'
/ # ping -c 4 c2
ping: bad address 'c2'
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.171 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.112 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.269 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.096 ms

--- 172.17.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.096/0.162/0.269 ms
/ # exit
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
d2273989e843   bridge       bridge    local
7318efe60d0f   host         host      local
e462f118fac6   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     more_tacos_please
local     new_test_volume
local     taco_tuesday
bradsimpson@ ~:


# BIND MOUNTS & VOLUMES


Last login: Tue Apr  4 12:12:38 on ttys003

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		oct-starter
Desktop		Library		Pictures	app		opt
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/12345_react         latest    c63116090e8b   3 weeks ago     441MB
postgres                           latest    3b6645d2c145   4 weeks ago     379MB
nginx                              alpine    2bc7edbc3cf2   7 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   7 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   2 months ago    568MB
bradsimps213/react_project         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   2 months ago    568MB
my_project                         latest    ae74e957ba0d   2 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   5 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   6 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   10 months ago   142MB
alpine                             latest    e66264b98777   10 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   18 months ago   13.3kB
bradsimpson@ app:docker image inspect nginx:alpine
[
    {
        "Id": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "RepoTags": [
            "nginx:alpine"
        ],
        "RepoDigests": [
            "nginx@sha256:207332a7d1d17b884b5a0e94bcf7c0f67f1a518b9bf8da6c2ea72c83eec889b8"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-02-11T10:04:34.596569339Z",
        "Container": "63b5216a48011264829cc343f16966f363497e4b835cb1e9fd8485ecace55493",
        "ContainerConfig": {
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
                "NGINX_VERSION=1.23.3",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.9"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "set -x     && apkArch=\"$(cat /etc/apk/arch)\"     && nginxPackages=\"         nginx=${NGINX_VERSION}-r${PKG_RELEASE}         nginx-module-xslt=${NGINX_VERSION}-r${PKG_RELEASE}         nginx-module-geoip=${NGINX_VERSION}-r${PKG_RELEASE}         nginx-module-image-filter=${NGINX_VERSION}-r${PKG_RELEASE}         nginx-module-njs=${NGINX_VERSION}.${NJS_VERSION}-r${PKG_RELEASE}     \"     && apk add --no-cache --virtual .checksum-deps         openssl     && case \"$apkArch\" in         x86_64|aarch64)             set -x             && KEY_SHA512=\"e09fa32f0a0eab2b879ccbbc4d0e4fb9751486eedda75e35fac65802cc9faa266425edf83e261137a2f4d16281ce2c1a5f4502930fe75154723da014214f0655\"             && wget -O /tmp/nginx_signing.rsa.pub https://nginx.org/keys/nginx_signing.rsa.pub             && if echo \"$KEY_SHA512 */tmp/nginx_signing.rsa.pub\" | sha512sum -c -; then                 echo \"key verification succeeded!\";                 mv /tmp/nginx_signing.rsa.pub /etc/apk/keys/;             else                 echo \"key verification failed!\";                 exit 1;             fi             && apk add -X \"https://nginx.org/packages/mainline/alpine/v$(egrep -o '^[0-9]+\\.[0-9]+' /etc/alpine-release)/main\" --no-cache $nginxPackages             ;;         *)             set -x             && tempDir=\"$(mktemp -d)\"             && chown nobody:nobody $tempDir             && apk add --no-cache --virtual .build-deps                 gcc                 libc-dev                 make                 openssl-dev                 pcre2-dev                 zlib-dev                 linux-headers                 libxslt-dev                 gd-dev                 geoip-dev                 libedit-dev                 bash                 alpine-sdk                 findutils             && su nobody -s /bin/sh -c \"                 export HOME=${tempDir}                 && cd ${tempDir}                 && curl -f -O https://hg.nginx.org/pkg-oss/archive/${NGINX_VERSION}-${PKG_RELEASE}.tar.gz                 && PKGOSSCHECKSUM=\\\"52a80f6c3b3914462f8a0b2fbadea950bcd79c1bd528386aff4c28d5a80c6920d783575a061a47b60fea800eef66bf5a0178a137ea51c37277fe9c2779715990 *${NGINX_VERSION}-${PKG_RELEASE}.tar.gz\\\"                 && if [ \\\"\\$(openssl sha512 -r ${NGINX_VERSION}-${PKG_RELEASE}.tar.gz)\\\" = \\\"\\$PKGOSSCHECKSUM\\\" ]; then                     echo \\\"pkg-oss tarball checksum verification succeeded!\\\";                 else                     echo \\\"pkg-oss tarball checksum verification failed!\\\";                     exit 1;                 fi                 && tar xzvf ${NGINX_VERSION}-${PKG_RELEASE}.tar.gz                 && cd pkg-oss-${NGINX_VERSION}-${PKG_RELEASE}                 && cd alpine                 && make module-geoip module-image-filter module-njs module-xslt                 && apk index -o ${tempDir}/packages/alpine/${apkArch}/APKINDEX.tar.gz ${tempDir}/packages/alpine/${apkArch}/*.apk                 && abuild-sign -k ${tempDir}/.abuild/abuild-key.rsa ${tempDir}/packages/alpine/${apkArch}/APKINDEX.tar.gz                 \"             && cp ${tempDir}/.abuild/abuild-key.rsa.pub /etc/apk/keys/             && apk del .build-deps             && apk add -X ${tempDir}/packages/alpine/ --no-cache $nginxPackages             ;;     esac     && apk del .checksum-deps     && if [ -n \"$tempDir\" ]; then rm -rf \"$tempDir\"; fi     && if [ -n \"/etc/apk/keys/abuild-key.rsa.pub\" ]; then rm -f /etc/apk/keys/abuild-key.rsa.pub; fi     && if [ -n \"/etc/apk/keys/nginx_signing.rsa.pub\" ]; then rm -f /etc/apk/keys/nginx_signing.rsa.pub; fi     && apk add --no-cache curl ca-certificates"
            ],
            "Image": "sha256:757a79f0b45ba3262ba978ba87c8aa3d201a1b877420394a913ad311259c5fe3",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
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
                "NGINX_VERSION=1.23.3",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.9"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "sha256:757a79f0b45ba3262ba978ba87c8aa3d201a1b877420394a913ad311259c5fe3",
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
        "Size": 40716702,
        "VirtualSize": 40716702,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/merged",
                "UpperDir": "/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff",
                "WorkDir": "/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:7cd52847ad775a5ddc4b58326cf884beee34544296402c6292ed76474c686d39",
                "sha256:d8a5a02a8c2d1e625a89a4956f6773baad42859509fb06b6c2e53b0ee3576dfd",
                "sha256:5e59460a18a391d945829d29a9b295b1c2fdeb0d09d1764012736698cacbdcc2",
                "sha256:152a948bab3b2e19f92a88342da9b5271b1e2879272ecdad2200eb59159ea624",
                "sha256:c4d67a5827ca405b493275f4e9df7d5e97f78ecb4bf48d77299e1175cb1dbcc4",
                "sha256:f1bee861c2ba8de7590cbc91799d2bb8a3579bcf1d1519c2445bd2d385338787",
                "sha256:042cd3f87f43b1dea43047cd1d4394440122cb2a14ffed326fad8b34d25660fd"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:--mount type=bind,source=absolute/path/to/source,target=path/in/container
-bash: --mount: command not found
bradsimpson@ app:--mount type=volume,source=volume_name,target=path/in/container
-bash: --mount: command not found
bradsimpson@ app:\ls
index.html
bradsimpson@ app:cd..
-bash: cd..: command not found
bradsimpson@ app:cd ..
bradsimpson@ ~:\ld
ld: warning: platform not specified
ld: warning: -arch not specified
ld: warning: No platform min-version specified on command line
ld: no object files specified
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		oct-starter
Desktop		Library		Pictures	app		opt
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html 
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
abbec9031c21   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c4
62757323dcf7   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c3
3e8a1e9aebd4   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Up 45 minutes   80/tcp    c2
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Up 45 minutes   80/tcp    c1
bradsimpson@ ~:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS     NAMES
abbec9031c21   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Exited (0) 6 seconds ago              c4
62757323dcf7   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Exited (0) 5 seconds ago              c3
3e8a1e9aebd4   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Exited (0) 6 seconds ago              c2
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   46 minutes ago   Exited (0) 5 seconds ago              c1
f181e5f493a4   nginx          "/docker-entrypoint.…"   2 hours ago      Exited (0) 45 minutes ago             adoring_jennings
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx:alpine
7099c8205f04bb8b9135c2adf20f9678ac4883a3a64fa32bffd122fb13f00849
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
7099c8205f04   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp   zealous_wescoff
bradsimpson@ ~:docker container exec -it zealous_wescoff ash
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
X11              fontconfig       nginx
apk              licenses         udhcpc
ca-certificates  man              xml
/usr/share # cd nginx/
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
50x.html    index.html
/usr/share/nginx/html # nano index.html
ash: nano: not found
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 43 MiB in 63 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
7099c8205f04   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp   zealous_wescoff
bradsimpson@ ~:docker container stop zealous_wescoff
zealous_wescoff
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html nginx:alpine
e2b6c144dd889823a34b8109167e560b7ffebf78410fdc9b1f637e5a577e179e
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
e2b6c144dd88   nginx:alpine   "/docker-entrypoint.…"   32 seconds ago   Up 31 seconds   0.0.0.0:8080->80/tcp   wonderful_faraday
bradsimpson@ ~:docker container exex -it wonderful_faraday
^[[D^[[Dunknown shorthand flag: 'i' in -it
See 'docker container --help'.

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

bradsimpson@ ~:docker container exex -it wonderful_faraday ash
unknown shorthand flag: 'i' in -it
See 'docker container --help'.

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

bradsimpson@ ~:docker container exec -it wonderful_faraday ash
/ # \ls
bin                   media                 srv
dev                   mnt                   sys
docker-entrypoint.d   opt                   tmp
docker-entrypoint.sh  proc                  usr
etc                   root                  var
home                  run
lib                   sbin
/ # cd usr/share/nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html/'
> 
> 
> 
> 
> '
ash: cd: can't cd to html/




: No such file or directory
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 43 MiB in 63 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ ~:cd app/
bradsimpson@ app:nano index.html 
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
e2b6c144dd88   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->80/tcp   wonderful_faraday
bradsimpson@ app:docker container stop wonderful_faraday
wonderful_faraday
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     more_tacos_please
local     new_test_volume
local     taco_tuesday
bradsimpson@ app:\clear

bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     more_tacos_please
local     new_test_volume
local     taco_tuesday
bradsimpson@ app:docker volume rm new_test_volume
new_test_volume
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     more_tacos_please
local     taco_tuesday
bradsimpson@ app:docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
more_tacos_please
taco_tuesday

Total reclaimed space: 95.6MB
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
bradsimpson@ app:docker volume create tuesday_taco
tuesday_taco
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     tuesday_taco
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/12345_react         latest    c63116090e8b   3 weeks ago     441MB
postgres                           latest    3b6645d2c145   4 weeks ago     379MB
nginx                              alpine    2bc7edbc3cf2   7 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   7 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   2 months ago    568MB
my_project                         latest    ae74e957ba0d   2 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   2 months ago    568MB
bradsimps213/react_project         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   5 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   6 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   10 months ago   142MB
alpine                             latest    e66264b98777   10 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   18 months ago   13.3kB
bradsimpson@ app:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:50a96a21f2992518c2cb4601467cf27c7ac852542d8913c1872fe45cd6449947
Deleted: sha256:3b6645d2c145df0062b13b5f4db33b428f7249d7139949e3c4a1fbc81b4d6de9
Deleted: sha256:0bd01830d3df996e6c15bfe59653338c52d508a04edd8698fe12924a557bd71a
Deleted: sha256:ae641a98aa7db8c84da13077d08f27de3684afff159dd628abfd02b0c039ff18
Deleted: sha256:7d25c72ebf25cac7a6c1810a6fe68bf63839413d4a6bc73883d4bd3f6cc65018
Deleted: sha256:32554de27c1a860feb450eaa7a5a90111a11d67792437c0ba6633781673cb915
Deleted: sha256:492f866ba89b42f8e9f9ff19b5654b4b3012c180390ca7b5cf2fb54f5379e476
Deleted: sha256:2b5e60dc357b214ee416152371bdef52423310adeeb208bfcfb1de1508e42ff6
Deleted: sha256:baced9268bcd3e0ee504dd8970cc4292d7937946a85e559b178c531bd6d79e27
Deleted: sha256:987360baba271ce89d9702fee3bbadd1a70b1e8b8da89f4532795a96460f87d8
Deleted: sha256:bd0bdce76b9c11e8497eb2bb064832bcd1705ac3515175593383745afcf05d02
Deleted: sha256:204c6a4731f5f940a7227d615396fc829e34b6550427084f7e27e3c83be8c9cf
Deleted: sha256:d359a0bc3ff5d8f0b32d73430685e90f1ca5285d3b85f80dc63b65e6011dae72
Deleted: sha256:a8a66fafc356a96cf4b4480f5132f2b95102c20dd8eb8e191930e7cf02be9ce9
Deleted: sha256:650abce4b096b06ac8bec2046d821d66d801af34f1f1d4c5e272ad030c7873db
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/12345_react         latest    c63116090e8b   3 weeks ago     441MB
nginx                              alpine    2bc7edbc3cf2   7 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   7 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   2 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   2 months ago    568MB
bradsimps213/react_project         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   2 months ago    568MB
my_project                         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   5 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   6 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   10 months ago   142MB
alpine                             latest    e66264b98777   10 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   18 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
f1f26f570256: Pull complete 
1c04f8741265: Pull complete 
dffc353b86eb: Pull complete 
18c4a9e6c414: Pull complete 
81f47e7b3852: Pull complete 
5e26c947960d: Pull complete 
a2c3dc85e8c3: Pull complete 
17df73636f01: Pull complete 
713535cdf17c: Pull complete 
52278a39eea2: Pull complete 
4ded87da67f6: Pull complete 
05fae4678312: Pull complete 
56b4f4aeea2d: Pull complete 
Digest: sha256:5a90725b3751c2c7ac311c9384dfc1a8f6e41823e341fb1dceed96a11677303a
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
postgres                           latest    80c558ffdc31   7 days ago      379MB
bradsimpson213/12345_react         latest    c63116090e8b   3 weeks ago     441MB
nginx                              alpine    2bc7edbc3cf2   7 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   7 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   2 months ago    568MB
bradsimps213/react_project         latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   2 months ago    568MB
my_project                         latest    ae74e957ba0d   2 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   2 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   5 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   6 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   10 months ago   142MB
alpine                             latest    e66264b98777   10 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   18 months ago   13.3kB
bradsimpson@ app:docker image inspect postgres
[
    {
        "Id": "sha256:80c558ffdc314a930fe201d69d9cd58a0fc0f6a833e3f5014268a02d36438c65",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:5a90725b3751c2c7ac311c9384dfc1a8f6e41823e341fb1dceed96a11677303a"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-03-27T22:29:58.584999554Z",
        "Container": "37363b6707e54fe57a4fecfe8e878e1e3a252bf7da7c147d8aa0eb84e46b9760",
        "ContainerConfig": {
            "Hostname": "37363b6707e5",
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
                "PG_VERSION=15.2-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:951e35d0a3d3ad81d1198dafe287472e755f7abc251af46780e19bb08c7b5e9c",
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
                "PG_VERSION=15.2-1.pgdg110+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:951e35d0a3d3ad81d1198dafe287472e755f7abc251af46780e19bb08c7b5e9c",
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
        "Size": 378712630,
        "VirtualSize": 378712630,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0bd7021617455ad3ee1fa565a491a1ad25e4566b96b7fe7ff51bb3ad355e7241/diff:/var/lib/docker/overlay2/36c2d6e5bbb03e82c94e93a2d95858aac70173d9f052bfb4ca21c427c3a074d9/diff:/var/lib/docker/overlay2/9391f1570cfc821f4d3edc27fde71d2201cb505a671bee8eb06c283cbb1b7b82/diff:/var/lib/docker/overlay2/d04f6d602e0c4c28150a503f87aa9839fc2ba6087a9a8ea0cc72a0871602da93/diff:/var/lib/docker/overlay2/8938a6fcaf1818e86e51630e404d27ac81dd7a50a3315456eff3be82cb5e92e1/diff:/var/lib/docker/overlay2/42b4c313f62e559c7b8ea6664a2431a2eccd037216bdcda84c7dc92cb36a41ab/diff:/var/lib/docker/overlay2/c2be8fa7c80722013af0e978a1b1a22010097c7f67ec0fa8808e082cd48a5906/diff:/var/lib/docker/overlay2/9f96df5e418c9495e7050cf4b3bfa9c79dd5da0758b0ca49abdcc1076d8b659e/diff:/var/lib/docker/overlay2/7df6f4f6b50bd6f0de60c82d4ba257cd6c76ff31518c79fdd15f342a328455c7/diff:/var/lib/docker/overlay2/00e6c0d351de7cde343839a33dbfb0f54b96eccb8e97873de2b2dc71e5ba4163/diff:/var/lib/docker/overlay2/91b226e7ca6a6872485bb26648ae564f46a60094b35f222caa4c0e32955e5fb3/diff:/var/lib/docker/overlay2/50a90222090cb473ce466a37c1541e5c99f21e43d3aad69e85935d1c4aeadab5/diff",
                "MergedDir": "/var/lib/docker/overlay2/db32b948717cd88562ca5286dbe232d56409340fa703fd31ddac5d74864e27a1/merged",
                "UpperDir": "/var/lib/docker/overlay2/db32b948717cd88562ca5286dbe232d56409340fa703fd31ddac5d74864e27a1/diff",
                "WorkDir": "/var/lib/docker/overlay2/db32b948717cd88562ca5286dbe232d56409340fa703fd31ddac5d74864e27a1/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:3af14c9a24c941c626553628cf1942dcd94d40729777f2fcfbcd3b8a3dfccdd6",
                "sha256:a9fa3183c5956f8d8d6c21c29162c340c3351a823a086a0a730c63d06bdb8717",
                "sha256:3a54f275df410ffd27ea5113a3207860a85c886769c6dd44f54a79c0e8db5b7b",
                "sha256:0188104e12976c1d19e4937e273a93d5909e81f751861440f2249fcec69f8651",
                "sha256:7bde5bee9d2d48ec0f0f2d78f9b4379ed9ca0f075deff67a127f4af7477640ce",
                "sha256:ef59638c463eb0beabf5c84d58bdc08ed3ecc9f20858c1692163404953cad43e",
                "sha256:96a5e612e773551c68afff7070700162981ee61854019ee595231bce957f1b45",
                "sha256:5edf3610ca635e2df28e6fd8d927a54a58e6eff11bb3fe95fe41e2d4fef0f0a4",
                "sha256:c97e083d6061ebe694d28322d08ae6d9ddb8027de9de9e0d439f56a28dbf245a",
                "sha256:c4a561c533779cfc8e3ebe80e617824e2f8d54258142ea8842075f1d06f7e619",
                "sha256:9168d2f63c22a7ec8ba96ca584107549f8f361fc149230badadc0f120ae3a172",
                "sha256:2c8793b227a3b1190bae5304fa60ec15210cd453fc7af3d51dc725cc09af23cd",
                "sha256:101df8fda4336738e863501d4ea68da1a6f5f379daaa332ee54d339debf73078"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 --mount type=volume,source=tuesday_taco,target=/var/lib/postgresql/data -e POSTGRES_PASSWORD=password postgres
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

waiting for server to start....2023-04-04 17:43:52.163 UTC [48] LOG:  starting PostgreSQL 15.2 (Debian 15.2-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
2023-04-04 17:43:52.167 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2023-04-04 17:43:52.176 UTC [51] LOG:  database system was shut down at 2023-04-04 17:43:51 UTC
2023-04-04 17:43:52.183 UTC [48] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

2023-04-04 17:43:52.358 UTC [48] LOG:  received fast shutdown request
waiting for server to shut down....2023-04-04 17:43:52.359 UTC [48] LOG:  aborting any active transactions
2023-04-04 17:43:52.362 UTC [48] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
2023-04-04 17:43:52.364 UTC [49] LOG:  shutting down
2023-04-04 17:43:52.366 UTC [49] LOG:  checkpoint starting: shutdown immediate
2023-04-04 17:43:52.378 UTC [49] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.004 s, sync=0.001 s, total=0.014 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB
2023-04-04 17:43:52.385 UTC [48] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2023-04-04 17:43:52.490 UTC [1] LOG:  starting PostgreSQL 15.2 (Debian 15.2-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
2023-04-04 17:43:52.491 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2023-04-04 17:43:52.491 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2023-04-04 17:43:52.498 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2023-04-04 17:43:52.505 UTC [62] LOG:  database system was shut down at 2023-04-04 17:43:52 UTC
2023-04-04 17:43:52.523 UTC [1] LOG:  database system is ready to accept connections
exit
^C2023-04-04 17:44:08.985 UTC [1] LOG:  received fast shutdown request
2023-04-04 17:44:08.987 UTC [1] LOG:  aborting any active transactions
2023-04-04 17:44:08.990 UTC [1] LOG:  background worker "logical replication launcher" (PID 65) exited with exit code 1
2023-04-04 17:44:08.998 UTC [60] LOG:  shutting down
2023-04-04 17:44:09.007 UTC [60] LOG:  checkpoint starting: shutdown immediate
2023-04-04 17:44:09.040 UTC [60] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.011 s, sync=0.007 s, total=0.043 s; sync files=2, longest=0.005 s, average=0.004 s; distance=0 kB, estimate=0 kB
2023-04-04 17:44:09.051 UTC [1] LOG:  database system is shut down
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 --mount type=volume,source=tuesday_taco,target=/var/lib/postgresql/data -d -e POSTGRES_PASSWORD=password postgres
docker: Error response from daemon: Conflict. The container name "/postgres1" is already in use by container "7950e3185674541dac87346045593b2a7040306f3bc62f709f74a3fab88e9c4d". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS     NAMES
7950e3185674   postgres       "docker-entrypoint.s…"   52 seconds ago      Exited (0) 31 seconds ago                postgres1
e2b6c144dd88   nginx:alpine   "/docker-entrypoint.…"   15 minutes ago      Exited (137) 10 minutes ago              wonderful_faraday
7099c8205f04   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago      Exited (0) 17 minutes ago                zealous_wescoff
abbec9031c21   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 21 minutes ago                c4
62757323dcf7   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 21 minutes ago                c3
3e8a1e9aebd4   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 21 minutes ago                c2
c88e1e943c74   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 21 minutes ago                c1
f181e5f493a4   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago             adoring_jennings
bradsimpson@ app:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
7950e3185674541dac87346045593b2a7040306f3bc62f709f74a3fab88e9c4d
e2b6c144dd889823a34b8109167e560b7ffebf78410fdc9b1f637e5a577e179e
7099c8205f04bb8b9135c2adf20f9678ac4883a3a64fa32bffd122fb13f00849
abbec9031c214069e4754e9d85909629001640b4a0d479487b0e639696fa6c2e
62757323dcf77adc3ba4bbd8b9179e130b439b5e9007625a41157f7725906cfc
3e8a1e9aebd4a181df451e1adb39a8c407383a766ef63049e2762a5b6b8153a7
c88e1e943c7405079875c9128da9cf5ad63bd02ca6287f475808d584821bdb4b
f181e5f493a456e90403b05d9dc3327bf8ec1608f6551db7df8a4410a568f588

Total reclaimed space: 6.088MB
bradsimpson@ app:\clear







bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 --mount type=volume,source=tuesday_taco,target=/var/lib/postgresql/data -d -e POSTGRES_PASSWORD=password postgres
3755178615cff9f4f81d14ad89e70aa8c5499ea4b069982a476be20a57bdeec7
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
3755178615cf   postgres   "docker-entrypoint.s…"   5 seconds ago   Up 4 seconds   0.0.0.0:5431->5432/tcp   postgres1
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.2 (Debian 15.2-1.pgdg110+1))
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

postgres=# CREATE DATABASE taco_tuesday with OWNER postgres;
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
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS                    NAMES
3755178615cf   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5431->5432/tcp   postgres1
bradsimpson@ app:docker container stop 3755178615cf
3755178615cf
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS                     PORTS     NAMES
3755178615cf   postgres   "docker-entrypoint.s…"   2 minutes ago   Exited (0) 9 seconds ago             postgres1
bradsimpson@ app:docker container rm postgres1
postgres1
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container run -p 5431:5432 --mount type=volume,source=tuesday_taco,target=/var/lib/postgresql/data -d -e POSTGRES_PASSWORD=password postgres
4e45dcabed8a6ff1ce5f934d0a407aba9ca55b939756bdd26f7210ad3c6db8ec
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
4e45dcabed8a   postgres   "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds   0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.2 (Debian 15.2-1.pgdg110+1))
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
bradsimpson@ app:


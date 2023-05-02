Last login: Tue May  2 09:34:55 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@ ~:docker container run hello-world
docker: Error response from daemon: dial unix docker.raw.sock: connect: no such file or directory.
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
bradsimpson213/nov_react           latest    8bf0a25eb594   3 weeks ago     568MB
postgres                           latest    80c558ffdc31   5 weeks ago     379MB
nginx                              alpine    2bc7edbc3cf2   2 months ago    40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   2 months ago    576MB
bradsimpson213/revisited_react     latest    303fa668755c   3 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   3 months ago    568MB
my_project                         latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   6 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   7 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   11 months ago   142MB
alpine                             latest    e66264b98777   11 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   19 months ago   13.3kB
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
49231614c94b   hello-world   "/hello"   2 minutes ago   Exited (0) 2 minutes ago             zealous_varahamihira


Last login: Tue May  2 09:35:01 on ttys005

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\clear












































bradsimpson@ ~:docker container run [flags] image name [commands][parameters]
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
2023/05/02 15:37:45 [notice] 1#1: using the "epoll" event method
2023/05/02 15:37:45 [notice] 1#1: nginx/1.21.6
2023/05/02 15:37:45 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/05/02 15:37:45 [notice] 1#1: OS: Linux 5.15.49-linuxkit
2023/05/02 15:37:45 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/05/02 15:37:45 [notice] 1#1: start worker processes
2023/05/02 15:37:45 [notice] 1#1: start worker process 31
2023/05/02 15:37:45 [notice] 1#1: start worker process 32
172.17.0.1 - - [02/May/2023:15:38:09 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:38:09 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
2023/05/02 15:38:09 [error] 31#31: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
172.17.0.1 - - [02/May/2023:15:38:33 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:38:34 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:38:35 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:38:36 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:38:37 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:38:37 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [02/May/2023:15:44:21 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" "-"
^C2023/05/02 15:44:28 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/05/02 15:44:28 [notice] 31#31: exiting
2023/05/02 15:44:28 [notice] 32#32: exiting
2023/05/02 15:44:28 [notice] 31#31: exit
2023/05/02 15:44:28 [notice] 32#32: exit
2023/05/02 15:44:28 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/05/02 15:44:28 [notice] 1#1: worker process 31 exited with code 0
2023/05/02 15:44:28 [notice] 1#1: signal 29 (SIGIO) received
2023/05/02 15:44:28 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/05/02 15:44:28 [notice] 1#1: worker process 32 exited with code 0
2023/05/02 15:44:28 [notice] 1#1: exit
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
a5d1738ddd0c   nginx     "/docker-entrypoint.…"   7 minutes ago   Exited (0) 24 seconds ago             cool_container
bradsimpson@ ~:clear

bradsimpson@ ~:docker container run -d -p 8000:80 nginx
200bd17f8c47685aa41cbdb19a0479f511b782426f6d960b23858d8bbb3b5c64
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
200bd17f8c47   nginx     "/docker-entrypoint.…"   28 seconds ago   Up 27 seconds   0.0.0.0:8000->80/tcp   distracted_gagarin
bradsimpson@ ~:docker container run --rm alpine sh
bradsimpson@ ~:docker container run --rm alpine ash
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
200bd17f8c47   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   distracted_gagarin
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
200bd17f8c47   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   distracted_gagarin
bradsimpson@ ~:docker container run -d --rm alpine ash
c1520f289622a9863be6e9e8deda1d656c137f2591d95b9739e7d7e7c1c4b1b4
bradsimpson@ ~:docker container run -d --rm alpine sh
effb7fc6a74ed7975488d30ca3b25653b06df0fac771eb05759eac87f11e25a9
bradsimpson@ ~:docker container run -d --rm alpine
e77fa44b60ff220f39eb4e037b5852eda4f8b6ecc130b9ceffd76ddd156cb1b0
bradsimpson@ ~:docker container run -d --rm alpine echo hello world
927983f7e1cf5ec3f24eabcf6fe850cd856fa8679bd2ef656ed766a0b7b28df8
bradsimpson@ ~:docker container run --rm alpine echo hello world
hello world
bradsimpson@ ~:docker container run --rm --name brads_container alpine echo hello world
hello world
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
200bd17f8c47   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->80/tcp   distracted_gagarin
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
200bd17f8c47   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->80/tcp   distracted_gagarin
bradsimpson@ ~:docker container run --name brads_container alpine echo hello world
hello world
bradsimpson@ ~:docker container ls -la
CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS                     PORTS     NAMES
b62fc7da08f8   alpine    "echo hello world"   3 seconds ago   Exited (0) 2 seconds ago             brads_container
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                      PORTS                    NAMES
b62fc7da08f8   alpine                     "echo hello world"       26 seconds ago   Exited (0) 25 seconds ago                            brads_container
200bd17f8c47   nginx                      "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:8000->80/tcp     distracted_gagarin
a5d1738ddd0c   nginx                      "/docker-entrypoint.…"   14 minutes ago   Exited (0) 8 minutes ago                             cool_container
49231614c94b   hello-world                "/hello"                 49 minutes ago   Exited (0) 49 minutes ago                            zealous_varahamihira
995e1771b696   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5000->3000/tcp   stupefied_hertz
bfc214c3a722   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               festive_swirles
2dbbf1c2d319   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                               epic_hertz
4e45dcabed8a   postgres                   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run --it alpine sh
unknown flag: --it
See 'docker container run --help'.
bradsimpson@ ~:docker container run -it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd bin/
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
/bin # quit
sh: quit: not found
/bin # exit
bradsimpson@ ~:docker container run --name vincents_container -d -p 8080:80 nginx
d20258abe3721b97200deceaca162c7089d07578b8edc9a752e8f48bc17b07a5
bradsimpson@ ~:docker container run -it --name test alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello world 
hello world
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                       PORTS                    NAMES
3f3af23ee783   alpine                     "sh"                     2 minutes ago    Exited (0) 2 minutes ago                              test
d20258abe372   nginx                      "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                 0.0.0.0:8080->80/tcp     vincents_container
66395a41a3ea   alpine                     "sh"                     7 minutes ago    Exited (127) 6 minutes ago                            relaxed_fermi
b62fc7da08f8   alpine                     "echo hello world"       9 minutes ago    Exited (0) 9 minutes ago                              brads_container
200bd17f8c47   nginx                      "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes                0.0.0.0:8000->80/tcp     distracted_gagarin
a5d1738ddd0c   nginx                      "/docker-entrypoint.…"   23 minutes ago   Exited (0) 16 minutes ago                             cool_container
49231614c94b   hello-world                "/hello"                 57 minutes ago   Exited (0) 57 minutes ago                             zealous_varahamihira
995e1771b696   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:5000->3000/tcp   stupefied_hertz
bfc214c3a722   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                festive_swirles
2dbbf1c2d319   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                epic_hertz
4e45dcabed8a   postgres                   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ ~:\clear

bradsimpson@ ~:echo hello world
hello world
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
d20258abe372   nginx     "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes    0.0.0.0:8080->80/tcp   vincents_container
200bd17f8c47   nginx     "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp   distracted_gagarin
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                       PORTS                    NAMES
3f3af23ee783   alpine                     "sh"                     4 minutes ago    Exited (0) 4 minutes ago                              test
d20258abe372   nginx                      "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                 0.0.0.0:8080->80/tcp     vincents_container
66395a41a3ea   alpine                     "sh"                     9 minutes ago    Exited (127) 8 minutes ago                            relaxed_fermi
b62fc7da08f8   alpine                     "echo hello world"       11 minutes ago   Exited (0) 11 minutes ago                             brads_container
200bd17f8c47   nginx                      "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes                0.0.0.0:8000->80/tcp     distracted_gagarin
a5d1738ddd0c   nginx                      "/docker-entrypoint.…"   25 minutes ago   Exited (0) 18 minutes ago                             cool_container
49231614c94b   hello-world                "/hello"                 59 minutes ago   Exited (0) 59 minutes ago                             zealous_varahamihira
995e1771b696   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:5000->3000/tcp   stupefied_hertz
bfc214c3a722   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                festive_swirles
2dbbf1c2d319   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                epic_hertz
4e45dcabed8a   postgres                   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ ~:docker container stop distracted_gagarin
distracted_gagarin
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
d20258abe372   nginx     "/docker-entrypoint.…"   7 minutes ago   Up 7 minutes   0.0.0.0:8080->80/tcp   vincents_container
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED             STATUS                         PORTS                    NAMES
3f3af23ee783   alpine                     "sh"                     6 minutes ago       Exited (0) 5 minutes ago                                test
d20258abe372   nginx                      "/docker-entrypoint.…"   7 minutes ago       Up 7 minutes                   0.0.0.0:8080->80/tcp     vincents_container
66395a41a3ea   alpine                     "sh"                     11 minutes ago      Exited (127) 10 minutes ago                             relaxed_fermi
b62fc7da08f8   alpine                     "echo hello world"       12 minutes ago      Exited (0) 12 minutes ago                               brads_container
200bd17f8c47   nginx                      "/docker-entrypoint.…"   18 minutes ago      Exited (0) 13 seconds ago                               distracted_gagarin
a5d1738ddd0c   nginx                      "/docker-entrypoint.…"   27 minutes ago      Exited (0) 20 minutes ago                               cool_container
49231614c94b   hello-world                "/hello"                 About an hour ago   Exited (0) About an hour ago                            zealous_varahamihira
995e1771b696   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago       0.0.0.0:5000->3000/tcp   stupefied_hertz
bfc214c3a722   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                  festive_swirles
2dbbf1c2d319   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                  epic_hertz
4e45dcabed8a   postgres                   "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago       0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED             STATUS                         PORTS                    NAMES
3f3af23ee783   alpine                     "sh"                     6 minutes ago       Exited (0) 6 minutes ago                                test
d20258abe372   nginx                      "/docker-entrypoint.…"   8 minutes ago       Up 8 minutes                   0.0.0.0:8080->80/tcp     vincents_container
66395a41a3ea   alpine                     "sh"                     11 minutes ago      Exited (127) 10 minutes ago                             relaxed_fermi
b62fc7da08f8   alpine                     "echo hello world"       13 minutes ago      Exited (0) 12 minutes ago                               brads_container
200bd17f8c47   nginx                      "/docker-entrypoint.…"   19 minutes ago      Exited (0) 33 seconds ago                               distracted_gagarin
a5d1738ddd0c   nginx                      "/docker-entrypoint.…"   27 minutes ago      Exited (0) 20 minutes ago                               cool_container
49231614c94b   hello-world                "/hello"                 About an hour ago   Exited (0) About an hour ago                            zealous_varahamihira
995e1771b696   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago       0.0.0.0:5000->3000/tcp   stupefied_hertz
bfc214c3a722   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                  festive_swirles
2dbbf1c2d319   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                  epic_hertz
4e45dcabed8a   postgres                   "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago       0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
d20258abe372   nginx     "/docker-entrypoint.…"   8 minutes ago   Up 8 minutes   0.0.0.0:8080->80/tcp   vincents_container
bradsimpson@ ~:docker container start cool_container
cool_container
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
d20258abe372   nginx     "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes   0.0.0.0:8080->80/tcp   vincents_container
a5d1738ddd0c   nginx     "/docker-entrypoint.…"   28 minutes ago   Up 3 seconds   0.0.0.0:8000->80/tcp   cool_container
bradsimpson@ ~:docker container stop a5d1738ddd0c vincents_container
a5d1738ddd0c
vincents_container
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear





bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                      COMMAND                  CREATED             STATUS                          PORTS                    NAMES
3f3af23ee783   alpine                     "sh"                     8 minutes ago       Exited (0) 8 minutes ago                                 test
d20258abe372   nginx                      "/docker-entrypoint.…"   10 minutes ago      Exited (0) About a minute ago                            vincents_container
66395a41a3ea   alpine                     "sh"                     14 minutes ago      Exited (127) 13 minutes ago                              relaxed_fermi
b62fc7da08f8   alpine                     "echo hello world"       15 minutes ago      Exited (0) 15 minutes ago                                brads_container
200bd17f8c47   nginx                      "/docker-entrypoint.…"   21 minutes ago      Exited (0) 3 minutes ago                                 distracted_gagarin
a5d1738ddd0c   nginx                      "/docker-entrypoint.…"   29 minutes ago      Exited (0) About a minute ago                            cool_container
49231614c94b   hello-world                "/hello"                 About an hour ago   Exited (0) About an hour ago                             zealous_varahamihira
995e1771b696   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago        0.0.0.0:5000->3000/tcp   stupefied_hertz
bfc214c3a722   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                   festive_swirles
2dbbf1c2d319   bradsimpson213/nov_react   "docker-entrypoint.s…"   3 weeks ago         Exited (1) 3 weeks ago                                   epic_hertz
4e45dcabed8a   postgres                   "docker-entrypoint.s…"   3 weeks ago         Exited (255) 3 weeks ago        0.0.0.0:5431->5432/tcp   lucid_zhukovsky
bradsimpson@ ~:docker container rm b62fc7da08f8
b62fc7da08f8
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
3f3af23ee7839815587f658604402ff89cacb51a189eabc7ff2a56e6698edcbe
d20258abe3721b97200deceaca162c7089d07578b8edc9a752e8f48bc17b07a5
66395a41a3eaa3c4a70f02514d71d82ec84edab927aa185689b44dbd45839df1
200bd17f8c47685aa41cbdb19a0479f511b782426f6d960b23858d8bbb3b5c64
a5d1738ddd0cb6b739e1786e77ce24996d3312af44fba440fbf0846d64175b49
49231614c94b470a55d91adfec7ee9c68f62fbb39065e2b34739898de9dba4c2
995e1771b696f3704e1299c5d1e7815b2ee27c80abed63f07b935c56bbc1574d
bfc214c3a722a2d059bb35e0cee270ff9081313047b60b77feabe8f9e9a23846
2dbbf1c2d3193372bd51dbb5670c8e62c05c277e05e3d2c6ea59c90f0619679a
4e45dcabed8a6ff1ce5f934d0a407aba9ca55b939756bdd26f7210ad3c6db8ec

Total reclaimed space: 58.42MB
bradsimpson@ ~:\clear






bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/nov_react           latest    8bf0a25eb594   3 weeks ago     568MB
postgres                           latest    80c558ffdc31   5 weeks ago     379MB
nginx                              alpine    2bc7edbc3cf2   2 months ago    40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   2 months ago    576MB
bradsimpson213/revisited_react     latest    303fa668755c   3 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   3 months ago    568MB
my_project                         latest    ae74e957ba0d   3 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   6 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   7 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   11 months ago   142MB
alpine                             latest    e66264b98777   11 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   19 months ago   13.3kB
bradsimpson@ ~:docker container run -p 8000:80 -d nginx
0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
0193056699c4   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:8000->80/tcp   charming_bassi
bradsimpson@ ~:docker container exec -it charming_bassi
"docker container exec" requires at least 2 arguments.
See 'docker container exec --help'.

Usage:  docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container
bradsimpson@ ~:docker container exec -it charming_bassi sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# cd lib	
# \ls
init  lsb  systemd  terminfo  udev  x86_64-linux-gnu
# cd ..
# cd usr
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share 
# \ls
X11		 common-licenses  fontconfig  libc-bin	  nginx        sensible-utils
adduser		 debconf	  fonts       lintian	  pam	       tabset
base-files	 debianutils	  gcc	      locale	  pam-configs  terminfo
base-passwd	 dict		  gdb	      man	  perl5        ucf
bash-completion  doc		  info	      maven-repo  pixmaps      xml
bug		 doc-base	  java	      menu	  polkit-1     zoneinfo
ca-certificates  dpkg		  keyrings    misc	  readline     zsh
# cd nginx	
# \ls 
html
# cd html	
# \ls
50x.html  index.html
# exit
bradsimpson@ ~:docker container inspect charming_bassi
[
    {
        "Id": "0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce",
        "Created": "2023-05-02T16:10:21.389587271Z",
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
            "Pid": 3893,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-02T16:10:22.090251036Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/hostname",
        "HostsPath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/hosts",
        "LogPath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce-json.log",
        "Name": "/charming_bassi",
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
                "LowerDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b/merged",
                "UpperDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b/diff",
                "WorkDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0193056699c4",
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
            "SandboxID": "190ba4a3d8d3344d22ace4566304637a23a33e7e408de09ef772181945cb258e",
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
            "SandboxKey": "/var/run/docker/netns/190ba4a3d8d3",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "305c54838c36e7ac0cf7f681263c917568bdf15d138d336efc18d82aa7e716e9",
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
                    "NetworkID": "be7fe1a8592597e0c5a948f7be09e14c0d4ec30b3f0328d23bebeb1446bf756a",
                    "EndpointID": "305c54838c36e7ac0cf7f681263c917568bdf15d138d336efc18d82aa7e716e9",
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


# NETWORKING SECTION

Last login: Tue May  2 11:21:00 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
be7fe1a85925   bridge       bridge    local
7318efe60d0f   host         host      local
e462f118fac6   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
0193056699c4   nginx     "/docker-entrypoint.…"   31 minutes ago   Up 31 minutes   0.0.0.0:8000->80/tcp   charming_bassi
bradsimpson@ ~:docker container inspect charming_bassi
[
    {
        "Id": "0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce",
        "Created": "2023-05-02T16:10:21.389587271Z",
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
            "Pid": 3893,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-02T16:10:22.090251036Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/hostname",
        "HostsPath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/hosts",
        "LogPath": "/var/lib/docker/containers/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce/0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce-json.log",
        "Name": "/charming_bassi",
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
                "LowerDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b/merged",
                "UpperDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b/diff",
                "WorkDir": "/var/lib/docker/overlay2/c457f3e37d6ff540b1227ad82201b1abcd6714d97c8d38c8f22465dbb97e045b/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0193056699c4",
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
            "SandboxID": "190ba4a3d8d3344d22ace4566304637a23a33e7e408de09ef772181945cb258e",
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
            "SandboxKey": "/var/run/docker/netns/190ba4a3d8d3",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "305c54838c36e7ac0cf7f681263c917568bdf15d138d336efc18d82aa7e716e9",
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
                    "NetworkID": "be7fe1a8592597e0c5a948f7be09e14c0d4ec30b3f0328d23bebeb1446bf756a",
                    "EndpointID": "305c54838c36e7ac0cf7f681263c917568bdf15d138d336efc18d82aa7e716e9",
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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
0193056699c4   nginx     "/docker-entrypoint.…"   31 minutes ago   Up 31 minutes   0.0.0.0:8000->80/tcp   charming_bassi
bradsimpson@ ~:docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
be7fe1a85925   bridge       bridge    local
7318efe60d0f   host         host      local
e462f118fac6   my_network   bridge    local
475754f27665   none         null      local
bradsimpson@ ~:docker network create --driver bridge taco_network
0d6561636bf900b89a42a575583f6ba619bbbcf1745b2b112eab5216b07e85f7
bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
be7fe1a85925   bridge         bridge    local
7318efe60d0f   host           host      local
e462f118fac6   my_network     bridge    local
475754f27665   none           null      local
0d6561636bf9   taco_network   bridge    local
bradsimpson@ ~:docker network prune
WARNING! This will remove all custom networks not used by at least one container.
Are you sure you want to continue? [y/N] n
bradsimpson@ ~:\clear

bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
be7fe1a85925   bridge         bridge    local
7318efe60d0f   host           host      local
e462f118fac6   my_network     bridge    local
475754f27665   none           null      local
0d6561636bf9   taco_network   bridge    local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
0193056699c4   nginx     "/docker-entrypoint.…"   51 minutes ago   Up 51 minutes   0.0.0.0:8000->80/tcp   charming_bassi
bradsimpson@ ~:docker container stop 0193056699c4
0193056699c4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run -d --name taco1 --network taco_network nginx:alpine
e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   80/tcp    taco1
bradsimpson@ ~:docker container run -d --name taco2 --network taco_network nginx:alpine
ffb5cf31c2bc0f6008490b02091c7dc0b8117f56d9880a3589d13ff4a66b9a9e
bradsimpson@ ~:docker container inspect taco1
[
    {
        "Id": "e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08",
        "Created": "2023-05-02T17:03:18.017432252Z",
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
            "Pid": 4099,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-02T17:03:19.251900678Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08/hostname",
        "HostsPath": "/var/lib/docker/containers/e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08/hosts",
        "LogPath": "/var/lib/docker/containers/e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08/e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08-json.log",
        "Name": "/taco1",
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
            "NetworkMode": "taco_network",
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
                "LowerDir": "/var/lib/docker/overlay2/67b4e55336efe024f5d6acf4a1401e03579726fae0dd7a7ad313b071b4176036-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/67b4e55336efe024f5d6acf4a1401e03579726fae0dd7a7ad313b071b4176036/merged",
                "UpperDir": "/var/lib/docker/overlay2/67b4e55336efe024f5d6acf4a1401e03579726fae0dd7a7ad313b071b4176036/diff",
                "WorkDir": "/var/lib/docker/overlay2/67b4e55336efe024f5d6acf4a1401e03579726fae0dd7a7ad313b071b4176036/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "e67bf9551856",
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
            "SandboxID": "cbac44bdc12a1e5eea653a2627a0f932cc6a8b1a8b443f045451c384280b1262",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/cbac44bdc12a",
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
                "taco_network": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "e67bf9551856"
                    ],
                    "NetworkID": "0d6561636bf900b89a42a575583f6ba619bbbcf1745b2b112eab5216b07e85f7",
                    "EndpointID": "97755d3fdca52ded3cab12b3a551f278c66373b2203aba0be01e973181e6397b",
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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS          PORTS     NAMES
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   43 seconds ago       Up 41 seconds   80/tcp    taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up 59 seconds   80/tcp    taco1
bradsimpson@ ~:dicker container run -d --name taco3 nginx:alpine
-bash: dicker: command not found
bradsimpson@ ~:docker container run -d --name taco3 nginx:alpine
162d1ec309c31213d509124ea680f73bde8c9dcd983c09bc8f3402923b7b3d03
bradsimpson@ ~:docker container run -d --name taco4 nginx:alpine
d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago        Up 3 seconds        80/tcp    taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   13 seconds ago       Up 11 seconds       80/tcp    taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    taco1
bradsimpson@ ~:docker container inspect taco4
[
    {
        "Id": "d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab",
        "Created": "2023-05-02T17:05:10.575015572Z",
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
            "Pid": 4446,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-05-02T17:05:11.846010825Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab/hostname",
        "HostsPath": "/var/lib/docker/containers/d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab/hosts",
        "LogPath": "/var/lib/docker/containers/d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab/d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab-json.log",
        "Name": "/taco4",
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
                "LowerDir": "/var/lib/docker/overlay2/66639c8af7340ac3e6db602d9ace5a9a0e403485b5efa55e659fc2157287e52c-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/66639c8af7340ac3e6db602d9ace5a9a0e403485b5efa55e659fc2157287e52c/merged",
                "UpperDir": "/var/lib/docker/overlay2/66639c8af7340ac3e6db602d9ace5a9a0e403485b5efa55e659fc2157287e52c/diff",
                "WorkDir": "/var/lib/docker/overlay2/66639c8af7340ac3e6db602d9ace5a9a0e403485b5efa55e659fc2157287e52c/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "d38aa5d5abbd",
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
            "SandboxID": "dfff60a0473a34a4bd38059581acfee4b09ff9199038b1310607b30c7b204ee2",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/dfff60a0473a",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "b58fe7cd1a82f60f0b46e5c3ab27ff0d079bb2870ac107281139d8b3e50487d6",
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
                    "NetworkID": "be7fe1a8592597e0c5a948f7be09e14c0d4ec30b3f0328d23bebeb1446bf756a",
                    "EndpointID": "b58fe7cd1a82f60f0b46e5c3ab27ff0d079bb2870ac107281139d8b3e50487d6",
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
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago        Up 3 minutes        80/tcp    taco1
bradsimpson@ ~:docker container exec -it taco1 ash
/ # ping -c 4 taco2
PING taco2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=3.169 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.114 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.105 ms
64 bytes from 172.18.0.3: seq=3 ttl=64 time=0.110 ms

--- taco2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.105/0.874/3.169 ms
/ # ping -c 4 taco3
ping: bad address 'taco3'
/ # ping -c 4 taco4
ping: bad address 'taco4'
/ # exit
bradsimpson@ ~:docker container exec -it taco3 ash
/ # ping -c 3 taco4
ping: bad address 'taco4'
/ # ping -c 3 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.319 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.570 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.103 ms

--- 172.17.0.3 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.103/0.330/0.570 ms
/ # exit


# BIND MOUNTS & VOLUMES SECTION

Last login: Tue May  2 13:39:03 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container run --mount type=bind,source=/absolute/path/toi/folder,target=/usr/share/nginx/html
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ ~:docker container instpect postgres

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
bradsimpson@ ~:docker container inspect postgres
[]
Error: No such container: postgres
bradsimpson@ ~:docker image inspect postgres
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
bradsimpson@ ~:\clear

bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		oct-starter
Desktop		Library		Pictures	app		opt
Documents	Movies		Postman		docker
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container run -d --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8000:80 nginx:alpine
a1f48984f673ff313dba337a35f05a0834af919c0da90aa9ecbf8ea3bb8e202b
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
a1f48984f673   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago    Up 5 seconds    0.0.0.0:8000->80/tcp   gallant_davinci
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp                 taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Up 47 minutes   80/tcp                 taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   80/tcp                 taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   48 minutes ago   Up 48 minutes   80/tcp                 taco1
bradsimpson@ ~:docker container exec -it gallant_davinci ash
/ # cd use
ash: cd: can't cd to use: No such file or directory
/ # cd usr/share/nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html
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
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     tuesday_taco
bradsimpson@ app:docker volume create even_more_tacos
even_more_tacos
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     even_more_tacos
local     tuesday_taco
bradsimpson@ app:\clear

bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/nov_react           latest    8bf0a25eb594   3 weeks ago     568MB
postgres                           latest    80c558ffdc31   5 weeks ago     379MB
nginx                              alpine    2bc7edbc3cf2   2 months ago    40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   2 months ago    576MB
bradsimpson213/revisited_react     latest    303fa668755c   3 months ago    568MB
my_project                         latest    ae74e957ba0d   3 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   6 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   7 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   11 months ago   142MB
alpine                             latest    e66264b98777   11 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   19 months ago   13.3kB
bradsimpson@ app:docker image rm postgres
Untagged: postgres:latest
Untagged: postgres@sha256:5a90725b3751c2c7ac311c9384dfc1a8f6e41823e341fb1dceed96a11677303a
Deleted: sha256:80c558ffdc314a930fe201d69d9cd58a0fc0f6a833e3f5014268a02d36438c65
Deleted: sha256:42295265527a128d149cae51c030d3ff8f73c26f677a1d2d4bd58ec8871fd288
Deleted: sha256:fb1e4f6c7386207d1c3016bb7ce62fdbce6d44873c209962f46e7a196a1a1e13
Deleted: sha256:560aee72760528dc6f70c3d42185046661b045bffae5a7868fc5a0e4d87768e9
Deleted: sha256:80e51af215303666907b4bfcbc18ae3727d873315df06bc2dbe4cf7594fa8472
Deleted: sha256:b5e59674b920bba2949cb9e8be813e8c92025eac9b65dd7715d7e740fbfc5ca5
Deleted: sha256:3bfddacb0f8b6a9d981c1b95835936b4c2bd87f8e687cb1500d0e22a096658a7
Deleted: sha256:5370c56d373d2913d9725e72d086bec15842d31a2ded959b75b8cafdf7f88e00
Deleted: sha256:c4ee003a49a60699e109b183c7f7a07110849d8fdf4dff94f9f978dc3366c56a
Deleted: sha256:b60e524912609cb1a0e024f456c804c0ea48548ee866244e81c3461555c1058b
Deleted: sha256:7d54a2289f66a10ba64dc1e17ca954103f26479b1944e37f4b0120572db9d6de
Deleted: sha256:500bc1706cd69debf2026bb47150d11fb0c71ed9f8399b262b9cc2c3a001d6bf
Deleted: sha256:998dfaa5025a073bea87e25ea62ce8aff95721b16375385964def8ea2d290a7b
Deleted: sha256:3af14c9a24c941c626553628cf1942dcd94d40729777f2fcfbcd3b8a3dfccdd6
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/nov_react           latest    8bf0a25eb594   3 weeks ago     568MB
nginx                              alpine    2bc7edbc3cf2   2 months ago    40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   2 months ago    576MB
bradsimpson213/revisited_react     latest    303fa668755c   3 months ago    568MB
bradsimps213/new_project           latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/my_project          latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/react_project       latest    ae74e957ba0d   3 months ago    568MB
my_project                         latest    ae74e957ba0d   3 months ago    568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   6 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   7 months ago    432MB
ubuntu                             latest    27941809078c   10 months ago   77.8MB
nginx                              latest    0e901e68141f   11 months ago   142MB
alpine                             latest    e66264b98777   11 months ago   5.53MB
hello-world                        latest    feb5d9fea6a5   19 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
26c5c85e47da: Pull complete 
1c30a4c3f519: Pull complete 
d5c0f1ae682d: Pull complete 
1b1b2890ec0f: Pull complete 
391087799df7: Pull complete 
b413b4057e31: Pull complete 
4fa4edfeab8b: Pull complete 
b0a4d596bc61: Pull complete 
f6d73cd87199: Pull complete 
62b0bb33c69b: Pull complete 
bb0ddb7e7f1a: Pull complete 
583ec94d38ee: Pull complete 
efdf2a922e82: Pull complete 
Digest: sha256:6cc97262444f1c45171081bc5a1d4c28b883ea46a6e0d1a45a8eac4a7f4767ab
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 -d --mount type=volume,source=even_more_tacos,target=/var/lib/postgresql/data postgres
8c05f671bd5ab8730958525180cbab65089bf48f6097eca26f41989a241c8b32
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
a1f48984f673   nginx:alpine   "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   0.0.0.0:8000->80/tcp   gallant_davinci
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   57 minutes ago   Up 57 minutes   80/tcp                 taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   57 minutes ago   Up 57 minutes   80/tcp                 taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago   Up 59 minutes   80/tcp                 taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago   Up 59 minutes   80/tcp                 taco1
bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 -d --mount type=volume,source=even_more_tacos,target=/var/lib/postgresql/data postgres
docker: Error response from daemon: Conflict. The container name "/postgres1" is already in use by container "8c05f671bd5ab8730958525180cbab65089bf48f6097eca26f41989a241c8b32". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
a1f48984f673   nginx:alpine   "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   0.0.0.0:8000->80/tcp   gallant_davinci
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   57 minutes ago   Up 57 minutes   80/tcp                 taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   58 minutes ago   Up 58 minutes   80/tcp                 taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago   Up 59 minutes   80/tcp                 taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago   Up 59 minutes   80/tcp                 taco1
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                         PORTS                  NAMES
8c05f671bd5a   postgres       "docker-entrypoint.s…"   41 seconds ago   Exited (1) 39 seconds ago                             postgres1
a1f48984f673   nginx:alpine   "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes                  0.0.0.0:8000->80/tcp   gallant_davinci
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   58 minutes ago   Up 58 minutes                  80/tcp                 taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   58 minutes ago   Up 58 minutes                  80/tcp                 taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago   Up 59 minutes                  80/tcp                 taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago   Up 59 minutes                  80/tcp                 taco1
0193056699c4   nginx          "/docker-entrypoint.…"   2 hours ago      Exited (0) About an hour ago                          charming_bassi
bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 -d -e POSTGRES_PASSWORD=password --mount type=volume,source=even_more_tacos,target=/var/lib/postgresql/data postgres
docker: Error response from daemon: Conflict. The container name "/postgres1" is already in use by container "8c05f671bd5ab8730958525180cbab65089bf48f6097eca26f41989a241c8b32". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
psql: error: could not connect to server: Connection refused
	Is the server running on host "localhost" (::1) and accepting
	TCP/IP connections on port 5431?
could not connect to server: Connection refused
	Is the server running on host "localhost" (127.0.0.1) and accepting
	TCP/IP connections on port 5431?
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS             PORTS                  NAMES
a1f48984f673   nginx:alpine   "/docker-entrypoint.…"   12 minutes ago      Up 12 minutes      0.0.0.0:8000->80/tcp   gallant_davinci
d38aa5d5abbd   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago      Up 59 minutes      80/tcp                 taco4
162d1ec309c3   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago      Up 59 minutes      80/tcp                 taco3
ffb5cf31c2bc   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Up About an hour   80/tcp                 taco2
e67bf9551856   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Up About an hour   80/tcp                 taco1
bradsimpson@ app:docker container stop taco1 taco2 taco3 taco4
taco1
taco2
taco3
taco4
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
a1f48984f673   nginx:alpine   "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8000->80/tcp   gallant_davinci
bradsimpson@ app:docker container stop gallant_davinci
gallant_davinci
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
8c05f671bd5ab8730958525180cbab65089bf48f6097eca26f41989a241c8b32
a1f48984f673ff313dba337a35f05a0834af919c0da90aa9ecbf8ea3bb8e202b
d38aa5d5abbd85e8acba5a52844d6791fb7079cda0efe9485b2208e4d4d4dbab
162d1ec309c31213d509124ea680f73bde8c9dcd983c09bc8f3402923b7b3d03
ffb5cf31c2bc0f6008490b02091c7dc0b8117f56d9880a3589d13ff4a66b9a9e
e67bf95518566717ab0e955361f9a8028eb9f90baba65bedba669648fc0b6a08
0193056699c44cc854c03c8e1d6efe74bcbc5f34709aae798c0a4d47ead546ce

Total reclaimed space: 3.045MB
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 --name postgres1 -d -e POSTGRES_PASSWORD=password --mount type=volume,source=even_more_tacos,target=/var/lib/postgresql/data postgres
1bbf6ad826b7265e9a9b1b90b863316d848f1c95e45d86ef51e21b6384ffb977
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

postgres=# CREATE DATABASE tacosforlunch WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                   List of databases
     Name      |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
---------------+----------+----------+------------+------------+-----------------------
 postgres      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 tacosforlunch | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS                    NAMES
1bbf6ad826b7   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5431->5432/tcp   postgres1
bradsimpson@ app:docker container stop postgres1
postgres1
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS                     PORTS     NAMES
1bbf6ad826b7   postgres   "docker-entrypoint.s…"   About a minute ago   Exited (0) 4 seconds ago             postgres1
bradsimpson@ app:docker container rm postgres1
postgres1
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container run -p 5431:5432 --name postgres2 -d -e POSTGRES_PASSWORD=password --mount type=volume,source=even_more_tacos,target=/var/lib/postgresql/data postgres
6ea55d053da64f992324eff788ea7b7489cce862598e4e00da7e36dab36ab6e0
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                   List of databases
     Name      |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
---------------+----------+----------+------------+------------+-----------------------
 postgres      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 tacosforlunch | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
 template1     | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
               |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:


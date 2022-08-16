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
react_fe                    latest    c320273135f5   7 weeks ago     377MB
bradsimpson213/test_react   latest    93489609ef4b   7 weeks ago     377MB
ubuntu                      latest    27941809078c   2 months ago    77.8MB
postgres                    latest    5b21e2e86aab   2 months ago    376MB
nginx                       latest    0e901e68141f   2 months ago    142MB
alpine                      latest    e66264b98777   2 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    d1165f221234   17 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
b7707df0eff5   hello-world   "/hello"   2 minutes ago   Exited (0) 2 minutes ago             stupefied_antonelli
bradsimpson@ ~:docker container run nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2022/08/16 15:32:57 [notice] 1#1: using the "epoll" event method
2022/08/16 15:32:57 [notice] 1#1: nginx/1.21.6
2022/08/16 15:32:57 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2022/08/16 15:32:57 [notice] 1#1: OS: Linux 5.10.25-linuxkit
2022/08/16 15:32:57 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2022/08/16 15:32:57 [notice] 1#1: start worker processes
2022/08/16 15:32:57 [notice] 1#1: start worker process 31
2022/08/16 15:32:57 [notice] 1#1: start worker process 32
^C2022/08/16 15:33:04 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/08/16 15:33:04 [notice] 32#32: exiting
2022/08/16 15:33:04 [notice] 31#31: exiting
2022/08/16 15:33:04 [notice] 32#32: exit
2022/08/16 15:33:04 [notice] 31#31: exit
2022/08/16 15:33:04 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2022/08/16 15:33:04 [notice] 1#1: worker process 32 exited with code 0
2022/08/16 15:33:04 [notice] 1#1: signal 29 (SIGIO) received
2022/08/16 15:33:04 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2022/08/16 15:33:04 [notice] 1#1: worker process 31 exited with code 0
2022/08/16 15:33:04 [notice] 1#1: exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run --name my_nginx -p 8080:80 -d nginx
3511a91d3f225b01e37d9734228a4db0528a398f56611210ffe2d928f5364e98
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
3511a91d3f22   nginx     "/docker-entrypoint.…"   17 seconds ago   Up 16 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   my_nginx
bradsimpson@ ~:docker container stop my_nginx
my_nginx
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
3511a91d3f22   nginx         "/docker-entrypoint.…"   6 minutes ago    Exited (0) 10 seconds ago             my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   8 minutes ago    Exited (0) 8 minutes ago              optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 36 minutes ago   Exited (0) 36 minutes ago             stupefied_antonelli
bradsimpson@ ~:docker container run -p 8080:80 -d nginx
1ecda725c78e395dcb2938620cb1f9f1cfc2118918c521113722e756514c2333
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
1ecda725c78e   nginx     "/docker-entrypoint.…"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   reverent_franklin
bradsimpson@ ~:docker container run -p 8080:80 -d --rm nginx
0fab6f1794d23fa0e80512d666a9087cb93ca65e287fb880e5c6c3a9683c2bd9
docker: Error response from daemon: driver failed programming external connectivity on endpoint hardcore_wu (778b4bbddb10cf1d0b0ff7ab754c77ba958c8dd1691575b623af0913ce3b0071): Bind for 0.0.0.0:8080 failed: port is already allocated.
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
1ecda725c78e   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   reverent_franklin
bradsimpson@ ~:docker container stop 1ecda725c78e
1ecda725c78e
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear


bradsimpson@ ~:docker container run -p 8080:80 -d --rm nginx
b8e29940eb3aa6349b02b12176b3e0a449100cad62d5833f9de183f9a8b233a4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
b8e29940eb3a   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 3 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_easley
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                                   NAMES
b8e29940eb3a   nginx         "/docker-entrypoint.…"   26 seconds ago   Up 24 seconds               0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_easley
1ecda725c78e   nginx         "/docker-entrypoint.…"   4 minutes ago    Exited (0) 45 seconds ago                                           reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   11 minutes ago   Exited (0) 6 minutes ago                                            my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   14 minutes ago   Exited (0) 14 minutes ago                                           optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 42 minutes ago   Exited (0) 42 minutes ago                                           stupefied_antonelli
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
b8e29940eb3a   nginx     "/docker-entrypoint.…"   56 seconds ago   Up 54 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hardcore_easley
bradsimpson@ ~:docker container stop hardcore_easley
hardcore_easley
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                          PORTS     NAMES
1ecda725c78e   nginx         "/docker-entrypoint.…"   6 minutes ago    Exited (0) About a minute ago             reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   13 minutes ago   Exited (0) 7 minutes ago                  my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   15 minutes ago   Exited (0) 15 minutes ago                 optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 43 minutes ago   Exited (0) 43 minutes ago                 stupefied_antonelli
bradsimpson@ ~:\clear






bradsimpson@ ~:docker container run -it --name test_it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd bin
/bin # \ls
arch           dd             fsync          linux32        mount          pwd            stty
ash            df             getopt         linux64        mountpoint     reformime      su
base64         dmesg          grep           ln             mpstat         rev            sync
bbconfig       dnsdomainname  gunzip         login          mv             rm             tar
busybox        dumpkmap       gzip           ls             netstat        rmdir          touch
cat            echo           hostname       lsattr         nice           run-parts      true
chattr         ed             ionice         lzop           pidof          sed            umount
chgrp          egrep          iostat         makemime       ping           setpriv        uname
chmod          false          ipcalc         mkdir          ping6          setserial      usleep
chown          fatattr        kbd_mode       mknod          pipe_progress  sh             watch
cp             fdflush        kill           mktemp         printenv       sleep          zcat
date           fgrep          link           more           ps             stat
/bin # cd ..
/ # cd media/
/media # \ls
cdrom   floppy  usb
/media # cd floppy
/media/floppy # \ls
/media/floppy # cd .
/media/floppy # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
64773e146963   alpine        "sh"                     2 minutes ago    Exited (0) 32 seconds ago             test_it
1ecda725c78e   nginx         "/docker-entrypoint.…"   9 minutes ago    Exited (0) 5 minutes ago              reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   17 minutes ago   Exited (0) 11 minutes ago             my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   19 minutes ago   Exited (0) 19 minutes ago             optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 47 minutes ago   Exited (0) 47 minutes ago             stupefied_antonelli
bradsimpson@ ~:\clear







bradsimpson@ ~:docker container run --name enginex -d -p 8080:80 nginx
b54f6d10283e8a959949a432719047baa8c8ce3e6701e6880fc1f3fb639694fd
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
b54f6d10283e   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   enginex
bradsimpson@ ~:docker container run --name test -it alpine sh
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
/bin # exit
bradsimpson@ ~:\ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		app.index.html
bradsimpson@ ~:ls
Applications	Downloads	Music		Public		opt
Desktop		Library		Pictures	app
Documents	Movies		Postman		app.index.html
bradsimpson@ ~:\clear







bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo Hello World
Hello World
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
b54f6d10283e   nginx     "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   enginex
bradsimpson@ ~:docker container stop enginex
enginex
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
e6214b88cd1f   alpine        "sh"                     2 minutes ago    Exited (0) 2 minutes ago              test
b54f6d10283e   nginx         "/docker-entrypoint.…"   4 minutes ago    Exited (0) 6 seconds ago              enginex
64773e146963   alpine        "sh"                     9 minutes ago    Exited (0) 8 minutes ago              test_it
1ecda725c78e   nginx         "/docker-entrypoint.…"   17 minutes ago   Exited (0) 13 minutes ago             reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   24 minutes ago   Exited (0) 18 minutes ago             my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   26 minutes ago   Exited (0) 26 minutes ago             optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 54 minutes ago   Exited (0) 54 minutes ago             stupefied_antonelli
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
e6214b88cd1f   alpine        "sh"                     4 minutes ago    Exited (0) 4 minutes ago              test
b54f6d10283e   nginx         "/docker-entrypoint.…"   6 minutes ago    Exited (0) 2 minutes ago              enginex
64773e146963   alpine        "sh"                     11 minutes ago   Exited (0) 10 minutes ago             test_it
1ecda725c78e   nginx         "/docker-entrypoint.…"   19 minutes ago   Exited (0) 15 minutes ago             reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   26 minutes ago   Exited (0) 20 minutes ago             my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   28 minutes ago   Exited (0) 28 minutes ago             optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 56 minutes ago   Exited (0) 56 minutes ago             stupefied_antonelli
bradsimpson@ ~:\clear

bradsimpson@ ~:docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
eab6be3dbd37   bridge    bridge    local
7318efe60d0f   host      host      local
475754f27665   none      null      local
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
react_fe                    latest    c320273135f5   7 weeks ago     377MB
bradsimpson213/test_react   latest    93489609ef4b   7 weeks ago     377MB
ubuntu                      latest    27941809078c   2 months ago    77.8MB
postgres                    latest    5b21e2e86aab   2 months ago    376MB
nginx                       latest    0e901e68141f   2 months ago    142MB
alpine                      latest    e66264b98777   2 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    d1165f221234   17 months ago   13.3kB
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:\clear


























bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run -d -p 8080:80 nginx
c5825045d1b780e817c3fe4fd18d679fcb232d64f4b652bfc2f81b3c82f27c02
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
c5825045d1b7   nginx     "/docker-entrypoint.…"   3 seconds ago   Up 2 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   hungry_kilby
bradsimpson@ ~:docker container stop hungry_kilby
hungry_kilby
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
c5825045d1b7   nginx         "/docker-entrypoint.…"   51 seconds ago   Exited (0) 11 seconds ago             hungry_kilby
e6214b88cd1f   alpine        "sh"                     7 minutes ago    Exited (0) 7 minutes ago              test
b54f6d10283e   nginx         "/docker-entrypoint.…"   9 minutes ago    Exited (0) 4 minutes ago              enginex
64773e146963   alpine        "sh"                     14 minutes ago   Exited (0) 13 minutes ago             test_it
1ecda725c78e   nginx         "/docker-entrypoint.…"   22 minutes ago   Exited (0) 18 minutes ago             reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   29 minutes ago   Exited (0) 23 minutes ago             my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   31 minutes ago   Exited (0) 31 minutes ago             optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 59 minutes ago   Exited (0) 59 minutes ago             stupefied_antonelli
bradsimpson@ ~:docker container run optimistic_mayer
Unable to find image 'optimistic_mayer:latest' locally
docker: Error response from daemon: pull access denied for optimistic_mayer, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
bradsimpson@ ~:docker container start optimistic_mayer
optimistic_mayer
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS     NAMES
d8c700f33bb9   nginx     "/docker-entrypoint.…"   32 minutes ago   Up 5 seconds   80/tcp    optimistic_mayer
bradsimpson@ ~:docker container start enginex hungry_kilby
enginex
Error response from daemon: driver failed programming external connectivity on endpoint hungry_kilby (db08e47fe47ca0f488736947378ae97711f3f804a0f7e8435b6ed68aa94f26a8): Bind for 0.0.0.0:8080 failed: port is already allocated
Error: failed to start containers: hungry_kilby
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS              PORTS                                   NAMES
b54f6d10283e   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 41 seconds       0.0.0.0:8080->80/tcp, :::8080->80/tcp   enginex
d8c700f33bb9   nginx     "/docker-entrypoint.…"   33 minutes ago   Up About a minute   80/tcp                                  optimistic_mayer
bradsimpson@ ~:docker container stop b54f6d10283e d8c700f33bb9
b54f6d10283e
d8c700f33bb9
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run ---->  docker container create & docker container start
[1] 10963
"docker container start" requires at least 1 argument.
See 'docker container start --help'.

Usage:  docker container start [OPTIONS] CONTAINER [CONTAINER...]

Start one or more stopped containers
bradsimpson@ ~:bad flag syntax: ----
See 'docker container run --help'.

[1]+  Exit 125                docker container run ---- container create > docker
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                          PORTS     NAMES
c5825045d1b7   nginx         "/docker-entrypoint.…"   5 minutes ago       Exited (128) 4 minutes ago                hungry_kilby
e6214b88cd1f   alpine        "sh"                     12 minutes ago      Exited (0) 11 minutes ago                 test
b54f6d10283e   nginx         "/docker-entrypoint.…"   14 minutes ago      Exited (0) About a minute ago             enginex
64773e146963   alpine        "sh"                     19 minutes ago      Exited (0) 17 minutes ago                 test_it
1ecda725c78e   nginx         "/docker-entrypoint.…"   27 minutes ago      Exited (0) 22 minutes ago                 reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   34 minutes ago      Exited (0) 28 minutes ago                 my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   36 minutes ago      Exited (0) About a minute ago             optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago              stupefied_antonelli
bradsimpson@ ~:docker container rm enginex
enginex
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED             STATUS                         PORTS     NAMES
c5825045d1b7   nginx         "/docker-entrypoint.…"   6 minutes ago       Exited (128) 5 minutes ago               hungry_kilby
e6214b88cd1f   alpine        "sh"                     12 minutes ago      Exited (0) 12 minutes ago                test
64773e146963   alpine        "sh"                     19 minutes ago      Exited (0) 18 minutes ago                test_it
1ecda725c78e   nginx         "/docker-entrypoint.…"   27 minutes ago      Exited (0) 23 minutes ago                reverent_franklin
3511a91d3f22   nginx         "/docker-entrypoint.…"   34 minutes ago      Exited (0) 28 minutes ago                my_nginx
d8c700f33bb9   nginx         "/docker-entrypoint.…"   36 minutes ago      Exited (0) 2 minutes ago                 optimistic_mayer
b7707df0eff5   hello-world   "/hello"                 About an hour ago   Exited (0) About an hour ago             stupefied_antonelli
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
c5825045d1b780e817c3fe4fd18d679fcb232d64f4b652bfc2f81b3c82f27c02
e6214b88cd1f159df01f4bc1160466a7a0de27cf3d08b75648da5dd7baaf8805
64773e1469637c6e47927cbd63cb94638ae32b0d6c40749fd3488d8728fb758d
1ecda725c78e395dcb2938620cb1f9f1cfc2118918c521113722e756514c2333
3511a91d3f225b01e37d9734228a4db0528a398f56611210ffe2d928f5364e98
d8c700f33bb94fcaaaae98e211ae2499d89a086d94399de01bc73de6a1ac75d5
b7707df0eff54c4f00f72f677b1617b41e9d99a3bed5cb74b6d42661b6ebf137

Total reclaimed space: 4.451kB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx
c56b363d19326f1c46e10316ad654f4403f226d70e759e4bac6abc67d146ff2b
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
c56b363d1932   nginx     "/docker-entrypoint.…"   7 seconds ago   Up 5 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   upbeat_kalam
bradsimpson@ ~:docker container exec -it upbeat_kalam sh
# \ls
bin   dev		   docker-entrypoint.sh  home  lib64  mnt  proc  run   srv  tmp  var
boot  docker-entrypoint.d  etc			 lib   media  opt  root  sbin  sys  usr
# cd run	
# \ls
lock  nginx.pid  utmp
# exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container run -d -p 8080:80 nginx
b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
b73b88a4b911   nginx     "/docker-entrypoint.…"   4 seconds ago   Up 2 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   condescending_lamport
bradsimpson@ ~:docker container inspect condescending_lamport
[
    {
        "Id": "b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf",
        "Created": "2022-08-16T16:38:16.665752244Z",
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
            "Pid": 4999,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2022-08-16T16:38:17.803642389Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf/hostname",
        "HostsPath": "/var/lib/docker/containers/b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf/hosts",
        "LogPath": "/var/lib/docker/containers/b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf/b73b88a4b9117b013f6d651625717d27678af259813133d1a655c56fa2f5e2bf-json.log",
        "Name": "/condescending_lamport",
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
                "LowerDir": "/var/lib/docker/overlay2/5cc14afb2eaedc32d1981da259b4c5ef9b9779319e725798eef749da50dee3b5-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/5cc14afb2eaedc32d1981da259b4c5ef9b9779319e725798eef749da50dee3b5/merged",
                "UpperDir": "/var/lib/docker/overlay2/5cc14afb2eaedc32d1981da259b4c5ef9b9779319e725798eef749da50dee3b5/diff",
                "WorkDir": "/var/lib/docker/overlay2/5cc14afb2eaedc32d1981da259b4c5ef9b9779319e725798eef749da50dee3b5/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b73b88a4b911",
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
            "SandboxID": "661a10d66868c37dd310267ccd627d9c1708eed8521e561a006f779e9cf87420",
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
            "SandboxKey": "/var/run/docker/netns/661a10d66868",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "4c6e3e0dac4c8168853041c7826b342714eb18033b2b76293da0eb15b3089c64",
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
                    "NetworkID": "eab6be3dbd37337ea94afcb65f4a22274b2df3cbea3ca742d1226b45a7c827d8",
                    "EndpointID": "4c6e3e0dac4c8168853041c7826b342714eb18033b2b76293da0eb15b3089c64",
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
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
react_fe                    latest    c320273135f5   7 weeks ago     377MB
bradsimpson213/test_react   latest    93489609ef4b   7 weeks ago     377MB
ubuntu                      latest    27941809078c   2 months ago    77.8MB
postgres                    latest    5b21e2e86aab   2 months ago    376MB
nginx                       latest    0e901e68141f   2 months ago    142MB
alpine                      latest    e66264b98777   2 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    d1165f221234   17 months ago   13.3kB
bradsimpson@ ~:docker image inspect alpine
[
    {
        "Id": "sha256:e66264b98777e12192600bf9b4d663655c98a090072e1bab49e233d7531d1294",
        "RepoTags": [
            "alpine:latest"
        ],
        "RepoDigests": [
            "alpine@sha256:686d8c9dfa6f3ccfc8230bc3178d23f84eeaf7e457f36f271ab1acc53015037c"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2022-05-23T19:19:31.970967174Z",
        "Container": "49320ab4701345c613d266d2b3cf2ff0265c553d463f9061e479b6c8ef839a1f",
        "ContainerConfig": {
            "Hostname": "49320ab47013",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/bin/sh\"]"
            ],
            "Image": "sha256:f9ee3a3800e8eec1d8d7fb76906dd5859498b12d27a0258b3df35bca9fa8a867",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
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
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh"
            ],
            "Image": "sha256:f9ee3a3800e8eec1d8d7fb76906dd5859498b12d27a0258b3df35bca9fa8a867",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 5529096,
        "VirtualSize": 5529096,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/3f1c8d74fe34fa48885ff511520a5e51ccf48761b02fea56d929b5dc00893e7c/merged",
                "UpperDir": "/var/lib/docker/overlay2/3f1c8d74fe34fa48885ff511520a5e51ccf48761b02fea56d929b5dc00893e7c/diff",
                "WorkDir": "/var/lib/docker/overlay2/3f1c8d74fe34fa48885ff511520a5e51ccf48761b02fea56d929b5dc00893e7c/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:24302eb7d9085da80f016e7e4ae55417e412fb7e0a8021e95e3b60c67cde557d"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
b73b88a4b911   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   condescending_lamport
bradsimpson@ ~:docker container stop b73b88a4b911
b73b88a4b911
bradsimpson@ ~:\clear


bradsimpson@ ~:docker container run --mount type=bind,source=absolute/path/to/a/folder\ ,target=absolute/path/to/container
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ ~:docker container run --mount type=volume,source=my_volume,target=absolute/path/to/container
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker volume create my_new_volume
my_new_volume
bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
react_fe                    latest    c320273135f5   7 weeks ago     377MB
bradsimpson213/test_react   latest    93489609ef4b   7 weeks ago     377MB
ubuntu                      latest    27941809078c   2 months ago    77.8MB
postgres                    latest    5b21e2e86aab   2 months ago    376MB
nginx                       latest    0e901e68141f   2 months ago    142MB
alpine                      latest    e66264b98777   2 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    d1165f221234   17 months ago   13.3kB
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
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:cd..
-bash: cd..: command not found
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container run -d --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8080:80 nginx:alpine
754b41adacbd463c8934edbe9183f9c18fc0562ccf488427a2db3a86eee86ca4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
754b41adacbd   nginx:alpine   "/docker-entrypoint.…"   9 seconds ago    Up 7 seconds    0.0.0.0:8080->80/tcp, :::8080->80/tcp   serene_ellis
33e7e58635ea   nginx:alpine   "/docker-entrypoint.…"   56 minutes ago   Up 56 minutes   80/tcp                                  c4
8664cd67f608   nginx:alpine   "/docker-entrypoint.…"   56 minutes ago   Up 56 minutes   80/tcp                                  c3
0effca0c9c1f   nginx:alpine   "/docker-entrypoint.…"   56 minutes ago   Up 56 minutes   80/tcp                                  c2
107017b63f19   nginx:alpine   "/docker-entrypoint.…"   57 minutes ago   Up 57 minutes   80/tcp                                  c1
bradsimpson@ ~:docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
754b41adacbd   nginx:alpine   "/docker-entrypoint.…"   37 seconds ago   Up 35 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   serene_ellis
bradsimpson@ ~:cd app
bradsimpson@ app:\ls
index.html
bradsimpson@ app:nano index.html
bradsimpson@ app:cd ..
bradsimpson@ ~:docker container exec -it serene_ellis ash
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
GeoIP            ca-certificates  licenses         misc             udhcpc
apk              doc              man              nginx            zoneinfo
/usr/share # cd nginx
/usr/share/nginx # \ls
html
/usr/share/nginx # cd html
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index/html
ash: nano: not found
/usr/share/nginx/html # apk install nano
ERROR: 'install' is not an apk command. See 'apk --help'.
/usr/share/nginx/html # apk nano
ERROR: 'nano' is not an apk command. See 'apk --help'.
/usr/share/nginx/html # apk --help
apk-tools 2.12.7, compiled for x86_64.

usage: apk [<OPTIONS>...] COMMAND [<ARGUMENTS>...]

Package installation and removal:
  add        Add packages to WORLD and commit changes
  del        Remove packages from WORLD and commit changes

System maintenance:
  fix        Fix, reinstall or upgrade packages without modifying WORLD
  update     Update repository indexes
  upgrade    Install upgrades available from repositories
  cache      Manage the local package cache

Querying package information:
  info       Give detailed information about packages or repositories
  list       List packages matching a pattern or other criteria
  dot        Render dependencies as graphviz graphs
  policy     Show repository policy for packages
  search     Search for packages by name or description

Repository maintenance:
  index      Create repository index file from packages
  fetch      Download packages from global repositories to a local directory
  manifest   Show checksums of package contents
  verify     Verify package integrity and signature

Miscellaneous:
  audit      Audit system for changes
  stats      Show statistics about repositories and installations
  version    Compare package versions or perform tests on version strings

This apk has coffee making abilities.
For more information: man 8 apk
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.15/community/x86_64/APKINDEX.tar.gz
(1/1) Installing nano (5.9-r0)
Executing busybox-1.34.1-r5.trigger
OK: 26 MiB in 43 packages
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgres1 -d --mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres  
6a7cd3d20ec109ede19728391023319c886246abb8c76e081a6b671485d491f9
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
6a7cd3d20ec1   postgres       "docker-entrypoint.s…"   6 seconds ago    Up 4 seconds    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres1
754b41adacbd   nginx:alpine   "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       serene_ellis
bradsimpson@ ~:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 14.3 (Debian 14.3-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
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

postgres=# \c test_db
psql (13.2, server 14.3 (Debian 14.3-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
You are now connected to database "test_db" as user "postgres".
test_db=# \dn
  List of schemas
  Name  |  Owner   
--------+----------
 public | postgres
(1 row)

test_db=# \d
              List of relations
 Schema |     Name      |   Type   |  Owner   
--------+---------------+----------+----------
 public | people        | table    | postgres
 public | people_id_seq | sequence | postgres
(2 rows)

test_db=# CREATE TABLE jokes(id SERIAL PRIMARY KEY, joke_body VARCHAR(250));
CREATE TABLE
test_db=# \d
              List of relations
 Schema |     Name      |   Type   |  Owner   
--------+---------------+----------+----------
 public | jokes         | table    | postgres
 public | jokes_id_seq  | sequence | postgres
 public | people        | table    | postgres
 public | people_id_seq | sequence | postgres
(4 rows)

test_db=# exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
6a7cd3d20ec1   postgres       "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres1
754b41adacbd   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       serene_ellis
bradsimpson@ ~:docker container stop postgres1
postgres1
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                   NAMES
754b41adacbd   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   serene_ellis
bradsimpson@ ~:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name postgres2 -d --mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres  
d5811e9e2172660f9719a86a79e2426507922caeab424effc412ed7356610342
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
d5811e9e2172   postgres       "docker-entrypoint.s…"   5 seconds ago    Up 4 seconds    0.0.0.0:5431->5432/tcp, :::5431->5432/tcp   postgres2
754b41adacbd   nginx:alpine   "/docker-entrypoint.…"   18 minutes ago   Up 18 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp       serene_ellis
bradsimpson@ ~:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 14.3 (Debian 14.3-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
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

postgres=# \c test_db
psql (13.2, server 14.3 (Debian 14.3-1.pgdg110+1))
WARNING: psql major version 13, server major version 14.
         Some psql features might not work.
You are now connected to database "test_db" as user "postgres".
test_db=# \d
              List of relations
 Schema |     Name      |   Type   |  Owner   
--------+---------------+----------+----------
 public | jokes         | table    | postgres
 public | jokes_id_seq  | sequence | postgres
 public | people        | table    | postgres
 public | people_id_seq | sequence | postgres
(4 rows)

test_db=# exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     my_new_volume
local     my_volume
local     my_volume2
local     postgres-data
bradsimpson@ ~:docker volume inspect postgres-data
[
    {
        "CreatedAt": "2022-08-16T18:03:51Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/postgres-data/_data",
        "Name": "postgres-data",
        "Options": {},
        "Scope": "local"
    }
]
bradsimpson@ ~:


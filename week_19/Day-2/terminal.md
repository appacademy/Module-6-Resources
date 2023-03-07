Last login: Tue Mar  7 10:00:12 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:\clear























bradsimpson@ ~:docker image ls
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
bradsimpson@ ~:docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@ ~:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
postgres                           latest    a26eb6069868   2 months ago    379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
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

bradsimpson@ ~:\clear

bradsimpson@ ~:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
postgres                           latest    a26eb6069868   2 months ago    379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS     NAMES
7ec09228258c   hello-world                        "/hello"                 26 minutes ago   Exited (0) 26 minutes ago             gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago               flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                optimistic_beaver
bradsimpson@ ~:docker container run [options flags] nginx [commands] [args]
docker: invalid reference format.
See 'docker run --help'.
bradsimpson@ ~:docker container run --name my_nginx_container -p 8000:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/03/07 16:36:37 [notice] 1#1: using the "epoll" event method
2023/03/07 16:36:37 [notice] 1#1: nginx/1.21.6
2023/03/07 16:36:37 [notice] 1#1: built by gcc 10.2.1 20210110 (Debian 10.2.1-6) 
2023/03/07 16:36:37 [notice] 1#1: OS: Linux 5.15.49-linuxkit
2023/03/07 16:36:37 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/03/07 16:36:37 [notice] 1#1: start worker processes
2023/03/07 16:36:37 [notice] 1#1: start worker process 31
2023/03/07 16:36:37 [notice] 1#1: start worker process 32
172.17.0.1 - - [07/Mar/2023:16:37:05 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"
2023/03/07 16:37:06 [error] 31#31: *2 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
172.17.0.1 - - [07/Mar/2023:16:37:06 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [07/Mar/2023:16:37:38 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"
^C2023/03/07 16:38:00 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/03/07 16:38:00 [notice] 31#31: exiting
2023/03/07 16:38:00 [notice] 31#31: exit
2023/03/07 16:38:00 [notice] 32#32: exiting
2023/03/07 16:38:00 [notice] 32#32: exit
2023/03/07 16:38:00 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/03/07 16:38:00 [notice] 1#1: worker process 32 exited with code 0
2023/03/07 16:38:00 [notice] 1#1: signal 29 (SIGIO) received
2023/03/07 16:38:00 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/03/07 16:38:00 [notice] 1#1: worker process 31 exited with code 0
2023/03/07 16:38:00 [notice] 1#1: exit
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED              STATUS                      PORTS     NAMES
b18d4f541223   nginx                              "/docker-entrypoint.…"   About a minute ago   Exited (0) 31 seconds ago             my_nginx_container
7ec09228258c   hello-world                        "/hello"                 34 minutes ago       Exited (0) 34 minutes ago             gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago         Exited (0) 20 hours ago               flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago          Exited (1) 3 weeks ago                optimistic_beaver
bradsimpson@ ~:docker container run -d -p 6000:80 nginx
150b81a0b58b8239c1176a06d67910bdaeafeb17cd7b3e4282c57c6b4d932e61
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
150b81a0b58b   nginx     "/docker-entrypoint.…"   29 seconds ago   Up 27 seconds   0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container run --rm alpine ash
bradsimpson@ ~:docker container run --rm alpine sh
bradsimpson@ ~:docker container run --rm alpine echo "hey there!"
-bash: !": event not found
bradsimpson@ ~:docker container run --rm alpine sh
bradsimpson@ ~:docker container run --rm -it alpine sh
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
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
150b81a0b58b   nginx     "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                  NAMES
150b81a0b58b   nginx                              "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:6000->80/tcp   sleepy_hertz
b18d4f541223   nginx                              "/docker-entrypoint.…"   10 minutes ago   Exited (0) 8 minutes ago                           my_nginx_container
7ec09228258c   hello-world                        "/hello"                 42 minutes ago   Exited (0) 42 minutes ago                          gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                            flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                             optimistic_beaver
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8080:80 nginx
f7b7ce1714a0bd38986dbafde648b80ff37677724f6d4a049ef86a83485392fb
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f7b7ce1714a0   nginx     "/docker-entrypoint.…"   11 seconds ago   Up 10 seconds   0.0.0.0:8080->80/tcp   serene_antonelli
150b81a0b58b   nginx     "/docker-entrypoint.…"   8 minutes ago    Up 8 minutes    0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container run -it --name test alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@ ~:docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                          PORTS                  NAMES
45e5c21663a4   alpine                             "sh"                     2 minutes ago    Exited (0) About a minute ago                          test
f7b7ce1714a0   nginx                              "/docker-entrypoint.…"   3 minutes ago    Up 3 minutes                    0.0.0.0:8080->80/tcp   serene_antonelli
150b81a0b58b   nginx                              "/docker-entrypoint.…"   12 minutes ago   Up 12 minutes                   0.0.0.0:6000->80/tcp   sleepy_hertz
b18d4f541223   nginx                              "/docker-entrypoint.…"   16 minutes ago   Exited (0) 14 minutes ago                              my_nginx_container
7ec09228258c   hello-world                        "/hello"                 49 minutes ago   Exited (0) 49 minutes ago                              gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                                flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                                 optimistic_beaver
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f7b7ce1714a0   nginx     "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:8080->80/tcp   serene_antonelli
150b81a0b58b   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS                  NAMES
45e5c21663a4   alpine                             "sh"                     3 minutes ago    Exited (0) 2 minutes ago                           test
f7b7ce1714a0   nginx                              "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:8080->80/tcp   serene_antonelli
150b81a0b58b   nginx                              "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes               0.0.0.0:6000->80/tcp   sleepy_hertz
b18d4f541223   nginx                              "/docker-entrypoint.…"   17 minutes ago   Exited (0) 15 minutes ago                          my_nginx_container
7ec09228258c   hello-world                        "/hello"                 50 minutes ago   Exited (0) 50 minutes ago                          gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                            flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                             optimistic_beaver
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
f7b7ce1714a0   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8080->80/tcp   serene_antonelli
150b81a0b58b   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container stop serene_antonelli
serene_antonelli
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
150b81a0b58b   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container stop 150b81a0b58b
150b81a0b58b
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                          PORTS     NAMES
45e5c21663a4   alpine                             "sh"                     5 minutes ago    Exited (0) 4 minutes ago                  test
f7b7ce1714a0   nginx                              "/docker-entrypoint.…"   6 minutes ago    Exited (0) About a minute ago             serene_antonelli
150b81a0b58b   nginx                              "/docker-entrypoint.…"   15 minutes ago   Exited (0) 31 seconds ago                 sleepy_hertz
b18d4f541223   nginx                              "/docker-entrypoint.…"   19 minutes ago   Exited (0) 17 minutes ago                 my_nginx_container
7ec09228258c   hello-world                        "/hello"                 52 minutes ago   Exited (0) 52 minutes ago                 gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                   flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                    optimistic_beaver
bradsimpson@ ~:docker container start serene_antonelli sleepy_hertz
serene_antonelli
sleepy_hertz
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
f7b7ce1714a0   nginx     "/docker-entrypoint.…"   7 minutes ago    Up 4 seconds   0.0.0.0:8080->80/tcp   serene_antonelli
150b81a0b58b   nginx     "/docker-entrypoint.…"   16 minutes ago   Up 3 seconds   0.0.0.0:6000->80/tcp   sleepy_hertz
bradsimpson@ ~:docker container stop serene_antonelli sleepy_hertz
serene_antonelli
sleepy_hertz
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                      PORTS     NAMES
45e5c21663a4   alpine                             "sh"                     7 minutes ago    Exited (0) 6 minutes ago              test
f7b7ce1714a0   nginx                              "/docker-entrypoint.…"   8 minutes ago    Exited (0) 57 seconds ago             serene_antonelli
150b81a0b58b   nginx                              "/docker-entrypoint.…"   17 minutes ago   Exited (0) 57 seconds ago             sleepy_hertz
b18d4f541223   nginx                              "/docker-entrypoint.…"   21 minutes ago   Exited (0) 19 minutes ago             my_nginx_container
7ec09228258c   hello-world                        "/hello"                 54 minutes ago   Exited (0) 54 minutes ago             gifted_gagarin
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago               flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                optimistic_beaver
bradsimpson@ ~:docker container rm 7ec09228258c
7ec09228258c
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED          STATUS                          PORTS     NAMES
45e5c21663a4   alpine                             "sh"                     7 minutes ago    Exited (0) 7 minutes ago                  test
f7b7ce1714a0   nginx                              "/docker-entrypoint.…"   8 minutes ago    Exited (0) About a minute ago             serene_antonelli
150b81a0b58b   nginx                              "/docker-entrypoint.…"   17 minutes ago   Exited (0) About a minute ago             sleepy_hertz
b18d4f541223   nginx                              "/docker-entrypoint.…"   21 minutes ago   Exited (0) 20 minutes ago                 my_nginx_container
1aa3f33b014b   hello-world                        "/hello"                 20 hours ago     Exited (0) 20 hours ago                   flamboyant_brattain
6343c7b450eb   bradsimpson213/amazing_react_app   "docker-entrypoint.s…"   3 weeks ago      Exited (1) 3 weeks ago                    optimistic_beaver
bradsimpson@ ~:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
45e5c21663a4a9cd917e3ffdbf039e2f0d7414df92528bb53ef780c9c52b2e8d
f7b7ce1714a0bd38986dbafde648b80ff37677724f6d4a049ef86a83485392fb
150b81a0b58b8239c1176a06d67910bdaeafeb17cd7b3e4282c57c6b4d932e61
b18d4f5412235f43ea54465324aa8ce60f44e19a5857fa699044b233d9de96ee
1aa3f33b014b72a6c713eb590f6c3cde5542e6bca8b315b5fea37b7b849f9e24
6343c7b450ebda60b2851472bb5a554d04cb958cf3d10a554d425b60eda69eff

Total reclaimed space: 48.01MB
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:\clear

bradsimpson@ ~:docker container run -d -p 8000:80 nginx
b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
b0e931f118f0   nginx     "/docker-entrypoint.…"   6 seconds ago   Up 4 seconds   0.0.0.0:8000->80/tcp   nervous_chaum
bradsimpson@ ~:docker container exec -it nervous_chaum sh
# \ls
bin   docker-entrypoint.d   home   media  proc	sbin  tmp
boot  docker-entrypoint.sh  lib    mnt	  root	srv   usr
dev   etc		    lib64  opt	  run	sys   var
# cd bin
# \ls
bash   df	      findmnt	lsblk	       pidof	  sleep     uname	  zfgrep
cat    dir	      grep	mkdir	       pwd	  stty	    uncompress	  zforce
chgrp  dmesg	      gunzip	mknod	       rbash	  su	    vdir	  zgrep
chmod  dnsdomainname  gzexe	mktemp	       readlink   sync	    wdctl	  zless
chown  domainname     gzip	more	       rm	  tar	    ypdomainname  zmore
cp     echo	      hostname	mount	       rmdir	  tempfile  zcat	  znew
dash   egrep	      ln	mountpoint     run-parts  touch     zcmp
date   false	      login	mv	       sed	  true	    zdiff
dd     fgrep	      ls	nisdomainname  sh	  umount    zegrep
# exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                  NAMES
b0e931f118f0   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8000->80/tcp   nervous_chaum
bradsimpson@ ~:docker container inspect nervous_chaum
[
    {
        "Id": "b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0",
        "Created": "2023-03-07T16:59:57.861326363Z",
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
            "Pid": 3473,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-03-07T16:59:58.791987116Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/hostname",
        "HostsPath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/hosts",
        "LogPath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0-json.log",
        "Name": "/nervous_chaum",
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
                "LowerDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e/merged",
                "UpperDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e/diff",
                "WorkDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b0e931f118f0",
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
            "SandboxID": "21e383adfaf1983a441763de95d986519a9a0ae9b55e5e34b99ff2b382ef920b",
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
            "SandboxKey": "/var/run/docker/netns/21e383adfaf1",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "0de2fb3338553ff1e59443f29758faea8c4b123505059e544f0a24d2b48112d9",
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
                    "NetworkID": "955c07b2055cabbca32e86b04195bc30f43fca1346d0dc860d43c0f0f2ac3105",
                    "EndpointID": "0de2fb3338553ff1e59443f29758faea8c4b123505059e544f0a24d2b48112d9",
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
bradsimpson@ ~:docker image inspect postgres
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
bradsimpson@ ~:



# Networking


bradsimpson@ ~:docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
955c07b2055c   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
ef43db5a14d2   my_network2    bridge    local
475754f27665   none           null      local
6000c9f47f19   taco_tuesday   bridge    local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
b0e931f118f0   nginx     "/docker-entrypoint.…"   29 minutes ago   Up 29 minutes   0.0.0.0:8000->80/tcp   nervous_chaum
bradsimpson@ ~:docker container inspect nervous_chaum
[
    {
        "Id": "b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0",
        "Created": "2023-03-07T16:59:57.861326363Z",
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
            "Pid": 3473,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-03-07T16:59:58.791987116Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0e901e68141fd02f237cf63eb842529f8a9500636a9419e3cf4fb986b8fe3d5d",
        "ResolvConfPath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/hostname",
        "HostsPath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/hosts",
        "LogPath": "/var/lib/docker/containers/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0/b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0-json.log",
        "Name": "/nervous_chaum",
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
                "LowerDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e-init/diff:/var/lib/docker/overlay2/3d4ad793b7c68679eb6fad6c18d3070dcd03ddd66327d33e14be8cf0466ceebb/diff:/var/lib/docker/overlay2/5e658b0521ccd6b7830ac4383470d8e91386454e7a6ad78a47cfd4cdd2b71c8f/diff:/var/lib/docker/overlay2/1393f8320b692fd474b2c07b70302a952e0c26485d478f6910d299d2d017d393/diff:/var/lib/docker/overlay2/189c71c9f609d85d6b0dfe1f3b20611c8baf9f488ca2a13bd74ec05a81f25e59/diff:/var/lib/docker/overlay2/5d797d4e2b754c3f0844351cf685c69c64c2d07d5bb386a17dd366c0657a1eb3/diff:/var/lib/docker/overlay2/9446d4d3347634d14e195b4906d0f9225e4b55550334c31e7d887bb39390df2b/diff",
                "MergedDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e/merged",
                "UpperDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e/diff",
                "WorkDir": "/var/lib/docker/overlay2/ae3c9007fdd1925e903be7a89cdb193559885ebe4bf933ed1a5ea605a607615e/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "b0e931f118f0",
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
            "SandboxID": "21e383adfaf1983a441763de95d986519a9a0ae9b55e5e34b99ff2b382ef920b",
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
            "SandboxKey": "/var/run/docker/netns/21e383adfaf1",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "0de2fb3338553ff1e59443f29758faea8c4b123505059e544f0a24d2b48112d9",
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
                    "NetworkID": "955c07b2055cabbca32e86b04195bc30f43fca1346d0dc860d43c0f0f2ac3105",
                    "EndpointID": "0de2fb3338553ff1e59443f29758faea8c4b123505059e544f0a24d2b48112d9",
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
955c07b2055c   bridge         bridge    local
7318efe60d0f   host           host      local
1a584f63c88c   my_network     bridge    local
ef43db5a14d2   my_network2    bridge    local
475754f27665   none           null      local
6000c9f47f19   taco_tuesday   bridge    local
bradsimpson@ ~:\clear

bradsimpson@ ~:docker network create even_more_taco_tuesday
2af1b34de9a0e3b7f1bf96c6ab3dd06d96557307ac45404b5a2e3fb8415d8823
bradsimpson@ ~:docker network ls
NETWORK ID     NAME                     DRIVER    SCOPE
955c07b2055c   bridge                   bridge    local
2af1b34de9a0   even_more_taco_tuesday   bridge    local
7318efe60d0f   host                     host      local
1a584f63c88c   my_network               bridge    local
ef43db5a14d2   my_network2              bridge    local
475754f27665   none                     null      local
6000c9f47f19   taco_tuesday             bridge    local
bradsimpson@ ~:docker network rm my_network2       
my_network2
bradsimpson@ ~:docker network ls
NETWORK ID     NAME                     DRIVER    SCOPE
955c07b2055c   bridge                   bridge    local
2af1b34de9a0   even_more_taco_tuesday   bridge    local
7318efe60d0f   host                     host      local
1a584f63c88c   my_network               bridge    local
475754f27665   none                     null      local
6000c9f47f19   taco_tuesday             bridge    local
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
b0e931f118f0   nginx     "/docker-entrypoint.…"   34 minutes ago   Up 34 minutes   0.0.0.0:8000->80/tcp   nervous_chaum
bradsimpson@ ~:docker container stop nervous_chaum
nervous_chaum
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ ~:docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
b0e931f118f0   nginx     "/docker-entrypoint.…"   34 minutes ago   Exited (0) 9 seconds ago             nervous_chaum
bradsimpson@ ~:docker container run -d --name c1 --network even_more_taco_tuesday nginx:alpine 
Unable to find image 'nginx:alpine' locally
alpine: Pulling from library/nginx
63b65145d645: Pull complete 
8c7e1fd96380: Pull complete 
86c5246c96db: Pull complete 
b874033c43fb: Pull complete 
dbe1551bd73f: Pull complete 
0d4f6b3f3de6: Pull complete 
2a41f256c40f: Pull complete 
Digest: sha256:207332a7d1d17b884b5a0e94bcf7c0f67f1a518b9bf8da6c2ea72c83eec889b8
Status: Downloaded newer image for nginx:alpine
f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90
bradsimpson@ ~:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
nginx                              alpine    2bc7edbc3cf2   3 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
postgres                           latest    a26eb6069868   2 months ago    379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
f7d70c521849   nginx:alpine   "/docker-entrypoint.…"   29 seconds ago   Up 25 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c2 --network even_more_taco_tuesday nginx:alpine 
1afb8a22a10df002a53c8bf8613eac618e09711e8c5217bd6b3dcd9354f51dab
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
1afb8a22a10d   nginx:alpine   "/docker-entrypoint.…"   15 seconds ago   Up 13 seconds   80/tcp    c2
f7d70c521849   nginx:alpine   "/docker-entrypoint.…"   55 seconds ago   Up 51 seconds   80/tcp    c1
bradsimpson@ ~:docker container run -d --name c3 nginx:alpine 
c4abceb863faf31b04113666056aece78c0b769dc3ec635ff153f7b1a487f22e
bradsimpson@ ~:docker container run -d --name c4 nginx:alpine 
ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
ad8aa412f18b   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago        Up 4 seconds        80/tcp    c4
c4abceb863fa   nginx:alpine   "/docker-entrypoint.…"   16 seconds ago       Up 14 seconds       80/tcp    c3
1afb8a22a10d   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
f7d70c521849   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@ ~:docker container inspect c1
[
    {
        "Id": "f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90",
        "Created": "2023-03-07T17:37:29.757987366Z",
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
            "Pid": 3784,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-03-07T17:37:32.460620745Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90/hostname",
        "HostsPath": "/var/lib/docker/containers/f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90/hosts",
        "LogPath": "/var/lib/docker/containers/f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90/f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90-json.log",
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
            "NetworkMode": "even_more_taco_tuesday",
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
                "LowerDir": "/var/lib/docker/overlay2/08593129de4b6523b3e4a7677dff77cea45c1a238b445ff045f3faaa062146e5-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/08593129de4b6523b3e4a7677dff77cea45c1a238b445ff045f3faaa062146e5/merged",
                "UpperDir": "/var/lib/docker/overlay2/08593129de4b6523b3e4a7677dff77cea45c1a238b445ff045f3faaa062146e5/diff",
                "WorkDir": "/var/lib/docker/overlay2/08593129de4b6523b3e4a7677dff77cea45c1a238b445ff045f3faaa062146e5/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "f7d70c521849",
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
            "SandboxID": "9131f25e4289bf9cce4013a04bb299909eacebcad558b44ba07e6a9db2573c19",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/9131f25e4289",
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
                "even_more_taco_tuesday": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "f7d70c521849"
                    ],
                    "NetworkID": "2af1b34de9a0e3b7f1bf96c6ab3dd06d96557307ac45404b5a2e3fb8415d8823",
                    "EndpointID": "e6884505b53b506b8af1cabf97fa4c9aa0587212da1c2ab5aa5b18e3d2403d38",
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
bradsimpson@ ~:docker container inspect c4
[
    {
        "Id": "ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386",
        "Created": "2023-03-07T17:39:05.501343727Z",
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
            "Pid": 4131,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-03-07T17:39:06.629880102Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2bc7edbc3cf2fce630a95d0586c48cd248e5df37df5b1244728a5c8c91becfe0",
        "ResolvConfPath": "/var/lib/docker/containers/ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386/hostname",
        "HostsPath": "/var/lib/docker/containers/ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386/hosts",
        "LogPath": "/var/lib/docker/containers/ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386/ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386-json.log",
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
                "LowerDir": "/var/lib/docker/overlay2/c4bb885250b4a62cb7179124d104ad31962cb9369c82e6732782c034300d707f-init/diff:/var/lib/docker/overlay2/658ee9ed262f80e08befddb9868d56b8eda02cb2798f3aadb02860668bb9bb05/diff:/var/lib/docker/overlay2/0766e1afc66834bc7b41fc13f4b585ddfd43c1e89d514b00257b8610a3a9212b/diff:/var/lib/docker/overlay2/88e81e6c85649d8d285f4da6085744f25e36ca05fe746f30c8f57cd5f2d1a5ba/diff:/var/lib/docker/overlay2/86921ac03c21c2fba4efa31456e64d0408c2f49c730f326635b6e603de1ba67c/diff:/var/lib/docker/overlay2/01e11ead3e9e95398b26c355234dbcca95e841a4d6a35dd6a1fb07918beacd5f/diff:/var/lib/docker/overlay2/abd761f9c8dd9021eed9c25ae08a406e70e7c45f7b4c724adc8a1059def28743/diff:/var/lib/docker/overlay2/e8e8671fe4d5a21bcf00a87568303a3f75ed638da04510d98f160b27186d2257/diff",
                "MergedDir": "/var/lib/docker/overlay2/c4bb885250b4a62cb7179124d104ad31962cb9369c82e6732782c034300d707f/merged",
                "UpperDir": "/var/lib/docker/overlay2/c4bb885250b4a62cb7179124d104ad31962cb9369c82e6732782c034300d707f/diff",
                "WorkDir": "/var/lib/docker/overlay2/c4bb885250b4a62cb7179124d104ad31962cb9369c82e6732782c034300d707f/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "ad8aa412f18b",
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
            "SandboxID": "e916df4b9c8125627acdd07433268bd4d3d91311fee19057f6b6dd7cec928b89",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/e916df4b9c81",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "f0512f069a1f4fbd57bf3dc35f8e9dd79be87c517b8c2098b9b9df62252ae3c8",
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
                    "NetworkID": "955c07b2055cabbca32e86b04195bc30f43fca1346d0dc860d43c0f0f2ac3105",
                    "EndpointID": "f0512f069a1f4fbd57bf3dc35f8e9dd79be87c517b8c2098b9b9df62252ae3c8",
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

bradsimpson@ ~:docker container exec -it c1 ash
/ # ping -c 3 c2
PING c2 (172.20.0.3): 56 data bytes
64 bytes from 172.20.0.3: seq=0 ttl=64 time=2.864 ms
64 bytes from 172.20.0.3: seq=1 ttl=64 time=0.169 ms
64 bytes from 172.20.0.3: seq=2 ttl=64 time=0.108 ms

--- c2 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.108/1.047/2.864 ms
/ # ping -c 3 c3
ping: bad address 'c3'
/ # ping -c 3 c4
ping: bad address 'c4'
/ # exit
bradsimpson@ ~:docker container exec -it c3 ash
/ # ping -c 3 c4
ping: bad address 'c4'
/ # ping -c 3 c1
ping: bad address 'c1'
/ # ping -c 3 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=8.157 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.088 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.076 ms

--- 172.17.0.3 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.076/2.773/8.157 ms
/ # exit
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
ad8aa412f18b   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c4
c4abceb863fa   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c3
1afb8a22a10d   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c2
f7d70c521849   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   80/tcp    c1
bradsimpson@ ~:\clear





bradsimpson@ ~:docker volume ls
DRIVER    VOLUME NAME
local     new_test_volume
local     taco_tuesday
bradsimpson@ ~:


# BIND MOUNTS & VOLUMES

Last login: Tue Mar  7 13:10:39 on ttys005

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker container run -d --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8000:80 nginx:alpine
3138446d3c12561b9ff082d670a92780ebd9533205131e72fd8bd30df5719aa6
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
3138446d3c12   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 4 seconds    0.0.0.0:8000->80/tcp   intelligent_grothendieck
f7d70c521849   nginx:alpine   "/docker-entrypoint.…"   56 minutes ago   Up 56 minutes   80/tcp                 c1
bradsimpson@ ~:docker container stop c1
c1
bradsimpson@ ~:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
3138446d3c12   nginx:alpine   "/docker-entrypoint.…"   18 seconds ago   Up 16 seconds   0.0.0.0:8000->80/tcp   intelligent_grothendieck
bradsimpson@ ~:docker container exec -it intelligent_grothendieck ash
/ # \ls
bin                   home                  proc                  sys
dev                   lib                   root                  tmp
docker-entrypoint.d   media                 run                   usr
docker-entrypoint.sh  mnt                   sbin                  var
etc                   opt                   srv
/ # cd usr
/usr # cd share
/usr/share # cd nginx
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
index.html
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
bradsimpson@ ~:cd app/
bradsimpson@ app:nano index.html 
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
3138446d3c12   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   0.0.0.0:8000->80/tcp   intelligent_grothendieck
bradsimpson@ app:docker container stop intelligent_grothendieck

intelligent_grothendieck
bradsimpson@ app:
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS     NAMES
3138446d3c12   nginx:alpine   "/docker-entrypoint.…"   5 minutes ago       Exited (0) 12 seconds ago                intelligent_grothendieck
ad8aa412f18b   nginx:alpine   "/docker-entrypoint.…"   59 minutes ago      Exited (0) 12 minutes ago                c4
c4abceb863fa   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 12 minutes ago                c3
1afb8a22a10d   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 12 minutes ago                c2
f7d70c521849   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (0) 5 minutes ago                 c1
b0e931f118f0   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago             nervous_chaum
bradsimpson@ app:docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
3138446d3c12561b9ff082d670a92780ebd9533205131e72fd8bd30df5719aa6
ad8aa412f18b52c47f813afa4bcdc818f21ca90d67f5eab679a1c7ff966d4386
c4abceb863faf31b04113666056aece78c0b769dc3ec635ff153f7b1a487f22e
1afb8a22a10df002a53c8bf8613eac618e09711e8c5217bd6b3dcd9354f51dab
f7d70c5218491875510d4a91ebe70dcf278edfe4aca195ec83783cd972076d90
b0e931f118f08cea258338fb35a803e438e423cbbaa173ba1ba0ebb5663092e0

Total reclaimed space: 3.046MB
bradsimpson@ app:\clear

bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
nginx                              alpine    2bc7edbc3cf2   3 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
postgres                           latest    a26eb6069868   2 months ago    379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
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

bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
nginx                              alpine    2bc7edbc3cf2   3 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
postgres                           latest    a26eb6069868   2 months ago    379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
bradsimpson@ app:docker image remove postgres
Untagged: postgres:latest
Untagged: postgres@sha256:f4cd32e7a418d9c9ba043e7d561243388202b654c740bcc85ca40b41d9fb4f1e
Deleted: sha256:a26eb6069868e4bfd0095788e541bb40711861bdfb2a8252103dea85cc0758aa
Deleted: sha256:73b81b35fa573e4f729e9a26a5d2ccab4c3ed6a1ed4f5464ca4883508e485b1c
Deleted: sha256:1caae16dd573e3c0759130b66b1e964aa5e78d1026d3e95469dfca3ffd50cb6a
Deleted: sha256:63a54560258d47025565ff7dcc4823b9890b62b01f425776b717359016901144
Deleted: sha256:b9a8015ddecae124ae95b200e2e8c1605a00e829259a43ef30ae3b6e93d8d086
Deleted: sha256:56ffd917f37fa0598af1adf1f4e0eac9b79bd78616e576afa181f60c230e6eca
Deleted: sha256:1a24afe05d08074ffd6f36e0d90c076c8af14c63a214373f0114cdd61004f0ff
Deleted: sha256:6db0369dd7f2e693cffaec685407266b7998da11745ee72e5fb463664a1d92c7
Deleted: sha256:a2445eb333edd04d417c6ad63bf0f8d56bf8371d9960e98dbbaf89039f57f1ef
Deleted: sha256:0eb1216f2e75f61441f2b8d700eb052c504f41ba81df7693a0aa21ece24c5434
Deleted: sha256:d91c9dc760d6c79827a3226617838e009a809cda0907711287ac43f25c3c2113
Deleted: sha256:986c1576e81d258abaac31a9dd0a05a62b3b1df42b7518f6a85d8d5656514e14
Deleted: sha256:8bf15f159b4ff03bafec40993ea940fdb497ac5b99f827fee2800dae57161fe8
Deleted: sha256:8a70d251b65364698f195f5a0b424e0d67de81307b79afbe662abd797068a069
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
nginx                              alpine    2bc7edbc3cf2   3 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
bradsimpson@ app:docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
3f9582a2cbe7: Pull complete 
0d9d08fc1a1a: Pull complete 
ecae4ccb4d1b: Pull complete 
e75693e0d7a5: Pull complete 
1b6d5aead1a8: Pull complete 
f2aa67d9a6b2: Pull complete 
7a3ec0371e36: Pull complete 
704d9d1b662d: Pull complete 
a6e09efc43e8: Pull complete 
cb87a0a6528d: Pull complete 
3e290cb732cd: Pull complete 
d44d65eaede3: Pull complete 
0c2430d596bb: Pull complete 
Digest: sha256:50a96a21f2992518c2cb4601467cf27c7ac852542d8913c1872fe45cd6449947
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@ app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
postgres                           latest    3b6645d2c145   6 days ago      379MB
nginx                              alpine    2bc7edbc3cf2   3 weeks ago     40.7MB
bradsimpson213/amazing_react_app   latest    1a8a2fa95b0a   3 weeks ago     576MB
bradsimpson213/revisited_react     latest    303fa668755c   7 weeks ago     568MB
bradsimpson213/my_project          latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/react_project       latest    ae74e957ba0d   7 weeks ago     568MB
my_project                         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/new_project           latest    ae74e957ba0d   7 weeks ago     568MB
bradsimps213/react_project         latest    ae74e957ba0d   7 weeks ago     568MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   4 months ago    560MB
bradsimpson213/test_app2           <none>    8edeca523aef   5 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   6 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   8 months ago    377MB
ubuntu                             latest    27941809078c   9 months ago    77.8MB
nginx                              latest    0e901e68141f   9 months ago    142MB
alpine                             latest    e66264b98777   9 months ago    5.53MB
hello-world                        latest    feb5d9fea6a5   17 months ago   13.3kB
bradsimpson@ app:\clear

bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     new_test_volume
local     taco_tuesday
bradsimpson@ app:docker volume create more_tacos_please
more_tacos_please
bradsimpson@ app:docker volume ls
DRIVER    VOLUME NAME
local     more_tacos_please
local     new_test_volume
local     taco_tuesday
bradsimpson@ app:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name my_postgres -d --mount type=volume,source=more_tacos_please,target=/var/lib/postgresql/data postgres 
e03ae05289fe4f8ab87390abaf91b36743c7b795019c8156d2eae0d00a63afa3
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
e03ae05289fe   postgres   "docker-entrypoint.s…"   6 seconds ago   Up 4 seconds   0.0.0.0:5431->5432/tcp   my_postgres
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

postgres=# CREATE DATABASE tacotuesday WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                  List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-------------+----------+----------+------------+------------+-----------------------
 postgres    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 tacotuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS                    NAMES
e03ae05289fe   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:5431->5432/tcp   my_postgres
bradsimpson@ app:docker container stop my_postgres
my_postgres
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS                     PORTS     NAMES
e03ae05289fe   postgres   "docker-entrypoint.s…"   2 minutes ago   Exited (0) 7 seconds ago             my_postgres
bradsimpson@ app:docker container rm my_postgres
my_postgres
bradsimpson@ app:docker container ls -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@ app:\clear

bradsimpson@ app:docker container run -p 5431:5432 -e POSTGRES_PASSWORD=password --name my_postgres2 -d --mount type=volume,source=more_tacos_please,target=/var/lib/postgresql/data postgres 
576959c4cff41aec0203942bb97567531d3c068cb7064828109d802d625c7a2b
bradsimpson@ app:docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                    NAMES
576959c4cff4   postgres   "docker-entrypoint.s…"   5 seconds ago   Up 3 seconds   0.0.0.0:5431->5432/tcp   my_postgres2
bradsimpson@ app:psql -p 5431 -h localhost -U postgres
Password for user postgres: 
psql (13.2, server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 13, server major version 15.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                  List of databases
    Name     |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-------------+----------+----------+------------+------------+-----------------------
 postgres    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 tacotuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
             |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# exit 
bradsimpson@ app:
bradsimpson@ app:
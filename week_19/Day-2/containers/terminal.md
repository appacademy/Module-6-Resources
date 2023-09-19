# CONTAINER CLI

Last login: Tue Sep 19 08:53:28 on ttys008
bradsimpson@Brads-MacBook-Air ~ % docker container run hello-world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
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

bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   15 hours ago   113MB
<none>                            <none>    23d8681bdbcf   15 hours ago   113MB
<none>                            <none>    8442fa932634   15 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   16 hours ago   144MB
<none>                            <none>    1be486eb8e9e   16 hours ago   814MB
<none>                            <none>    f6211611ef7b   17 hours ago   814MB
<none>                            <none>    ec44781411c1   18 hours ago   814MB
<none>                            <none>    e3758b5271b3   18 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   7 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   7 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
hello-world                       latest    b038788ddb22   4 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker image rm hello-world
Error response from daemon: conflict: unable to remove repository reference "hello-world" (must force) - container 87e873dab3a7 is using its referenced image b038788ddb22
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                          PORTS     NAMES
87e873dab3a7   hello-world    "/hello"                 About a minute ago   Exited (0) About a minute ago             suspicious_margulis
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   15 hours ago         Exited (0) 15 hours ago                   pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   15 hours ago         Exited (0) 15 hours ago                   romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container rm suspicious_margulis

suspicious_margulis
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a                 
CONTAINER ID   IMAGE          COMMAND                  CREATED        STATUS                    PORTS     NAMES
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   15 hours ago   Exited (0) 15 hours ago             pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   15 hours ago   Exited (0) 15 hours ago             romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   15 hours ago   113MB
<none>                            <none>    23d8681bdbcf   15 hours ago   113MB
<none>                            <none>    8442fa932634   15 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   16 hours ago   144MB
<none>                            <none>    1be486eb8e9e   16 hours ago   814MB
<none>                            <none>    f6211611ef7b   17 hours ago   814MB
<none>                            <none>    ec44781411c1   18 hours ago   814MB
<none>                            <none>    e3758b5271b3   18 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   7 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   7 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
hello-world                       latest    b038788ddb22   4 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker image rm hellp-world
Error response from daemon: No such image: hellp-world:latest
bradsimpson@Brads-MacBook-Air ~ % docker image ls            
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   15 hours ago   113MB
<none>                            <none>    23d8681bdbcf   15 hours ago   113MB
<none>                            <none>    8442fa932634   15 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   16 hours ago   144MB
<none>                            <none>    1be486eb8e9e   16 hours ago   814MB
<none>                            <none>    f6211611ef7b   17 hours ago   814MB
<none>                            <none>    ec44781411c1   18 hours ago   814MB
<none>                            <none>    e3758b5271b3   18 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   7 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   7 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
hello-world                       latest    b038788ddb22   4 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker image rm hello-world
Untagged: hello-world:latest
Untagged: hello-world@sha256:a13ec89cdf897b3e551bd9f89d499db6ff3a7f44c5b9eb8bca40da20eb4ea1fa
Deleted: sha256:b038788ddb222cb7d6025b411759e4f5abe9910486c8f98534ead97befd77dd7
Deleted: sha256:a7866053acacfefb68912a8916b67d6847c12b51949c6b8a5580c6609c08ae45
bradsimpson@Brads-MacBook-Air ~ % \clear        

bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   15 hours ago   113MB
<none>                            <none>    23d8681bdbcf   15 hours ago   113MB
<none>                            <none>    8442fa932634   15 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   16 hours ago   144MB
<none>                            <none>    1be486eb8e9e   16 hours ago   814MB
<none>                            <none>    f6211611ef7b   17 hours ago   814MB
<none>                            <none>    ec44781411c1   18 hours ago   814MB
<none>                            <none>    e3758b5271b3   18 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   7 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   7 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
bradsimpson@Brads-MacBook-Air ~ % docker container run hello-world       
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
70f5ac315c5a: Pull complete 
Digest: sha256:4f53e2564790c8e7856ec08e384732aa38dc43c52f02952483e3f003afbf23db
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
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

bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run [options flags] image_name [additonal commands or arguements] 
zsh: bad pattern: [options
bradsimpson@Brads-MacBook-Air ~ % docker container run                         









































bradsimpson@Brads-MacBook-Air ~ %                      
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % 








































bradsimpson@Brads-MacBook-Air ~ % 
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run --name cool_container -p 8000:80 nginx
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/09/19 15:25:56 [notice] 1#1: using the "epoll" event method
2023/09/19 15:25:56 [notice] 1#1: nginx/1.25.1
2023/09/19 15:25:56 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2023/09/19 15:25:56 [notice] 1#1: OS: Linux 6.3.13-linuxkit
2023/09/19 15:25:56 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/09/19 15:25:56 [notice] 1#1: start worker processes
2023/09/19 15:25:56 [notice] 1#1: start worker process 29
2023/09/19 15:25:56 [notice] 1#1: start worker process 30
2023/09/19 15:25:56 [notice] 1#1: start worker process 31
2023/09/19 15:25:56 [notice] 1#1: start worker process 32
192.168.65.1 - - [19/Sep/2023:15:26:18 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
2023/09/19 15:26:19 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.65.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
192.168.65.1 - - [19/Sep/2023:15:26:19 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
192.168.65.1 - - [19/Sep/2023:15:26:29 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
192.168.65.1 - - [19/Sep/2023:15:26:30 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
192.168.65.1 - - [19/Sep/2023:15:26:30 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
192.168.65.1 - - [19/Sep/2023:15:26:31 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
192.168.65.1 - - [19/Sep/2023:15:26:32 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36" "-"
^C2023/09/19 15:27:12 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/09/19 15:27:12 [notice] 30#30: exiting
2023/09/19 15:27:12 [notice] 31#31: exiting
2023/09/19 15:27:12 [notice] 32#32: exiting
2023/09/19 15:27:12 [notice] 31#31: exit
2023/09/19 15:27:12 [notice] 32#32: exit
2023/09/19 15:27:12 [notice] 30#30: exit
2023/09/19 15:27:12 [notice] 29#29: exiting
2023/09/19 15:27:12 [notice] 29#29: exit
2023/09/19 15:27:12 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/09/19 15:27:12 [notice] 1#1: worker process 31 exited with code 0
2023/09/19 15:27:12 [notice] 1#1: signal 29 (SIGIO) received
2023/09/19 15:27:12 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/09/19 15:27:12 [notice] 1#1: worker process 32 exited with code 0
2023/09/19 15:27:12 [notice] 1#1: signal 29 (SIGIO) received
2023/09/19 15:27:12 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2023/09/19 15:27:12 [notice] 1#1: worker process 30 exited with code 0
2023/09/19 15:27:12 [notice] 1#1: signal 29 (SIGIO) received
2023/09/19 15:27:12 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/09/19 15:27:12 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2023/09/19 15:27:12 [notice] 1#1: worker process 29 exited with code 0
2023/09/19 15:27:12 [notice] 1#1: exit
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                      PORTS     NAMES
ea74fcad86b3   nginx          "/docker-entrypoint.…"   About a minute ago   Exited (0) 22 seconds ago             cool_container
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
/bin # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls   
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
f0e031555192   nginx     "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:8000->80/tcp   busy_banach
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
f0e031555192   nginx          "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:8000->80/tcp   busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   10 minutes ago   Exited (0) 8 minutes ago                           cool_container
d6716e28836a   hello-world    "/hello"                 26 minutes ago   Exited (0) 26 minutes ago                          sleepy_tu
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   16 hours ago     Exited (0) 16 hours ago                            pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -it alpine     
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
22c42d9291a3   alpine         "/bin/sh"                20 seconds ago   Exited (0) 8 seconds ago                           clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   7 minutes ago    Up 7 minutes                0.0.0.0:8000->80/tcp   busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   10 minutes ago   Exited (0) 9 minutes ago                           cool_container
d6716e28836a   hello-world    "/hello"                 27 minutes ago   Exited (0) 27 minutes ago                          sleepy_tu
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   16 hours ago     Exited (0) 16 hours ago                            pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % \clear


















bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 8080:80 nginx
eec94608825fffa274fa515429ef81b41d07dc35a6e708ad181cb3fe6783564a
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
eec94608825f   nginx     "/docker-entrypoint.…"   7 seconds ago   Up 6 seconds   0.0.0.0:8080->80/tcp   affectionate_bassi
f0e031555192   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 8 minutes   0.0.0.0:8000->80/tcp   busy_banach
bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 8080:80 nginx
36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1
docker: Error response from daemon: driver failed programming external connectivity on endpoint zealous_chaum (90efc4c80a1a2c7a87772414de65a10ba6a2cb640bc4629f0d390796014b344c): Bind for 0.0.0.0:8080 failed: port is already allocated.
bradsimpson@Brads-MacBook-Air ~ % docker container run -it --name test alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                  NAMES
eec94608825f   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp   affectionate_bassi
f0e031555192   nginx     "/docker-entrypoint.…"   10 minutes ago       Up 10 minutes       0.0.0.0:8000->80/tcp   busy_banach
bradsimpson@Brads-MacBook-Air ~ % docker container run --name greet_me --rm ubunut echo hello world
Unable to find image 'ubunut:latest' locally
docker: Error response from daemon: pull access denied for ubunut, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run --name greet_me --rm ubuntu echo hello world 
hello world
bradsimpson@Brads-MacBook-Air ~ % echo hello world
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
eec94608825f   nginx     "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes    0.0.0.0:8080->80/tcp   affectionate_bassi
f0e031555192   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes   0.0.0.0:8000->80/tcp   busy_banach
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
c6291f8d625c   alpine         "sh"                     2 minutes ago    Exited (0) 2 minutes ago                           test
36eb27ccf7be   nginx          "/docker-entrypoint.…"   3 minutes ago    Created                                            zealous_chaum
eec94608825f   nginx          "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:8080->80/tcp   affectionate_bassi
22c42d9291a3   alpine         "/bin/sh"                6 minutes ago    Exited (0) 6 minutes ago                           clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   13 minutes ago   Up 13 minutes               0.0.0.0:8000->80/tcp   busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   17 minutes ago   Exited (0) 15 minutes ago                          cool_container
d6716e28836a   hello-world    "/hello"                 34 minutes ago   Exited (0) 34 minutes ago                          sleepy_tu
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   16 hours ago     Exited (0) 16 hours ago                            pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
eec94608825f   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8080->80/tcp   affectionate_bassi
f0e031555192   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes   0.0.0.0:8000->80/tcp   busy_banach
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
c6291f8d625c   alpine         "sh"                     4 minutes ago    Exited (0) 4 minutes ago                           test
36eb27ccf7be   nginx          "/docker-entrypoint.…"   5 minutes ago    Created                                            zealous_chaum
eec94608825f   nginx          "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8080->80/tcp   affectionate_bassi
22c42d9291a3   alpine         "/bin/sh"                7 minutes ago    Exited (0) 7 minutes ago                           clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   14 minutes ago   Up 14 minutes               0.0.0.0:8000->80/tcp   busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   18 minutes ago   Exited (0) 17 minutes ago                          cool_container
d6716e28836a   hello-world    "/hello"                 35 minutes ago   Exited (0) 35 minutes ago                          sleepy_tu
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   16 hours ago     Exited (0) 16 hours ago                            pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   16 hours ago   113MB
<none>                            <none>    23d8681bdbcf   16 hours ago   113MB
<none>                            <none>    8442fa932634   16 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   16 hours ago   144MB
<none>                            <none>    1be486eb8e9e   16 hours ago   814MB
<none>                            <none>    f6211611ef7b   18 hours ago   814MB
<none>                            <none>    ec44781411c1   18 hours ago   814MB
<none>                            <none>    e3758b5271b3   18 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   7 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   7 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
hello-world                       latest    b038788ddb22   4 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
55327caa5de1   bridge         bridge    local
0c4794c37db6   host           host      local
2be63f87cace   my_network     bridge    local
61b3161ebf7d   none           null      local
5bd45a71ad73   taco_network   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker volume ls
DRIVER    VOLUME NAME
local     taco_tues
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
c6291f8d625c   alpine         "sh"                     5 minutes ago    Exited (0) 5 minutes ago                           test
36eb27ccf7be   nginx          "/docker-entrypoint.…"   6 minutes ago    Created                                            zealous_chaum
eec94608825f   nginx          "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:8080->80/tcp   affectionate_bassi
22c42d9291a3   alpine         "/bin/sh"                9 minutes ago    Exited (0) 8 minutes ago                           clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes               0.0.0.0:8000->80/tcp   busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   19 minutes ago   Exited (0) 18 minutes ago                          cool_container
d6716e28836a   hello-world    "/hello"                 36 minutes ago   Exited (0) 36 minutes ago                          sleepy_tu
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   16 hours ago     Exited (0) 16 hours ago                            pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container ls   
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
eec94608825f   nginx     "/docker-entrypoint.…"   7 minutes ago    Up 6 minutes    0.0.0.0:8080->80/tcp   affectionate_bassi
f0e031555192   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8000->80/tcp   busy_banach
bradsimpson@Brads-MacBook-Air ~ % docker container stop affectionate_bassi f0e031555192 
affectionate_bassi
f0e031555192
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % \clear




bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS     NAMES
c6291f8d625c   alpine         "sh"                     6 minutes ago    Exited (0) 6 minutes ago              test
36eb27ccf7be   nginx          "/docker-entrypoint.…"   7 minutes ago    Created                               zealous_chaum
eec94608825f   nginx          "/docker-entrypoint.…"   7 minutes ago    Exited (0) 24 seconds ago             affectionate_bassi
22c42d9291a3   alpine         "/bin/sh"                10 minutes ago   Exited (0) 9 minutes ago              clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   16 minutes ago   Exited (0) 24 seconds ago             busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   20 minutes ago   Exited (0) 19 minutes ago             cool_container
d6716e28836a   hello-world    "/hello"                 37 minutes ago   Exited (0) 37 minutes ago             sleepy_tu
e7be82eea601   23d8681bdbcf   "/bin/sh -c 'gunicor…"   16 hours ago     Exited (0) 16 hours ago               pedantic_goodall
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago               romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container start zealous_chaum
zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container ls                 
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   7 minutes ago   Up 2 seconds   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container rm sleepy_tu pedantic_goodall


sleepy_tu
pedantic_goodall
bradsimpson@Brads-MacBook-Air ~ % docker container ls                           
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS              PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   8 minutes ago   Up About a minute   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
c6291f8d625c   alpine         "sh"                     7 minutes ago    Exited (0) 7 minutes ago                           test
36eb27ccf7be   nginx          "/docker-entrypoint.…"   8 minutes ago    Up About a minute           0.0.0.0:8080->80/tcp   zealous_chaum
eec94608825f   nginx          "/docker-entrypoint.…"   9 minutes ago    Exited (0) 2 minutes ago                           affectionate_bassi
22c42d9291a3   alpine         "/bin/sh"                11 minutes ago   Exited (0) 11 minutes ago                          clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   18 minutes ago   Exited (0) 2 minutes ago                           busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   22 minutes ago   Exited (0) 20 minutes ago                          cool_container
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
c6291f8d625c   alpine         "sh"                     8 minutes ago    Exited (0) 8 minutes ago                           test
36eb27ccf7be   nginx          "/docker-entrypoint.…"   9 minutes ago    Up About a minute           0.0.0.0:8080->80/tcp   zealous_chaum
eec94608825f   nginx          "/docker-entrypoint.…"   9 minutes ago    Exited (0) 2 minutes ago                           affectionate_bassi
22c42d9291a3   alpine         "/bin/sh"                11 minutes ago   Exited (0) 11 minutes ago                          clever_easley
f0e031555192   nginx          "/docker-entrypoint.…"   18 minutes ago   Exited (0) 2 minutes ago                           busy_banach
ea74fcad86b3   nginx          "/docker-entrypoint.…"   22 minutes ago   Exited (0) 21 minutes ago                          cool_container
d126b6b1565f   8442fa932634   "/bin/sh -c 'flask r…"   16 hours ago     Exited (0) 16 hours ago                            romantic_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
c6291f8d625cbbb9c341d4e4b8f74276db9ab47e2520a8735a55f5c7a65cd480
eec94608825fffa274fa515429ef81b41d07dc35a6e708ad181cb3fe6783564a
22c42d9291a36342c9d2aafc875b176b3df5afe47a5f0fe1b5e1093391b85c8c
f0e031555192fa04bf1ca8733e79b4c60e7f291a7acc5c4dba443ddcfda4753a
ea74fcad86b33475bc2559d8d79906dcb1f5f9e663b5dd8c0f93d4c2862eae50
d126b6b1565fbd73cc5fe1edcec774a0fdf2f283470443a2069fadfc7b723889

Total reclaimed space: 19.68kB
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   16 hours ago   113MB
<none>                            <none>    23d8681bdbcf   16 hours ago   113MB
<none>                            <none>    8442fa932634   16 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   16 hours ago   144MB
<none>                            <none>    1be486eb8e9e   16 hours ago   814MB
<none>                            <none>    f6211611ef7b   18 hours ago   814MB
<none>                            <none>    ec44781411c1   18 hours ago   814MB
<none>                            <none>    e3758b5271b3   18 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   7 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   7 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
hello-world                       latest    b038788ddb22   4 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 2 minutes   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it zealous_chaum sh
# \ls
bin   docker-entrypoint.d   home   mnt	 root  srv  usr
boot  docker-entrypoint.sh  lib    opt	 run   sys  var
dev   etc		    media  proc  sbin  tmp
# cd usr
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share
# \ls
X11		 debconf      fonts	libgcrypt20  nginx	  tabset
base-files	 debianutils  gcc	lintian      pam	  terminfo
base-passwd	 dict	      gdb	locale	     pam-configs  util-linux
bash-completion  doc	      info	man	     perl5	  xml
bug		 doc-base     java	maven-repo   pixmaps	  zoneinfo
ca-certificates  dpkg	      keyrings	menu	     polkit-1	  zsh
common-licenses  fontconfig   libc-bin	misc	     readline
# cd nginx	
# \ls
html
# cd html	
# \ls
50x.html  index.html
# exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls                       
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % 


# NETWORKING

Last login: Tue Sep 19 10:59:31 on ttys008
bradsimpson@Brads-MacBook-Air ~ % >....                                         
bin  games  include  lib  libexec  local  sbin  share  src
# cd share
# \ls
X11              debconf      fonts     libgcrypt20  nginx        tabset
base-files       debianutils  gcc       lintian      pam          terminfo
base-passwd      dict         gdb       locale       pam-configs  util-linux
bash-completion  doc          info      man          perl5        xml
bug              doc-base     java      maven-repo   pixmaps      zoneinfo
ca-certificates  dpkg         keyrings  menu         polkit-1     zsh
common-licenses  fontconfig   libc-bin  misc         readline
# cd nginx
# \ls
html
# cd html
# \ls
50x.html  index.html
# exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS
  PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   14 minutes ago   Up 6 minutes
  0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~\clear
zsh: parse error near `<'
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % \clear























bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
55327caa5de1   bridge         bridge    local
0c4794c37db6   host           host      local
2be63f87cace   my_network     bridge    local
61b3161ebf7d   none           null      local
5bd45a71ad73   taco_network   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker network prune
WARNING! This will remove all custom networks not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Networks:
my_network
taco_network

bradsimpson@Brads-MacBook-Air ~ % docker network ls   
NETWORK ID     NAME      DRIVER    SCOPE
55327caa5de1   bridge    bridge    local
0c4794c37db6   host      host      local
61b3161ebf7d   none      null      local
bradsimpson@Brads-MacBook-Air ~ % \clear
















bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
55327caa5de1   bridge    bridge    local
0c4794c37db6   host      host      local
61b3161ebf7d   none      null      local
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   34 minutes ago   Up 26 minutes   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container inspect zealous_chaum
[
    {
        "Id": "36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1",
        "Created": "2023-09-19T15:39:12.488259584Z",
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
            "Pid": 4440,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-09-19T15:46:45.877248419Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1/hostname",
        "HostsPath": "/var/lib/docker/containers/36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1/hosts",
        "LogPath": "/var/lib/docker/containers/36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1/36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1-json.log",
        "Name": "/zealous_chaum",
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
            "ConsoleSize": [
                39,
                87
            ],
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
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
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
                "LowerDir": "/var/lib/docker/overlay2/598bdee746003cc2af82091996adf6ed1c0df231c4b16faf3dde2095f9e58400-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/598bdee746003cc2af82091996adf6ed1c0df231c4b16faf3dde2095f9e58400/merged",
                "UpperDir": "/var/lib/docker/overlay2/598bdee746003cc2af82091996adf6ed1c0df231c4b16faf3dde2095f9e58400/diff",
                "WorkDir": "/var/lib/docker/overlay2/598bdee746003cc2af82091996adf6ed1c0df231c4b16faf3dde2095f9e58400/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "36eb27ccf7be",
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
                "NGINX_VERSION=1.25.1",
                "NJS_VERSION=0.7.12",
                "PKG_RELEASE=1~bookworm"
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
            "SandboxID": "052fe6af665d5170a1b5ac1880798bd6a7141841974a1d422a9837ed6ffef804",
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
            "SandboxKey": "/var/run/docker/netns/052fe6af665d",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "e73f6026c80e8a62dd7e93cdfb48189ead03289cb15035ae7582fb2472dfccfe",
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
                    "NetworkID": "55327caa5de17af707254494e8631f02aa9a634c6e66da5d46f57b42ef298de0",
                    "EndpointID": "e73f6026c80e8a62dd7e93cdfb48189ead03289cb15035ae7582fb2472dfccfe",
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
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
55327caa5de1   bridge    bridge    local
0c4794c37db6   host      host      local
61b3161ebf7d   none      null      local
bradsimpson@Brads-MacBook-Air ~ % docker network create --driver bridge my_network
60994c698b8b5bf011c1030808e8681d4ae0fec76049def7eb282f299a306fa9
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
55327caa5de1   bridge       bridge    local
0c4794c37db6   host         host      local
60994c698b8b   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
36eb27ccf7be   nginx     "/docker-entrypoint.…"   40 minutes ago   Up 32 minutes   0.0.0.0:8080->80/tcp   zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container stop zealous_chaum
zealous_chaum
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c1 --network my_network nginx:alpine
69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c2 --network my_network nginx:alpine 
e5f729d879efeee148f2d127bd03516ed19fa9a360546c82e79d0a7b81749449
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
e5f729d879ef   nginx:alpine   "/docker-entrypoint.…"   5 seconds ago    Up 4 seconds    80/tcp    c2
69c19dfd0c9c   nginx:alpine   "/docker-entrypoint.…"   16 seconds ago   Up 15 seconds   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c1
[
    {
        "Id": "69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307",
        "Created": "2023-09-19T16:21:10.146995263Z",
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
            "Pid": 9111,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-09-19T16:21:10.319720347Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307/hostname",
        "HostsPath": "/var/lib/docker/containers/69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307/hosts",
        "LogPath": "/var/lib/docker/containers/69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307/69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307-json.log",
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
            "ConsoleSize": [
                37,
                80
            ],
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
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
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
                "LowerDir": "/var/lib/docker/overlay2/08547042ac5c1e20fae501f58eaceefdbe4c3d40621e69921f5d4dacea688615-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/08547042ac5c1e20fae501f58eaceefdbe4c3d40621e69921f5d4dacea688615/merged",
                "UpperDir": "/var/lib/docker/overlay2/08547042ac5c1e20fae501f58eaceefdbe4c3d40621e69921f5d4dacea688615/diff",
                "WorkDir": "/var/lib/docker/overlay2/08547042ac5c1e20fae501f58eaceefdbe4c3d40621e69921f5d4dacea688615/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "69c19dfd0c9c",
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
                "NGINX_VERSION=1.25.1",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.12"
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
            "SandboxID": "0c31d00bf31a4f0a530c31c0c43de753ce4189451c3b890f332f732547491e0c",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/0c31d00bf31a",
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
                        "69c19dfd0c9c"
                    ],
                    "NetworkID": "60994c698b8b5bf011c1030808e8681d4ae0fec76049def7eb282f299a306fa9",
                    "EndpointID": "53e2d883f49012f90be816e0db8d3eca65aec55c7c70f8460614a2671630dc39",
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
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c3 nginx:alpine
0f19558e8f44d43ca91c8c1476434f0ed12df39532148625e1f90d7f4c7bc74b
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c4 nginx:alpine 
d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c4
[
    {
        "Id": "d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461",
        "Created": "2023-09-19T16:22:18.527840336Z",
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
            "Pid": 9592,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-09-19T16:22:18.688242961Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461/hostname",
        "HostsPath": "/var/lib/docker/containers/d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461/hosts",
        "LogPath": "/var/lib/docker/containers/d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461/d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461-json.log",
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
            "ConsoleSize": [
                37,
                80
            ],
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
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
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
                "LowerDir": "/var/lib/docker/overlay2/ab6da4c8e555b7ff883a0be8fe4bf07000a39de1df61814c9c1a7d64b31bdde8-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/ab6da4c8e555b7ff883a0be8fe4bf07000a39de1df61814c9c1a7d64b31bdde8/merged",
                "UpperDir": "/var/lib/docker/overlay2/ab6da4c8e555b7ff883a0be8fe4bf07000a39de1df61814c9c1a7d64b31bdde8/diff",
                "WorkDir": "/var/lib/docker/overlay2/ab6da4c8e555b7ff883a0be8fe4bf07000a39de1df61814c9c1a7d64b31bdde8/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "d6be95d64a36",
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
                "NGINX_VERSION=1.25.1",
                "PKG_RELEASE=1",
                "NJS_VERSION=0.7.12"
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
            "SandboxID": "9ce0e23bc52a7c1171422b7ecc808478a89e7fc99bcc30e4f51808f613be8131",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/9ce0e23bc52a",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "e08ee2145b11a6393b919fa21347d6305daa007602a5e0e8bfe61ea0ad455cf1",
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
                    "NetworkID": "55327caa5de17af707254494e8631f02aa9a634c6e66da5d46f57b42ef298de0",
                    "EndpointID": "e08ee2145b11a6393b919fa21347d6305daa007602a5e0e8bfe61ea0ad455cf1",
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
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
d6be95d64a36   nginx:alpine   "/docker-entrypoint.…"   31 seconds ago       Up 30 seconds       80/tcp    c4
0f19558e8f44   nginx:alpine   "/docker-entrypoint.…"   38 seconds ago       Up 37 seconds       80/tcp    c3
e5f729d879ef   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
69c19dfd0c9c   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 sh
/ # ping -c 4 c2
PING c2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.230 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.258 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.244 ms
64 bytes from 172.18.0.3: seq=3 ttl=64 time=0.243 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.230/0.243/0.258 ms
/ # ping -c 4 c3
ping: bad address 'c3'
/ # ping -c 4 c4
ping: bad address 'c4'
/ # exit 
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c3 sh 
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.311 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.127 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.289 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.129 ms

--- 172.17.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.127/0.214/0.311 ms
/ # docker network ls
sh: docker: not found
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS     NAMES
d6be95d64a36   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   80/tcp    c4
0f19558e8f44   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   80/tcp    c3
e5f729d879ef   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c2
69c19dfd0c9c   nginx:alpine   "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME         DRIVER    SCOPE
55327caa5de1   bridge       bridge    local
0c4794c37db6   host         host      local
60994c698b8b   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 sh
/ # ping c2
PING c2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.171 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.255 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.165 ms
64 bytes from 172.18.0.3: seq=3 ttl=64 time=0.122 ms
64 bytes from 172.18.0.3: seq=4 ttl=64 time=0.121 ms
64 bytes from 172.18.0.3: seq=5 ttl=64 time=0.161 ms
64 bytes from 172.18.0.3: seq=6 ttl=64 time=0.125 ms
64 bytes from 172.18.0.3: seq=7 ttl=64 time=0.189 ms
64 bytes from 172.18.0.3: seq=8 ttl=64 time=0.242 ms
64 bytes from 172.18.0.3: seq=9 ttl=64 time=0.141 ms
64 bytes from 172.18.0.3: seq=10 ttl=64 time=0.111 ms
64 bytes from 172.18.0.3: seq=11 ttl=64 time=0.159 ms
64 bytes from 172.18.0.3: seq=12 ttl=64 time=0.126 ms
64 bytes from 172.18.0.3: seq=13 ttl=64 time=0.131 ms
64 bytes from 172.18.0.3: seq=14 ttl=64 time=0.170 ms
64 bytes from 172.18.0.3: seq=15 ttl=64 time=0.120 ms
64 bytes from 172.18.0.3: seq=16 ttl=64 time=0.118 ms
64 bytes from 172.18.0.3: seq=17 ttl=64 time=0.206 ms
64 bytes from 172.18.0.3: seq=18 ttl=64 time=0.160 ms
64 bytes from 172.18.0.3: seq=19 ttl=64 time=0.171 ms
64 bytes from 172.18.0.3: seq=20 ttl=64 time=0.145 ms
^C
--- c2 ping statistics ---
21 packets transmitted, 21 packets received, 0% packet loss
round-trip min/avg/max = 0.111/0.157/0.255 ms
/ # exit
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % 


# VOLUMES & BIND MOUNTS


Last login: Tue Sep 19 11:57:34 on ttys008
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Movies			Postman Agent
Documents		Music			Public
Downloads		Pictures		app
Library			Postman			requirements.txt
bradsimpson@Brads-MacBook-Air ~ % rm app
rm: app: is a directory
bradsimpson@Brads-MacBook-Air ~ % rm -rf app
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Movies			Postman Agent
Documents		Music			Public
Downloads		Pictures		requirements.txt
Library			Postman
bradsimpson@Brads-MacBook-Air ~ % \clear























bradsimpson@Brads-MacBook-Air ~ % docker container run --mount type=bind,source=direcct/path/to/subfolder,targetr=path/to/where/container/wants/it 
invalid argument "type=bind,source=direcct/path/to/subfolder,targetr=path/to/where/container/wants/it" for "--mount" flag: unexpected key 'targetr' in 'targetr=path/to/where/container/wants/it'
See 'docker container run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker volume ls
DRIVER    VOLUME NAME
local     taco_tues
bradsimpson@Brads-MacBook-Air ~ % mkdir app
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Movies			Postman Agent
Documents		Music			Public
Downloads		Pictures		app
Library			Postman			requirements.txt
bradsimpson@Brads-MacBook-Air ~ % cd app
bradsimpson@Brads-MacBook-Air app % touch index.html
bradsimpson@Brads-MacBook-Air app % nano index.html
bradsimpson@Brads-MacBook-Air app % \sl
zsh: command not found: sl
bradsimpson@Brads-MacBook-Air app % \ls
index.html
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
d6be95d64a36   nginx:alpine   "/docker-entrypoint.…"   43 minutes ago   Up 43 minutes   80/tcp    c4
0f19558e8f44   nginx:alpine   "/docker-entrypoint.…"   43 minutes ago   Up 43 minutes   80/tcp    c3
e5f729d879ef   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c2
69c19dfd0c9c   nginx:alpine   "/docker-entrypoint.…"   44 minutes ago   Up 44 minutes   80/tcp    c1
bradsimpson@Brads-MacBook-Air app % docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@Brads-MacBook-Air app % docker container ls              
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker container run -d -p 8000:80 --moun     
unknown flag: --moun
See 'docker container run --help'.
bradsimpson@Brads-MacBook-Air app % cd ..
bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 8000:80 --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html nginx:alpine
5f9b52626ce5dd8d21051928824538ff7428eb2116e7f6080b1af6f6ec40c86e
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
5f9b52626ce5   nginx:alpine   "/docker-entrypoint.…"   34 seconds ago   Up 32 seconds   0.0.0.0:8000->80/tcp   cool_raman
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it cool_raman sh
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
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
sh: nano: not found
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/aarch64/APKINDEX.tar.gz
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 44 MiB in 63 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@Brads-MacBook-Air ~ % cd app 
bradsimpson@Brads-MacBook-Air app % nano index.html 
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                  NAMES
5f9b52626ce5   nginx:alpine   "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   cool_raman
bradsimpson@Brads-MacBook-Air app % docker container stop cool_raman
cool_raman
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker volume ls
DRIVER    VOLUME NAME
local     taco_tues
bradsimpson@Brads-MacBook-Air app % docker volume create my_volume
my_volume
bradsimpson@Brads-MacBook-Air app % docker volume ls
DRIVER    VOLUME NAME
local     my_volume
local     taco_tues
bradsimpson@Brads-MacBook-Air app % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch              latest    85fd9d51fbc4   17 hours ago   113MB
<none>                            <none>    23d8681bdbcf   17 hours ago   113MB
<none>                            <none>    8442fa932634   18 hours ago   113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   18 hours ago   144MB
<none>                            <none>    1be486eb8e9e   18 hours ago   814MB
<none>                            <none>    f6211611ef7b   19 hours ago   814MB
<none>                            <none>    ec44781411c1   20 hours ago   814MB
<none>                            <none>    e3758b5271b3   20 hours ago   814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   7 days ago     1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   7 days ago     1.21GB
<none>                            <none>    3e9c435ed215   7 days ago     1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   7 days ago     976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   7 days ago     976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   7 days ago     976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   7 days ago     976MB
bradsimpson213/my_starter         <none>    6afd10397145   8 days ago     976MB
bradsimpson213/my_starter         <none>    31b768bb850b   8 days ago     994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   3 weeks ago    575MB
<none>                            <none>    6277c82a8b27   4 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   4 weeks ago    433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   7 weeks ago    451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   2 months ago   569MB
nginx                             alpine    66bf2c914bf4   3 months ago   41MB
alpine                            latest    5053b247d78b   3 months ago   7.66MB
nginx                             latest    2d21d843073b   3 months ago   192MB
ubuntu                            latest    cfb01e8e3121   3 months ago   69.2MB
hello-world                       latest    b038788ddb22   4 months ago   9.14kB
bradsimpson@Brads-MacBook-Air app % docker image inspect postgres
[
    {
        "Id": "sha256:ee56d70bcdf1aeca472a9899de653eb4d72f4a3ac31d9b0b95e677488ce766f3",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:a5e89e5f2679863bedef929c4a7ec5d1a2cb3c045f13b47680d86f8701144ed7"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-08-16T06:40:57.929475525Z",
        "Container": "850331b21eb942e9dad178c06146950af0dbe9b0794213e3fa9306637db74286",
        "ContainerConfig": {
            "Hostname": "850331b21eb9",
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
                "PG_VERSION=15.4-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:92c6e333aa36edb1932ac4198c20f986e32ad86ebd3c71bac7005ce622a6412c",
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
                "PG_VERSION=15.4-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:92c6e333aa36edb1932ac4198c20f986e32ad86ebd3c71bac7005ce622a6412c",
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
        "Architecture": "arm64",
        "Variant": "v8",
        "Os": "linux",
        "Size": 433237434,
        "VirtualSize": 433237434,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/19c2c0fd488f257ec64ccf2debc443f8d7b2fb51b6b424507b12dad8ceced5a2/diff:/var/lib/docker/overlay2/720cfe7bbf41f9167a5fd897387c047d1bd0b0788cbc76be818c124b40b9a2fc/diff:/var/lib/docker/overlay2/9ef2f2492f5d7b33f6842bcaa73544a5827441b370d59019178746eecc897887/diff:/var/lib/docker/overlay2/098e106cd4ce7d71eea1122353cfa08e6521f041a813df4e610aaa7db533fd44/diff:/var/lib/docker/overlay2/b524502fc40aece8a126f52872ffccdf33c8fd18eeb9896a73bbd37015162ce5/diff:/var/lib/docker/overlay2/82809c2f97a7559d2fc6bdd9ed979c89ddb5c62f689ca8dd8434aad7640f3cef/diff:/var/lib/docker/overlay2/2fd26a6716c4892966fdd7caf05ae2642c03c3e2c9cbc5afab58dd380bd5c4ee/diff:/var/lib/docker/overlay2/7651afd27ca6e197a766ffec66f5b77825ff7a28995c07ae0c878b9c3adde831/diff:/var/lib/docker/overlay2/033e377d2a69f2b5d8db1c9d16b65c47942292f658e8f72e06acf41007c25880/diff:/var/lib/docker/overlay2/494c1f85e9803b52bc30144d2937350c16dd654a3006dbe4a5d729497e0f72f6/diff:/var/lib/docker/overlay2/c18e7cdc5c90c2494b09769891c51c5f39fc475fc11a79c21493f1baa3beb564/diff:/var/lib/docker/overlay2/b0b9235892d66406d3e465349a8d3bb35f2f913af34c6ee5b5ea35da390ceb0c/diff",
                "MergedDir": "/var/lib/docker/overlay2/20fbafa167fcf3207196a945fa86cd01387bc47d52e362b965e6ff1c89058887/merged",
                "UpperDir": "/var/lib/docker/overlay2/20fbafa167fcf3207196a945fa86cd01387bc47d52e362b965e6ff1c89058887/diff",
                "WorkDir": "/var/lib/docker/overlay2/20fbafa167fcf3207196a945fa86cd01387bc47d52e362b965e6ff1c89058887/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:1c3daa06574284614db07a23682ab6d1c344f09f8093ee10e5de4152a51677a1",
                "sha256:310729fcb068da6941441d9627a3d8979e7dbd015c220324331e34af28b7e20c",
                "sha256:6cc6868915f4c4d399ec0026fd321acfd0b92e84cd2a51076e89041b3e3118b6",
                "sha256:10e10c831ae45343e95ad309a6e12d4248559f9dcffe3ca5b099044dfb1ced6e",
                "sha256:efeb668f57b52b8fe563c95296cd13a75431ab67e7a3b557b72ba4ef8d66e5de",
                "sha256:7df7b7f4d502154fb5a18da05456d5c74d9f70248a33112213c9469bb297470c",
                "sha256:79f05f53fceaaeffa6f88270b63f5b50d8359b7f66d6fb99a7ae2ebface34634",
                "sha256:f051436a55899d9ef6c1f7a74e487575a9d27e6046c0938ac49825972ada314e",
                "sha256:7cfa7dde137d5b682278bc5a0a6b5bec23ae142ddcec996d86faa2eec65ddaa3",
                "sha256:5bcc055db6d18a9f0252d404cecccfdb200a0124f510082bd6a95bb11e9ab5ae",
                "sha256:41961c2bd4aabfda25d4260d75f79052fd1f5a0c1645df7c43f3c2b3c711c794",
                "sha256:0e77db6aa900fe556e68e07ae83c1ba2008cd4a33b50e7f2898153731df0a104",
                "sha256:2a315bcee097176f1ba5a2916416eb2e40ef7348eba15212d3d95494af541b2e"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@Brads-MacBook-Air app % docker container run -e POSTGRES_PASSWORD=password --name postgres1 --mount type=volume,source=my_volume,target=/var/lib/postgresql/data postgres
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
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
waiting for server to start....2023-09-19 17:18:49.490 UTC [48] LOG:  starting PostgreSQL 15.4 (Debian 15.4-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2023-09-19 17:18:49.491 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2023-09-19 17:18:49.493 UTC [51] LOG:  database system was shut down at 2023-09-19 17:18:49 UTC
2023-09-19 17:18:49.496 UTC [48] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

2023-09-19 17:18:49.626 UTC [48] LOG:  received fast shutdown request
waiting for server to shut down....2023-09-19 17:18:49.626 UTC [48] LOG:  aborting any active transactions
2023-09-19 17:18:49.627 UTC [48] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
2023-09-19 17:18:49.627 UTC [49] LOG:  shutting down
2023-09-19 17:18:49.628 UTC [49] LOG:  checkpoint starting: shutdown immediate
2023-09-19 17:18:49.631 UTC [49] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.002 s, sync=0.001 s, total=0.004 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB
2023-09-19 17:18:49.634 UTC [48] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2023-09-19 17:18:49.749 UTC [1] LOG:  starting PostgreSQL 15.4 (Debian 15.4-1.pgdg120+1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2023-09-19 17:18:49.750 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2023-09-19 17:18:49.750 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2023-09-19 17:18:49.751 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2023-09-19 17:18:49.753 UTC [62] LOG:  database system was shut down at 2023-09-19 17:18:49 UTC
2023-09-19 17:18:49.756 UTC [1] LOG:  database system is ready to accept connections
^C2023-09-19 17:18:54.117 UTC [1] LOG:  received fast shutdown request
2023-09-19 17:18:54.119 UTC [1] LOG:  aborting any active transactions
2023-09-19 17:18:54.121 UTC [1] LOG:  background worker "logical replication launcher" (PID 65) exited with exit code 1
2023-09-19 17:18:54.122 UTC [60] LOG:  shutting down
2023-09-19 17:18:54.125 UTC [60] LOG:  checkpoint starting: shutdown immediate
2023-09-19 17:18:54.131 UTC [60] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.002 s, sync=0.001 s, total=0.010 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB
2023-09-19 17:18:54.135 UTC [1] LOG:  database system is shut down
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % docker container run -e POSTGRES_PASSWORD=password --name postgres1 --mount type=volume,source=my_volume,target=/var/lib/postgresql/data -d postgres
docker: Error response from daemon: Conflict. The container name "/postgres1" is already in use by container "003d83821ce8e77c6c05422c5f52253b3b4c872c2e68e76813331c3ae7e30885". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS     NAMES
003d83821ce8   postgres       "docker-entrypoint.s…"   38 seconds ago   Exited (0) 30 seconds ago             postgres1
5f9b52626ce5   nginx:alpine   "/docker-entrypoint.…"   10 minutes ago   Exited (0) 6 minutes ago              cool_raman
d6be95d64a36   nginx:alpine   "/docker-entrypoint.…"   57 minutes ago   Exited (0) 13 minutes ago             c4
0f19558e8f44   nginx:alpine   "/docker-entrypoint.…"   57 minutes ago   Exited (0) 13 minutes ago             c3
e5f729d879ef   nginx:alpine   "/docker-entrypoint.…"   58 minutes ago   Exited (0) 13 minutes ago             c2
69c19dfd0c9c   nginx:alpine   "/docker-entrypoint.…"   58 minutes ago   Exited (0) 13 minutes ago             c1
36eb27ccf7be   nginx          "/docker-entrypoint.…"   2 hours ago      Exited (0) 59 minutes ago             zealous_chaum
bradsimpson@Brads-MacBook-Air app % docker container rm postgres1
postgres1
bradsimpson@Brads-MacBook-Air app % docker container run -e POSTGRES_PASSWORD=password --name postgres1 --mount type=volume,source=my_volume,target=/var/lib/postgresql/data -d postgres
41298975e431c2a0eac5ef9e1bbb92b0bba21914c0cd25077ba1bcda359f0460
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS      NAMES
41298975e431   postgres   "docker-entrypoint.s…"   4 seconds ago   Up 4 seconds   5432/tcp   postgres1
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres1 sh
# psql -p 5432 -h localhost -U postgres 
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \ls
invalid command \ls
Try \? for help.
postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider | 
  Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-
----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
=c/postgres          +
           |          |          |            |            |            |                 | 
postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
=c/postgres          +
           |          |          |            |            |            |                 | 
postgres=CTc/postgres
(3 rows)






















postgres=# CREATE DATABASE taco_tues WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider | 
  Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-
----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tues | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
=c/postgres          +
           |          |          |            |            |            |                 | 
postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
=c/postgres          +
           |          |          |            |            |            |                 | 
postgres=CTc/postgres
(4 rows)





















postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS      NAMES
41298975e431   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp   postgres1
bradsimpson@Brads-MacBook-Air app % docker container stop postgres1
postgres1
bradsimpson@Brads-MacBook-Air app % docker container prune 
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
41298975e431c2a0eac5ef9e1bbb92b0bba21914c0cd25077ba1bcda359f0460
5f9b52626ce5dd8d21051928824538ff7428eb2116e7f6080b1af6f6ec40c86e
d6be95d64a365742de6830f8d09381e33c9153dfbfb20c859aa85db3fe11b461
0f19558e8f44d43ca91c8c1476434f0ed12df39532148625e1f90d7f4c7bc74b
e5f729d879efeee148f2d127bd03516ed19fa9a360546c82e79d0a7b81749449
69c19dfd0c9cfabe47ed5c87698af1bf5c20123161061ac46d323636ff641307
36eb27ccf7be2ce08fe2cee788cb4deb42c020aae478b24d8d39e07be6243aa1

Total reclaimed space: 3.075MB
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker container run -e POSTGRES_PASSWORD=password --name postgres2 --mount type=volume,source=my_volume,target=/var/lib/postgresql/data -d postgres 
27a1537c2e1beff7355ca27c3731329910a5de3c2b17a3903e0f70f4d3cb42f9
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres2 sh 
# psql -p 5431 -h localhost -U postgres
psql: error: connection to server at "localhost" (127.0.0.1), port 5431 failed: Connection refused
	Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (::1), port 5431 failed: Cannot assign requested address
	Is the server running on that host and accepting TCP/IP connections?
# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider | 
  Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-
----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tues | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
=c/postgres          +
           |          |          |            |            |            |                 | 
postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
=c/postgres          +
           |          |          |            |            |            |                 | 
postgres=CTc/postgres
(4 rows)





















postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls 
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS      NAMES
27a1537c2e1b   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp   postgres2
bradsimpson@Brads-MacBook-Air app % docker container stop postgres2
postgres2
bradsimpson@Brads-MacBook-Air app % 







bradsimpson@Brads-MacBook-Air ~ % 


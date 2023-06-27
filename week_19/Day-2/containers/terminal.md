Last login: Fri Jun 23 15:47:30 on ttys011
bradsimpson@Brads-MacBook-Air ~ % docker container run hello world
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run hello world
Unable to find image 'hello:latest' locally
docker: Error response from daemon: pull access denied for hello, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker login
Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
Username: bradsimpson213
Password: 
Login Succeeded

Logging in with your password grants your terminal complete access to your account. 
For better security, log in with a limited-privilege personal access token. Learn more at https://docs.docker.com/go/access-tokens/
bradsimpson@Brads-MacBook-Air ~ % docker container run hello world
Unable to find image 'hello:latest' locally
docker: Error response from daemon: pull access denied for hello, repository does not exist or may require 'docker login': denied: requested access to the resource is denied.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
70f5ac315c5a: Pull complete 
Digest: sha256:a13ec89cdf897b3e551bd9f89d499db6ff3a7f44c5b9eb8bca40da20eb4ea1fa
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

bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch   latest    853467a132ef   17 hours ago   1.59GB
<none>                 <none>    df9580143a75   3 days ago     1.59GB
hello-world            latest    b038788ddb22   7 weeks ago    9.14kB
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 3000:3000 [image name] commands
zsh: bad pattern: [image
bradsimpson@Brads-MacBook-Air ~ % docker container run --name cool_container -p 8000:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
95039a22a7cc: Pull complete 
08eddbefbcc8: Pull complete 
46b1df06a982: Pull complete 
33291f895f32: Pull complete 
f78a742b4ab6: Pull complete 
acc5d9f3837d: Pull complete 
658cd775cca5: Pull complete 
Digest: sha256:593dac25b7733ffb7afe1a72649a43e574778bf025ad60514ef40f6b5d606247
Status: Downloaded newer image for nginx:latest
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/06/27 15:13:37 [notice] 1#1: using the "epoll" event method
2023/06/27 15:13:37 [notice] 1#1: nginx/1.25.1
2023/06/27 15:13:37 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2023/06/27 15:13:37 [notice] 1#1: OS: Linux 5.15.49-linuxkit-pr
2023/06/27 15:13:37 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/06/27 15:13:37 [notice] 1#1: start worker processes
2023/06/27 15:13:37 [notice] 1#1: start worker process 29
2023/06/27 15:13:37 [notice] 1#1: start worker process 30
2023/06/27 15:13:37 [notice] 1#1: start worker process 31
2023/06/27 15:13:37 [notice] 1#1: start worker process 32
172.17.0.1 - - [27/Jun/2023:15:13:59 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [27/Jun/2023:15:13:59 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
2023/06/27 15:13:59 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
172.17.0.1 - - [27/Jun/2023:15:14:11 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [27/Jun/2023:15:14:12 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [27/Jun/2023:15:14:12 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
^C2023/06/27 15:14:58 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/06/27 15:14:58 [notice] 29#29: exiting
2023/06/27 15:14:58 [notice] 32#32: exiting
2023/06/27 15:14:58 [notice] 29#29: exit
2023/06/27 15:14:58 [notice] 32#32: exit
2023/06/27 15:14:58 [notice] 30#30: exiting
2023/06/27 15:14:58 [notice] 30#30: exit
2023/06/27 15:14:58 [notice] 31#31: exiting
2023/06/27 15:14:58 [notice] 31#31: exit
2023/06/27 15:14:58 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2023/06/27 15:14:58 [notice] 1#1: worker process 30 exited with code 0
2023/06/27 15:14:58 [notice] 1#1: signal 29 (SIGIO) received
2023/06/27 15:14:58 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/06/27 15:14:58 [notice] 1#1: worker process 32 exited with code 0
2023/06/27 15:14:58 [notice] 1#1: signal 29 (SIGIO) received
2023/06/27 15:14:58 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2023/06/27 15:14:58 [notice] 1#1: worker process 29 exited with code 0
2023/06/27 15:14:58 [notice] 1#1: signal 29 (SIGIO) received
2023/06/27 15:14:58 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/06/27 15:14:58 [notice] 1#1: worker process 31 exited with code 0
2023/06/27 15:14:58 [notice] 1#1: exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                      PORTS                    NAMES
ad6fe840b796   nginx          "/docker-entrypoint.…"   About a minute ago   Exited (0) 24 seconds ago                            cool_container
818201d69e63   hello-world    "/hello"                 10 minutes ago       Exited (0) 10 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago         Exited (0) 11 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % docker container run -p -d 8000:80 nginx 
docker: Invalid containerPort: -d.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % docker container run -p 8000:80 -d nginx
1948c101acebf25d38033b92fba3598743ae28e2d4b09858f4c4a9b5a9b2d2cb
bradsimpson@Brads-MacBook-Air ~ % docker container ls 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
1948c101aceb   nginx     "/docker-entrypoint.…"   35 seconds ago   Up 35 seconds   0.0.0.0:8000->80/tcp   nifty_ishizaka
bradsimpson@Brads-MacBook-Air ~ % docker container run --rm -it alpine sh
Unable to find image 'alpine:latest' locally
latest: Pulling from library/alpine
8c6d1654570f: Already exists 
Digest: sha256:82d1e9d7ed48a7523bdebc18cf6290bdb97b82302a8a9c27d4fe885949ea94d1
Status: Downloaded newer image for alpine:latest
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd bin
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
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
1948c101aceb   nginx     "/docker-entrypoint.…"   5 minutes ago   Up 5 minutes   0.0.0.0:8000->80/tcp   nifty_ishizaka
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                    NAMES
1948c101aceb   nginx          "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8000->80/tcp     nifty_ishizaka
ad6fe840b796   nginx          "/docker-entrypoint.…"   8 minutes ago    Exited (0) 7 minutes ago                             cool_container
818201d69e63   hello-world    "/hello"                 17 minutes ago   Exited (0) 17 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago     Exited (0) 18 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % docker container run -it alpine    
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a         
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                    NAMES
ba4eb06017db   alpine         "/bin/sh"                11 seconds ago   Exited (0) 3 seconds ago                             heuristic_pike
1948c101aceb   nginx          "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes                0.0.0.0:8000->80/tcp     nifty_ishizaka
ad6fe840b796   nginx          "/docker-entrypoint.…"   9 minutes ago    Exited (0) 7 minutes ago                             cool_container
818201d69e63   hello-world    "/hello"                 18 minutes ago   Exited (0) 18 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago     Exited (0) 19 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -p 8080:80 -d nginx
4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae
bradsimpson@Brads-MacBook-Air ~ % docker container run --name test -it alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS                      PORTS                    NAMES
11dab2b1b190   alpine         "sh"                     16 seconds ago       Exited (0) 7 seconds ago                             test
4a69088639b3   nginx          "/docker-entrypoint.…"   About a minute ago   Up About a minute           0.0.0.0:8080->80/tcp     nifty_banzai
ba4eb06017db   alpine         "/bin/sh"                3 minutes ago        Exited (0) 3 minutes ago                             heuristic_pike
1948c101aceb   nginx          "/docker-entrypoint.…"   9 minutes ago        Up 9 minutes                0.0.0.0:8000->80/tcp     nifty_ishizaka
ad6fe840b796   nginx          "/docker-entrypoint.…"   12 minutes ago       Exited (0) 11 minutes ago                            cool_container
818201d69e63   hello-world    "/hello"                 21 minutes ago       Exited (0) 21 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago         Exited (0) 22 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % echo hello world
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container run --rm --name greet_me ubuntu echo hello world
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
b2837baf7808: Pull complete 
Digest: sha256:6120be6a2b7ce665d0cbddc3ce6eae60fe94637c6a66985312d1f02f63cc0bcd
Status: Downloaded newer image for ubuntu:latest
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                    NAMES
11dab2b1b190   alpine         "sh"                     2 minutes ago    Exited (0) 2 minutes ago                             test
4a69088639b3   nginx          "/docker-entrypoint.…"   3 minutes ago    Up 3 minutes                0.0.0.0:8080->80/tcp     nifty_banzai
ba4eb06017db   alpine         "/bin/sh"                5 minutes ago    Exited (0) 5 minutes ago                             heuristic_pike
1948c101aceb   nginx          "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes               0.0.0.0:8000->80/tcp     nifty_ishizaka
ad6fe840b796   nginx          "/docker-entrypoint.…"   14 minutes ago   Exited (0) 13 minutes ago                            cool_container
818201d69e63   hello-world    "/hello"                 23 minutes ago   Exited (0) 23 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago     Exited (0) 24 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   7 minutes ago    Up 7 minutes    0.0.0.0:8080->80/tcp   nifty_banzai
1948c101aceb   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8000->80/tcp   nifty_ishizaka
bradsimpson@Brads-MacBook-Air ~ % docker container stop nifty_banzai 1948c101aceb
nifty_banzai
1948c101aceb
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                    NAMES
11dab2b1b190   alpine         "sh"                     7 minutes ago    Exited (0) 6 minutes ago                             test
4a69088639b3   nginx          "/docker-entrypoint.…"   8 minutes ago    Exited (0) 15 seconds ago                            nifty_banzai
ba4eb06017db   alpine         "/bin/sh"                10 minutes ago   Exited (0) 10 minutes ago                            heuristic_pike
1948c101aceb   nginx          "/docker-entrypoint.…"   15 minutes ago   Exited (0) 15 seconds ago                            nifty_ishizaka
ad6fe840b796   nginx          "/docker-entrypoint.…"   19 minutes ago   Exited (0) 17 minutes ago                            cool_container
818201d69e63   hello-world    "/hello"                 28 minutes ago   Exited (0) 28 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago     Exited (0) 29 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % docker container start  nifty_banzai
nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   9 minutes ago   Up 7 seconds   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container rm nifty_ishizaka
nifty_ishizaka
bradsimpson@Brads-MacBook-Air ~ % docker container ls                 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS              PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   10 minutes ago   Up About a minute   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                    NAMES
11dab2b1b190   alpine         "sh"                     8 minutes ago    Exited (0) 8 minutes ago                             test
4a69088639b3   nginx          "/docker-entrypoint.…"   10 minutes ago   Up About a minute           0.0.0.0:8080->80/tcp     nifty_banzai
ba4eb06017db   alpine         "/bin/sh"                12 minutes ago   Exited (0) 11 minutes ago                            heuristic_pike
ad6fe840b796   nginx          "/docker-entrypoint.…"   21 minutes ago   Exited (0) 19 minutes ago                            cool_container
818201d69e63   hello-world    "/hello"                 30 minutes ago   Exited (0) 30 minutes ago                            elastic_stonebraker
d20e329cdf7f   df9580143a75   "docker-entrypoint.s…"   17 hours ago     Exited (0) 31 minutes ago   0.0.0.0:3000->3000/tcp   patchstagram
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
11dab2b1b1909c5fbfd20bb8bb0b025ab58cab3a2e01c530fe9427e3dcce4911
ba4eb06017db2c2ea7d036fd918712f0a63f8af6dc4c49f25f3f32716ca67c40
ad6fe840b7964886721678a9165752c17e826c74bebd3faf3e7eca5cce80adc2
818201d69e63aed31c1eb6f292c238ccf876dc367d501d2db8e484dea751558d
d20e329cdf7ffbd1d7e927714ebd578030d75390594b000aa9ab9ca6d9652dca

Total reclaimed space: 178MB
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS              PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   10 minutes ago   Up About a minute   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch   latest    853467a132ef   17 hours ago   1.59GB
<none>                 <none>    df9580143a75   3 days ago     1.59GB
alpine                 latest    5053b247d78b   12 days ago    7.66MB
nginx                  latest    2d21d843073b   13 days ago    192MB
ubuntu                 latest    cfb01e8e3121   3 weeks ago    69.2MB
hello-world            latest    b038788ddb22   7 weeks ago    9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
f22c9d6b461b   bridge          bridge    local
0c4794c37db6   host            host      local
61b3161ebf7d   none            null      local
2274e2801027   patch_network   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker volume ls
DRIVER    VOLUME NAME
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it nifty_banzai
"docker container exec" requires at least 2 arguments.
See 'docker container exec --help'.

Usage:  docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]

Execute a command in a running container
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it nifty_banzai sh
# \ls
bin   dev		   docker-entrypoint.sh  home  media  opt   root  sbin	sys  usr
boot  docker-entrypoint.d  etc			 lib   mnt    proc  run   srv	tmp  var
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
4a69088639b3   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container inspect nifty_banzai
[
    {
        "Id": "4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae",
        "Created": "2023-06-27T15:24:45.753327135Z",
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
            "Pid": 5397,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-06-27T15:33:42.097174884Z",
            "FinishedAt": "2023-06-27T15:32:39.160111549Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/hostname",
        "HostsPath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/hosts",
        "LogPath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae-json.log",
        "Name": "/nifty_banzai",
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
                46,
                93
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
                "LowerDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a/merged",
                "UpperDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a/diff",
                "WorkDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "4a69088639b3",
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
            "SandboxID": "7ab1423637911cad0d769ab58fdd2640376275b366ea6ecff9e1c7314b042234",
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
            "SandboxKey": "/var/run/docker/netns/7ab142363791",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "ba5ffe86ab530b6305d7cf2033527305b2f99bcb136fa6001dd9a199f5f1eb01",
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
                    "NetworkID": "f22c9d6b461bc85e9b9fe365520691761f6b68dc896ae72d93a1bf2c8c6e1466",
                    "EndpointID": "ba5ffe86ab530b6305d7cf2033527305b2f99bcb136fa6001dd9a199f5f1eb01",
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
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch   latest    853467a132ef   17 hours ago   1.59GB
<none>                 <none>    df9580143a75   3 days ago     1.59GB
alpine                 latest    5053b247d78b   12 days ago    7.66MB
nginx                  latest    2d21d843073b   13 days ago    192MB
ubuntu                 latest    cfb01e8e3121   3 weeks ago    69.2MB
hello-world            latest    b038788ddb22   7 weeks ago    9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker image inspect nginx
[
    {
        "Id": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:593dac25b7733ffb7afe1a72649a43e574778bf025ad60514ef40f6b5d606247"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-06-14T03:47:04.608168367Z",
        "Container": "3d692c6bf8c27f8927a126f64dda01db9513712ef8b2f6e606dfb22e2bfba211",
        "ContainerConfig": {
            "Hostname": "3d692c6bf8c2",
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
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"nginx\" \"-g\" \"daemon off;\"]"
            ],
            "Image": "sha256:5b0110e5e828098bdd36b1f65802bd907a1bc04091213fb8b78645cc69f72ead",
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
            "Image": "sha256:5b0110e5e828098bdd36b1f65802bd907a1bc04091213fb8b78645cc69f72ead",
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
        "Architecture": "arm64",
        "Variant": "v8",
        "Os": "linux",
        "Size": 192298817,
        "VirtualSize": 192298817,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/merged",
                "UpperDir": "/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff",
                "WorkDir": "/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:28729e4ae0abb44b42af819e47380bb8cc20e05d94c9f241f52122a1144a4401",
                "sha256:9778a1e5c8724bdaa5f17fb130a6fd055ca7fce663f8ebeddf755b2025c0bb42",
                "sha256:a02619bcaf18f97f71e9b3cb04e78a76be5b67d00510b3dab523cd1f5f6f6245",
                "sha256:ef823dda6d4f6348b36eb5a0cecfbb9dc52a7d05dc9c52116bee854cdfc6be88",
                "sha256:e97ed8d349b812fc7726ecb304d237653bf8e495f7d2e2d3031d71f7a64e74d7",
                "sha256:79b41f6a1b71bf2da50e101be580edd14fc614dcb78d3636a6bfbfd6602318a4",
                "sha256:0f024290dd085b43aa4e75ee57598636d88ff4d02920bffc05b528051495d0be"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]

## Networking


Last login: Tue Jun 27 08:48:30 on ttys009
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
f22c9d6b461b   bridge          bridge    local
0c4794c37db6   host            host      local
61b3161ebf7d   none            null      local
2274e2801027   patch_network   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   27 minutes ago   Up 18 minutes   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container inspect nifty_banzai
[
    {
        "Id": "4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae",
        "Created": "2023-06-27T15:24:45.753327135Z",
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
            "Pid": 5397,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-06-27T15:33:42.097174884Z",
            "FinishedAt": "2023-06-27T15:32:39.160111549Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/hostname",
        "HostsPath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/hosts",
        "LogPath": "/var/lib/docker/containers/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae/4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae-json.log",
        "Name": "/nifty_banzai",
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
                46,
                93
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
                "LowerDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a/merged",
                "UpperDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a/diff",
                "WorkDir": "/var/lib/docker/overlay2/a414c75fb5ccd33a928b947fbc55871c0f8b0ca26408b1d4500b419f21d3954a/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "4a69088639b3",
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
            "SandboxID": "7ab1423637911cad0d769ab58fdd2640376275b366ea6ecff9e1c7314b042234",
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
            "SandboxKey": "/var/run/docker/netns/7ab142363791",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "ba5ffe86ab530b6305d7cf2033527305b2f99bcb136fa6001dd9a199f5f1eb01",
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
                    "NetworkID": "f22c9d6b461bc85e9b9fe365520691761f6b68dc896ae72d93a1bf2c8c6e1466",
                    "EndpointID": "ba5ffe86ab530b6305d7cf2033527305b2f99bcb136fa6001dd9a199f5f1eb01",
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
NETWORK ID     NAME            DRIVER    SCOPE
f22c9d6b461b   bridge          bridge    local
0c4794c37db6   host            host      local
61b3161ebf7d   none            null      local
2274e2801027   patch_network   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker network rm patch_network  
patch_network
bradsimpson@Brads-MacBook-Air ~ % docker network ls                
NETWORK ID     NAME      DRIVER    SCOPE
f22c9d6b461b   bridge    bridge    local
0c4794c37db6   host      host      local
61b3161ebf7d   none      null      local
bradsimpson@Brads-MacBook-Air ~ % docker network create --driver bridge taco_tuesday
64d8cbfca39b5503ee9415f5c4c71bc40792aed291159b7bc54defe8ece7506f
bradsimpson@Brads-MacBook-Air ~ % docker network ls                                 
NETWORK ID     NAME           DRIVER    SCOPE
f22c9d6b461b   bridge         bridge    local
0c4794c37db6   host           host      local
61b3161ebf7d   none           null      local
64d8cbfca39b   taco_tuesday   bridge    local
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   33 minutes ago   Up 24 minutes   0.0.0.0:8080->80/tcp   nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container stop nifty_banzai

nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                     PORTS     NAMES
4a69088639b3   nginx     "/docker-entrypoint.…"   33 minutes ago   Exited (0) 8 seconds ago             nifty_banzai
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c1 --network taco_tuesday nginx:alpine
Unable to find image 'nginx:alpine' locally
alpine: Pulling from library/nginx
edb6bdbacee9: Pull complete 
e7b9f8564496: Pull complete 
e6a8c530945d: Pull complete 
a31273f49e64: Pull complete 
4fbf2e3beac8: Pull complete 
467b5f1f71f7: Pull complete 
3a6c132398b3: Pull complete 
fca8748d6c5b: Pull complete 
Digest: sha256:2d194184b067db3598771b4cf326cfe6ad5051937ba1132b8b7d4b0184e0d0a6
Status: Downloaded newer image for nginx:alpine
23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c2 --network taco_tuesday nginx:alpine
40b4e98ba0124e274ecd1ffdc1b1ad44ef1967330afd288aceef0e21010360b6
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
40b4e98ba012   nginx:alpine   "/docker-entrypoint.…"   6 seconds ago    Up 6 seconds    80/tcp    c2
23c25e5d12ee   nginx:alpine   "/docker-entrypoint.…"   14 seconds ago   Up 13 seconds   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c3 nginx:alpine
a7d648e6e7a17849744083e1192d884315881cdefd693ff5a9ba63fb354463ce
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c4 nginx:alpine
43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c
bradsimpson@Brads-MacBook-Air ~ % docker container l

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Execute a command in a running container
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
  run         Create and run a new container from an image
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
43ed5f308648   nginx:alpine   "/docker-entrypoint.…"   7 seconds ago    Up 6 seconds    80/tcp    c4
a7d648e6e7a1   nginx:alpine   "/docker-entrypoint.…"   18 seconds ago   Up 17 seconds   80/tcp    c3
40b4e98ba012   nginx:alpine   "/docker-entrypoint.…"   51 seconds ago   Up 51 seconds   80/tcp    c2
23c25e5d12ee   nginx:alpine   "/docker-entrypoint.…"   59 seconds ago   Up 59 seconds   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c4
[
    {
        "Id": "43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c",
        "Created": "2023-06-27T16:01:49.372628262Z",
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
            "Pid": 8319,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-06-27T16:01:49.597468387Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c/hostname",
        "HostsPath": "/var/lib/docker/containers/43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c/hosts",
        "LogPath": "/var/lib/docker/containers/43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c/43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c-json.log",
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
                46,
                104
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
                "LowerDir": "/var/lib/docker/overlay2/3c011c6af81f4887cbea9543dde0cb6aeca505942435262e31189bb4cddbc637-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/3c011c6af81f4887cbea9543dde0cb6aeca505942435262e31189bb4cddbc637/merged",
                "UpperDir": "/var/lib/docker/overlay2/3c011c6af81f4887cbea9543dde0cb6aeca505942435262e31189bb4cddbc637/diff",
                "WorkDir": "/var/lib/docker/overlay2/3c011c6af81f4887cbea9543dde0cb6aeca505942435262e31189bb4cddbc637/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "43ed5f308648",
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
            "SandboxID": "c1aba0d7d4f997ba1b8d1b6ae92a201e1c64f5bdbf8704e6bd91379c75a3a524",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/c1aba0d7d4f9",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "d87d83301308203dde37e22aa9137e9d23a8f33fed88258a4e1f991b4b4db26a",
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
                    "NetworkID": "f22c9d6b461bc85e9b9fe365520691761f6b68dc896ae72d93a1bf2c8c6e1466",
                    "EndpointID": "d87d83301308203dde37e22aa9137e9d23a8f33fed88258a4e1f991b4b4db26a",
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
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c1
[
    {
        "Id": "23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02",
        "Created": "2023-06-27T16:00:57.099467751Z",
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
            "Pid": 7904,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-06-27T16:00:57.46779471Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02/hostname",
        "HostsPath": "/var/lib/docker/containers/23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02/hosts",
        "LogPath": "/var/lib/docker/containers/23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02/23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02-json.log",
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
            "ConsoleSize": [
                46,
                104
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
                "LowerDir": "/var/lib/docker/overlay2/06cd324366125ecb1e4e1b7c5da4fc00cc253f29ef31189542cc27f43d75e32d-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/06cd324366125ecb1e4e1b7c5da4fc00cc253f29ef31189542cc27f43d75e32d/merged",
                "UpperDir": "/var/lib/docker/overlay2/06cd324366125ecb1e4e1b7c5da4fc00cc253f29ef31189542cc27f43d75e32d/diff",
                "WorkDir": "/var/lib/docker/overlay2/06cd324366125ecb1e4e1b7c5da4fc00cc253f29ef31189542cc27f43d75e32d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "23c25e5d12ee",
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
            "SandboxID": "4639c94048fb0f4f115e1989c4ff0ea6ec82511578b46a29c242347070935a40",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/4639c94048fb",
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
                        "23c25e5d12ee"
                    ],
                    "NetworkID": "64d8cbfca39b5503ee9415f5c4c71bc40792aed291159b7bc54defe8ece7506f",
                    "EndpointID": "b07b947eca91cc81673ffe84db6a2cc4023da3958cb4014d38a3dda5a0b15812",
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
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
43ed5f308648   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
a7d648e6e7a1   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
40b4e98ba012   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c2
23c25e5d12ee   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
43ed5f308648   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
a7d648e6e7a1   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
40b4e98ba012   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
23c25e5d12ee   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 ash
/ # ping -c 4 c2
PING c2 (172.18.0.3): 56 data bytes
64 bytes from 172.18.0.3: seq=0 ttl=64 time=0.253 ms
64 bytes from 172.18.0.3: seq=1 ttl=64 time=0.159 ms
64 bytes from 172.18.0.3: seq=2 ttl=64 time=0.187 ms
64 bytes from 172.18.0.3: seq=3 ttl=64 time=0.176 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.159/0.193/0.253 ms
/ # ping -c 4 c3
ping: bad address 'c3'
/ # ping -c 4 c4
ping: bad address 'c4'
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c3 ash
/ # ping -c 5 c4
ping: bad address 'c4'
/ # ping -c 5 c1
ping: bad address 'c1'
/ # ping -c 5 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.543 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.154 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.130 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.134 ms
64 bytes from 172.17.0.3: seq=4 ttl=64 time=0.135 ms

--- 172.17.0.3 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 0.130/0.219/0.543 ms
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container stop c1 c2 c3 c4
c1
c2
c3
c4
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
43ed5f3086481b58967c488ecf05b7aa47bfedd787746d2dd89b64e6c01e6c3c
a7d648e6e7a17849744083e1192d884315881cdefd693ff5a9ba63fb354463ce
40b4e98ba0124e274ecd1ffdc1b1ad44ef1967330afd288aceef0e21010360b6
23c25e5d12ee2a20df29d5a596141e5d66f9d5bdd043156ba15a2b4f8e945f02
4a69088639b366f0a99ad6f9347431bdd9db38e33851d29dda66258958ede2ae

Total reclaimed space: 5.561kB
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % 


Volumes & Bind Mounts

Last login: Tue Jun 27 11:46:44 on ttys009
bradsimpson@Brads-MacBook-Air ~ % container container run - other flags --mount type=bind,source=/path/to/local/folder,target=/path/in/container 
zsh: command not found: container
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Library			Pictures
Documents		Movies			Public
Downloads		Music			requirements.txt
bradsimpson@Brads-MacBook-Air ~ % mkdir app
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Library			Pictures		requirements.txt
Documents		Movies			Public
Downloads		Music			app
bradsimpson@Brads-MacBook-Air ~ % cd app
bradsimpson@Brads-MacBook-Air app % touch index.html
bradsimpson@Brads-MacBook-Air app % \ls
index.html
bradsimpson@Brads-MacBook-Air app % nano index/html
bradsimpson@Brads-MacBook-Air app % nano index.html
bradsimpson@Brads-MacBook-Air app % \LS
index.html
bradsimpson@Brads-MacBook-Air app % docker container run -d --mount type=bind,source="$(pwd)",target=/usr/sahre/nginx/html -p 8000:80 nginx:alpine
f7bd8da0265c04258a20cefc96340ac8b1d5fd43a33eefaaa603a702150ee0e3
bradsimpson@Brads-MacBook-Air app % docker container ls                                             
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                  NAMES
f7bd8da0265c   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8000->80/tcp   inspiring_easley
bradsimpson@Brads-MacBook-Air app % docker container stop inspiring_easley
inspiring_easley
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % docker container run -d --mount type=bind,source="$(pwd)",target=/usr/share/nginx/html -p 8000:80 nginx:alpine
6757ebc75be164afe4cd578948677ccf1d5f1326fc119b0bb5563ef3dc5df30d
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
6757ebc75be1   nginx:alpine   "/docker-entrypoint.…"   39 seconds ago   Up 38 seconds   0.0.0.0:8000->80/tcp   pensive_mendel
bradsimpson@Brads-MacBook-Air app % docker container stop pensive_mendel

pensive_mendel
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air app % cd..                            
zsh: command not found: cd..
bradsimpson@Brads-MacBook-Air app % docker container run --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8000:80 nginx:alpine 
docker: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: /host_mnt/Users/bradsimpson/app/app.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air app % docker container run -d --mount type=bind,source="$(pwd)",target=/usr/share/nginx/html -p 8000:80 nginx:alpine
27e4eff593acc6306b41490005609fd6d20dc81cf6313e088f48d513b81f7d1f
bradsimpson@Brads-MacBook-Air app % docker container ls       
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
27e4eff593ac   nginx:alpine   "/docker-entrypoint.…"   54 seconds ago   Up 53 seconds   0.0.0.0:8000->80/tcp   dreamy_cori
bradsimpson@Brads-MacBook-Air app % docker container exec -ot pensive_mendel ash

unknown shorthand flag: 'o' in -ot
See 'docker container exec --help'.
bradsimpson@Brads-MacBook-Air app % docker container exec -it pensive_mendel ash

Error response from daemon: Container 6757ebc75be164afe4cd578948677ccf1d5f1326fc119b0bb5563ef3dc5df30d is not running
bradsimpson@Brads-MacBook-Air app % docker container ls                         
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                  NAMES
27e4eff593ac   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8000->80/tcp   dreamy_cori
bradsimpson@Brads-MacBook-Air app % docker container exec -it dreamy_cori ash              

/ # \ls
bin                   home                  proc                  sys
dev                   lib                   root                  tmp
docker-entrypoint.d   media                 run                   usr
docker-entrypoint.sh  mnt                   sbin                  var
etc                   opt                   srv
/ # cd usr\share
ash: cd: can't cd to usrshare: No such file or directory
/ # cd usr
/usr # \ls
bin    lib    local  sbin   share
/usr # cd share
/usr/share # \ls
GeoIP            ca-certificates  licenses         nginx            zoneinfo
X11              doc              man              udhcpc
apk              fontconfig       misc             xml
/usr/share # cd nginx/
/usr/share/nginx # cd html/
/usr/share/nginx/html # \ls
index.html
/usr/share/nginx/html # nano index.html
ash: nano: not found
/usr/share/nginx/html # apk add nano
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/main/aarch64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.17/community/aarch64/APKINDEX.tar.gz
(1/1) Installing nano (7.0-r0)
Executing busybox-1.35.0-r29.trigger
OK: 44 MiB in 63 packages
/usr/share/nginx/html # nano index.html
/usr/share/nginx/html # exit
bradsimpson@Brads-MacBook-Air app % nano index.html 
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker volume ls
DRIVER    VOLUME NAME
bradsimpson@Brads-MacBook-Air app % docker volume create taco_tuesday
taco_tuesday
bradsimpson@Brads-MacBook-Air app % docker volume ls                 
DRIVER    VOLUME NAME
local     taco_tuesday
bradsimpson@Brads-MacBook-Air app % docker pull postgres
Using default tag: latest
latest: Pulling from library/postgres
95039a22a7cc: Already exists 
72b83e03b5c2: Pull complete 
de8ceb62b1b0: Pull complete 
9e16ad653676: Pull complete 
0757b59384e8: Pull complete 
e6eadf7bc48c: Pull complete 
6a99aa4659fc: Pull complete 
1e71d99c61ce: Pull complete 
75d0c3c5b483: Pull complete 
a60f45d3d4d8: Pull complete 
4cfefb72ee99: Pull complete 
c95b581dac8e: Pull complete 
b4cb3065c98f: Pull complete 
Digest: sha256:7c0ee16b6a3b4403957ece2c186ff05c57097a557403ae5216ef1286e47c249c
Status: Downloaded newer image for postgres:latest
docker.io/library/postgres:latest
bradsimpson@Brads-MacBook-Air app % docker image ls
REPOSITORY             TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/patch   latest    853467a132ef   18 hours ago   1.59GB
<none>                 <none>    df9580143a75   3 days ago     1.59GB
nginx                  alpine    66bf2c914bf4   12 days ago    41MB
postgres               latest    11a95ab93cf5   12 days ago    433MB
alpine                 latest    5053b247d78b   12 days ago    7.66MB
nginx                  latest    2d21d843073b   13 days ago    192MB
ubuntu                 latest    cfb01e8e3121   3 weeks ago    69.2MB
hello-world            latest    b038788ddb22   7 weeks ago    9.14kB
bradsimpson@Brads-MacBook-Air app % docker image inspect postgres
[
    {
        "Id": "sha256:11a95ab93cf5794c4bb89ae2b7269a4663cc6696756aca8a2ce4860105184f96",
        "RepoTags": [
            "postgres:latest"
        ],
        "RepoDigests": [
            "postgres@sha256:7c0ee16b6a3b4403957ece2c186ff05c57097a557403ae5216ef1286e47c249c"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2023-06-14T21:07:24.254607687Z",
        "Container": "e2b391263727bd91e921205480df8c3dd0021e737de6491a0b7ab0a2dc7490a9",
        "ContainerConfig": {
            "Hostname": "e2b391263727",
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
                "PG_VERSION=15.3-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"postgres\"]"
            ],
            "Image": "sha256:9cc4b4dcd16aee3888b9a2e1d483f2344f67cce428159fe2dcfa38a130269f02",
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
                "PG_VERSION=15.3-1.pgdg120+1",
                "PGDATA=/var/lib/postgresql/data"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "sha256:9cc4b4dcd16aee3888b9a2e1d483f2344f67cce428159fe2dcfa38a130269f02",
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
        "Size": 433159328,
        "VirtualSize": 433159328,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/288f6317c63b02ced4bce72578d61cac8962cec3556bb03945758577b5622c19/diff:/var/lib/docker/overlay2/21890d284a06e646056b762093aa38868da2f1f636f70423d74e486f9df2d8df/diff:/var/lib/docker/overlay2/e4fdd137f40fe7a5aec41fdb17dc6cd9d17d632cb58a708c0e32c58472db1045/diff:/var/lib/docker/overlay2/90bdb32d739b289b351d7528f17a7cfc610c590bdc89c4d08f2f3ee0acb8768f/diff:/var/lib/docker/overlay2/69f47c9b44ed4fb6c97932587af77cbb9d4e61de55dbf1960819a284888d28f8/diff:/var/lib/docker/overlay2/175180c76619e2418532e5158857fe16dee71b0f3d8c1e81f32abc59dbd7eb79/diff:/var/lib/docker/overlay2/8e68a263d15172d409235515b384395f1896ff48b691fae2031f032b9836cc62/diff:/var/lib/docker/overlay2/2fb815ca91c4acd6ac0cf939690521364fcfd463f9a60d733ec529fd0f02fda0/diff:/var/lib/docker/overlay2/af2c683751bdbc07ea080b4c7840d2598b7866b6a008373e075393ee272f0151/diff:/var/lib/docker/overlay2/92bf6a14949dbbda8f8816d6a7edfed5f3188cc482ab293a0a6f47fe2a3c1d4f/diff:/var/lib/docker/overlay2/0835ecfb04eaeecf69e5cc688fda280ce0b5d5d91a5090c67f66b6deb06695e2/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/0a4b6906db0a476f99100b84da30116d39547c842c66796848bf9e2650a2e1e9/merged",
                "UpperDir": "/var/lib/docker/overlay2/0a4b6906db0a476f99100b84da30116d39547c842c66796848bf9e2650a2e1e9/diff",
                "WorkDir": "/var/lib/docker/overlay2/0a4b6906db0a476f99100b84da30116d39547c842c66796848bf9e2650a2e1e9/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:28729e4ae0abb44b42af819e47380bb8cc20e05d94c9f241f52122a1144a4401",
                "sha256:c042635585bd8b34be16f16d032868c3d113106bf4459487c832a7b39ce142b4",
                "sha256:5b0229845239b75c54974e4548b41ac30da7beadeffafd174fa900091ef8053d",
                "sha256:83b38388b03cbee2326190c7f071d20067a8155ec0d938c233b6a13db6b12db6",
                "sha256:134ca6824fbb72cbe3d7eb7c499054312ec9d6a5c08a1239b78c0c50eb42acd7",
                "sha256:5071efce4d46d55fffa4a20ba83e926e61c618721a5158bc269d98983ac1b7fc",
                "sha256:844bf44e2438035601bccf04fb640f42a161d6f4ea18337d76760301fccffc60",
                "sha256:efb8faff4aafd5b2a10f4f3294441e034b071066e2fd9d5a6d5a0e9ee1a3e4c4",
                "sha256:65f3994e4a5f64169bdababfa2a98bf04868de57389bb2f4e7091dba5e528e8a",
                "sha256:2e4362dcc298c365e4db9075bc72ca06ac8081fe87fc61aa7af91a992bad4b2f",
                "sha256:d9c3ebe18da6b3981b87d2084df2318640b7f7b9ab8a02590c54a046ceb96a53",
                "sha256:b18dd5920f4017fd86bc5f9b018693c3b085d19115fe8beca26bec59be85b445",
                "sha256:5685c619037a4d41f72e6adaa150fdfdb0f9a944c4bac06c4861ad0765785359"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker container run -p 5432:5432 -e POSTGRES_PASSWORD=password --name postgres -d --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Create and run a new container from an image
bradsimpson@Brads-MacBook-Air app % docker container run -p 5432:5432 -e POSTGRES_PASSWORD=password --name postgres -d --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data postgres
2738002371ba28be447e7ab23d10e3ea26efeaafc06b009bd63adff31737e366
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
2738002371ba   postgres       "docker-entrypoint.s…"   7 seconds ago    Up 6 seconds    0.0.0.0:5432->5432/tcp   postgres
27e4eff593ac   nginx:alpine   "/docker-entrypoint.…"   13 minutes ago   Up 12 minutes   0.0.0.0:8000->80/tcp     dreamy_cori
bradsimpson@Brads-MacBook-Air app % psql -p 5432 -h localhost -U postgres
zsh: command not found: psql
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres sh
# psql -p 5432 -h localhost -u postgres
/usr/lib/postgresql/15/bin/psql: invalid option -- 'u'
psql: hint: Try "psql --help" for more information.
# psql -p 5432 -h localhost -U postgres
psql (15.3 (Debian 15.3-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access 
privileges   
-----------+----------+----------+------------+------------+------------+-----------------+----------
-------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgr
es          +
           |          |          |            |            |            |                 | postgres=
CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgr
es          +
           |          |          |            |            |            |                 | postgres=
CTc/postgres
(3 rows)
































postgres=# CREATE DATABASE tacos WITH USER postgres;
ERROR:  syntax error at or near "USER"
LINE 1: CREATE DATABASE tacos WITH USER postgres;
                                   ^
postgres=# CREATE DATABASE tacos WITH OWNER postgres;
CREATE DATABASE
postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access 
privileges   
-----------+----------+----------+------------+------------+------------+-----------------+----------
-------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 tacos     | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgr
es          +
           |          |          |            |            |            |                 | postgres=
CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgr
es          +
           |          |          |            |            |            |                 | postgres=
CTc/postgres
(4 rows)






























postgres=# exit
# docker container ls
sh: 3: docker: not found
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
2738002371ba   postgres       "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    0.0.0.0:5432->5432/tcp   postgres
27e4eff593ac   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp     dreamy_cori
bradsimpson@Brads-MacBook-Air app % docker container stop postgres
postgres
bradsimpson@Brads-MacBook-Air app % docker container rm postgres
postgres
bradsimpson@Brads-MacBook-Air app % docker container run -p 5432:5432 -e POSTGRES_PASSWORD=password --name postgres2 -d --mount type=volume,source=taco_tuesday,target=/var/lib/postgresql/data postgres
a36aac87c7f8ed21ee71756990c11a6c1517eafcdd89cc39e604bf072553c6ce
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
a36aac87c7f8   postgres       "docker-entrypoint.s…"   5 seconds ago    Up 4 seconds    0.0.0.0:5432->5432/tcp   postgres2
27e4eff593ac   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   0.0.0.0:8000->80/tcp     dreamy_cori
bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres2 sh
# psql -p 5432 -h localhost -U postgres
psql (15.3 (Debian 15.3-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access 
privileges   
-----------+----------+----------+------------+------------+------------+-----------------+----------
-------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 tacos     | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgr
es          +
           |          |          |            |            |            |                 | postgres=
CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgr
es          +
           |          |          |            |            |            |                 | postgres=
CTc/postgres
(4 rows)


























postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % '




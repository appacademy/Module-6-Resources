# CONTAINER COMMANDS


Last login: Thu Jul 13 18:40:28 on ttys003
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
REPOSITORY                  TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/taco_react   latest    aea6ddf0f44b   3 weeks ago    569MB
<none>                      <none>    df9580143a75   4 weeks ago    1.59GB
nginx                       alpine    66bf2c914bf4   5 weeks ago    41MB
postgres                    latest    11a95ab93cf5   5 weeks ago    433MB
alpine                      latest    5053b247d78b   5 weeks ago    7.66MB
nginx                       latest    2d21d843073b   5 weeks ago    192MB
ubuntu                      latest    cfb01e8e3121   7 weeks ago    69.2MB
hello-world                 latest    b038788ddb22   2 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker container run -flags image-name options/commands
unknown shorthand flag: 'f' in -flags
See 'docker container run --help'.
bradsimpson@Brads-MacBook-Air ~ % \clear



bradsimpson@Brads-MacBook-Air ~ %                     
bradsimpson@Brads-MacBook-Air ~ % \cleart
zsh: command not found: cleart
bradsimpson@Brads-MacBook-Air ~ % \clear 

bradsimpson@Brads-MacBook-Air ~ % docker container run --name first -p 8000:80 nginx 
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/07/25 15:16:35 [notice] 1#1: using the "epoll" event method
2023/07/25 15:16:35 [notice] 1#1: nginx/1.25.1
2023/07/25 15:16:35 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2023/07/25 15:16:35 [notice] 1#1: OS: Linux 5.15.49-linuxkit-pr
2023/07/25 15:16:35 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2023/07/25 15:16:35 [notice] 1#1: start worker processes
2023/07/25 15:16:35 [notice] 1#1: start worker process 29
2023/07/25 15:16:35 [notice] 1#1: start worker process 30
2023/07/25 15:16:35 [notice] 1#1: start worker process 31
2023/07/25 15:16:35 [notice] 1#1: start worker process 32
172.17.0.1 - - [25/Jul/2023:15:16:58 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [25/Jul/2023:15:16:58 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8000/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
2023/07/25 15:16:58 [error] 29#29: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8000", referrer: "http://localhost:8000/"
172.17.0.1 - - [25/Jul/2023:15:17:13 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [25/Jul/2023:15:17:14 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
172.17.0.1 - - [25/Jul/2023:15:17:14 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36" "-"
^C2023/07/25 15:17:53 [notice] 1#1: signal 2 (SIGINT) received, exiting
2023/07/25 15:17:53 [notice] 31#31: exiting
2023/07/25 15:17:53 [notice] 31#31: exit
2023/07/25 15:17:53 [notice] 29#29: exiting
2023/07/25 15:17:53 [notice] 29#29: exit
2023/07/25 15:17:53 [notice] 32#32: exiting
2023/07/25 15:17:53 [notice] 32#32: exit
2023/07/25 15:17:53 [notice] 30#30: exiting
2023/07/25 15:17:53 [notice] 30#30: exit
2023/07/25 15:17:53 [notice] 1#1: signal 17 (SIGCHLD) received from 32
2023/07/25 15:17:53 [notice] 1#1: worker process 32 exited with code 0
2023/07/25 15:17:53 [notice] 1#1: signal 29 (SIGIO) received
2023/07/25 15:17:53 [notice] 1#1: signal 17 (SIGCHLD) received from 29
2023/07/25 15:17:53 [notice] 1#1: worker process 29 exited with code 0
2023/07/25 15:17:53 [notice] 1#1: worker process 31 exited with code 0
2023/07/25 15:17:53 [notice] 1#1: signal 29 (SIGIO) received
2023/07/25 15:17:53 [notice] 1#1: signal 17 (SIGCHLD) received from 31
2023/07/25 15:17:53 [notice] 1#1: signal 17 (SIGCHLD) received from 30
2023/07/25 15:17:53 [notice] 1#1: worker process 30 exited with code 0
2023/07/25 15:17:53 [notice] 1#1: exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                      PORTS     NAMES
9d437b355724   nginx         "/docker-entrypoint.…"   About a minute ago   Exited (0) 34 seconds ago             first
38ba8606864d   hello-world   "/hello"                 12 minutes ago       Exited (0) 12 minutes ago             priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -p 8000:80 -d --rm nginx
3499e0763ba1c7e7673471c4d7d4a1ea637f349b0a10fe37d8493ace751e0f4d
bradsimpson@Brads-MacBook-Air ~ % docker contains ls
docker: 'contains' is not a docker command.
See 'docker --help'
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
3499e0763ba1   nginx     "/docker-entrypoint.…"   18 seconds ago   Up 17 seconds   0.0.0.0:8000->80/tcp   clever_mclaren
bradsimpson@Brads-MacBook-Air ~ % docker container run -it --name alpine alpine sh
/ # \ls
bin    etc    lib    mnt    proc   run    srv    tmp    var
dev    home   media  opt    root   sbin   sys    usr
/ # cd bin/
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
/bin # exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                  NAMES
3499e0763ba1   nginx     "/docker-entrypoint.…"   3 minutes ago   Up 3 minutes   0.0.0.0:8000->80/tcp   clever_mclaren
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS                      PORTS                  NAMES
68ec539036e4   alpine        "sh"                     About a minute ago   Exited (0) 16 seconds ago                          alpine
3499e0763ba1   nginx         "/docker-entrypoint.…"   3 minutes ago        Up 3 minutes                0.0.0.0:8000->80/tcp   clever_mclaren
9d437b355724   nginx         "/docker-entrypoint.…"   8 minutes ago        Exited (0) 6 minutes ago                           first
38ba8606864d   hello-world   "/hello"                 18 minutes ago       Exited (0) 18 minutes ago                          priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -p 8080:80 -d nginx
89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   16 seconds ago   Up 15 seconds   0.0.0.0:8080->80/tcp   recursing_murdock
3499e0763ba1   nginx     "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes    0.0.0.0:8000->80/tcp   clever_mclaren
bradsimpson@Brads-MacBook-Air ~ % docker container run --name test -it alpine sh 
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container run --name greet_me --rm ubuntu echo hello world
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
b76c1ef02635   alpine        "sh"                     2 minutes ago    Exited (0) 2 minutes ago                           test
89fd711280e8   nginx         "/docker-entrypoint.…"   4 minutes ago    Up 4 minutes                0.0.0.0:8080->80/tcp   recursing_murdock
68ec539036e4   alpine        "sh"                     8 minutes ago    Exited (0) 7 minutes ago                           alpine
3499e0763ba1   nginx         "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes               0.0.0.0:8000->80/tcp   clever_mclaren
9d437b355724   nginx         "/docker-entrypoint.…"   15 minutes ago   Exited (0) 14 minutes ago                          first
38ba8606864d   hello-world   "/hello"                 25 minutes ago   Exited (0) 25 minutes ago                          priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/taco_react   latest    aea6ddf0f44b   3 weeks ago    569MB
<none>                      <none>    df9580143a75   4 weeks ago    1.59GB
nginx                       alpine    66bf2c914bf4   5 weeks ago    41MB
postgres                    latest    11a95ab93cf5   5 weeks ago    433MB
alpine                      latest    5053b247d78b   5 weeks ago    7.66MB
nginx                       latest    2d21d843073b   5 weeks ago    192MB
ubuntu                      latest    cfb01e8e3121   7 weeks ago    69.2MB
hello-world                 latest    b038788ddb22   2 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   5 minutes ago    Up 5 minutes    0.0.0.0:8080->80/tcp   recursing_murdock
3499e0763ba1   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes   0.0.0.0:8000->80/tcp   clever_mclaren
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   0.0.0.0:8080->80/tcp   recursing_murdock
3499e0763ba1   nginx     "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp   clever_mclaren
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
b76c1ef02635   alpine        "sh"                     9 minutes ago    Exited (0) 9 minutes ago                           test
89fd711280e8   nginx         "/docker-entrypoint.…"   11 minutes ago   Up 11 minutes               0.0.0.0:8080->80/tcp   recursing_murdock
68ec539036e4   alpine        "sh"                     14 minutes ago   Exited (0) 13 minutes ago                          alpine
3499e0763ba1   nginx         "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes               0.0.0.0:8000->80/tcp   clever_mclaren
9d437b355724   nginx         "/docker-entrypoint.…"   21 minutes ago   Exited (0) 20 minutes ago                          first
38ba8606864d   hello-world   "/hello"                 32 minutes ago   Exited (0) 32 minutes ago                          priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/taco_react   latest    aea6ddf0f44b   3 weeks ago    569MB
<none>                      <none>    df9580143a75   4 weeks ago    1.59GB
nginx                       alpine    66bf2c914bf4   5 weeks ago    41MB
postgres                    latest    11a95ab93cf5   5 weeks ago    433MB
alpine                      latest    5053b247d78b   5 weeks ago    7.66MB
nginx                       latest    2d21d843073b   5 weeks ago    192MB
ubuntu                      latest    cfb01e8e3121   7 weeks ago    69.2MB
hello-world                 latest    b038788ddb22   2 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
200128a29a77   bridge         bridge    local
0c4794c37db6   host           host      local
61b3161ebf7d   none           null      local
64d8cbfca39b   taco_tuesday   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker volume ls
DRIVER    VOLUME NAME
local     taco_tuesday
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   12 minutes ago   Up 12 minutes   0.0.0.0:8080->80/tcp   recursing_murdock
3499e0763ba1   nginx     "/docker-entrypoint.…"   18 minutes ago   Up 18 minutes   0.0.0.0:8000->80/tcp   clever_mclaren
bradsimpson@Brads-MacBook-Air ~ % docker container stop recursing_murdock 3499e0763ba1
recursing_murdock
3499e0763ba1
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
b76c1ef02635   alpine        "sh"                     11 minutes ago   Exited (0) 11 minutes ago             test
89fd711280e8   nginx         "/docker-entrypoint.…"   13 minutes ago   Exited (0) 22 seconds ago             recursing_murdock
68ec539036e4   alpine        "sh"                     16 minutes ago   Exited (0) 16 minutes ago             alpine
9d437b355724   nginx         "/docker-entrypoint.…"   23 minutes ago   Exited (0) 22 minutes ago             first
38ba8606864d   hello-world   "/hello"                 34 minutes ago   Exited (0) 34 minutes ago             priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % docker container ls -la
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                      PORTS     NAMES
b76c1ef02635   alpine    "sh"      11 minutes ago   Exited (0) 11 minutes ago             test
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a 
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS     NAMES
b76c1ef02635   alpine        "sh"                     11 minutes ago   Exited (0) 11 minutes ago             test
89fd711280e8   nginx         "/docker-entrypoint.…"   13 minutes ago   Exited (0) 33 seconds ago             recursing_murdock
68ec539036e4   alpine        "sh"                     17 minutes ago   Exited (0) 16 minutes ago             alpine
9d437b355724   nginx         "/docker-entrypoint.…"   24 minutes ago   Exited (0) 22 minutes ago             first
38ba8606864d   hello-world   "/hello"                 34 minutes ago   Exited (0) 34 minutes ago             priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % docker container start recursing_murdock
recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % docker container ls                     
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   13 minutes ago   Up 6 seconds   0.0.0.0:8080->80/tcp   recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS                      PORTS                  NAMES
b76c1ef02635   alpine        "sh"                     13 minutes ago   Exited (0) 12 minutes ago                          test
89fd711280e8   nginx         "/docker-entrypoint.…"   14 minutes ago   Up 50 seconds               0.0.0.0:8080->80/tcp   recursing_murdock
68ec539036e4   alpine        "sh"                     18 minutes ago   Exited (0) 17 minutes ago                          alpine
9d437b355724   nginx         "/docker-entrypoint.…"   25 minutes ago   Exited (0) 24 minutes ago                          first
38ba8606864d   hello-world   "/hello"                 35 minutes ago   Exited (0) 35 minutes ago                          priceless_elbakyan
bradsimpson@Brads-MacBook-Air ~ % docker container rm hello-world
Error response from daemon: No such container: hello-world
bradsimpson@Brads-MacBook-Air ~ % docker container rm 38ba8606864d
38ba8606864d
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a          
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS                  NAMES
b76c1ef02635   alpine    "sh"                     13 minutes ago   Exited (0) 13 minutes ago                          test
89fd711280e8   nginx     "/docker-entrypoint.…"   15 minutes ago   Up About a minute           0.0.0.0:8080->80/tcp   recursing_murdock
68ec539036e4   alpine    "sh"                     19 minutes ago   Exited (0) 18 minutes ago                          alpine
9d437b355724   nginx     "/docker-entrypoint.…"   26 minutes ago   Exited (0) 24 minutes ago                          first
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
b76c1ef02635395527c45bfb7a375bcba4c52d35a13e3379a2994e221314380e
68ec539036e4bc308d35cdb3f71eba43e1cbcd60eb1019b9578893338989d753
9d437b3557249b627ebe2f314ba6b4bcfdeb6cc17f4386aedae1447e899138a3

Total reclaimed space: 1.119kB
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED        SIZE
bradsimpson213/taco_react   latest    aea6ddf0f44b   3 weeks ago    569MB
<none>                      <none>    df9580143a75   4 weeks ago    1.59GB
nginx                       alpine    66bf2c914bf4   5 weeks ago    41MB
postgres                    latest    11a95ab93cf5   5 weeks ago    433MB
alpine                      latest    5053b247d78b   5 weeks ago    7.66MB
nginx                       latest    2d21d843073b   5 weeks ago    192MB
ubuntu                      latest    cfb01e8e3121   7 weeks ago    69.2MB
hello-world                 latest    b038788ddb22   2 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   17 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it recursing_murdock sh
# \ls
bin   dev		   docker-entrypoint.sh  home  media  opt   root  sbin	sys  usr
boot  docker-entrypoint.d  etc			 lib   mnt    proc  run   srv	tmp  var
# cd usr
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share
# \ls
X11		 common-licenses  dpkg	      java	   man	       pam-configs  terminfo
base-files	 debconf	  fontconfig  keyrings	   maven-repo  perl5	    util-linux
base-passwd	 debianutils	  fonts       libc-bin	   menu        pixmaps	    xml
bash-completion  dict		  gcc	      libgcrypt20  misc        polkit-1     zoneinfo
bug		 doc		  gdb	      lintian	   nginx       readline     zsh
ca-certificates  doc-base	  info	      locale	   pam	       tabset
# cd nginx
# \ls
html
# cd html	
# \ls
50x.html  index.html
# exit
bradsimpson@Brads-MacBook-Air ~ % 


# NETWORKING


Last login: Tue Jul 25 11:49:40 on ttys007
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
200128a29a77   bridge         bridge    local
0c4794c37db6   host           host      local
61b3161ebf7d   none           null      local
64d8cbfca39b   taco_tuesday   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   33 minutes ago   Up 19 minutes   0.0.0.0:8080->80/tcp   recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % docker container inspect recursing_murdock
[
    {
        "Id": "89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053",
        "Created": "2023-07-25T15:27:31.200017552Z",
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
            "Pid": 7106,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-07-25T15:41:20.11224413Z",
            "FinishedAt": "2023-07-25T15:40:11.72322771Z"
        },
        "Image": "sha256:2d21d843073b4df6a03022861da4cb59f7116c864fe90b3b5db3b90e1ce932d3",
        "ResolvConfPath": "/var/lib/docker/containers/89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053/hostname",
        "HostsPath": "/var/lib/docker/containers/89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053/hosts",
        "LogPath": "/var/lib/docker/containers/89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053/89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053-json.log",
        "Name": "/recursing_murdock",
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
                42,
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
                "LowerDir": "/var/lib/docker/overlay2/89f7703ec4bb98dbec4435b1799eb261e5f1e63f573d40ecc47ddeec860e829f-init/diff:/var/lib/docker/overlay2/80c0d951ea84b8f3270723a20f2f529241dbbd45fb2622fa3c6b618e3325dfb5/diff:/var/lib/docker/overlay2/11cb118caa40a3099df7a324cc18c7423112edae245447848f6ab12ec357081f/diff:/var/lib/docker/overlay2/18ecb8b555fd5d03131e2766662964c3b83c9938e9aaec68e440b1000fac0f11/diff:/var/lib/docker/overlay2/78cf9c681ec67cbb61ce143084a2b197f86e2192dd6ce86a48554f53cbbb0f5a/diff:/var/lib/docker/overlay2/409e2bf2e463d93ce887a4c6a07ec018b4f0b6210aa94d9ce84f6285b8f7b340/diff:/var/lib/docker/overlay2/506f25698e9ff48f088110b5dd62fe113a2895206f40b29aec16846d90cd7713/diff:/var/lib/docker/overlay2/aff10c7882ab3ca8e994823de96214ef8d937e9b85c1204753a12d5690f391c5/diff",
                "MergedDir": "/var/lib/docker/overlay2/89f7703ec4bb98dbec4435b1799eb261e5f1e63f573d40ecc47ddeec860e829f/merged",
                "UpperDir": "/var/lib/docker/overlay2/89f7703ec4bb98dbec4435b1799eb261e5f1e63f573d40ecc47ddeec860e829f/diff",
                "WorkDir": "/var/lib/docker/overlay2/89f7703ec4bb98dbec4435b1799eb261e5f1e63f573d40ecc47ddeec860e829f/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "89fd711280e8",
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
            "SandboxID": "1c56ed3b5c0d12d10858d9fae9f15da97e809f23f198606012c01acf83b75b71",
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
            "SandboxKey": "/var/run/docker/netns/1c56ed3b5c0d",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "5fa72ba9bab6d74726b5dd4a595596f926af67b8b8b45084818a29bb8cc8823f",
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
                    "NetworkID": "200128a29a776b2e92291752807a4c0de456977f1667b495ffcf738d2872dbcf",
                    "EndpointID": "5fa72ba9bab6d74726b5dd4a595596f926af67b8b8b45084818a29bb8cc8823f",
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
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   34 minutes ago   Up 21 minutes   0.0.0.0:8080->80/tcp   recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % docker network ls  
NETWORK ID     NAME           DRIVER    SCOPE
200128a29a77   bridge         bridge    local
0c4794c37db6   host           host      local
61b3161ebf7d   none           null      local
64d8cbfca39b   taco_tuesday   bridge    local
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
bradsimpson@Brads-MacBook-Air ~ % docker network ls
NETWORK ID     NAME           DRIVER    SCOPE
200128a29a77   bridge         bridge    local
0c4794c37db6   host           host      local
61b3161ebf7d   none           null      local
64d8cbfca39b   taco_tuesday   bridge    local
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker network create --driver bridge my_network
2be63f87cace85209b27fc8799b15f6bcb436bfb2d4df53f359605f1b1576619
bradsimpson@Brads-MacBook-Air ~ % docker network ls                               
NETWORK ID     NAME           DRIVER    SCOPE
200128a29a77   bridge         bridge    local
0c4794c37db6   host           host      local
2be63f87cace   my_network     bridge    local
61b3161ebf7d   none           null      local
64d8cbfca39b   taco_tuesday   bridge    local
bradsimpson@Brads-MacBook-Air ~ % docker network rm taco_tuesday
taco_tuesday
bradsimpson@Brads-MacBook-Air ~ % docker network ls             
NETWORK ID     NAME         DRIVER    SCOPE
200128a29a77   bridge       bridge    local
0c4794c37db6   host         host      local
2be63f87cace   my_network   bridge    local
61b3161ebf7d   none         null      local
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
89fd711280e8   nginx     "/docker-entrypoint.…"   42 minutes ago   Up 28 minutes   0.0.0.0:8080->80/tcp   recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % docker container stop recursing_murdock

recursing_murdock
bradsimpson@Brads-MacBook-Air ~ % docker container ls                    
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c1 --network my_network nginx:alpine
0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c2 --network my_network nginx:alpine 
96c8bd783d13218df7159db1b054315f682ec85116a89852125f5caf16a26c63
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
96c8bd783d13   nginx:alpine   "/docker-entrypoint.…"   4 seconds ago    Up 4 seconds    80/tcp    c2
0adcb8cf7b34   nginx:alpine   "/docker-entrypoint.…"   13 seconds ago   Up 13 seconds   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c1
[
    {
        "Id": "0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d",
        "Created": "2023-07-25T16:11:46.024453795Z",
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
            "Pid": 11211,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-07-25T16:11:46.207695295Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d/hostname",
        "HostsPath": "/var/lib/docker/containers/0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d/hosts",
        "LogPath": "/var/lib/docker/containers/0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d/0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d-json.log",
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
                46,
                99
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
                "LowerDir": "/var/lib/docker/overlay2/e306ff120674b2111de8bff6f4a509441da964f9d8f506e43f693684e33400c2-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/e306ff120674b2111de8bff6f4a509441da964f9d8f506e43f693684e33400c2/merged",
                "UpperDir": "/var/lib/docker/overlay2/e306ff120674b2111de8bff6f4a509441da964f9d8f506e43f693684e33400c2/diff",
                "WorkDir": "/var/lib/docker/overlay2/e306ff120674b2111de8bff6f4a509441da964f9d8f506e43f693684e33400c2/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "0adcb8cf7b34",
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
            "SandboxID": "83772fabe4d2cb34719936d2eb206fc829b2f19edda0f2437f3c3b0a1f87cb1d",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/83772fabe4d2",
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
                        "0adcb8cf7b34"
                    ],
                    "NetworkID": "2be63f87cace85209b27fc8799b15f6bcb436bfb2d4df53f359605f1b1576619",
                    "EndpointID": "039f19cce2b104256a8073e8821bf58b772da0bb715e3f0c45dba87e080b929d",
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
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c3 nginx:alpine
2dd387522d0dedf2b15356985a6d613dd80798a56f6ab57c2bd70a4a7fa29d8c
bradsimpson@Brads-MacBook-Air ~ % docker container run -d --name c4 nginx:alpine 
98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd
bradsimpson@Brads-MacBook-Air ~ % docker container inspect c4
[
    {
        "Id": "98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd",
        "Created": "2023-07-25T16:13:24.442895382Z",
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
            "Pid": 11768,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-07-25T16:13:24.644682716Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:66bf2c914bf4d0aac4b62f09f9f74ad35898d613024a0f2ec94dca9e79fac6ea",
        "ResolvConfPath": "/var/lib/docker/containers/98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd/hostname",
        "HostsPath": "/var/lib/docker/containers/98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd/hosts",
        "LogPath": "/var/lib/docker/containers/98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd/98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd-json.log",
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
                99
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
                "LowerDir": "/var/lib/docker/overlay2/b3da8bab3a76773f266aba4b09d350cd93e67fb4e66fdfb8fe589ede724e3f8d-init/diff:/var/lib/docker/overlay2/647a1f9e4c9b6c7373dda8cc6bfaf043643937900e08999038352818a01cd05c/diff:/var/lib/docker/overlay2/24725ff88ecb44d283bed4fbaa517a5e0e5cbae124c0607064a08e01403b6452/diff:/var/lib/docker/overlay2/42fce0a44605c073f0f80eab7e94426685255d5b9cf53811f57b22aabb2e5787/diff:/var/lib/docker/overlay2/343ffb4ee390b1071933b39cc22e679d0196b73f19fa8b10c72873bfe77effaf/diff:/var/lib/docker/overlay2/e50487c91c51ba1602a6c8776b58b5383a37f6b14f249736a87588f2a831aa60/diff:/var/lib/docker/overlay2/c45ae8da3e73d60ad3833e00105d832c8252039e8f0b0ed181644f936c01d6f9/diff:/var/lib/docker/overlay2/3e6a64f7d286c79f617a6adc7832a2fdddee4bd877816812952da86c482edfe8/diff:/var/lib/docker/overlay2/ead025bc032cd2b273c109b69f2dc045b12f5474a097ee4c2f59525d0d62398d/diff",
                "MergedDir": "/var/lib/docker/overlay2/b3da8bab3a76773f266aba4b09d350cd93e67fb4e66fdfb8fe589ede724e3f8d/merged",
                "UpperDir": "/var/lib/docker/overlay2/b3da8bab3a76773f266aba4b09d350cd93e67fb4e66fdfb8fe589ede724e3f8d/diff",
                "WorkDir": "/var/lib/docker/overlay2/b3da8bab3a76773f266aba4b09d350cd93e67fb4e66fdfb8fe589ede724e3f8d/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "98bbb3b4e384",
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
            "SandboxID": "b9728ac3b7bc4d4b089f0756a5d65023b10541cc7ec906733ed7621391d8bdbe",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/b9728ac3b7bc",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "7ba81a59c9046bb4104fc71b4ba12a409da7f41d3425b914ceec15955c5fa7e6",
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
                    "NetworkID": "200128a29a776b2e92291752807a4c0de456977f1667b495ffcf738d2872dbcf",
                    "EndpointID": "7ba81a59c9046bb4104fc71b4ba12a409da7f41d3425b914ceec15955c5fa7e6",
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

/ # exit
bradsimpson@Brads-MacBook-Air ~ % \clear







bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
98bbb3b4e384   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   80/tcp    c4
2dd387522d0d   nginx:alpine   "/docker-entrypoint.…"   17 minutes ago   Up 17 minutes   80/tcp    c3
96c8bd783d13   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   80/tcp    c2
0adcb8cf7b34   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container stop 98bbb3b4e384 2dd387522d0d
98bbb3b4e384
2dd387522d0d
bradsimpson@Brads-MacBook-Air ~ % docker container ls                            
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS     NAMES
96c8bd783d13   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   80/tcp    c2
0adcb8cf7b34   nginx:alpine   "/docker-entrypoint.…"   19 minutes ago   Up 19 minutes   80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container stop 96c8bd783d13 0adcb8cf7b34  
96c8bd783d13
0adcb8cf7b34
bradsimpson@Brads-MacBook-Air ~ % \clear


#  Bind Mounts


bradsimpson@Brads-MacBook-Air ~ % docker volume ls
DRIVER    VOLUME NAME
local     taco_tuesday
bradsimpson@Brads-MacBook-Air ~ % docker container run --mount type=bind,source=/app/public,target=absolute/path/in/container image-name commands
docker: Error response from daemon: invalid mount config for type "bind": invalid mount path: 'absolute/path/in/container' mount path must be absolute.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air ~ % \ls
Desktop			Library			Pictures		requirements.txt
Documents		Movies			Public
Downloads		Music			app
bradsimpson@Brads-MacBook-Air ~ % cd app
bradsimpson@Brads-MacBook-Air app % \ls     
index.html
bradsimpson@Brads-MacBook-Air app % nano index.html
bradsimpson@Brads-MacBook-Air app % cd //
bradsimpson@Brads-MacBook-Air / % docker container run -d --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8000:80 nginx:alpine 
docker: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: //app.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air / % docker container run -d --mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html -p 8000:80 nginx:alpine
docker: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: //app.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air / % docker container run -d --mount type=bind,source=/app,target=/usr/share/nginx/html -p 8000:80 nginx:alpine 
docker: Error response from daemon: invalid mount config for type "bind": bind source path does not exist: /app.
See 'docker run --help'.
bradsimpson@Brads-MacBook-Air / % \ls                                                                     
Applications	Users		cores		home		sbin		var
Library		Volumes		dev		opt		tmp
System		bin		etc		private		usr
bradsimpson@Brads-MacBook-Air / % cd app
cd: no such file or directory: app
bradsimpson@Brads-MacBook-Air / % \ls
Applications	Users		cores		home		sbin		var
Library		Volumes		dev		opt		tmp
System		bin		etc		private		usr
bradsimpson@Brads-MacBook-Air / % \ls
Applications	Users		cores		home		sbin		var
Library		Volumes		dev		opt		tmp
System		bin		etc		private		usr
bradsimpson@Brads-MacBook-Air / %       

# docker container ls
sh: 3: docker: not found
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
a8556b448a84   postgres       "docker-entrypoint.s…"   2 minutes ago    Up 2 minutes    0.0.0.0:5432->5432/tcp   pg1
c27d888a7923   nginx:alpine   "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes   0.0.0.0:8000->80/tcp     hopeful_pasteur
bradsimpson@Brads-MacBook-Air app % docker container stop pg1
pg1
bradsimpson@Brads-MacBook-Air app % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS                      PORTS                  NAMES
a8556b448a84   postgres       "docker-entrypoint.s…"   2 minutes ago    Exited (0) 8 seconds ago                           pg1
51eca7299eab   postgres       "docker-entrypoint.s…"   3 minutes ago    Exited (0) 3 minutes ago                           postgres
dcd5dbd24737   postgres       "docker-entrypoint.s…"   4 minutes ago    Exited (1) 4 minutes ago                           postgres1
c27d888a7923   nginx:alpine   "/docker-entrypoint.…"   15 minutes ago   Up 15 minutes               0.0.0.0:8000->80/tcp   hopeful_pasteur
98bbb3b4e384   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Exited (0) 27 minutes ago                          c4
2dd387522d0d   nginx:alpine   "/docker-entrypoint.…"   45 minutes ago   Exited (0) 27 minutes ago                          c3
96c8bd783d13   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Exited (0) 27 minutes ago                          c2
0adcb8cf7b34   nginx:alpine   "/docker-entrypoint.…"   47 minutes ago   Exited (0) 27 minutes ago                          c1
89fd711280e8   nginx          "/docker-entrypoint.…"   2 hours ago      Exited (0) 48 minutes ago                          recursing_murdock
bradsimpson@Brads-MacBook-Air app % docker container prune 
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
a8556b448a84a645e9d37e4681561641fc135a24df8e6c9904bc37b7d04e9058
51eca7299eab58aa6719314949f8482eb7e7a9315d37a3fb84e3b8074f94f350
dcd5dbd247371299ea10354805ef34148411f66ae16ab830bc7fac13460b238a
98bbb3b4e3845db41fe23534eb92545de36ca891dce26d099a0fea9f4d9a7ccd
2dd387522d0dedf2b15356985a6d613dd80798a56f6ab57c2bd70a4a7fa29d8c
96c8bd783d13218df7159db1b054315f682ec85116a89852125f5caf16a26c63
0adcb8cf7b34eaeedb68791c5aa82f43364b663cd91690344f3d62be297cf08d
89fd711280e87f53686b8a808b35dbca8dff74392d3da6c902380f7741f02053

Total reclaimed space: 5.667kB
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % docker container s

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


# Volumes


Run 'docker container COMMAND --help' for more information on a command.
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
c27d888a7923   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp   hopeful_pasteur
bradsimpson@Brads-MacBook-Air app % docker container run -p 5432:5432 -e POSRTGRES_PASSWORD=password --name pg2 -d --mount type=volume,source=my_volume,target=/var/lib/postgresql/data postgres 
d303cd783b5ce6e67a62f221a76a185e354cf365686ecd05865fdf540be77eff
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                    NAMES
d303cd783b5c   postgres       "docker-entrypoint.s…"   5 seconds ago    Up 5 seconds    0.0.0.0:5432->5432/tcp   pg2
c27d888a7923   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago   Up 16 minutes   0.0.0.0:8000->80/tcp     hopeful_pasteur
bradsimpson@Brads-MacBook-Air app % docker container exec -it pg2 sh
# psql -p 5432 -h localhost -U postgres
psql (15.3 (Debian 15.3-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                  List of databases
     Name     |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   
Access privileges   
--------------+----------+----------+------------+------------+------------+-----------------+---
--------------------
 postgres     | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tuesday | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c
/postgres          +
              |          |          |            |            |            |                 | po
stgres=CTc/postgres
 template1    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c
/postgres          +
              |          |          |            |            |            |                 | po
stgres=CTc/postgres
(4 rows)



postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air app % 

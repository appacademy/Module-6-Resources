#  CONTAINER CLI

  Exited (0) 17 minutes ago                             priceless_murdock
cb672c4a8ef6   alpine                           "ash"                    17 minutes ago   Exited (0) 17 minutes ago                             cranky_archimedes
fe14c9c7ae9c   alpine                           "/bin/sh"                18 minutes ago   Exited (0) 18 minutes ago                             condescending_ride
1e347115139d   nginx                            "/docker-entrypoint.…"   21 minutes ago   Exited (0) 4 minutes ago                              mystifying_ride
ab4a4b0f863b   nginx                            "/docker-entrypoint.…"   26 minutes ago   Exited (0) 2 minutes ago                              my_container
31ff746e6b70   hello-world                      "/hello"                 38 minutes ago   Exited (0) 38 minutes ago                             serene_satoshi
a0cc5dc8296d   hello-world                      "/hello"                 20 hours ago     Exited (0) 20 hours ago                               sleepy_einstein
af98054f7cb5   alpine                           "echo hello world"       3 weeks ago      Exited (0) 3 weeks ago                                elegant_davinci
b16dae3fda47   alpine                           "echo 'hello world'"     3 weeks ago      Exited (0) 3 weeks ago                                quirky_villani
12a3975c1596   bradsimpson213/taco_tues-react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     0.0.0.0:3000->3000/tcp   ecstatic_jones
913e467eb882   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago     5432/tcp                 postgres2
8076f58c26ff   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                romantic_curie
c3b2c14eabed   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago     80/tcp                   c4
9c3aec309568   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago     80/tcp                   c3
76cdc8329e64   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago     80/tcp                   c2
a3c1d1e23c83   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago     80/tcp                   c1
c9fd81f2a59e   nginx                            "/docker-entrypoint.…"   4 weeks ago      Exited (0) 4 weeks ago                                silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container start boring_ptolemy
boring_ptolemy
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
d01c4905d4bc   nginx     "/docker-entrypoint.…"   11 minutes ago   Up 5 seconds   0.0.0.0:8080->80/tcp   boring_ptolemy
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                        PORTS                    NAMES
4f01751fdb42   alpine                           "sh"                     10 minutes ago   Exited (130) 10 minutes ago                            test
d01c4905d4bc   nginx                            "/docker-entrypoint.…"   12 minutes ago   Up 37 seconds                 0.0.0.0:8080->80/tcp     boring_ptolemy
704ba2e58250   alpine                           "sh"                     16 minutes ago   Exited (0) 15 minutes ago                              kind_edison
530da23563f9   alpine                           "sh"                     18 minutes ago   Exited (0) 18 minutes ago                              priceless_murdock
cb672c4a8ef6   alpine                           "ash"                    18 minutes ago   Exited (0) 18 minutes ago                              cranky_archimedes
fe14c9c7ae9c   alpine                           "/bin/sh"                19 minutes ago   Exited (0) 19 minutes ago                              condescending_ride
1e347115139d   nginx                            "/docker-entrypoint.…"   22 minutes ago   Exited (0) 5 minutes ago                               mystifying_ride
ab4a4b0f863b   nginx                            "/docker-entrypoint.…"   27 minutes ago   Exited (0) 3 minutes ago                               my_container
31ff746e6b70   hello-world                      "/hello"                 40 minutes ago   Exited (0) 40 minutes ago                              serene_satoshi
a0cc5dc8296d   hello-world                      "/hello"                 20 hours ago     Exited (0) 20 hours ago                                sleepy_einstein
af98054f7cb5   alpine                           "echo hello world"       3 weeks ago      Exited (0) 3 weeks ago                                 elegant_davinci
b16dae3fda47   alpine                           "echo 'hello world'"     3 weeks ago      Exited (0) 3 weeks ago                                 quirky_villani
12a3975c1596   bradsimpson213/taco_tues-react   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago      0.0.0.0:3000->3000/tcp   ecstatic_jones
913e467eb882   postgres                         "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago      5432/tcp                 postgres2
8076f58c26ff   nginx:alpine                     "/docker-entrypoint.…"   3 weeks ago      Exited (0) 3 weeks ago                                 romantic_curie
c3b2c14eabed   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago      80/tcp                   c4
9c3aec309568   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago      80/tcp                   c3
76cdc8329e64   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago      80/tcp                   c2
a3c1d1e23c83   nginx:alpine                     "/docker-entrypoint.…"   4 weeks ago      Exited (255) 4 weeks ago      80/tcp                   c1
c9fd81f2a59e   nginx                            "/docker-entrypoint.…"   4 weeks ago      Exited (0) 4 weeks ago                                 silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container rm 8076f58c26ff romantic_curie
romantic_curie
Error response from daemon: removal of container 8076f58c26ff is already in progress
bradsimpson@Brads-MacBook-Air ~ % docker container rm a3c1d1e23c83  sleepy_einstein
a3c1d1e23c83
sleepy_einstein
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
4f01751fdb422b483e126c9f8fbf0e27af91d65daed9ac06267d7fb4a3c1cdc5
704ba2e58250baa939a9ed08c04830ca575803f459b0798ba21649c885f619ed
530da23563f9c79cf8c82807aeca4a0a0734065b31fb9fa758536cfab86e6c23
cb672c4a8ef6b23332909cbb50f3cdbe4d7776a1647f404370384b2363657325
fe14c9c7ae9caec8bf4121e7d812241553f583e68f200ed793ff733795fc5ab5
1e347115139d5dc9b4bb5044b446719e4c6390fa5d8e1e45a6df8cdaa93b82e4
ab4a4b0f863b56f62dedeeac5f67d2c941e53dad4c49017ed20b31f15d8b0371
31ff746e6b708ad1449b927e19d6a662d8c04b146a0e3ed2864a0f4c2f30b3cd
af98054f7cb5c8e4ecdd770fa4d7788d3bb26696060cb8416d5b279e763848b7
b16dae3fda4780620307738121657d00e9e5e1c8b84f612e19621e78896b6292
12a3975c159606539be7e2857724f29045b22b4c66f2b23d3836701d66c5f541
913e467eb88288832b705efdf5cded8b150875d2a7c6faefc81fcbdeeed70038
c3b2c14eabed9b6e4ef8586f413001cc301790c59bb28b05b1e90aa8a12e0563
9c3aec309568058a45fef83bf29f03ccf4470702def4e62a4ce93a58f83c1352
76cdc8329e6439e780aecbd9d41ad7c91eaeb519997b6c6b7aa510bc9983edfb
c9fd81f2a59e70f7c5ce832e458b783da4c92e557366b8a066d0a3f3956f7ef0

Total reclaimed space: 48.53MB
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
d01c4905d4bc   nginx     "/docker-entrypoint.…"   15 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp   boring_ptolemy
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it  boring_ptolemy sh
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
# ^C
# exit
bradsimpson@Brads-MacBook-Air ~ % 



# NETWORKING

            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": null
            },
            "SandboxKey": "/var/run/docker/netns/d41be3c520c0",
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
                "taco_today": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": [
                        "4d77799a7d31"
                    ],
                    "NetworkID": "aab807bb7f01ad0991647cc7514c69fdf5a8057785874b03e39a98cda28151bc",
                    "EndpointID": "31e7bdd5c80a4e2b5f4d44ae8555a2d5e3fd78f72f63b27bd2b494ddfdb123fa",
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
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
5ecf404cef04   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
083b4eaf90a5   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
adeac7a3c4cb   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
4d77799a7d31   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 sh
/ # ping -c 4 c2 
PING c2 (172.20.0.3): 56 data bytes
64 bytes from 172.20.0.3: seq=0 ttl=64 time=0.120 ms
64 bytes from 172.20.0.3: seq=1 ttl=64 time=0.192 ms
64 bytes from 172.20.0.3: seq=2 ttl=64 time=0.226 ms
64 bytes from 172.20.0.3: seq=3 ttl=64 time=0.114 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.114/0.163/0.226 ms
/ # ping -c 4 c3 
ping: bad address 'c3'
/ # ping -c 4 c4 
ping: bad address 'c4'
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c3 sh
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 c2
ping: bad address 'c2'
/ # ping -c 4 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.140 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.140 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.160 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.229 ms

--- 172.17.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.140/0.167/0.229 ms
/ # 



# BIND MOUNTS & VOLUMES

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

bradsimpson@Brads-MacBook-Air app % docker container exec -it postgres2 sh 

# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_time | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
(4 rows)

postgres=# exit 
# exit
bradsimpson@Brads-MacBook-Air app % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED              STATUS              PORTS      NAMES
dbada9136a38   postgres   "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp   postgres2
bradsimpson@Brads-MacBook-Air app % docker container stop postgres2
postgres2
bradsimpson@Brads-MacBook-Air app % \clear

bradsimpson@Brads-MacBook-Air app % 









































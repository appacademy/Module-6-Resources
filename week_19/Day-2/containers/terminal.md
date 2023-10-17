# CONTAINER COMMANDS

            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5000"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/84d32fa72679",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "c37179e3f7c8fe7dad3e5a9ee63edc886f73dfb536654059f8f7b678ed6e8356",
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
                    "NetworkID": "c683084e8312230618373d57df20ce3e602a13c083563f043f7afdbc697d69d5",
                    "EndpointID": "c37179e3f7c8fe7dad3e5a9ee63edc886f73dfb536654059f8f7b678ed6e8356",
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
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % 










































bradsimpson@Brads-MacBook-Air ~ % docker container run -d -p 8080:80 nginx
daa0435d90631fe9ca13804d8f341483a77aa3f1389369957da98298de313558
bradsimpson@Brads-MacBook-Air ~ % docker container run -it --name test alpine sh
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container run --name greet_me --rm ubuntu echo hello world
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
bfbe77e41a78: Pull complete 
Digest: sha256:2b7412e6465c3c7fc5bb21d3e6f1917c167358449fecac8176c6e496e5c1f05f
Status: Downloaded newer image for ubuntu:latest
hello world
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
daa0435d9063   nginx     "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes    0.0.0.0:8080->80/tcp   unruffled_noether
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   20 minutes ago   Up 20 minutes   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                      PORTS                    NAMES
1ca69eb87eb2   alpine                        "sh"                     3 minutes ago    Exited (0) 3 minutes ago                             test
daa0435d9063   nginx                         "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:8080->80/tcp     unruffled_noether
c9fd81f2a59e   nginx                         "/docker-entrypoint.…"   20 minutes ago   Up 20 minutes               0.0.0.0:5000->80/tcp     silly_dhawan
104e5d9d8ed7   nginx                         "/docker-entrypoint.…"   25 minutes ago   Exited (0) 24 minutes ago                            my_container
a5d5ccb8308a   hello-world                   "/hello"                 35 minutes ago   Exited (0) 35 minutes ago                            zen_cerf
382e546ebd9b   hello-world                   "/hello"                 20 hours ago     Exited (0) 20 hours ago                              nervous_matsumoto
d3f98edb35d6   nginx                         "/docker-entrypoint.…"   3 weeks ago      Exited (255) 20 hours ago   0.0.0.0:500->80/tcp      vigilant_gagarin
b178af824c14   bradsimpson213/my_fancy_app   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   serene_swartz
27a1537c2e1b   postgres                      "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker image ls
REPOSITORY                        TAG       IMAGE ID       CREATED        SIZE
ubuntu                            latest    e343402cadef   12 days ago    69.2MB
bradsimpson213/my_fancy_app       latest    2e962f4183bc   3 weeks ago    578MB
bradsimpson213/patch              latest    85fd9d51fbc4   4 weeks ago    113MB
<none>                            <none>    23d8681bdbcf   4 weeks ago    113MB
<none>                            <none>    8442fa932634   4 weeks ago    113MB
bradsimpson213/patchstagram       latest    fdb3d88cc9df   4 weeks ago    144MB
<none>                            <none>    1be486eb8e9e   4 weeks ago    814MB
<none>                            <none>    f6211611ef7b   4 weeks ago    814MB
<none>                            <none>    ec44781411c1   4 weeks ago    814MB
<none>                            <none>    e3758b5271b3   4 weeks ago    814MB
bradsimpson213/my_flask_starter   latest    5a987801c667   5 weeks ago    1.21GB
bradsimpson213/my_flask_starter   <none>    5106d41fd79a   5 weeks ago    1.21GB
<none>                            <none>    3e9c435ed215   5 weeks ago    1.23GB
bradsimpson213/my_starter         latest    982c7b107bb2   5 weeks ago    976MB
bradsimpson213/my_starter         <none>    d67adf9f658a   5 weeks ago    976MB
bradsimpson213/my_starter         <none>    8c2a30d1ab93   5 weeks ago    976MB
bradsimpson213/my_starter         <none>    887a2903d7f6   5 weeks ago    976MB
bradsimpson213/my_starter         <none>    6afd10397145   5 weeks ago    976MB
bradsimpson213/my_starter         <none>    31b768bb850b   5 weeks ago    994MB
bradsimpson213/aptil_react_taco   latest    08caba4d9ff4   7 weeks ago    575MB
<none>                            <none>    6277c82a8b27   8 weeks ago    113MB
postgres                          latest    ee56d70bcdf1   2 months ago   433MB
bradsimpson213/my_react_app       latest    0e6d1fad2b08   2 months ago   451MB
bradsimpson213/taco_react         latest    aea6ddf0f44b   3 months ago   569MB
nginx                             alpine    66bf2c914bf4   4 months ago   41MB
alpine                            latest    5053b247d78b   4 months ago   7.66MB
nginx                             latest    2d21d843073b   4 months ago   192MB
hello-world                       latest    b038788ddb22   5 months ago   9.14kB
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
daa0435d9063   nginx     "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes    0.0.0.0:8080->80/tcp   unruffled_noether
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                      PORTS                    NAMES
1ca69eb87eb2   alpine                        "sh"                     6 minutes ago    Exited (0) 6 minutes ago                             test
daa0435d9063   nginx                         "/docker-entrypoint.…"   9 minutes ago    Up 9 minutes                0.0.0.0:8080->80/tcp     unruffled_noether
c9fd81f2a59e   nginx                         "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes               0.0.0.0:5000->80/tcp     silly_dhawan
104e5d9d8ed7   nginx                         "/docker-entrypoint.…"   28 minutes ago   Exited (0) 27 minutes ago                            my_container
a5d5ccb8308a   hello-world                   "/hello"                 38 minutes ago   Exited (0) 38 minutes ago                            zen_cerf
382e546ebd9b   hello-world                   "/hello"                 20 hours ago     Exited (0) 20 hours ago                              nervous_matsumoto
d3f98edb35d6   nginx                         "/docker-entrypoint.…"   3 weeks ago      Exited (255) 20 hours ago   0.0.0.0:500->80/tcp      vigilant_gagarin
b178af824c14   bradsimpson213/my_fancy_app   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   serene_swartz
27a1537c2e1b   postgres                      "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container ls   
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
daa0435d9063   nginx     "/docker-entrypoint.…"   10 minutes ago   Up 10 minutes   0.0.0.0:8080->80/tcp   unruffled_noether
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   23 minutes ago   Up 23 minutes   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container stop daa0435d9063 silly_dhawan
daa0435d9063
silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container ls                            
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                      PORTS                    NAMES
1ca69eb87eb2   alpine                        "sh"                     7 minutes ago    Exited (0) 7 minutes ago                             test
daa0435d9063   nginx                         "/docker-entrypoint.…"   11 minutes ago   Exited (0) 14 seconds ago                            unruffled_noether
c9fd81f2a59e   nginx                         "/docker-entrypoint.…"   24 minutes ago   Exited (0) 14 seconds ago                            silly_dhawan
104e5d9d8ed7   nginx                         "/docker-entrypoint.…"   30 minutes ago   Exited (0) 28 minutes ago                            my_container
a5d5ccb8308a   hello-world                   "/hello"                 39 minutes ago   Exited (0) 39 minutes ago                            zen_cerf
382e546ebd9b   hello-world                   "/hello"                 20 hours ago     Exited (0) 20 hours ago                              nervous_matsumoto
d3f98edb35d6   nginx                         "/docker-entrypoint.…"   3 weeks ago      Exited (255) 20 hours ago   0.0.0.0:500->80/tcp      vigilant_gagarin
b178af824c14   bradsimpson213/my_fancy_app   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago    0.0.0.0:3000->3000/tcp   serene_swartz
27a1537c2e1b   postgres                      "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                               postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container start zen_cerf
zen_cerf
bradsimpson@Brads-MacBook-Air ~ % docker container start silly_dhawan
silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   29 minutes ago   Up 7 seconds   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS                          PORTS                    NAMES
1ca69eb87eb2   alpine                        "sh"                     12 minutes ago   Exited (0) 12 minutes ago                                test
daa0435d9063   nginx                         "/docker-entrypoint.…"   15 minutes ago   Exited (0) 4 minutes ago                                 unruffled_noether
c9fd81f2a59e   nginx                         "/docker-entrypoint.…"   29 minutes ago   Up 14 seconds                   0.0.0.0:5000->80/tcp     silly_dhawan
104e5d9d8ed7   nginx                         "/docker-entrypoint.…"   34 minutes ago   Exited (0) 33 minutes ago                                my_container
a5d5ccb8308a   hello-world                   "/hello"                 44 minutes ago   Exited (0) About a minute ago                            zen_cerf
382e546ebd9b   hello-world                   "/hello"                 20 hours ago     Exited (0) 20 hours ago                                  nervous_matsumoto
d3f98edb35d6   nginx                         "/docker-entrypoint.…"   3 weeks ago      Exited (255) 20 hours ago       0.0.0.0:500->80/tcp      vigilant_gagarin
b178af824c14   bradsimpson213/my_fancy_app   "docker-entrypoint.s…"   3 weeks ago      Exited (255) 3 weeks ago        0.0.0.0:3000->3000/tcp   serene_swartz
27a1537c2e1b   postgres                      "docker-entrypoint.s…"   3 weeks ago      Exited (0) 3 weeks ago                                   postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   29 minutes ago   Up 58 seconds   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container rm b178af824c14
b178af824c14
bradsimpson@Brads-MacBook-Air ~ % docker container ls             
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS              PORTS                  NAMES
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   30 minutes ago   Up About a minute   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
1ca69eb87eb2dc569f611b890a15c0387da80e9c31d00ba64d6bde9209cb46da
daa0435d90631fe9ca13804d8f341483a77aa3f1389369957da98298de313558
104e5d9d8ed7fbd4d64c9049b2a76b1e9f913a3429192014a2d4e0eea3e2f58f
a5d5ccb8308a20f820b8efe966cc8c053ab4c892f2b40c4b091b8fd6b34c9ca4
382e546ebd9b6b2f25fd3f3dcb743a9c2c9e0728c9269b68c1ebe43e58dcbc71
d3f98edb35d66ecd481ee6a852b6df3dd98cdda939cfbe392186ddcd0884c5d9
27a1537c2e1beff7355ca27c3731329910a5de3c2b17a3903e0f70f4d3cb42f9

Total reclaimed space: 3.289kB
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   31 minutes ago   Up 2 minutes   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it silly_dhawan sh
# \ls
bin   dev		   docker-entrypoint.sh  home  media  opt   root  sbin	sys  usr
boot  docker-entrypoint.d  etc			 lib   mnt    proc  run   srv	tmp  var
# cd usr
# \ls
bin  games  include  lib  libexec  local  sbin	share  src
# cd share
# \ls
X11		 ca-certificates  doc	      gcc	libc-bin     maven-repo  pam-configs  tabset	  zsh
base-files	 common-licenses  doc-base    gdb	libgcrypt20  menu	 perl5	      terminfo
base-passwd	 debconf	  dpkg	      info	lintian      misc	 pixmaps      util-linux
bash-completion  debianutils	  fontconfig  java	locale	     nginx	 polkit-1     xml
bug		 dict		  fonts       keyrings	man	     pam	 readline     zoneinfo
# cd nginx
# \ls
html
# cd html
# ls
50x.html  index.html
# exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS         PORTS                  NAMES
c9fd81f2a59e   nginx     "/docker-entrypoint.…"   34 minutes ago   Up 5 minutes   0.0.0.0:5000->80/tcp   silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % 


## NETWORKING

        }
    }
]
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS     NAMES
c3b2c14eabed   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c4
9c3aec309568   nginx:alpine   "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp    c3
76cdc8329e64   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c2
a3c1d1e23c83   nginx:alpine   "/docker-entrypoint.…"   2 minutes ago        Up 2 minutes        80/tcp    c1
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c1 sh
/ # ping -c 4 c2
PING c2 (172.19.0.3): 56 data bytes
64 bytes from 172.19.0.3: seq=0 ttl=64 time=0.228 ms
64 bytes from 172.19.0.3: seq=1 ttl=64 time=0.163 ms
64 bytes from 172.19.0.3: seq=2 ttl=64 time=0.280 ms
64 bytes from 172.19.0.3: seq=3 ttl=64 time=0.220 ms

--- c2 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.163/0.222/0.280 ms
/ # ping -c 4 c3
ping: bad address 'c3'
/ # ping -c 4 c4
ping: bad address 'c4'
/ # exit
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it c3 sh 
/ # ping -c 4 c4
ping: bad address 'c4'
/ # ping -c 4 c1
ping: bad address 'c1'
/ # ping -c 4 c2
ping: bad address 'c2'
/ # ping -c 4 172.17.0.3
PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.224 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.158 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.159 ms
64 bytes from 172.17.0.3: seq=3 ttl=64 time=0.144 ms

--- 172.17.0.3 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 0.144/0.171/0.224 ms
/ # exit
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % 



## VOLUMES & BIND MOUNTS

   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tues | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
(4 rows)

postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air ~ % docker container ls
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS      NAMES
6e0c86a7dabb   postgres   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   5432/tcp   postgres1
bradsimpson@Brads-MacBook-Air ~ % docker container stop postgres1
postgres1
bradsimpson@Brads-MacBook-Air ~ % docker container ls            
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS     NAMES
6e0c86a7dabb   postgres       "docker-entrypoint.s…"   2 minutes ago       Exited (0) 8 seconds ago                 postgres1
8076f58c26ff   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago      Exited (0) 12 minutes ago                romantic_curie
c3b2c14eabed   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 21 minutes ago    80/tcp    c4
9c3aec309568   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 21 minutes ago    80/tcp    c3
76cdc8329e64   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 21 minutes ago    80/tcp    c2
a3c1d1e23c83   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 21 minutes ago    80/tcp    c1
c9fd81f2a59e   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago             silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % docker container rm postgres1
postgres1
bradsimpson@Brads-MacBook-Air ~ % docker container ls -a       
CONTAINER ID   IMAGE          COMMAND                  CREATED             STATUS                         PORTS     NAMES
8076f58c26ff   nginx:alpine   "/docker-entrypoint.…"   16 minutes ago      Exited (0) 12 minutes ago                romantic_curie
c3b2c14eabed   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 22 minutes ago    80/tcp    c4
9c3aec309568   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 22 minutes ago    80/tcp    c3
76cdc8329e64   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 22 minutes ago    80/tcp    c2
a3c1d1e23c83   nginx:alpine   "/docker-entrypoint.…"   About an hour ago   Exited (255) 22 minutes ago    80/tcp    c1
c9fd81f2a59e   nginx          "/docker-entrypoint.…"   2 hours ago         Exited (0) About an hour ago             silly_dhawan
bradsimpson@Brads-MacBook-Air ~ % \clear

bradsimpson@Brads-MacBook-Air ~ % docker container run -e POSTGRES_PASSWORD=password --name postgres2 --mount type=volume,source=my_taco_tues,target=/var/lib/postgresql/data -d postgres 
913e467eb88288832b705efdf5cded8b150875d2a7c6faefc81fcbdeeed70038
bradsimpson@Brads-MacBook-Air ~ % docker container ls           
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS      NAMES
913e467eb882   postgres   "docker-entrypoint.s…"   8 seconds ago   Up 7 seconds   5432/tcp   postgres2
bradsimpson@Brads-MacBook-Air ~ % docker container exec -it postgres2 sh 
# psql -p 5432 -h localhost -U postgres
psql (15.4 (Debian 15.4-1.pgdg120+1))
Type "help" for help.

postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges   
-----------+----------+----------+------------+------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 taco_tues | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
(4 rows)

postgres=# exit
# exit
bradsimpson@Brads-MacBook-Air ~ % 










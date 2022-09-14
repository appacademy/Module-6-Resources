Last login: Wed Sep 14 11:05:15 on ttys005

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker image ls
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
postgres                    latest    75993dd36176   28 hours ago    376MB
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:docker image history hello-world
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
feb5d9fea6a5   11 months ago   /bin/sh -c #(nop)  CMD ["/hello"]               0B        
<missing>      11 months ago   /bin/sh -c #(nop) COPY file:50563a97010fd7ce…   13.3kB    
bradsimpson@ ~:docker image history nginx
IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
0e901e68141f   3 months ago   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B        
<missing>      3 months ago   /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B        
<missing>      3 months ago   /bin/sh -c #(nop)  EXPOSE 80                    0B        
<missing>      3 months ago   /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B        
<missing>      3 months ago   /bin/sh -c #(nop) COPY file:09a214a3e07c919a…   4.61kB    
<missing>      3 months ago   /bin/sh -c #(nop) COPY file:0fd5fca330dcd6a7…   1.04kB    
<missing>      3 months ago   /bin/sh -c #(nop) COPY file:0b866ff3fc1ef5b0…   1.96kB    
<missing>      3 months ago   /bin/sh -c #(nop) COPY file:65504f71f5855ca0…   1.2kB     
<missing>      3 months ago   /bin/sh -c set -x     && addgroup --system -…   61.1MB    
<missing>      3 months ago   /bin/sh -c #(nop)  ENV PKG_RELEASE=1~bullseye   0B        
<missing>      3 months ago   /bin/sh -c #(nop)  ENV NJS_VERSION=0.7.3        0B        
<missing>      3 months ago   /bin/sh -c #(nop)  ENV NGINX_VERSION=1.21.6     0B        
<missing>      3 months ago   /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B        
<missing>      3 months ago   /bin/sh -c #(nop)  CMD ["bash"]                 0B        
<missing>      3 months ago   /bin/sh -c #(nop) ADD file:134f25aec8adf83cb…   80.4MB    
bradsimpson@ ~:\clear






bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
postgres                    latest    75993dd36176   28 hours ago    376MB
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
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
bradsimpson@ ~:\clear

bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
postgres                    latest    75993dd36176   28 hours ago    376MB
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
react_fe                    latest    c320273135f5   2 months ago    377MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:docker image rm react_fe
Untagged: react_fe:latest
Deleted: sha256:c320273135f5bd5c7fbf6a12bcfff4b61b537380e6ee7730b82272fa21b90358
bradsimpson@ ~:docker image rm react_fe
Error: No such image: react_fe
bradsimpson@ ~:docker image ls
REPOSITORY                  TAG       IMAGE ID       CREATED         SIZE
postgres                    latest    75993dd36176   28 hours ago    376MB
bradsimpson213/react_test   latest    4de311ebce05   3 weeks ago     545MB
bradsimpson213/test_react   latest    93489609ef4b   2 months ago    377MB
ubuntu                      latest    27941809078c   3 months ago    77.8MB
nginx                       latest    0e901e68141f   3 months ago    142MB
alpine                      latest    e66264b98777   3 months ago    5.53MB
nginx                       alpine    b1c3acb28882   3 months ago    23.4MB
hello-world                 latest    feb5d9fea6a5   11 months ago   13.3kB
bradsimpson@ ~:

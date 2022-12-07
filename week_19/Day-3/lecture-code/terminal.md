Last login: Wed Dec  7 11:01:26 on ttys003

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
bradsimpson@ ~:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
postgres                         latest    4c6b3cc10e6b   24 hours ago    379MB
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   8 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ ~:docker image history nginx  
IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
0e901e68141f   6 months ago   /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B        
<missing>      6 months ago   /bin/sh -c #(nop)  STOPSIGNAL SIGQUIT           0B        
<missing>      6 months ago   /bin/sh -c #(nop)  EXPOSE 80                    0B        
<missing>      6 months ago   /bin/sh -c #(nop)  ENTRYPOINT ["/docker-entr…   0B        
<missing>      6 months ago   /bin/sh -c #(nop) COPY file:09a214a3e07c919a…   4.61kB    
<missing>      6 months ago   /bin/sh -c #(nop) COPY file:0fd5fca330dcd6a7…   1.04kB    
<missing>      6 months ago   /bin/sh -c #(nop) COPY file:0b866ff3fc1ef5b0…   1.96kB    
<missing>      6 months ago   /bin/sh -c #(nop) COPY file:65504f71f5855ca0…   1.2kB     
<missing>      6 months ago   /bin/sh -c set -x     && addgroup --system -…   61.1MB    
<missing>      6 months ago   /bin/sh -c #(nop)  ENV PKG_RELEASE=1~bullseye   0B        
<missing>      6 months ago   /bin/sh -c #(nop)  ENV NJS_VERSION=0.7.3        0B        
<missing>      6 months ago   /bin/sh -c #(nop)  ENV NGINX_VERSION=1.21.6     0B        
<missing>      6 months ago   /bin/sh -c #(nop)  LABEL maintainer=NGINX Do…   0B        
<missing>      6 months ago   /bin/sh -c #(nop)  CMD ["bash"]                 0B        
<missing>      6 months ago   /bin/sh -c #(nop) ADD file:134f25aec8adf83cb…   80.4MB    
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
bradsimpson@ ~:docker image ls
REPOSITORY                       TAG       IMAGE ID       CREATED         SIZE
postgres                         latest    4c6b3cc10e6b   24 hours ago    379MB
bradsimpson213/wacky_wed-react   latest    393facc51351   3 weeks ago     376MB
bradsimpson213/wing_wednesday    latest    09dccc5d2562   8 weeks ago     560MB
bradsimpson213/test_app2         <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test        latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react        latest    93489609ef4b   5 months ago    377MB
ubuntu                           latest    27941809078c   6 months ago    77.8MB
nginx                            latest    0e901e68141f   6 months ago    142MB
alpine                           latest    e66264b98777   6 months ago    5.53MB
nginx                            alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                      latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ ~:docker image rm bradsimpson213/wacky_wed-react 
Untagged: bradsimpson213/wacky_wed-react:latest
Untagged: bradsimpson213/wacky_wed-react@sha256:10c8e08a705a11542d7fc951bd72bebe24932f681248cd9967168bce7e2171ef
Deleted: sha256:393facc51351d1079d7043c5436332b7872eca2a5ccc725841a488ebee582661
bradsimpson@ ~:docker image ls
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
postgres                        latest    4c6b3cc10e6b   24 hours ago    379MB
bradsimpson213/wing_wednesday   latest    09dccc5d2562   8 weeks ago     560MB
bradsimpson213/test_app2        <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test       latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   5 months ago    377MB
ubuntu                          latest    27941809078c   6 months ago    77.8MB
nginx                           latest    0e901e68141f   6 months ago    142MB
alpine                          latest    e66264b98777   6 months ago    5.53MB
nginx                           alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ ~:\clear

bradsimpson@ ~:cd Desktop/
bradsimpson@ Desktop:cd Module-6/
bradsimpson@ Module-6:\ls
Week 17	Week 18	Week 19	temp
bradsimpson@ Module-6:cd Week\ 19/
bradsimpson@ Week 19:cd D3/
bradsimpson@ D3:cd my-app/
bradsimpson@ my-app:\ls
Dockerfile		package-lock.json	src
README.md		package.json
node_modules		public
bradsimpson@ my-app:docker login
Authenticating with existing credentials...
Login Succeeded
bradsimpson@ my-app:docker build -t bradsimpson213/react_masterpiece .
[+] Building 185.4s (11/11) FINISHED                                                    
 => [internal] load build definition from Dockerfile                               0.2s
 => => transferring dockerfile: 167B                                               0.1s
 => [internal] load .dockerignore                                                  0.1s
 => => transferring context: 34B                                                   0.0s
 => [internal] load metadata for docker.io/library/node:18-alpine3.15              1.9s
 => [auth] library/node:pull token for registry-1.docker.io                        0.0s
 => [1/5] FROM docker.io/library/node:18-alpine3.15@sha256:cd3a7004267e419477bbf  38.2s
 => => resolve docker.io/library/node:18-alpine3.15@sha256:cd3a7004267e419477bbfc  0.0s
 => => sha256:cd3a7004267e419477bbfc50e0502df8607a0b9b4465092f6e2 1.43kB / 1.43kB  0.0s
 => => sha256:8ff75a7157acb6207467ac9fb6fb426177b3fa01950ef90ae26 1.16kB / 1.16kB  0.0s
 => => sha256:e685ae170a555e20bec3f958eeb40c002a273829feb4050a67c 6.44kB / 6.44kB  0.0s
 => => sha256:b2ff27170c0301410e4c5131aa6c012325a4a225acc83531 46.28MB / 46.28MB  19.5s
 => => sha256:857f24243633abc60ce0e3e4df37c2b425efa9be5540e0a04a2 2.35MB / 2.35MB  6.3s
 => => sha256:f5234ba59f34209d3dde3f0ece7672ad2239d3359a3668122eb5a92 450B / 450B  0.5s
 => => extracting sha256:b2ff27170c0301410e4c5131aa6c012325a4a225acc8353101ab7df  12.4s
 => => extracting sha256:857f24243633abc60ce0e3e4df37c2b425efa9be5540e0a04a29abf8  0.5s
 => => extracting sha256:f5234ba59f34209d3dde3f0ece7672ad2239d3359a3668122eb5a92d  0.0s
 => [internal] load build context                                                  0.3s
 => => transferring context: 1.17MB                                                0.3s
 => [2/5] WORKDIR /app                                                             0.9s
 => [3/5] COPY package*.json ./                                                    0.1s
 => [4/5] RUN npm install                                                        119.9s
 => [5/5] COPY . .                                                                 0.2s
 => exporting to image                                                            23.5s 
 => => exporting layers                                                           23.5s 
 => => writing image sha256:68bd7528996885b59b0626e2c1a4f0ad8f166ab8e348a7d9c311f  0.0s 
 => => naming to docker.io/bradsimpson213/react_masterpiece                        0.0s 
                                                                                        
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
bradsimpson@ my-app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
bradsimpson213/react_masterpiece   latest    68bd75289968   34 seconds ago   433MB
postgres                           latest    4c6b3cc10e6b   25 hours ago     379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   8 weeks ago      560MB
bradsimpson213/test_app2           <none>    8edeca523aef   2 months ago     432MB
bradsimpson213/react_test          latest    4de311ebce05   3 months ago     545MB
bradsimpson213/test_react          latest    93489609ef4b   5 months ago     377MB
ubuntu                             latest    27941809078c   6 months ago     77.8MB
nginx                              latest    0e901e68141f   6 months ago     142MB
alpine                             latest    e66264b98777   6 months ago     5.53MB
nginx                              alpine    b1c3acb28882   6 months ago     23.4MB
hello-world                        latest    feb5d9fea6a5   14 months ago    13.3kB
bradsimpson@ my-app:docker image push bradsimpson213/react_masterpiece
Using default tag: latest
The push refers to repository [docker.io/bradsimpson213/react_masterpiece]
bec76d16ac10: Pushed 
a69770d11db5: Pushed 
147e5963de7b: Pushed 
4828ba10c2be: Pushed 
7873ffdc5975: Mounted from library/node 
6c3b0ca38fdf: Mounted from library/node 
2510f5d20f3d: Mounted from library/node 
34d5ebaa5410: Mounted from bradsimpson213/wing_wednesday 
latest: digest: sha256:c07ceb961a38beff5b32ba6e5eb49614dc6a91745c3205207b36b9b1bac6e188 size: 1997
bradsimpson@ my-app:\clear

bradsimpson@ my-app:docker image ls
REPOSITORY                         TAG       IMAGE ID       CREATED         SIZE
bradsimpson213/react_masterpiece   latest    68bd75289968   2 minutes ago   433MB
postgres                           latest    4c6b3cc10e6b   25 hours ago    379MB
bradsimpson213/wing_wednesday      latest    09dccc5d2562   8 weeks ago     560MB
bradsimpson213/test_app2           <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test          latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react          latest    93489609ef4b   5 months ago    377MB
ubuntu                             latest    27941809078c   6 months ago    77.8MB
nginx                              latest    0e901e68141f   6 months ago    142MB
alpine                             latest    e66264b98777   6 months ago    5.53MB
nginx                              alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                        latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ my-app:docker image rm bradsimpson213/react_masterpiece
Untagged: bradsimpson213/react_masterpiece:latest
Untagged: bradsimpson213/react_masterpiece@sha256:c07ceb961a38beff5b32ba6e5eb49614dc6a91745c3205207b36b9b1bac6e188
Deleted: sha256:68bd7528996885b59b0626e2c1a4f0ad8f166ab8e348a7d9c311f3530d3cae93
bradsimpson@ my-app:docker image ls
REPOSITORY                      TAG       IMAGE ID       CREATED         SIZE
postgres                        latest    4c6b3cc10e6b   25 hours ago    379MB
bradsimpson213/wing_wednesday   latest    09dccc5d2562   8 weeks ago     560MB
bradsimpson213/test_app2        <none>    8edeca523aef   2 months ago    432MB
bradsimpson213/react_test       latest    4de311ebce05   3 months ago    545MB
bradsimpson213/test_react       latest    93489609ef4b   5 months ago    377MB
ubuntu                          latest    27941809078c   6 months ago    77.8MB
nginx                           latest    0e901e68141f   6 months ago    142MB
alpine                          latest    e66264b98777   6 months ago    5.53MB
nginx                           alpine    b1c3acb28882   6 months ago    23.4MB
hello-world                     latest    feb5d9fea6a5   14 months ago   13.3kB
bradsimpson@ my-app:docker container run -p 3001:3000 bradsimpson213/react_masterpiece
Unable to find image 'bradsimpson213/react_masterpiece:latest' locally
latest: Pulling from bradsimpson213/react_masterpiece
9621f1afde84: Already exists 
b2ff27170c03: Already exists 
857f24243633: Already exists 
f5234ba59f34: Already exists 
0bd68c39b2c5: Already exists 
8ca25a7cea46: Already exists 
16f495b91199: Already exists 
3d099c83f963: Already exists 
Digest: sha256:c07ceb961a38beff5b32ba6e5eb49614dc6a91745c3205207b36b9b1bac6e188
Status: Downloaded newer image for bradsimpson213/react_masterpiece:latest

> my-app@0.1.0 start
> react-scripts start

Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
(node:26) [DEP_WEBPACK_DEV_SERVER_ON_AFTER_SETUP_MIDDLEWARE] DeprecationWarning: 'onAfterSetupMiddleware' option is deprecated. Please use the 'setupMiddlewares' option.
(Use `node --trace-deprecation ...` to show where the warning was created)
(node:26) [DEP_WEBPACK_DEV_SERVER_ON_BEFORE_SETUP_MIDDLEWARE] DeprecationWarning: 'onBeforeSetupMiddleware' option is deprecated. Please use the 'setupMiddlewares' option.
Starting the development server...

Compiled successfully!

You can now view my-app in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://172.17.0.3:3000

Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
Compiling...
Compiled successfully!
webpack compiled successfully


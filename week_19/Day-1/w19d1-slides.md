<style>
    .present {
        text-align: left;
        
    }
</style>

---

###### tags: `Week 19` `W19D2`

---

# Docker Container CLI
## Week 19 Day 2

---


## Roday's Docker Topics

- Container terminal commands
- Networks
- Bind Mounts & Volumes- 


---

## Lecture Videos 1 (17 minutes)
Watch:
- Container Intro (12:00)

---

## What is a Container?

A container runs an application. It is a unit of software that contains the source code, linux distro, dependencies, and other tools the application needs to run.

When we build a container, we are starting up an application image.

---

### `docker container run` ([Official documentation](https://docs.docker.com/engine/reference/commandline/container_run/))
Usage:
```shell
docker container run [OPTIONS] image-name [COMMAND] [ARG...]
```
- You always need to specify the image—__every container is based on an image__.
- The optional "OPTIONS" are specified with a flag.
    - Any options you include will come before the image name
- Each image has a default command—that will be replaced if you specify a new command (after the image-name)


---

#### Commonly used flags for `docker container run`:


| flag               | purpose                                                | example usage   |
| ------------------ | ------------------------------------------------------ | --------------- |
| `--name`           | specify a name for the container                       | `--name hello`  |
| `-p` / `--publish` | publish a port to the "outside world" on your localhost (externalport:internalport) | `-p 8080:80`    |
| `-d`               | detached session (runs in background)                  | `-d`            |
| `--rm`             | automatically remove container once stopped            | `--rm`          |
| `-it`              | use an interactive session (e.g. bash)                 | `-it` / `-i -t` |


---

### Pop quiz

1. Let's run a container based on the *nginx* image, in detached mode. We want to publish the contents of that container's internal port 80, to my localhost at port 8080.

2. Let's run a container based on the *alpine* image and name it "test". We want to run it with an interactive terminal, and use the command `sh`.

3. Let's run a container based on the *ubuntu* image and name it "greet_me". We want the container to be removed automatically once it is stopped. Let's have it use the command `echo hello world`.

---

### Pop quiz (answer key)
1.
```bash
docker container run -p 8080:80 -d nginx
```
2.
```bash
docker container run -it --name test alpine sh
```
3.
```bash
docker container run --name greet_me --rm ubuntu echo hello world
```

---



### `docker container ls` ([Official documentation](https://docs.docker.com/engine/reference/commandline/container_ls/))
Purpose: list containers (can be used interchangeably with `docker ps`)
- `-a` flag includes stopped containers

Usage:
```bash
docker container ls [OPTIONS]
```

---


### `docker container stop` ([Official documentation](https://docs.docker.com/engine/reference/commandline/container_stop/))
Purpose: stop a container (or containers) that is currently running.

Usage:
```bash
docker container stop [OPTIONS] CONTAINER [CONTAINER...]
```

---


### `docker container start` ([Official documentation](https://docs.docker.com/engine/reference/commandline/container_start/))
Purpose: start a stopped container (or containers)
- this will not create a new container, the container must already exist


Usage:
```bash
 docker container start [OPTIONS] CONTAINER [CONTAINER...]
```

---

### `docker container rm` ([Official documentation](https://docs.docker.com/engine/reference/commandline/container_rm/))
Purpose: remove a container
- by default you can only remove stopped containers
- `-f` flag forces removal even if container is running

Usage:
```
 docker container rm [OPTIONS] CONTAINER [CONTAINER...]
```

---

### `docker container prune` ([Official documentation](https://docs.docker.com/engine/reference/commandline/container_prune/))
Purpose: remove all stopped containers

Usage:
```
 docker container prune [OPTIONS]
```


---

### `docker container exec` ([Official documentation](https://docs.docker.com/engine/reference/commandline/exec/))
Purpose: execute a command within a running container
- often useful for opening interactive shell (uses same `-it` flag as container run)
```
docker container exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

---

## Lecture Videos 2 (12 minutes)
Watch:
- Docker Networking (8:30)

---

### Docker networks
Networks allow containers to communicate with each other, whether or not they are exposing ports.
[Official documentation](https://docs.docker.com/network/)


---

### Docker networks
The Docker engine comes with 3 network drivers:
- `bridge` - allows containers connected to the same bridge network to communicate, while providing isolation from containers which are not connected to that bridge network
- `host` - uses host machine's networking stack and namespace
- `none` - disables all networking for a container

---

### Networking with Docker
By default, containers are connected to the "bridge" driver network. While containers can communicate via IP address over the bridge network, it does not enable DNS resolution.

To be able to communicate via domain name over a network we must create a custom network.

---

### Creating custom networks ([Official documentation](https://docs.docker.com/engine/reference/commandline/network_create/))

Creating a custom network will allow the containers on that network to interact with each other.
```bash
docker network create [OPTIONS] network-name
```

```bash
docker network ls
```


---

### Networking demo [1/2]
Let's create a network, and attach containers to it so we can see how networked containers communicate. 

For comparison, we'll use two containers that are on the default network.
```bash
# create a network based on the bridge driver, called "test-network"
docker network create --driver bridge test-network
# create two images on that network
docker container run -d --name c1 --network test-network nginx:alpine
docker container run -d --name c2 --network test-network nginx:alpine

# create two more images, without specifying a network
docker container run -d --name c3 nginx:alpine
docker container run -d --name c4 nginx:alpine
```

---

### Networking demo [2/2]

```bash
# access the shell on one of our two networked containers
docker container exec -it c1 ash
# ping a container that is not on the network
ping -c 2 c3
# ping a container that is on the network
ping -c 2 c2


docker container exec -it c3 ash
ping -c 2 c1
ping -c 2 c4
```


---

## Lecture videos 3 (25 minutes)
Watch:
- Persistant Data in Docker: Bind Mounts (9:00)
- Persistant Data in Docker: Volumes (8:30)

---

### Docker volumes/bind mounts

Using bind mounts and volumes allows data to persist even after a container is gone.

Bind mounts directly mount the contents of a folder on your filesystem into your container.

Volumes are managed by Docker—so you wouldn't directly access the files, but can be accessed and modified from within a container.

---

### Options for creating volumes/bind mounts

There are two different types of syntax you can use with `docker container run` to establish volumes and bind mounts. Both flags can create either volumes or bind mounts.
- `-v` and `--mount` flags have the same purpose.
- `--mount` is typically preferred as it is considered to be clearer.

```bash
docker container run -v ...
docker container run --mount ...
```

---

### `--mount` syntax

Pass in a series of `<key>=<value>` pairs in any order, separated by a comma.

Type must be "bind" for bind mounts, or "volume" for volumes


---

### `--mount` syntax
#### for bind mounts

```
--mount type=bind,source=/absolute/path,target=/absolute/path/in/container
```
#### for volumes

```
--mount type=volume,source=name_of_volume,target=/absolute/path/in/container
```


---


### Bind mounts
[Official documentation](https://docs.docker.com/storage/bind-mounts/)

- Bind mounts connect a folder in your file system to a folder on your container
- Convenience in simple cases—any changes made in one place will change what's present in the other


---

### Demo: Serve a Website [1/2]
First, create a folder called __app__ in your current directory, and make an empty __index.html__ file inside the folder. 
```bash=
# run an nginx:alpine-based container, in detached mode
# mount the /app folder into the container at the path where nginx serves
# its files from (/usr/share/nginx/html)
# and expose port 80 to view the contents
docker container run -d \
--mount type=bind,source="$(pwd)/app",target=/usr/share/nginx/html \
-p 8080:80 nginx:alpine
```

---

### Demo: Serve a Website [2/2]
Once your container is running, visit localhost:8080—you should see a blank page. Add some content to your html page, then save and refresh localhost:8080. Now you can see the new content you added, because the contents of your folder stays in sync with the contents of the folder inside your container.


---

### Volumes
[Official documentation](https://docs.docker.com/storage/volumes/)
Volumes are managed from within Docker—don't depend on your file structure.

You wouldn't modify the contents directly (only from inside a container), but you can use it to spin up new containers with same contents.

Instead of providing a path to the folder (like you would with a bind mount) you can provide the name of the volume.

Think of a volume like a flash drive, you can connect it to you computer, then take that same drive and connect it to another

---

### Demo: Persist data from a postgres instance that runs in a container

```bash=
# pull the postgres image so we can inspect it
docker pull postgres
# inspect the image to find out what the path to the volume should be
# and what port we want to expose
docker image inspect postgres
```

---

### Demo: Persist data from a postgres instance that runs in a container

```bash=
# run the container with a volume named "postgres-data"
# that corresponds to the path where a 
# postgres container stores its data
# (/var/lib/postgresql/data)
docker container run -p 5431:5432 \
-e POSTGRES_PASSWORD=password \
--name postgres5431 -d \
--mount type=volume,source=postgres-data,target=/var/lib/postgresql/data postgres
# now use the psql command line tool to connect
# to the postgres instance running in our container
psql -p 5431 -h localhost -U postgres
```

---

### Project time!

Today's projects are:
- First Containers
- Container Fun

Once you finish these projects, please coordinate with your groups for more project planning time.
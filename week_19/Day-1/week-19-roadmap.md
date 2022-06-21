# Docker Intro and Week 19 Roadmap

---

## What is Docker?
![shipping container](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/MAERSK_MC_KINNEY_M%C3%96LLER_%26_MARSEILLE_MAERSK_%2848694054418%29.jpg/1920px-MAERSK_MC_KINNEY_M%C3%96LLER_%26_MARSEILLE_MAERSK_%2848694054418%29.jpg)

Docker is a platform that allows for development and deployment of software in packages called *containers*.

---

### Docker containers

- Containers are:
    - **Isolated:** They do not interact with your local filesystem/OS or other containers (unless we configure them to do so)
    - **Ephemeral:** They can be deleted (& recreated) easily without worry
    - **Lightweight:** They are single-purpose and contain only what they need for that purpose
    - **Reproducible:** We can rebuild the same container over & over with a single command

---

### How does Docker work?
#### Part 1: Your Computer
In order to understand Docker, we should first discuss how our computers work to begin with.

Your computer has physical hardware, an OS, and a kernel that interfaces between the two, which are all tightly coupled.

When we build & deploy apps with this environment, we are limited to the performance of our machine and the libraries that are compatible with it.

---

### How does Docker work?
#### Part 2: Why not use a VM?
A VM has an OS that is *decoupled* from your computer's hardware. With VMs, can have multiple OSs running on a computer.

A VM has a kernel & hypervisor. The kernel interfaces between the hardware and the OS. The hypervisor creates & runs a VM.

A VM is heavy - we often don't need an entirely separate kernel & hypervisor just for the purposes of deploying an application.


---

### How does Docker work?
#### Part 3: Docker containers
A Docker container is like a mini-VM that is hardware agnostic - it doesn't care about the host OS.

It is lightweight - it consists only of a small Linux distribution and necessary libraries & resources. It does not have its own kernel or hypervisor.

This makes it much more scalable and allows us to run many more containers on one machine than VMs.

---

### Cool... but why are we learning about Docker?
- We can easily scale an application using a cluster of containers on one or more machines
- We can easily share our application with others for testing & development
    - We can build a template for our application called an *image* 
    - We can automate the process of building & deploying that image with *docker compose*
- We can run the same application on *any* machine without worrying about performance or incompatibilites
    - Having psycopg issues on your M1? Use a Docker container!

---


## Docker topics
- Intro and installation (today)
- Docker Containers (Tuesday)
- Docker Images & Dockerfiles (Wednesday)
- Docker Compose (Thursday)
- Microservices (Friday)

---

### Docker containers (Tuesday)

- A docker container is a lightweight package which contains only the software and dependencies we need to run a single process
- A container is a running image
- We'll explore containers & use the command line interface to work with them

---

### Docker images (Wednesday)

- Images are templates for building docker containers
- Images allow you to make the same container over and over
- We can customize/build our own images using a Dockerfile

---

### Docker-compose (Thursday)

- Easily spin up a collection of containers, and configure them to communicate with one another

---

### Microservices (Friday morning)

- Microservices are a design principle that involves separating an application into sub-services
- We can use Docker to implement a microservice-based approach to development & deployment

### Friday afternoon
- Mark Rodriguez talks to us about Mod7!
- Walkthrough the group project starter
- Group project planning

---

### Group Project Planning
We will have time allotted each day this week to work on group project planning!

Use [project planning sheet in this repo](https://github.com/appacademy/Module-6-Resources/blob/main/group_project_resources/project-planning-sheet.md) to help guide your planning this week.

You must produce 4 design documents for approval by your project advisor this week: 
- Feature list
- User stories
- Database schema
- Grading scorecard

---

### Group Projects
You are free to choose between cloning an existing app, creating your own, or something in between! Possible clones are listed in a/A Open under `Week 20 - Python Project -> Expectations -> Python Group Project`.

You must use the Python project starter code.

You must have 4 MVP features - at least 2 of which must be full CRUD features.

You may use packages and modules not covered by the App Academy curriculum (React libraries, Flask libraries, etc.), but CSS libraries are not permitted for this project.

---

### Today's itinerary [1/2]
1. Docker introduction:
    - Video: [12-minute Docker Overview](https://www.youtube.com/watch?v=YFl2mCHdv24) (listed under Tuesday in Open)
    - Reading: Non Technical Overview of Docker

2. Docker installation (if not already installed):
    - Reading: Docker Installation
        - If you want to test your installation:
        - `docker container run --rm hello-world`
    - NOTE FOR WSL USERS: You must upgrade to WSL2 to use Docker

3. Alpine Linux video & readings
    - Video: Installing Packages on Alpine Linux
    - Reading: Notes for Installing Packages on Alpine Linux
    - Reading: Linux Basics


---

### Today's itinerary [2/2]

Start meeting with your groups and project planning!
<style>
    .present {
        text-align: left;
    }
</style>

---

###### tags: `Week 19` `W19D1`

---

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

- In order to understand Docker, we should first discuss how our computers work to begin with.
- Your computer has physical hardware, an OS, and a kernel that interfaces between the two, which are all tightly coupled.
- When we build & deploy apps with this environment, we are limited to the performance of our machine and the libraries that are compatible with it.

---

### How does Docker work?
#### Part 2: Why not use a VM?

- A VM has an OS that is *decoupled* from your computer's hardware. With VMs, can have multiple OSs running on a computer.
- A VM has a kernel & hypervisor. The kernel interfaces between the hardware and the OS. The hypervisor creates & runs a VM.
- A VM is heavy - we often don't need an entirely separate kernel & hypervisor just for the purposes of deploying an application.


---

### VM Visualization 

<img src="https://k21academy.com/wp-content/uploads/2020/06/Virtual_Machine_Architecture.png" />



---

### How does Docker work?
#### Part 3: Docker containers

- A Docker container is like a mini-VM that is hardware agnostic - it doesn't care about the host OS.
- It is lightweight - it consists only of a small Linux distribution and necessary libraries & resources. It does not have its own kernel or hypervisor.
- This makes it much more scalable and allows us to run many more containers on one machine than VMs.


---

### Docker Visualization

<img src="https://k21academy.com/wp-content/uploads/2020/06/output-onlinepngtools-16.png" />



---

### Virtual Machine vs Docker

<img src="https://k21academy.com/wp-content/uploads/2020/05/2020_05_13_12_19_07_PowerPoint_Slide_Show_Azure_AZ104_M01_Compute_ed1_-1024x467.png" />


---

### Cool... but why are we learning about Docker?
- We can easily scale an application using a cluster of containers on one or more machines
- We can easily share our application with others for testing & development
    - We can build a template for our application called an *image* 
    - We can automate the process of building & deploying that image with *docker compose*
- We can run the same application on *any* machine without worrying about performance or incompatibilites
   

---


## Docker topics
- Intro and installation (today)
- Docker Containers (Tuesday)
- Docker Images & Dockerfiles (Wednesday)
- Docker Compose (Thursday)

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
- Multithreading/concurrency EOD from Caleb Braaten!

---

### Project Begins! (Friday)
- Fishing up all project documentation
- Mark Rodriguez talks to us about ~the future~!
- Walkthrough the project starter

---

### Group Project Planning
We will have time allotted each day this week to work on group project planning!

Use [this schedule](https://github.com/appacademy/Module-6-Resources/blob/main/group_project_resources/project-planning-sheet.md) to help guide your planning this week.

You must produce 4 design documents for approval by your project advisor this week: 
- Feature list
- User stories
- Database schema
- Grading scorecard


---



## Steps to Get Started on the Project

1. Come up with an idea for your project with your group and create a Feature List for Instructor approval. Make sure to get instructor approval on your feature list before continuing on with your other design docs.
2. Start an empty git repository WITHOUT a readme and create a wiki in your repo to hold all of your design docs. Share your wiki with your project advisor.
3. The project starter repo will be released on Friday. Do not start coding until this is released AND you have finished your design docs!


---


## Daily Planning Schedule

The following schedule is a general guideline for how to proceed with project planning.



| Day | Tasks to Work On         | Design Docs Due                |
| :------: | :--------------- | :--------------------- |
|   Monday    | Choose Project, Feature List        |     |
|   Tuesday    | Feature List, User Stories      | Feature List    |
|   Wednesday    | Scorecard Link   | Scorecard Link, User Stories   |
|   Thursday    | DB Schema         |   |
|   Friday    | DB Schema, *Optional: API Routes, Wire Frames, Redux State Shape, Set up Scrum Board & Issues*         | DB Schema     |



---

## Optional Design Docs

You do not need to follow this schedule exactly! We prefer to you to take time with your planning - it is ok to turn in your docs after their "due" dates.

Submit your design docs for review by tagging your project lead in your group slack channel with a link to your GitHub wiki page.

Redux State Shape, API routes, Frontend Routes, and Wire Frames are optional but might be helpful!


---


## Instructor GitHub Handles

Please add your instructors to your project repo.

- Brad: bradsimpson213
- John: jwily
- David: hisownspace
- Cesar: 171cas
- Drew:  Drewthurm21


---


## SCORECARD!  [Scorecard Template](https://docs.google.com/spreadsheets/d/1OtaNB31kl_FhGrEPl-GoOmTvJrQurAF1jsr3Ts_d-I4/edit#gid=1927083016)

Please make a **copy** of this template for your scorecard. Fill out the purple sections and share your scorecard with your project advisor and cohort lead.




___



### Group Projects
You are free to choose between cloning an existing app, creating your own, or something in between! Possible clones are listed in a/A Open under `Week 20 - Python Project -> Expectations -> Python Group Project`.

You must use the Python project starter code.

You must have 4 MVP features - at least 2 of which must be full CRUD features.

You may use packages and modules not covered by the App Academy curriculum (React libraries, Flask libraries, etc.), but CSS libraries are not permitted for this project.

---

### Today's itinerary [1/2]
1. Docker introduction:
    - Reading: Non Technical Overview of Docker
    - Video: [12-minute Docker Overview](https://www.youtube.com/watch?v=YFl2mCHdv24)

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
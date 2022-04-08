# Microservices
## Week 19 Day 5

---

## What are Microservices?

Microservices are a method of designing applications in terms of many sub-services rather than a single, monolithic service.

Each microservice is a small, isolated service that interacts with other microservices to construct a complete application.

Microservices are organized around an application's services, not around its technology layers.

---

## Microservice architecture

Each microservice is a complete technology stack. It may contain server-side APIs, databases, and sometimes client-side UI.

![](https://i.imgur.com/9lTeUcv.png)

---

## What are the benefits?
There are many benefits to a microservice-based approach to development:
- Each service can be developed, tested, and maintained by a separate team
- Each service can be scaled up/down more easily
- Better fault isolation
- Can diversify technologies more easily

---

## What are the downsides?
There are of course downsides to this design framework:
- Remote calls are more expensive between separated services
    - Higher chance of communication failure
- Deployment can be more complicated
- Can be difficult to maintain with differing languages/technologies between services

---

## Implementing Microservices with Docker

We can use `docker compose` to implement and bring up a microservice-based application with ease.

This tool allows us to automate application set up and scale up individual services with new containers as needed.

With this approach, each microservice image is built using a `Dockerfile`. The complete application is then created with `docker compose`, which starts up all necessary microservice containers, networks, and volumes.

---

## Today's Schedule

- Microservices projects are optional
- Finish up all project planning today and make sure your **feature list, user stories, and DB schema are approved**
- 12:30 PST: Discussion with Mark about ~ the future ~
- 2:30 PST: project starter walkthrough!

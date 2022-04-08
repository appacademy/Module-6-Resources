# User-facing routes

## `/login`

### Log in page

This page displays a log in form

* `GET /login`
* `POST /login`

## `/signup`

This page displays a signup form.

### Sign up page

* `GET /signup`
* `POST /signup`

## `/`

This page displays the ten most recent FauxTweets and their FauxLikes, as well as a navigation bar with login/signup or logout buttons.  Each FauxTweet has an update and delete button _if it belongs to the currently logged in user_.  Logged in users can FauxLike the FauxTweets on this page.

* `GET /`
* `POST /fauxtweets/:id/fauxlikes`
* `DELETE /fauxtweets/:id/fauxlikes`

## `/fauxtweets`

This page displays a form with which a logged in user can craft a new FauxTweet, as well as a navigation bar with login/signup or logout buttons.

* `POST /fauxtweets`

## `/fauxtweets/:id`

This page displays individual FauxTweets with associated FauxComments and FauxLikes, as well as a navigation bar with login/signup or logout buttons.  If the logged in user owns the FauxTweet, this page also displays an update and delete button.  Logged in users can FauxLike the FauxTweet and FauxComments on this page, and can post FauxComments.  The logged in owners of those FauxComments can update or delete them.

* `GET /fauxtweets/:id`
* `POST /fauxtweets/:id/fauxlikes`
* `DELETE /fauxtweets/:id/fauxlikes`
* `POST /fauxtweets/:id/fauxcomments`
* `DELETE /fauxtweets/:id/fauxcomments`

# User Stories

## Users

### Sign Up

* As an unregistered and unauthorized user, I want to be able to sign up for the website via a sign-up form.
  * When I'm on the `/signup` page:
    * I would like to be able to enter my email, username, and preferred password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the sign-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the sign-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
    * So that I can try again without needing to refill forms I entered valid data into.

### Log in

* As a registered and unauthorized user, I want to be able to log in to the website via a log-in form.
  * When I'm on the `/login` page:
    * I would like to be able to enter my email and password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the lob-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the log-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
      * So that I can try again without needing to refill forms I entered valid data into.

### Demo User

* As an unregistered and unauthorized user, I would like an easy to find and clear button on both the `/signup` and `/login` pages to allow me to visit the site as a guest without signing up or logging in.
  * When I'm on either the `/signup` or `/login` pages:
    * I can click on a Demo User button to log me in and allow me access as a normal user.
      * So that I can test the site's features and functionality without needing to stop and enter credentials.

### Log Out

* As a logged in user, I want to log out via an easy to find log out button on the navigation bar.
  * While on any page of the site:
    * I can log out of my account and be redirected to a page displaying recent FauxTweets.
      * So that I can easily log out to keep my information secure.

## FauxTweets

### Create FauxTweets

* As a logged in user, I want to be able to post new FauxTweets.
  * When I'm on the `/new-fauxtweet` page:
    * I can write and submit a new FauxTweet.
      * So that I can share my thoughts and memes with my friends.

### Viewing FauxTweets

* As a logged in _or_ logged out user, I want to be able to view a selection of the most recent FauxTweets.
  * When I'm on the `/fauxtweets` page:
    * I can view the ten most recently posted FauxTweets.
      * So that I can read and interact with the thoughts and memes of my friends.

* As a logged in _or_ logged out user, I want to be able to view a specific FauxTweet and its associated FauxComments and FauxLikes.
  * When I'm on the `/fauxtweets/:id` page:
    * I can view the content of the FauxTweet, as well as the associated FauxComments and FauxLikes.
      * So that I can read and interact with the thoughts and memes of my friends, and add my own thoughts and memes in the FauxComments.

### Updating FauxTweets

* As a logged in user, I want to be able to edit my FauxTweets by clicking an Edit button associated with the FauxTweet anywhere that FauxTweet appears.
  * When I'm on the `/fauxtweets`, `/fauxtweets/:id`, or `/users/:id/fauxtweets` pages:
    * I can click "Edit" to make permanent changes to FauxTweets I have posted.
      * So that I can fix any errors I make in my FauxTweets.

### Deleting FauxTweets

* As a logged in user, I want to be able to delete my FauxTweets by clicking a Delete button associated with the FauxTweet anywhere that FauxTweet appears.
  * When I'm on the `/fauxtweets`, `/fauxtweets/:id`, or `/users/:id/fauxtweets` pages:
    * I can click "Delete" to permanently delete a FauxTweet I have posted.
      * So that when I realize I shouldn't have publicly said something, I can easily remove it.

# API-Routes

This web app uses the following API routes to dynamically update the page to create a single-page-app-like feel for the user for specific features.

## FauxComments

* A logged in user may delete one of their own FauxComments, removing it from the list of visible FauxComments without causing a refresh/redirect.

  * `DELETE /api/fauxcomments/:id`

## FauxLikes

* A logged in user can FauxLike or FauxUnlike a FauxTweet or FauxComment with visible confirmation without causing a refresh/redirect.
  
  * `POST /api/fauxtweets/:id/likes`
  * `POST /api/fauxcomments/:id/likes`
  * `DELETE /api/fauxtweets/:id/likes`
  * `DELETE /api/fauxcomments/:id/likes`

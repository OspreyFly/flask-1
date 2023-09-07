### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  1. Python syntax is clean and easier to read while JavaScript has a more flexible, but messier looking C based syntax with brackets and semi colons.
  2. Python can be used for many more purposes because of how many supporting libraries are available. However, Javascript is dominant in Web Development.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  1. Using error handling like try & catch
  2. Checking that it exists before trying to access it

- What is a unit test?

  A test that is focused on very limited scope functions.

- What is an integration test?

  A test that is focused on finding bugs related to dependancies outside the scope of a file or program.

- What is the role of web application framework, like Flask?

  To simplify the process of managing different views and handling requests.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  If the page is all about pretzels, it makes sense to create a route just for that because it's essential. However, if 'pretzel' is part of a search or filter then it makes more sense to include it as a query parameter.

- How do you collect data from a URL placeholder parameter using Flask?

  You must define a route with a placeholder in the url using angle brackets to indicate the parameter. Then you can access it as a parameter of the view function.

- How do you collect data from the query string using Flask?

  You can use the request.args method and assign it to a variable.

- How do you collect data from the body of the request using Flask?

  Using request.json

- What is a cookie and what kinds of things are they commonly used for?

  They are string and value pairs of information that the server wants the client browser to store.

- What is the session object in Flask?

  It can be used to store session information about a user's browsing instance

- What does Flask's `jsonify()` do?

  It creates data that can be used in a response.

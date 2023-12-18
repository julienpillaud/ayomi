# Ayomi

This project define an API to make calculation with the `Reverse Polish Notation`

1. Calculate the result

The route `POST` `/rpn` allow to send in the body a list of operators and operands to get the result.
The elements and the result are saved in the database.

Operators accepted : `+` `-` `*` `/`

2. Retrieve the results

The route at `GET` `/rpn/csv` download a csv file with all the results in the database.

The route `GET` `/rpn` can retrieve the results acording to the specified filter.

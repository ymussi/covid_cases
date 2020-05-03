# Covid Cases
Api responsible for capturing data on covid19 cases in Brazil.

The data are saved raw in a relational database.

# to get the BrazilIO data and update our database:

- https://covid-cases-br.herokuapp.com/cases/

# To search cases of the specific city:

- https://covid-cases-br.herokuapp.com/cases/list-cases/{city}

- OBS: this url -> https://covid-cases-br.herokuapp.com/cases/list-cases return cases of the "São Paulo"


# TODO

- Set up a task scheduler to retrieve the data every day at 01:00pm
- Tests
- ...
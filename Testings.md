# Testings

## Automated Testings

- Unit testings in `posts` app.

  - ### PostListView Testcase

    ![Post list view testcase](static/readme-images/post-list-view-test.png)

  - ### PostDetailView Testcase

    ![Post details view testcase](static/readme-images/post-details-view-tests.png)

  - ### Results for the testings

    ![result od Post testcase](static/readme-images/post-automated-result.png)

## URL Testings

- Both the development and deployed versions of each URL have been manually tested by adding all the `/profiles`, `/posts`, `/comments`, `/likes`, `/bookmarks`, and `/followers` next to url path one at a time to ensure everything is working.

  ![url testings perfomed](static/readme-images/url-testings.png)

## CRUD Functionality Testings

- Tested that users can search posts by post title or by the username of the posts owner.

- ### Development Testings

  - To test each crud functionality. I created two separate users and went through each url and their crud endpoints to test if everything was working as expected and everything was working fine.

- ### Deployed Testings

  - To test the deployed site, same steps were taken as development testing, only this time I had to use the Admin panel `https://coding-library-drf-api.herokuapp.com/admin/` to test all the crud functionalities.

  ![crud testings perfomed](static/readme-images/crud-testings.png)

  Additionally, frontend crud testing has been performed, which can be found on [Coding Library](https://github.com/hashim222/p5-coding-library) testings section.

## Code Validation

- This project has been run through the [Code Institutes python linter](https://pep8ci.herokuapp.com/) and [pylint](https://pypi.org/project/pylint/)(which was installed in the project) and found no errors or warnings except in the `settings.py` file long line which was related to built-in Django code.

  ![CI python linter to validate my code](static/readme-images/CI-python-linter-test.png)
  ![pylint to find any problems in my code](static/readme-images/pylint-code-validator.png)

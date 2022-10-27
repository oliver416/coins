## Note
The difference between `develop` and `master` branches is a commit related to the docker development in `master` branch.
## Develop environment
```commandline
git checkout develop
pipenv shell
./manage.py runserver 
```
## Master environment
```commandline
git checkout master
docker-compose up
```
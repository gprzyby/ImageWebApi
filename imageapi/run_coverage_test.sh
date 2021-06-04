#!/bin/bash

activate_venv () {
  source ../venv/bin/activate
}

cleanup_test_enviroment () {
  coverage erase
}

test_and_create_html_report () {
  coverage run manage.py test
  coverage report
  coverage html
}

activate_venv
cleanup_test_enviroment
test_and_create_html_report
nohup xdg-open htmlcov/index.html &

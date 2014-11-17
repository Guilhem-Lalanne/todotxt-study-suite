#!/bin/bash
# command to copy these over to your actual todotxt
# mostly for me when I make updates to the script
# still have to change these varialbes though so?

export TODO_DIR="/media/Data/Dropbox/.todo"
export TODO_ACTIONS_DIR="$HOME/.todo.actions.d"

cp .todo.actions.d/* $TODO_ACTIONS_DIR

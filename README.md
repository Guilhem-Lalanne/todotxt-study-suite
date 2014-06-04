punch
=====

Punch for Todo.txt

This is a fork of https://github.com/adewinter/punch, which is a project forked from http://code.google.com/p/punch-time-tracking/:

 " Punch is a time-tracking add-on for todo.txt - a command line to-do list list utility. Punch works alongside the todo.txt script files popularized by Life Hacker and todotxt.org. All time tracking info is kept in a separate file, so no harm is done to the todo.txt system. It does use your todo.cfg file and todo.txt file to streamline time tracking. "

features
========

Adding the feature to specify a custom time to punch in and out.

ex. `punch in 31 8:23' where '31' is the line number of the task you wish to track and 8:23 is the time you started that task

ex. 'punch out 14:05' where '14:05' is the time you ended that task

todo
====

+ currently the argument arfter the line number for 'punch in' is used to specify the file to get the todo from. need to figure out a way to keep this functionality

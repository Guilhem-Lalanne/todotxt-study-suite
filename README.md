contents
========
- addr
- lsgroup
- lsp
- punch
- daily


_addr_: add task with the projects and contexts of the last added task
====

A helpful todo.sh command when you are adding lots of related tasks. It simply appends the tags of the most recent item to the item you add.

ex. `./todo.sh add 'SOMETHING @context +project'`
ex. `./todo.sh addr 'SOMETHING ELSE'`

<pre>
$ t add 'here is a a task +context +project'
59 here is a a task +context +project
TODO: 59 added.

$ t addr 'here is another task'
Appending: +context +project
60 here is another task
TODO: 60 added.
60 here is another task +context
60 here is another task +context +project
</pre>


_lsgroup_: 
=====
# Prints in columns organized by either context or group

To print your todo.txt by context.

####lsgc
ex. `./todo.sh lsgc`

To print your todo.txt by project.

####lsgp
ex. `./todo.sh lsgp`

<pre>
$ t lsgc
@play                                              @code                                              
(A) task                                           (B) task                                           
(C) task                                           task                                               
task                                               task +research                                     
task                                               task +tool                                         
task                                                                                                  
task                                                                                                  
                                                                                                      
@email                                             @context                                           
(A) this guy                                       (A) task +project                                  
(A) this guy +project                              (D) task +project                                  
this guy                                           task +project                                      
this guy                                                                                              
this guy                                                                                              
this guy                                                                                              
this guy                                                                                              
this guy   
</pre>

_lsp_:  
=====
# Prints out all your top priorit tasks from (A)...(E)

Ok, this is actually really just an alias for ls that passes "'(A)\|(B)...(E)'". Doesn't mean that it isn't useful :P


_watch_: 
=====
Watches your todo text and syncs with google drive with [https://github.com/odeke-em/drive](this client written in Go.)

Executes todo,sh lsgp for you while with color on file changes. Also runs `drive pull` and `drive push`.


<!-- 
_punch_: still a work in progress
=====

Punch for Todo.txt

This is a fork of https://github.com/adewinter/punch, which is a project forked from http://code.google.com/p/punch-time-tracking/:

 " Punch is a time-tracking add-on

  for todo.txt - a command line to-do list list utility. Punch works alongside the todo.txt script files popularized by Life Hacker and todotxt.org. All time tracking info is kept in a separate file, so no harm is done to the todo.txt system. It does use your todo.cfg file and todo.txt file to streamline time tracking. "

####features

Adding the feature to specify a custom time to punch in and out.

ex. `punch in 31 8:23` where '31' is the line number of the task you wish to track and 8:23 is the time you started that task
ex. `punch out 14:05` where '14:05' is the time you ended that task

####todo

+ currently the argument arfter the line number for 'punch in' is used to specify the file to get the todo from. need to figure out a way to keep this functionality


_daily_: still a work in progress
=====

Daily is a python script to track your daily stats over time, such as the time you wake up, the time yo go to bed, the things you eat everyday. In the future, hopefully it will support graphing these stats over itme so you can see trends.

-->

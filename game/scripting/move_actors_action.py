from game.scripting.action import Action
# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor
class MoveActorsAction(Action):

    def execute(self, cast, script):

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
            
"""
Directing is good
SCripting main stuff is good
The drwaing needs to be updated
Casting name space should mostly be used with the exception of not calling it snake and changing the class name
and a little bit of code. 
Tron is really just 2 snakes but their paths are growing by one.
In essence just check if they collide which is already there.

"""
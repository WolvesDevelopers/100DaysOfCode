print("""                   ==========THE DRAGON CAVE ADVENTURE I==========

                               _
                            ==(W{==========-      /===-
                              ||  (.--.)         /===-_---~~~~~~~~~------____
                              | \_,|**|,__      |===-~___                _,-'`
                 -==\\        `\ ' `--'   ),    `//~\\   ~~~~`---.___.-~~
             ______-==|        /`\_. .__/\ \    | |  \\           _-~`
       __--~~~  ,-/-==\\      (   | .  |~~~~|   | |   `\        ,'
    _-~       /'    |  \\     )__/==0==-\<>/   / /      \      /
  .'        /       |   \\      /~\___/~~\/  /' /        \   /'
 /  ____  /         |    \`\.__/-~~   \  |_/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _) | ;  ),   __--~~
                    '~~--_/      _-~/- |/ \   '-~ \
                   {\__--_/}    / \\_>-|)<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |   _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o-o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
""")



print("Welcome to Dragon Cave.")
print("Your mission is find the Legendary Dragon and Kill him.") 


path = input("You're at a cross road. Where do you want to go ? type left or right\n").lower()
if (path == "left"):
    prompt = "To reach the dragon's cave, you must cross the swamp of the dead.\n "
    prompt += 'Type "wait" to wait for a boat. Type "swim" to swim across. \n'
    question1 = input(prompt).lower()
    
    if(question1 == "wait"):
        prompt2 ="You arrive at the cave unharmed. Inside the cave there are 3 paths each path has a flag. One red, one yellow and one blue, which color do you choose?\n"
        question2 = input(prompt2).title()
        
        if(question2 == "Yellow"):
            print("You have encountered the legendary Dragon, and have had a fierce battle, but thanks to Valkirim's magic sword you have won the battle.\nAll the treasures stolen by the dragon are now yours.")
        elif(question2 == "Blue"):
            print("In this path a protection mechanism has been activated, hundreds of arrows were thrown at our adventurer and he has died.\nGame Over.")       
        elif(question2 == "Red"):
            print("Unfortunately for our adventurer, this path was slippery, and led straight to the dragons' nest, our adventurer was eaten by dragon hatchlings and died.\nGame Over.")
        else:
            print("Our adventurer was bitten by a poisonous snake, and has died before entering a trail.\nGame Over")
    
    else:
        print("While swimming through the swamp, our adventurer was ambushed by goblins that were camouflaged with mud, our adventurer was violently attacked and died.\nGame Over.")

else:
    print("This path led our adventurer to the garden of poisonous flowers, where the thorns put an end to his adventure.\nGame Over.")

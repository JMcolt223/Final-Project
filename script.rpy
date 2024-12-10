# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Character dimensions 700 x 1048
#Backgrounds 1920 x 1080

define m = Character("Mia", color = "#ff0303")
define ka = Character("Katie", color ="#45f03c")
define a = Character("Ash", color = "#110dd5")
define k = Character("Kent", color = "#ff6a00")
define j = Character("James", color = "#a409b5")
define s = Character("Steve (You)", color = "#ffffff")

# The game starts here.
#Choose your scenario... either the superior drink, everyone falls in love with  you,
# the ghost girl, or the penny pinchers, or the one where they all get along. 

label start:

    
    scene bg black
    "Battle of the Beverages!"
    #Battle of the superior drink.. Just dialougue


    scene bg cafe


    show kent confident 4 at left

    k "Hey boss man, I would die for your famous punch right now."

    show mia mock with moveinright

    m "Ordering a punch in a cafe. Classic."
    m "Not to mention..."
    m "It's seven in the morning."

    a "I'm telling you, the punch here is the future."
    a "Sweet, tangy, and just enough fizz to keep you guessing"
    a "You're all missing out."

    show mia doubt 

    m "Kent, we get it. You love a good false reality."
    m "Some of us like to enjoy our drinks without needing a flashy light show in a glass."

    show katie worry 2 at right with moveinright

    ka "Mia, don't you think that's a little harsh?"
    ka "I mean... James is just as excited... Right, James?"

    hide kent with dissolve

    show james normal at left with moveinleft

    j "Me?"
    j "Excited?"
    j "Not possible."

    hide katie worry 2 with dissolve

    show kent confident 4 at right with moveinright

    m "Can we talk about what's really important?"
    m "Some of us have taste, Kent..."

    show kent oh man

    k "Yeah you never stop blabbering do ya?"
    k "I'm tired of you sitting there all prissy with your cute little caramel latte"
    k "Try something different for a change..."

    show mia very mad

    m "There is nothing wrong with my Cutesy Caramel Latte."
    m "It's perfectly ordinary."
    m "Why can't you be mature for once and just order something normal."
    
    k "It sounds like you want me to be as bland and boring as James"
    k "Thinks he's so manly for ordering a black coffee"
    k "Talk about grow up."

    j "Bland and boring?"
    j "Classy."
    j "Come on kids just hug and make up all right?"

    m "There must be a way we can solve this..."

    k "Hmm..."
    k "I've got it!"
    k "How about a battle of the beverages?"
    
    m "Oh, come on."
    m "You sound ridiculous."

    j "You must be joking."

    k "I'm not!"
    k "Come on guys, it'll be a blast!"
    k "We can solve this like real adults."

    show mia doubt

    m "'Real' and 'adult' are the last two words I would use to describe you."

    hide kent oh man with dissolve
    show katie worry 2 at right with moveinright

    ka "Wait, Mia"
    ka "I think he may be on to something..."

    m "Onto something?"
    m "Or on something..."

    ka "..."

    j "Just suck it up and play his stupid game, Mia"

    hide katie worry 2 with dissolve
    show kent confident 4 at right with moveinright

    k "Oh..."
    k "You guys thought you weren't gonna be involved huh?"

    j "Oh boy..."

    hide james normal with dissolve
    show katie worry 2 at left with moveinleft

    ka "Eek!"
    

    k "That's right ladies and gents. We're ALL gonna participate in this battle."
    k "And I mean EVERYONE..."
    k "Steve?"

    menu:
        k "You in?"
        "...":
            k "Great! You're the best bro!"
        "Nah, I'm good.":
            k "Was that a yes I heard?"
            k "I think it was!"
            k "Thanks Steve your the man."

    s "......."

    ka "Ummm Kent are you sure he wants to do this..."
    ka "I just don't want him to feel pressured..."

    k "Awwww look at this little sweetheart"
    k "Does someone have a wittle cwush on Stevey Weevy?"
    k "And he's fine."
    k "Trust me"
    k "It's a bro thing"
    k "I can like totally mind read"

    m "Whatever, Kent, just tell us what you want."

    k "So here's the plan..."
    k "We order what we think is the best drink at this cafe right"
    k "We each give a speech on why our drink is the best"
    k "Then, we have Steve try each one and choose his favorite"
    k "Whaddya say?"

    m "..."
    m "Beating you in battle of the beverages doesn't sound too shabby"
    m "I'm in."

    k "James?"

    hide katie worry 2 with dissolve
    show james normal at left with moveinleft


    j "Why am I always dragged into everyone's mess..."
    j "..."
    j "Ugh..."
    j "I'm in..."

    k "Love the spirit, James!"
    k "Katie?"

    hide james normal with dissolve
    show katie worry 2 at left with moveinleft

    ka "I guess I'm in..."
    ka "Do I really have to do a speech..."

    k "Sweet!"
    k "Without further ado..."
    k "Let's begin"

    scene bg black
    "First contestant..."
    "Kent"

    scene bg cafe
    show kent confident 4

    k "Okay boss let's get this show on a roll."
    k "Here I present you..."
    k "The Power Packs a Punch punch!"
    k "With this bad boy right here you're getting over four times the caffiene!"
    k "Energy for days!"
    k "Right on!"
    k "The taste... mmm... the taste"
    k "Absolutely awesome"
    k "The name of the drink is no lie... It really packs a punch"
    k "Perfect amount of sweet and tangy"
    k "Did I mention that the taste just dances on your tongue?"

    scene bg black
    "Contestant number two..."
    "Mia"

    scene bg cafe

    show mia doubt

    m "I'm gonna switch things up for this one..."
    m "Here I have..."
    m "The Cute Kitty cappuccino "
    m "I can't deny that it's meowtastic!"
    m "Unlike Kent's disgrace for a drink... the Cute Kitty cappuccino is perfect for any time of day"
    m "Morning, evening, night, midnight, you tell me!"
    m "Not too sweet, but the perfect sweetness to bitterness ratio."
    m "Just looking at the drink gives me a cuteness overload!"

    scene bg black
    "Contestant number three..."
    "James"
 
    scene bg cafe
    show james normal

    j "Alright. Let's get this over with"
    j "Here I have a dark roast black coffee"
    j "Not too sugary so you won't get fat"
    j "Tastes good. Definitely an aquired taste"
    j "It's also the cheapest"
    j "Is there more to say?"

    scene bg black
    "Final contestent..."
    "Katie"

    scene bg cafe
    show katie worry 2

    ka "Hi." 
    ka "I really like the Crazy for Cocoa Puffs Frappucino"
    ka "I guess I just really like sweet drinks haha..."
    ka "I hope you like it..."
    ka "It's really good and yummy"
    ka "I would get it every single day, but I know my friends would make fun of me for it..."
    ka "But you wouldn't care right, Steve?"

    scene bg black
    "Alright time for you to choose the winner."
    "Stressful wasn't it?"

    menu:
        "Who's drink won?"
        "Kent":
            scene bg cafe
            show kent confident 4

            k "Man, I knew I could trust you"
            k "I told you that punch was to die for didn't I?"
            k "Hey, thanks for choosing me"
        "Mia":
            scene bg cafe
            show mia doubt

            m "I won! Yes!"
            m "I knew my drink was the bomb."
            m "Steve you're the best!"
            m "I love-"
            m "..."
        "James":
            scene bg cafe
            show james normal

            j "Cool."
            j "Thanks."
            j "..."

        "Katie":
            scene bg cafe
            show katie worry 2

            ka "Steve!"
            ka "You really chose me..."
            ka "Thanks..."
            ka "Eek!!!"



    
    

    #continue argument and then show the next day...

    scene bg black
    "Love is in the Air"


    #Everyone falls in love with Steve
    # YOu get to pick ur girl and have a fun scene with whoever you choose
    #3 endings
    scene bg cafe

    show katie worry 2 

    ka "Hey..."
    ka "I'm sorry you had to hear all that yesterday, Steve"

    menu:
        "It's no big deal.":
            ka "Okay..."
        "Don't worry about it.":
            ka "I'll try. I just feel so bad."

    ka "Anyway..."
    ka "I'd like to order... if that's okay of course."
    ka "I just need something to calm the nerves."
    ka "Yesterday was a lot for me"
    
    menu:
        ka "What do you reccommend?"
        "Green tea":
            ka "That sounds wonderful!"
            ka "Perfect to calm me down."
        "A venti caramel latte with extra caramel, oat milk, extra whipped cream, and 4 pumps of simple syrup.":
            ka "That wouldn't work at all!"
            ka "Just thinking about that makes my skin crawl..."
            ka "I'll just go with a green tea... thanks..."
    
    "Here you go"

    ka "Thank you!"    
    
    scene bg black
     
    "Katie guzzles down her drink."

    scene bg cafe
    show katie worry 2
    ka "Mmm just what I needed!"


    ka "You know..."
    ka "You're a really great guy Steve."
    ka "*Blushes cutely*"

    hide katie worry 2 with dissolve

    scene bg black
    s "???"

    show bg cafe
    show mia doubt with dissolve

    m "Steve, I really need your help"
    m "I don't know why I'm here I'm late for a work meeting"
    m "Boss is gonna kill me..."
    m "Hey can I just get a Sugar Bear Snickerdoodle iced coffee?"

    menu:
        "You got it sister":
            m "Oh... sister..."
            m "Just a sister..."
        "No prob":
            m "Thanks."
    
    m "So... Steve... the man"
    m "How's life goin?"

    menu:
        "Shouldn't you go to work?":
            m "I'm telling I swear I was possessed."
            m "Something is in the air today... I can feel it."
            m "I was dragged here by a spirit."
            m "I must have a purpose here."
        "Go to work? Lazy...":
            m "Don't say that!"
            m "I was possessed by a devil."
            m "He led me to you..."
            m "Funny huh... must be a sign."
    
    s "..."

    m "Maybe the wind blew me hear today."
    m "Or maybe I'm just being silly" 
    m "Hey Steve..."
    m "*Starts blusing*"
    m "Are you... into me?"

    scene bg black
    s "What was that..."

    scene bg cafe

    show ash normal with dissolve

    a "Hey."
    a "Can I..."
    a "Oh..."
    a "I was mumbling again wasn't I?"
    a "I'm sorry"
    a "Wait, why did I apologize"
    a "Why am I talking so much?"
    a "Ugh... embarassing."
    a "Can I..."
    a "Can I get an extra hot super large hot cocoa?"
    a "*mumbles* Like you..."
    a "Ugh. Just hand it over."
    a "Hey, wait."
    a "You seem pretty cool."
    a "Do you think I'm cool?"
    a "You better..."

    scene bg black

    "What is going on today?"

    scene bg cafe
    "All three girls show up"
    "They have hearts in their eyes."
    "Good luck..."

    show mia doubt with moveinleft
    show katie worry 2 at left with moveinleft
    show ash normal at right with moveinright

    m "Steve... you've got some explaining to do..."
    m "Seems you've been flirting with other women..."
    m "Nope nuh uh this won't slide"
    m "I'm sorry, but..."
    m "You're gonna have to chooose..."

    ka "Mia! Don't do this to him..."

    m "Quiet, pipsqueak."

    a "..."
    a "Choose wisely..."
    a "Or else..."
    a "Just kidding hahahaha"

    menu:
        "Who are you taking on a date?"
        "Mia":
            m "Smart choice."
            m "Let's roll."

            scene bg city
            show mia doubt
            m "I thought it would be fun to show you where I grew up."
            m "Neat, isn't it?"
            m "It's a little ratchet, but... it's home... heh..."
            m "I thought we could drink."
            m "Surely, we both need it."
            m "Let's drink to our hearts content!"

            scene bg black
            "Mia gets absolutely plastered..."
            "You only had on sip of beer."

            scene bg city 
            show mia doubt

            m "Blerghhh"
            m "Mmm"
            m "'Cuse me"
            m "Hahaha Schteve..."
            m "I wuvvv you!!"
            m "Heheheheh..."
            m "Come home with me."

            scene bg black
            "You take Mia home."
            "She vomitted all over you."
            "You never want to see alcohol again..."
            "Even I feel bad for you..."
            "I'm not even real."

        "Katie":
            ka "Eeeeeek! Really?"
            ka "Oh... sorry I got too excited."
            ka "So... let's go?"
            scene bg field
            show katie worry 2 with dissolve

            ka "I told you I knew a spot hehehe!"
            ka "Hey, Steve..."
            ka "I just wanted to say"
            ka "I'm so happy that you chose me..."
            ka "I'm usually so shy... but when I'm around you I feel more comfortable."
            ka "Let's have a picnic. What do you say?"

            menu:
                "Deal.":
                    ka "Hehehehehehe eeeeeek!"
                "Mmm yummers":
                    ka "Let's get to grubbin! Hehehe"

            scene bg black

            "You guys gobble down some food as you enjoy the view..."
            scene bg field

            show katie worry 2 with dissolve

            ka "Mmm! I'm stuffed like a turkey!"
            ka "Steve..."
            ka "This was a blast!"
            ka "I hope you feel the same..."
            ka "*Blushes*"

        "Ash...?":
            a "I knew it muahaha!"
            a "For some reason the guys always choose the crazy girls."
            a "I knew I was your type"
            a "Come with me."

            scene bg cave
            show ash normal with dissolve

            a "So..."
            a "Welcome to my favorite place..."
            a "Do you like it?"

            menu:
                "Absolutely more than anything! *nervously*":
                    a "Right answer."
                "I love it haha... *shaking in your boots*":
                    a "I knew you'd love it."

            a "Hey, I want to give you a gift."
            a "Hold out your hand."
            a "..."
            a "It's a bone!"
            a "Cute right?"
            a "Wow."
            a "I'm so glad you understand me"
            a "I love you, Steve."
            a "Marry me-"

            scene bg black
            "You attempt to run away..."
            "Ash is not far behind you..."
            "You haven't been hitting the gym recently so you run out of breathe..."
            "You've been captured by Ash"





    scene bg black

    show james normal 
    j "Whew"
    j "You made it..."
    j "I have no idea how you survivied this torturous game..."
    j "I commend that."

    show kent confident 4 at right with moveinright

    k "Yeah, man I salute you"
    k "Those girls were crazyyyy!"
    
    j "Kent...."

    k "Haha sorry!" 

    hide kent confident 4 with dissolve

    j "..."
    j "I guess this is the end?"

    scene bg black
    "The End..."

#The one with the ghost girl (Ash)
    scene bg cafe





    # This ends the game.

    return

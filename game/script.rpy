# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define a = Character ("Anu (You)", who_color="#F3C324", what_color="#FFFFFF")
define guide = Character ("Guided Lady", who_color="#EBBFFF", what_color="#FFFFFF")

image anu_breathe_inout:

    "anulargesticker.png"

    subpixel True
    truecenter

    pause .45
    zoom 1.0
    ease 1.25 zoom 1.25
    pause 1.25
    ease 1.0 zoom 1.0
    pause 2.0
    zoom 1.0
    ease 1.0 zoom 1.25
    pause 1.25
    ease 1.0 zoom 1.0


image journey_to_zen:
   
    "anuroomstandardat80.png" with fade
    pause 4.0
    "anunearzen.png" with fade
    pause 4.0
    "anuzenstate.png" with fade
    pause 4.0



    
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #scene theplaceholder
    #scene theplaceholderv_two

    play music "Cold & Rainy Looped.mp3" 
    

    show emptyroom
    with fade

    # These display lines of dialogue.

    
    #//////NARRATION

    "It's 8pm and you've just gotten into your comfy home clothes..."
    "You know - the ones  NO HUMAN  is supposed to see you in, apart from Lumi and baby Shai."
    "Lumi has 'clocked in' for childcare responsibilities to give you an opportunity to do your daily evening meditation..."
    "...even though it's working out to be a weekly meditation session at best."

    hide emptyroom
    show anuroomstandard
    with fade
    play sound "freesound_community-jumping-on-a-bed-84619.mp3"

    "You flop onto your matress in the sacred haven that is your bedroom, tap 'play' on your guided meditation audio and close your eyes."  
    "Hopefully, maybe this time you'll be able to reach 'Zen' state within the next half hour."

    #
    #
    label menu_options_a: #----ROUND1

    hide anuroomstandard
    show theradio
    with fade

    guide "'Hello and welcome, you have done something great today - you have taken time for yourself to check in.'"
    guide "'Now, let's begin...'" 
    guide "'Let your muscles relax, take a moment and...'" 

    guide "'Pick a thought you want to focus on...'" #round1 question
    
    a "Let's see, I want to think about..."

    hide theradio
    show theradiochoices
    
    menu:
        "My Worth?": #midanswer
            a "I’m not doing enough at home. Is Shai really getting what he needs from me?"
            show thetryagain
            "       " #this is so no text shows up on the image cards
            jump after_try_again_R1
    
            label after_try_again_R1:
                hide thetryagain
                jump menu_options_a
                #return
                        
        "My Duties?": #badanswer
            a "Work, study, parenting! I think I've bitten off more than I can chew..."
            show thebadending
            with fade
            "       " #this is so no text shows up on the image cards
            jump after_bad_ending_R1
    
            label after_bad_ending_R1:
                hide thebadending
                jump start
      
        "My Needs?": #goodanswer
            show anuroomstandardat30
            with fade
            a "What do I really need right now in this moment?"            
    #end of menu
        
    #
    #
  
    label menu_options_b: #----ROUND2

    hide anuroomstandardat30
    show theradio
    with fade

    guide "'Have you secured that thought? Great now let's dive deeper.'"
    guide "'Focus on reaching 'Zen',  DON'T  let your mind stray!'"
    guide "'Observe the state you're in at this moment...'" #round2 question

    a "Well, now all I can think about is..."

    hide theradio
    show theradiochoices

    menu:
        "My Body": #badanswer
            a "I can feel my rolls – my body’s not what it used to be." 
            show thebadending
            "       " #this is so no text shows up on the image cards
            jump after_bad_ending_R2
                
            label after_bad_ending_R2:
                hide thebadending
                jump start          
   
        "My Breathwork": #goodanswer
            hide theradiochoices
            show emptyroomat30 
            # option 1 static - no animation
            show anu_breathe_inout # option 2  dynamic animation
            queue sound ["vikukachannel-inhalar-exhalar-respira-breathe-171044.mp3", "vikukachannel-inhalar-exhalar-respira-breathe-171044.mp3"]
            a "Let me see if I can steady my breathing, in... out.. in.. out..."
            hide emptyroomat30
            show crashsound
            play sound "freeeverythingxx-rubble-crash-275691.mp3"


        "My Stress Level": #midanswer
            a "I’m too stressed right now to do this, maybe I should come back to this later..."
            show thetryagain
            with fade
            "       " #this is so no text shows up on the image cards
            jump after_try_again_R2
                
            label after_try_again_R2:
                hide thetryagain
                jump menu_options_b
                #return
    #end of menu

    #
    #

    #//////NARRATION
    
    "You hear Shai's wails and babbles as he's being told off..."
    "followed by the busy patter of Lumi's feet in the next room." 
    "You can feel your mind cycling backward pulling you out of your 'Zen' state."
    
    hide crashsound
    show anuroomstandardat30
    with fade

    "As if clinging on to the side of a swinging merry-go-round: you try to focus on the hushed tones of the guiding voice..." 
    
    label menu_options_c: #----ROUND3

    hide anuroomstandardat30
    show theradio
    with fade

    guide "'Now finish this sentence for our final elevation to Zen state.'"
    guide "'Today I am most grateful for...'" #round3 question

    a "Hmmm..."
    a "'Today I am most grateful for..."

    hide theradio
    show theradiochoices
   
    menu:
        "My Clarity": #goodanswer
            show anuroomstandardat60
            with fade
            a "Everything I have, Everything I am, Everything I will be."
            hide anuroomstandardat60
            jump goodending_blurb

        "I don't know": #badanswer
            a "Oh my days! Welp, that’s it – at least I tried." 
            show thebadending
            with fade
            "       " #this is so no text shows up on the image cards
            return
                                   
        "My Family": #midanswer           
            a "It sounds like things are hectic out there, maybe I should check what's going on with Shai and Lumi. It’ll only be two minutes... "
            show thetryagain
            with fade
            "       " #this is so no text shows up on the image cards
            return
    #end of menu

    #
    #

    #//////NARRATION
    label goodending_blurb:

    show journey_to_zen
    with fade

    "You feel a weight lifted as you exhale and a smile dances accross your face."
    "All your experiences and emotions have brought you to this moment, to this point in time."
    "For this you are grateful - it's exactly where you need to be..."
    "That's really all that matters."

    hide journey_to_zen
    show thegoodending
    with fade
    "       " #this is so no text shows up on the image cards
  

    # This ends the game.

    return

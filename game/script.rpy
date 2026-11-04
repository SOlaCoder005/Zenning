# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Anu", who_color="#F5DA27", what_color="#FFFFFF")
define guide = Character ("Guided Lady", who_color="#EBBFFF", what_color="#FFFFFF")


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
    show anulevel1

    # These display lines of dialogue.

    
    #//////NARRATION

    "It's 7pm and you've just gotten into your comfy home clothes..."
    "You know - the ones no human is supposed to see you in, apart from Lumi and baby Shai."
    "Lumi has 'clocked in' for childcare responsibilities to give you an opportunity to do your daily evening meditation..."
    "...even though it's working out to be a weekly mediation session at best."
    "You crawl up onto your large cushion in the sacred haven you call your 'creative space', tap 'play' on your guided meditation audio and close your eyes."  
    "Hopefully, maybe this time you'll be able to reach 'Zen' state within the next half hour."

    #
    #
    label menu_options_a: #----ROUND1

    hide anulevel1
    show theradio
    
    guide "'Hello and welcome, you have done something great today - you have taken time for yourself to check in."
    guide "'Now, let's begin...'" 
    guide "'Let your muscles relax, take a moment and...'" 

    guide "'Pick a thought you want to focus on...'" #round1 question

    hide theradio
    show theradiochoices
    
    menu:
        "Sufficiency?": #midanswer
            a "I’m not doing enough at home. Is Shai really getting what he needs from me?"
            show thetryagain
            "       " #this is so no text shows up on the image cards
            jump after_try_again_R1
    
            label after_try_again_R1:
                hide thetryagain
                jump menu_options_a
                #return
                        
        "Capability?": #badanswer
            a "Work, study, parenting! I think I've bitten off more than I can chew..."
            show thebadending
            "       " #this is so no text shows up on the image cards
            jump after_bad_ending_R1
    
            label after_bad_ending_R1:
                hide thebadending
                jump start
      
        "Needs?": #goodanswer
            show anulevel2
            a "What do I really need right now in this moment?"            
    #end of menu
        
    #
    #
  
    label menu_options_b: #----ROUND2

    hide anulevel2
    show theradio
    
    guide "'Have you secured that thought?' \n\n'Great now let's dive deeper."
    guide "Focus on your body, observe the state you're in at this moment...'" #round2 question

    hide theradio
    show theradiochoices

    menu:
        "Body": #badanswer
            a "I can feel my rolls – my body’s not what it used to be." 
            show thebadending
            "       " #this is so no text shows up on the image cards
            jump after_bad_ending_R2
                
            label after_bad_ending_R2:
                hide thebadending
                jump start          
      
        "Breathwork": #goodanswer
            hide theradiochoices
            show anulevel2
            #zoom in and out
            a "Let me see if I can steady my breathing, in... out.. in.. out..."
            hide anulevel2
            show crashsound

        "Stressed": #midanswer
            a "I’m too stressed right now to do this, maybe I should come back to this later..."
            show thetryagain
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
    
    "You hear Shai's wails and babbles as he's being told off and then the busy patter of Lumi's feet in the next room." 
    "You can feel your mind cycling backward pulling you out of your 'Zen' state."
    
    hide crashsound
    show theradio
    
    "As if clinging on to the side of a swinging merry-go-round: you try to focus on the hushed tones of the guiding voice..." 
    
    label menu_options_c: #----ROUND3

    guide "'Now finish this sentence for our final elevation to Zen state.'"
    guide "'Today I am most grateful for...'" #round3 question

    hide theradio
    show theradiochoices

    menu:
        "Clarity": #goodanswer
            show anulevel3
            a "Everything I have, Everything I am, Everything I will be."
            hide anulevel3
            jump goodending_blurb

        "I don't know": #badanswer
            a "Oh my days! Welp, that’s it – at least I tried." 
            show thebadending
            "       " #this is so no text shows up on the image cards
            return
                                   
        "Family": #midanswer           
            a "It sounds like things are hectic out there, maybe I should check what's going on with Shai and Lumi. It’ll only be two minutes... "
            show thetryagain
            "       " #this is so no text shows up on the image cards
            return
    #end of menu

    #
    #

    #//////NARRATION
    label goodending_blurb:

    show anuzenstate

    "You feel a weight lifted as you exhale and a smile dances accross your face."
    "All your experiences and emotions have brought you to this moment, to this point in time."
    "For this you are greatful - it's exactly where you need to be..."
    "That's really all that matters."

    hide anuzenstate
    show thegoodending

    "       " #this is so no text shows up on the image cards
  

    # This ends the game.

    return

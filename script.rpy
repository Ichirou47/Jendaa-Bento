#define all characters here
define y = "You"
define k = Character("Koyuki",color="#ec76f5")
define f = Character("Fuwari",color="#fcdc3d")
define n = Character("Natsumi",color="#5eeb86")
#define all transforms here
transform hidari:
    xalign 0.0
    yalign 1.0
transform migi:
    xalign 1.0
    yalign 1.0
#game start
label start:
    #test label for game

    scene school with fade
    pause

    "My first day of school"

    "Also the first day for many other freshmen like me"

    "I wonder what's in store for me here at New Gekkoukan High"

    "*walks toward the school bulletin board*"

    show fuwa smile open with dissolve
    pause
    f "yo"
    show fuwa smile open at hidari with move
    pause
    #koyuki smile with transform and transition
    k "hiya"
    #natsumi smile with transform and transition
    n "hello"

    f "We're 3 of the 4 main heroines in this Visual Novel"

    f "Pleased to meet you!"

    y "Uhh... Nice to meet you?.."

    show fuwa laugh at hidari

    f "The MC's quite a cutie don't you think so Koyu-chi?"

    k "Uhhm... Yeah... I guess..."

    f "What about you Natsumi?"

    n "Yeah... he does look rather cute"

    "What's up with these girls?!.."

    "Visual Novel?!.."

    "Oh god, I don't think my highschool life here will be normal.."

return

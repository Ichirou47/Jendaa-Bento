#define all characters here
define y = "You"
define k = Character("Koyuki",color="#ec76f5")
define f = Character("Fuwari",color="#fcdc3d")
define n = Character("Natsumi",color="#5eeb86")
define ku = Character("Kuga", color="954535")
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

    "I wonder what's in store for me here at Maple High"

    "*walks toward the school bulletin board*"

    show fuwa smile open with dissolve
    pause
    f "Yo"
    show fuwa smile open at hidari with move
    pause
    #koyuki smile with transform and transition
    k "Hiya"
    #natsumi smile with transform and transition
    n "Hello"

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

    scene school with wipedown

    show fuwa mad at hidari

    f "Hey,look out! You almost bumped into me!"

    y "Oh! Sorry about that, I didnt see you there."

    f "Yeah! You could've passed by me if I didn't say anything"

    "I stood there awkwardly, still surprised by how easily she strikes up a conversation,
    not to mention how pretty she is. Her eyes scanned up and down, seemingly annoyed by me,
    or just checking me out."

    scene school with fade

    show fuwa good at migi

    f "Good morning!"

    y "Good morning."

    f "So, you're heading to school too?"

    y "Yeah"

    y "(come on dude say something)"

    f "Well..."

    f "Please excuse me, I gotta hurry up cause my friend is waiting for me. "

    y "Oh yeah sure."

    f "See ya!"

return

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

    f "So, you're heading to class too?"

    y "Yeah"

    y "(come on dude say something)"

    f "Well..."

    f "Please excuse me, I gotta hurry up cause my friend is waiting for me. "

    y "Oh yeah sure."

    f "See ya!"

    "She trots ahead of me looking as if she doesnt want to be slowed down by anything.
    I lost sight of her when she took the next turn, and by then it felt like the tension in
    the air was snapped away..... Man, couldn't I have said something there? I thought all of
    those manga I've read would help me strike conversations but once you're in the spot.....
    You're in the spotlight!"

    y "Maybe i should join the speech club instead..... Nah, i'd rather be dead.
       But how come I've never bumped into her on my first day? I've been using the
       same route and nothing happened before. Maybe its just my luck....."

       
       return

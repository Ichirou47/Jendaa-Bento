#define all characters here----------
define y = "You"
define ko = Character("Koyuki",color="#ec76f5")
define f = Character("Fuwari",color="#fcdc3d")
define n = Character("Natsumi",color="#5eeb86")
define m = Character("Melissa")#<<<---Needs color---
define ku = Character("Kuga", color="#954535")
define u = DynamicCharacter("u")#Unknown character

#define all transforms here----------
transform hidari:
    xalign 0.0
    yalign 1.0
transform migi:
    xalign 1.0
    yalign 1.0

#game start----------
label start:
    #just do this if you wanna change the name/color for a character
    $u = Character("???",color="#fcdc3d")#Fuwari

    scene bg mcroom with fade
    pause

    "(Juuuust one more chapter). But lowkey, I know I am psychologically unconvinced of myself if I could even go that far."

    "Laying on my right on this travel futon in a dark and almost empty room, I finally shift my eyes to the clock on my phone
    and notice it's already 12:30 am."

    "Groaning in annoyance, I reluctantly lock the phone and try to sleep. (At least it didn’t end at a cliffhanger) I thought,
    because if it did, I would physically need to read more. But tomorrow is an important day of school as a first year."

    "The day I got to pick my after school club. Of course, I know what I’m going to choose already."

    "But now that I think about it, I still haven't unpack like half of my luggage. Maybe I’ll do it on the weekend.
    But now that I think about it again, I could use the weekend to read some more chapters."

    "I ponder at the mental list of mangas
    to read on my wish list, and decided that maybe I should do it tomorrow"

    scene bg neighborhood with fade

    "After a lonely breakfast in my uncle’s apartment, I made my way down the street toward my new school. This is the early season of spring,
    reminding me of the picnic memories with my family back in (insert village name) under the cherry blossoms."

    "But as that reminiscence creeps,
    I snap myself to reality."

    "I’m a big high schooler now! I gotta be independant. (Poor ol’ uncle (name) won’t always be there for me!).
    This was the only way I could continue studying, unfortunately."

    "I mean, I wouldn’t have minded staying back home in the rurals, but all the big shot certificates are here in the city! Well,
    not the “city” city, this is a suburb…"

    "Speaking of which, these house walls (or gates?) look like the spitting image
    straight out of some romcom."

    "I wonder who’s gonna pop up from the other side of this corner I’m approaching at a totally regular walking speed
    totally oblivious of the total chances I might bump into a total stranger…"

    "(Nobody was there)"

    "I chuckled softly, lesson number one in the city : ‘Don’t get your hopes up'"

    "Walking down this lonely road I thought about the friends I already made so far. It’s my third day here and I think
    I’m finally losing the nervousness of being a total stranger to this new place."

    "Still I can’t help but think about stuff like {b}that{/b}.
    Like, bumping into someone at a corner and we become friends like in the mang-"

    u "{i}Woah~ there!{/i}"

    "(Huh?). I suddenly shift my head over to the source of the voice."

    show fuwa mad with fade

    u "You almost bumped into me at the corner and became my friend like in those mangas~!"

    "I look over at the sudden appearance of a girl to my left. She stood as tall as me and almost a little too close."

    y "Oh! Sorry about that, I didnt see you there."

    show fuwa pout

    u "Yeah! You could've passed by me if I didn't say anything"

    "I am genuinely surprised at how easily she strikes a conversation with me."

    "That alone already puts her beyond my league,
    not to mention the strength of her looks with her blonde hair tied up to a messy sort of ponytail waving through the weak morning wind."

    "Still shocked at the matter, I stood there awkwardly, I’m seeing her eyes scanning up and down like she’s either annoyed at me,
    or is checking me out?"

    show fuwa smile open

    u "Anyways..."

    u "Good morning!"

    y "Uhh... Good morning."

    u "So, you're heading to class too?"

    y "Yeah"

    y "(come on dude say something)"

    u "Well..."

    show fuwa smile closed

    u "Please excuse me, I gotta hurry up cause my friend is waiting for me. "

    y "Oh yeah sure."

    show fuwa smile open

    u "See ya!"

    hide fuwa smile open

    "She trots ahead of me looking as if she doesnt want to be slowed down by anything.
    I lost sight of her when she took the next turn, and by then it felt like the tension in
    the air was snapped away....."

    "Man, couldn't I have said something there? I thought all of
    those manga I've read would help me strike conversations but once you're in the spot.....
    You're in the spotlight!"

    y "Maybe i should join the speech club instead..... Nah, i'd rather be dead.
    But how come I've never bumped into her on my first day? I've been using the
    same route and nothing happened before. Maybe its just my luck....."

    y "Wait a minute, she mentioned manga. That means she’s a reader too!
    I wonder if I’ll get to see her again since I’m going for the manga club."

    y "But if that is really going to happen, I better prepare my guts."

    "Regardless, I kept going until I finally got to class and the school day started."

    scene school with fade

    "It was already lunch time, and the second our maths teacher turned to face the door to
    begin his exit, the guy sitting in front of me turned his chair around to face my gaze..."

    ku "So you’re certain, you’re going for the manga club?"

    "He asked with an *unconvinced* tone in his voice.
    Despite being quite a speaker, he always manages to keep a cool face when he talks.
    Sometimes it’s hard for me to tell if he’s exaggerating things."

    y "100 percent certain"

    ku "Dangit dude, I mean, I like reading manga as much as the next person,
    but... I could read them at home you know... "

    "I was looking around the room seeing the other students walking about. Almost staring into nothingness.
    It was lucky of me to have a seat at the rear-left corner of the class."

    "It gave me a full view of the class.I recgonized some new faces entering the classroom too.
    it seems that some people already made friends with the other classes."

    "Seeing the sight
    gave me a pinch of nostalgic feeling from my old school back at home. Anyway, back to Kuga."

    y "Bro... Manga is my passion! My identity... My freaking purpose is to live!
    (I raised my voice a little higher, exaggerating my enthusiasm a bit.) i can't throw my chance
    of being with people who like the same thing i do."

    ku "Have you thought about the other clubs though? There's chess! It's popular nowadays"

    y "I'd rather do my homework then bust my brain on some board pieces in front of someone likely smarter
    than me and suffer the inevitable loss of my intellectual pride."

    $u = Character("???",color="#ec76f5")#Koyuki
    u "{i}Pfft!{/i}"

    "I heard a barely audible puffing sound from someone's voice. Glancing to my right at the source of it,
    the girl next to my table retracted her face away in an attempt to hide her mini laughing fit."

    "That's
    pretty cool though, i made a girl laugh... I think. Arghh, but i didnt catch her name last time. Why am I
    so bad at this? Anyway, i figured i should keep my voice down a little. And it seems, Kuga still has
    some more to say to me..."

    ku "Anyways, what about... the art club?"

    y "I can't draw."

    ku "They might teach you ?"

    y "I'll pass"

    ku "How about ping-pong?"

    y "They got ping-pong?"

    ku "I dunno. Do they?"

    y "..."

    ku "..."

    ku "How about one of the sports clubs…?"

    y "..."

    ku "..."

    "We both burst out laughing"

    ku "Anyway, next one... Music club?"

    y "I don’t even have an instrument"

    ku "You can buy one"

    y "No money."

    ku "They’ll probably lend you one…"

    y "N-"

    $u = Character("???",color="#5eeb86")
    u "Nope!"

    "We both suddenly heard a reply from elsewhere."

    u "You’ll have to bring your own instrument if you wanna join the music club."

    "This time, it was a different girl, she sat across the same table from my neighbour mini-laughing-fit-girl.
    It seems that they’re both having lunch together with their bentos already."

    ku "How do you know?"

    u "I asked the seniors!"

    ku "Oh. You plan on joining the music club?"

    u "Well yeah~, and I’m sorry but you can only join if you’ve got your own gear."

    y "Wait a minute. You’re not from this class"

    u "Uh… yeah. I’m from 1-C. I’m just eating with Koyuki here…"

    "(koyuki huh?.. but what's her Surname?..)"

    ku "Oh! You know Aoki-san"

    "God bless you for your existence Kuga"

    u "Yeah, we’ve been friends for a long time. I’m Aizawa, by the way. Nice to meet you"

    "(Aizawa Aizawa Aizawa Aizawa. Must remember. Aizawa Aizawa Aizawa Aizawa)"
    $u = Character("Aizawa",color="#5eeb86")

    ku "I’m Shinri, this is Tetsuya-san"

    y "Nice to meet you guys. And uh… Sorry Aoki-san, I guess this is the first time I’ve talked to you since the first day"

    "(I looked over to my table-neighbour waiting for a reply.
    But awkwardly enough, she points her head down shyly and I think I could make out her eyeballs looking over at Aizawa.
    Is she actually shy...?)"

    u "Owh don’t mind her, she’s shy like that. Which is why I come here to keep her company (Aizawa retorts Aoki’s eyeballing with an annoyed glare in return)."

return

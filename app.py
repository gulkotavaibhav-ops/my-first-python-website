from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():

    return """

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>For Varleen ✨</title>

<style>

/* =========================================================

   RESET

========================================================= */

* {

    margin: 0;

    padding: 0;

    box-sizing: border-box;

}

html {

    scroll-behavior: smooth;

}

body {

    background: #05050b;

    color: #fff;

    font-family: Georgia, "Times New Roman", serif;

    overflow-x: hidden;

}

/* =========================================================

   BACKGROUND

========================================================= */

body::before {

    content: "";

    position: fixed;

    inset: 0;

    background:

        radial-gradient(circle at 20% 20%, rgba(142, 92, 255, .14), transparent 30%),

        radial-gradient(circle at 80% 30%, rgba(255, 92, 177, .10), transparent 30%),

        radial-gradient(circle at 50% 90%, rgba(71, 128, 255, .10), transparent 35%);

    pointer-events: none;

    z-index: -3;

}

.aurora {

    position: fixed;

    width: 700px;

    height: 700px;

    border-radius: 50%;

    filter: blur(120px);

    opacity: .18;

    background: linear-gradient(135deg, #8b5cf6, #ec4899);

    top: -300px;

    left: -200px;

    animation: auroraMove 15s infinite alternate ease-in-out;

    z-index: -2;

}

@keyframes auroraMove {

    0% {

        transform: translate(0, 0) scale(1);

    }

    100% {

        transform: translate(80vw, 50vh) scale(1.4);

    }

}

/* =========================================================

   STARS

========================================================= */

#stars {

    position: fixed;

    inset: 0;

    pointer-events: none;

    z-index: -1;

}

.star {

    position: absolute;

    width: 2px;

    height: 2px;

    background: white;

    border-radius: 50%;

    animation: twinkle infinite alternate;

}

@keyframes twinkle {

    from {

        opacity: .15;

        transform: scale(.5);

    }

    to {

        opacity: 1;

        transform: scale(1.5);

    }

}

/* =========================================================

   MOUSE GLOW

========================================================= */

.cursor-glow {

    position: fixed;

    width: 350px;

    height: 350px;

    border-radius: 50%;

    background: radial-gradient(

        circle,

        rgba(174, 135, 255, .12),

        transparent 65%

    );

    transform: translate(-50%, -50%);

    pointer-events: none;

    z-index: 0;

}

/* =========================================================

   INTRO

========================================================= */

.intro {

    position: fixed;

    inset: 0;

    background: #05050b;

    display: flex;

    justify-content: center;

    align-items: center;

    text-align: center;

    z-index: 99999;

    transition: opacity 1.2s ease, visibility 1.2s ease;

}

.intro.hide {

    opacity: 0;

    visibility: hidden;

}

.intro-content {

    padding: 30px;

}

.intro-small {

    color: #a78bfa;

    letter-spacing: 6px;

    text-transform: uppercase;

    font-size: 12px;

    margin-bottom: 25px;

}

.intro h1 {

    font-size: clamp(45px, 9vw, 100px);

    font-weight: normal;

    background: linear-gradient(

        90deg,

        #fff,

        #c4b5fd,

        #f9a8d4,

        #fff

    );

    background-size: 300%;

    -webkit-background-clip: text;

    color: transparent;

    animation: gradientMove 6s linear infinite;

}

@keyframes gradientMove {

    0% {

        background-position: 0%;

    }

    100% {

        background-position: 300%;

    }

}

.intro p {

    margin-top: 20px;

    color: #aaa;

    font-family: Arial, sans-serif;

}

.enter-btn {

    margin-top: 35px;

    border: 1px solid rgba(255,255,255,.25);

    background: rgba(255,255,255,.05);

    color: white;

    padding: 15px 32px;

    border-radius: 50px;

    cursor: pointer;

    font-size: 14px;

    transition: transform .35s ease, background .3s ease, border-color .3s ease, box-shadow .3s ease;

    position: relative;

    z-index: 10;

    backdrop-filter: blur(15px);

}

.enter-btn:hover {

    transform: translateY(-4px);

    background: rgba(167,139,250,.2);

    border-color: #a78bfa;

    box-shadow: 0 15px 50px rgba(139,92,246,.3);

}


/* =========================================================
   CINEMA EFFECTS
========================================================= */
.intro::before,.intro::after{content:"";position:absolute;left:0;right:0;height:10vh;background:#000;z-index:1;pointer-events:none}.intro::before{top:0}.intro::after{bottom:0}.intro-content{position:relative;z-index:2}.cinema-kicker{color:rgba(255,255,255,.55);font-family:Arial,sans-serif;font-size:10px;letter-spacing:5px;text-transform:uppercase;margin-bottom:18px}.cinema-line{width:90px;height:1px;margin:22px auto;background:linear-gradient(90deg,transparent,rgba(255,255,255,.8),transparent)}.challenge-note{margin-top:18px;color:rgba(255,255,255,.52);font-family:Arial,sans-serif;font-size:12px;min-height:18px}.cinema-grain{position:fixed;inset:-50%;width:200%;height:200%;pointer-events:none;z-index:99998;opacity:.035;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.8'/%3E%3C/svg%3E");animation:grainMove .18s steps(2) infinite}@keyframes grainMove{0%{transform:translate(0,0)}25%{transform:translate(2%,-1%)}50%{transform:translate(-1%,2%)}75%{transform:translate(1%,1%)}100%{transform:translate(-2%,-1%)}}#petals{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:9990}.petal{position:absolute;top:-12vh;width:12px;height:18px;border-radius:80% 20% 80% 20%;background:linear-gradient(135deg,#fff,#f9a8d4 55%,#ec4899);box-shadow:0 2px 10px rgba(236,72,153,.35);opacity:0;animation:petalFall linear forwards}@keyframes petalFall{0%{opacity:0;transform:translate3d(0,-10vh,0) rotate(0deg) scale(.7)}10%{opacity:.95}100%{opacity:0;transform:translate3d(var(--drift),115vh,0) rotate(var(--spin)) scale(1)}}.cinematic-reveal{animation:cinemaReveal 1.7s cubic-bezier(.2,.8,.2,1) both}@keyframes cinemaReveal{from{opacity:0;transform:scale(1.08) translateY(25px);filter:blur(10px)}to{opacity:1;transform:scale(1) translateY(0);filter:blur(0)}}


/* =========================================================
   CINEMATIC PHOTO REVEAL
========================================================= */

#cinematic-reveal {
    position: fixed;
    inset: 0;
    z-index: 99997;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
        radial-gradient(circle at 50% 42%, rgba(139,92,246,.18), transparent 35%),
        rgba(3,3,8,.97);
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: opacity 1.4s ease, visibility 1.4s ease;
    overflow: hidden;
}

#cinematic-reveal.show {
    opacity: 1;
    visibility: visible;
}

.cinematic-vignette {
    position: absolute;
    inset: 0;
    background: radial-gradient(circle, transparent 30%, rgba(0,0,0,.72) 100%);
    pointer-events: none;
}

.cinematic-photo {
    position: relative;
    z-index: 3;
    width: min(370px, 70vw);
    max-height: 76vh;
    object-fit: contain;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.28);
    box-shadow:
        0 35px 100px rgba(0,0,0,.65),
        0 0 80px rgba(236,72,153,.18);
    opacity: 0;
    transform: scale(1.16) translateY(28px);
    filter: blur(14px) brightness(.7);
}

#cinematic-reveal.show .cinematic-photo {
    animation: cinematicPhotoIn 2.2s cubic-bezier(.16,.84,.24,1) .15s forwards;
}

@keyframes cinematicPhotoIn {
    0% {
        opacity: 0;
        transform: scale(1.16) translateY(28px);
        filter: blur(14px) brightness(.7);
    }
    45% {
        opacity: 1;
        filter: blur(3px) brightness(.9);
    }
    100% {
        opacity: 1;
        transform: scale(1) translateY(0);
        filter: blur(0) brightness(1);
    }
}

.cinematic-caption {
    position: absolute;
    z-index: 4;
    bottom: 8%;
    color: rgba(255,255,255,.8);
    font-family: Georgia, serif;
    font-size: 13px;
    letter-spacing: 6px;
    text-transform: uppercase;
    opacity: 0;
    transform: translateY(15px);
}

#cinematic-reveal.show .cinematic-caption {
    animation: captionIn 1.2s ease 1.15s forwards;
}

@keyframes captionIn {
    to { opacity: 1; transform: translateY(0); }
}

.flower {
    position: absolute;
    top: -12vh;
    z-index: 8;
    pointer-events: none;
    user-select: none;
    opacity: 0;
    animation: flowerFall linear forwards;
    will-change: transform, opacity;
    text-shadow: 0 4px 15px rgba(0,0,0,.3);
}

@keyframes flowerFall {
    0% {
        opacity: 0;
        transform: translate3d(0,-12vh,0) rotate(0deg) scale(.45);
    }
    8% { opacity: .95; }
    55% { opacity: 1; }
    100% {
        opacity: 0;
        transform:
            translate3d(var(--drift),115vh,0)
            rotate(var(--spin))
            scale(1.08);
    }
}

.photo-frame.revealed {
    opacity: 1 !important;
    visibility: visible !important;
}
.hero-photo-hidden {
    opacity: 0;
    visibility: hidden;
}

.hero-photo-hidden.revealed {
    opacity: 1;
    visibility: visible;
    animation: cinemaReveal 1.4s ease both;
}

.hero-content.cinematic-content {
    opacity: 0;
    transform: translateY(20px);
}

.hero-content.cinematic-content.revealed {
    animation: contentRise 1.4s ease .2s forwards;
}

@keyframes contentRise {
    to { opacity: 1; transform: translateY(0); }
}

/* More cinematic surprise */

#cinematic-reveal.persistent-flowers {
    opacity: 1;
    visibility: visible;
    pointer-events: none;
    background: transparent;
    transition: opacity 1.5s ease;
}

#cinematic-reveal.persistent-flowers .cinematic-vignette,
#cinematic-reveal.persistent-flowers .cinematic-photo,
#cinematic-reveal.persistent-flowers .cinematic-caption {
    transition: opacity 1.5s ease;
}

#cinematic-reveal.persistent-flowers.flowers-only {
    background: transparent;
}

#cinematic-reveal.persistent-flowers.flowers-only .cinematic-vignette,
#cinematic-reveal.persistent-flowers.flowers-only .cinematic-photo,
#cinematic-reveal.persistent-flowers.flowers-only .cinematic-caption {
    opacity: 0 !important;
    animation: none !important;
    visibility: hidden;
}

.surprise-burst {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9996;
}

/* =========================================================

   NAVIGATION

========================================================= */

nav {

    position: fixed;

    top: 20px;

    left: 50%;

    transform: translateX(-50%);

    z-index: 1000;

    padding: 12px 22px;

    background: rgba(10,10,20,.55);

    border: 1px solid rgba(255,255,255,.1);

    border-radius: 50px;

    backdrop-filter: blur(20px);

    display: flex;

    gap: 25px;

}

nav a {

    color: #aaa;

    text-decoration: none;

    font-family: Arial, sans-serif;

    font-size: 12px;

    transition: .3s;

}

nav a:hover {

    color: white;

}

/* =========================================================

   HERO

========================================================= */

.hero {

    min-height: 100vh;

    display: flex;

    justify-content: center;

    align-items: center;

    text-align: center;

    padding: 100px 25px;

    position: relative;

}

.hero-content {

    max-width: 950px;

}

.overline {

    color: #a78bfa;

    letter-spacing: 7px;

    text-transform: uppercase;

    font-size: 12px;

    margin-bottom: 30px;

}

.hero h1 {

    font-size: clamp(70px, 14vw, 170px);

    line-height: .9;

    font-weight: normal;

    background: linear-gradient(

        120deg,

        #fff,

        #c4b5fd,

        #f9a8d4,

        #fff

    );

    background-size: 300%;

    -webkit-background-clip: text;

    color: transparent;

    animation: gradientMove 8s linear infinite;

    text-shadow: 0 0 80px rgba(167,139,250,.15);

}

.hero-description {

    margin: 35px auto;

    max-width: 600px;

    color: #aaa6b7;

    font-size: 19px;

    line-height: 1.9;

}

.scroll {

    margin-top: 70px;

    color: #777;

    font-family: Arial, sans-serif;

    font-size: 11px;

    letter-spacing: 3px;

    text-transform: uppercase;

}

.scroll span {

    display: block;

    margin-top: 12px;

    font-size: 20px;

    animation: bounce 2s infinite;

}

@keyframes bounce {

    50% {

        transform: translateY(8px);

    }

}

/* =========================================================

   SECTIONS

========================================================= */

section {

    min-height: 80vh;

    max-width: 1100px;

    margin: auto;

    padding: 120px 25px;

    position: relative;

}

.section-label {

    color: #a78bfa;

    text-transform: uppercase;

    letter-spacing: 5px;

    font-size: 11px;

    font-family: Arial, sans-serif;

    margin-bottom: 20px;

}

.section-title {

    font-size: clamp(38px, 6vw, 70px);

    font-weight: normal;

    margin-bottom: 25px;

}

.section-description {

    color: #9692a2;

    font-size: 18px;

    line-height: 1.8;

    max-width: 650px;

}

/* =========================================================

   CARDS

========================================================= */

.cards {

    margin-top: 60px;

    display: grid;

    grid-template-columns: repeat(3, 1fr);

    gap: 20px;

}

.card {

    padding: 40px 30px;

    min-height: 280px;

    border-radius: 25px;

    background: linear-gradient(

        145deg,

        rgba(255,255,255,.07),

        rgba(255,255,255,.025)

    );

    border: 1px solid rgba(255,255,255,.09);

    backdrop-filter: blur(15px);

    transition: .5s;

    position: relative;

    overflow: hidden;

}

.card::before {

    content: "";

    position: absolute;

    width: 200px;

    height: 200px;

    background: #8b5cf6;

    filter: blur(100px);

    opacity: 0;

    transition: .5s;

}

.card:hover {

    transform: translateY(-12px);

    border-color: rgba(167,139,250,.5);

}

.card:hover::before {

    opacity: .15;

}

.card-icon {

    font-size: 35px;

    margin-bottom: 30px;

}

.card h3 {

    font-size: 24px;

    font-weight: normal;

    margin-bottom: 15px;

}

.card p {

    color: #92909d;

    line-height: 1.8;

}

/* =========================================================

   LETTER

========================================================= */

.letter-wrapper {

    margin-top: 60px;

    perspective: 1000px;

}

.letter {

    padding: 60px;

    border-radius: 30px;

    background:

        linear-gradient(

            135deg,

            rgba(167,139,250,.10),

            rgba(249,168,212,.05)

        );

    border: 1px solid rgba(255,255,255,.1);

    box-shadow:

        0 30px 100px rgba(0,0,0,.3),

        inset 0 0 50px rgba(255,255,255,.02);

    font-size: 20px;

    line-height: 2;

    color: #cbc7d5;

    transition: transform .5s;

}

.letter:hover {

    transform: rotateX(2deg) rotateY(-2deg);

}

.signature {

    margin-top: 35px;

    color: #fff;

    font-style: italic;

    font-size: 25px;

}

/* =========================================================

   TIMELINE

========================================================= */

.timeline {

    margin-top: 70px;

    border-left: 1px solid rgba(167,139,250,.4);

    padding-left: 35px;

}

.timeline-item {

    margin-bottom: 55px;

    position: relative;

}

.timeline-item::before {

    content: "";

    position: absolute;

    width: 10px;

    height: 10px;

    background: #a78bfa;

    border-radius: 50%;

    left: -41px;

    top: 7px;

    box-shadow: 0 0 20px #a78bfa;

}

.timeline-item h3 {

    font-size: 25px;

    font-weight: normal;

    margin-bottom: 10px;

}

.timeline-item p {

    color: #92909d;

    line-height: 1.8;

}

/* =========================================================

   SURPRISE

========================================================= */

.surprise {

    text-align: center;

    min-height: 100vh;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

}

.surprise .section-title {

    max-width: 800px;

}

.reveal-btn {

    margin-top: 40px;

    padding: 18px 38px;

    border-radius: 50px;

    border: 1px solid rgba(255,255,255,.2);

    background: linear-gradient(

        135deg,

        rgba(139,92,246,.25),

        rgba(236,72,153,.15)

    );

    color: white;

    cursor: pointer;

    font-family: Georgia, serif;

    font-size: 16px;

    transition: .4s;

}

.reveal-btn:hover {

    transform: scale(1.06);

    box-shadow: 0 20px 60px rgba(139,92,246,.25);

}

.secret {

    max-width: 700px;

    margin-top: 50px;

    font-size: 28px;

    line-height: 1.7;

    color: #e4d9ff;

    opacity: 0;

    transform: translateY(20px);

    transition: 1s;

    pointer-events: none;

}

.secret.show {

    opacity: 1;

    transform: translateY(0);

    pointer-events: auto;

}

/* =========================================================

   HEARTS

========================================================= */

.heart {

    position: fixed;

    pointer-events: none;

    color: #f9a8d4;

    font-size: 20px;

    z-index: 9999;

    animation: heartFloat 4s ease-out forwards;

}

@keyframes heartFloat {

    0% {

        transform: translateY(0) scale(.5);

        opacity: 1;

    }

    100% {

        transform:

            translateY(-100vh)

            rotate(360deg)

            scale(1.4);

        opacity: 0;

    }

}

/* =========================================================

   FOOTER

========================================================= */

footer {

    text-align: center;

    padding: 80px 25px;

    color: #555260;

    font-family: Arial, sans-serif;

    font-size: 12px;

    letter-spacing: 1px;

}

/* =========================================================

   MOBILE

========================================================= */

@media (max-width: 750px) {

    nav {

        display: none;

    }

    .cards {

        grid-template-columns: 1fr;

    }

    section {

        padding: 90px 20px;

    }

    .letter {

        padding: 30px;

        font-size: 17px;

    }

    .hero-description {

        font-size: 17px;

    }

}

</style>

</head>

<body>

<div class="cinema-grain"></div>
<div id="petals"></div>

<audio id="music-player" preload="auto" loop>
    <source src="/static/othaiyadi-pathayila.mp3" type="audio/mpeg">
</audio>

<div id="cinematic-reveal" aria-hidden="true">
    <div class="cinematic-vignette"></div>
    <img class="cinematic-photo" src="/static/varleen.png" alt="A cinematic photo">
    <div class="cinematic-caption">A little something for you</div>
</div>


<div class="aurora"></div>

<div id="stars"></div>

<div class="cursor-glow"></div>

<!-- =====================================================

     INTRO

===================================================== -->

<div class="intro" id="intro">

    <div class="intro-content">

        <div class="cinema-kicker">A tiny cinematic experience</div>

        <div class="intro-small">

            A little something

        </div>

        <h1>For Varleen</h1>

        <p>

            This isn't just another website.

        </p>

        <div class="cinema-line"></div>

        <button class="enter-btn" id="enter-btn" onclick="enterSite()">

            Open ✨

        </button>

        <div class="challenge-note" id="challenge-note">
            You might have to work a little for this one 😌
        </div>

    </div>

</div>

<!-- =====================================================

     NAV

===================================================== -->

<nav>

    <a href="#beginning">Beginning</a>

    <a href="#why">Why You</a>

    <a href="#letter">Letter</a>

    <a href="#surprise">Surprise</a>

</nav>

<!-- =====================================================

     HERO

===================================================== -->

<div class="hero" id="beginning">

    <div class="hero-content cinematic-content" id="hero-content">

        <div class="overline">

            One name. One little universe.

        </div>

        <h1>Varleen</h1>

        <p class="hero-description">

            I could have sent you a message.

            <br>

            Instead, I learned how to build a website.

            <br><br>

            Maybe that's slightly excessive.

            <br>

            But some people are worth the extra effort.

        </p>

        <div class="photo-frame hero-photo-hidden" id="photo-frame">
            <img src="/static/varleen.png" alt="A photo">
        </div>

        <div class="scroll">

            Keep scrolling

            <span>↓</span>

        </div>

    </div>

</div>

<!-- =====================================================

     WHY YOU

===================================================== -->

<section id="why">

    <div class="section-label">

        Chapter 01

    </div>

    <h2 class="section-title">

        Why you?

    </h2>

    <p class="section-description">

        There are things about someone that are difficult

        to put into a sentence.

        Sometimes it's not one particular thing.

        It's simply the way conversations can make an

        ordinary day feel a little different.

    </p>

    <div class="cards">

        <div class="card">

            <div class="card-icon">

                ✨

            </div>

            <h3>

                Your energy

            </h3>

            <p>

                There's something about you that makes

                conversations feel different from the

                usual ones.

            </p>

        </div>

        <div class="card">

            <div class="card-icon">

                🌙

            </div>

            <h3>

                Your presence

            </h3>

            <p>

                Some conversations disappear from your

                mind almost immediately.

                Somehow, ours tend to stick around.

            </p>

        </div>

        <div class="card">

            <div class="card-icon">

                🫶

            </div>

            <h3>

                Just you

            </h3>

            <p>

                And honestly, maybe everything doesn't

                need a complicated explanation.

            </p>

        </div>

    </div>

</section>

<!-- =====================================================

     TIMELINE

===================================================== -->

<section>

    <div class="section-label">

        Chapter 02

    </div>

    <h2 class="section-title">

        The little things.

    </h2>

    <p class="section-description">

        The best stories aren't always made from huge

        moments.

        Sometimes they're made from tiny conversations,

        random thoughts and unexpected connections.

    </p>

    <div class="timeline">

        <div class="timeline-item">

            <h3>

                The beginning

            </h3>

            <p>

                Somewhere in a CA freshers group,

                two people who didn't really know each

                other started talking.

            </p>

        </div>

        <div class="timeline-item">

            <h3>

                The conversations

            </h3>

            <p>

                Random thoughts, funny conversations,

                little jokes and those moments that

                somehow stay in your mind.

            </p>

        </div>

        <div class="timeline-item">

            <h3>

                And then this website

            </h3>

            <p>

                Because apparently I decided learning

                Python was a reasonable way of saying

                "hey, you're pretty interesting."

            </p>

        </div>

    </div>

</section>

<!-- =====================================================

     LETTER

===================================================== -->

<section id="letter">

    <div class="section-label">

        Chapter 03

    </div>

    <h2 class="section-title">

        A letter, of sorts.

    </h2>

    <div class="letter-wrapper">

        <div class="letter">

            Dear Varleen,

            <br><br>

            I wanted to make you something.

            Not something I could simply copy and paste.

            Something that took time.

            <br><br>

            So I started learning how to build websites,

            opened VS Code, fought with terminals,

            installed Python packages,

            and somehow ended up here.

            <br><br>

            I don't know if a website can properly explain

            why someone stands out.

            Probably not.

            <br><br>

            But maybe the effort behind it can.

            <br><br>

            So here it is.

            A tiny corner of the internet that exists

            simply because <strong>you</strong> inspired me

            to make it.

            <br><br>

            I hope it makes you smile.

            <div class="signature">

                — Vaibhav

            </div>

        </div>

    </div>

</section>

<!-- =====================================================

     SURPRISE

===================================================== -->

<section class="surprise" id="surprise">

    <div class="section-label">

        Final chapter

    </div>

    <h2 class="section-title">

        I saved one last thing for you.

    </h2>

    <p class="section-description"

       style="text-align:center;">

        You made it this far.

        <br>

        So I think you deserve to see it.

    </p>

    <button

        class="reveal-btn"

        id="surprise-btn"

        onclick="reveal()">

        Open the surprise ✨

    </button>

    <div class="secret" id="secret">

        If this website made you smile even for a second,

        <br><br>

        then all those lines of code were worth it.

        <br><br>

        And if you ever wonder why I made all this...

        <br><br>

        <strong>

            Sometimes someone can simply be interesting

            enough to inspire something unexpected.

        </strong>

        ✨

    </div>

</section>

<footer>

    Made with Python, curiosity,

    too many lines of code,

    and a little bit of heart.

    <br><br>

    For Varleen · 2026

</footer>

<script>

/* =====================================================

   CREATE STARS

===================================================== */

const stars = document.getElementById("stars");

for (let i = 0; i < 140; i++) {

    const star = document.createElement("div");

    star.className = "star";

    star.style.left =

        Math.random() * 100 + "%";

    star.style.top =

        Math.random() * 100 + "%";

    star.style.animationDuration =

        (1.5 + Math.random() * 4) + "s";

    star.style.animationDelay =

        Math.random() * 4 + "s";

    star.style.opacity =

        Math.random();

    stars.appendChild(star);

}

/* =====================================================

   INTRO

===================================================== */

let dodgeCount = 0;
let unlocked = false;
let lastDodge = 0;
const intro = document.getElementById("intro");
const button = document.getElementById("enter-btn");
const note = document.getElementById("challenge-note");

function moveButton(){
    if(unlocked)return;
    const now=Date.now();
    if(now-lastDodge<650)return;
    lastDodge=now;
    if(dodgeCount>=4){note.textContent="Okay... you caught me. ✨";button.style.transform="translate(0,0)";return;}
    dodgeCount++;
    const x=(Math.random()*240)-120;
    const y=(Math.random()*150)-75;
    const r=(Math.random()*10)-5;
    button.style.transform=`translate(${x}px,${y}px) rotate(${r}deg)`;
    const messages=["A little too close 😌","You almost had it 😂","Not that easy... 👀","Okay okay... one more try ✨"];
    note.textContent=messages[dodgeCount-1];
}

function checkButtonProximity(e){
    if(unlocked || !button || intro.style.display === "none") return;
    const rect=button.getBoundingClientRect();
    const cx=rect.left + rect.width/2;
    const cy=rect.top + rect.height/2;
    const distance=Math.hypot(e.clientX-cx, e.clientY-cy);

    // Make the button dodge before the cursor actually reaches it.
    if(distance < 170){
        moveButton();
    }
}

// Listen on the document so the dodge still works after the button moves.
document.addEventListener("pointermove", checkButtonProximity, {passive:true});


function createFlowers(containerId = "cinematic-reveal", count = 125) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const flowers = ["🌸", "🌺", "🌷", "🌼", "💮", "✿", "❀"];
    const colors = ["#ffffff", "#ffd1e6", "#f9a8d4", "#e9d5ff", "#fde68a", "#fecdd3"];

    for (let i = 0; i < count; i++) {
        const flower = document.createElement("span");
        flower.className = "flower";
        flower.textContent = flowers[Math.floor(Math.random() * flowers.length)];

        const size = 14 + Math.random() * 25;
        flower.style.left = (Math.random() * 108 - 4) + "vw";
        flower.style.fontSize = size + "px";
        flower.style.color = colors[Math.floor(Math.random() * colors.length)];
        flower.style.setProperty("--drift", ((Math.random() * 420) - 210) + "px");
        flower.style.setProperty("--spin", ((Math.random() * 1200) - 600) + "deg");
        flower.style.animationDuration = (5 + Math.random() * 6) + "s";
        flower.style.animationDelay = (Math.random() * 2.8) + "s";

        container.appendChild(flower);
    }
}


function startFlowerRain(containerId = "cinematic-reveal") {
    const container = document.getElementById(containerId);
    if (!container || window.flowerRainTimer) return;

    // Keep a steady stream of different flowers falling over the photo.
    const symbols = ["🌸", "🌺", "🌷", "🌼", "💮", "✿", "❀", "✾"];
    const colors = ["#ffffff", "#ffd1e6", "#f9a8d4", "#e9d5ff", "#fde68a", "#fecdd3"];

    function spawnFlower() {
        if (!document.getElementById(containerId)) return;

        const flower = document.createElement("span");
        flower.className = "flower";
        flower.textContent = symbols[Math.floor(Math.random() * symbols.length)];

        flower.style.left = (Math.random() * 104 - 2) + "vw";
        flower.style.fontSize = (13 + Math.random() * 25) + "px";
        flower.style.color = colors[Math.floor(Math.random() * colors.length)];
        flower.style.setProperty("--drift", ((Math.random() * 360) - 180) + "px");
        flower.style.setProperty("--spin", ((Math.random() * 1200) - 600) + "deg");
        flower.style.animationDuration = (5 + Math.random() * 6) + "s";

        container.appendChild(flower);

        // Prevent the DOM from growing forever.
        setTimeout(() => flower.remove(), 12000);
    }

    // Start with a full, already-flowing scene.
    for (let i = 0; i < 45; i++) {
        setTimeout(spawnFlower, i * 85);
    }

    window.flowerRainTimer = setInterval(spawnFlower, 180);
}

function stopFlowerRain() {
    if (window.flowerRainTimer) {
        clearInterval(window.flowerRainTimer);
        window.flowerRainTimer = null;
    }
}

function createPetalBurst() {
    const container = document.getElementById("cinematic-reveal");
    if (!container) return;

    const petals = ["🌸", "🌺", "🌷", "🌼", "💮", "✿", "❀", "✾"];
    for (let i = 0; i < 45; i++) {
        const petal = document.createElement("span");
        petal.className = "flower";
        petal.textContent = petals[Math.floor(Math.random() * petals.length)];
        petal.style.left = "50%";
        petal.style.top = "42%";
        petal.style.fontSize = (10 + Math.random() * 20) + "px";
        petal.style.setProperty("--drift", ((Math.random() * 700) - 350) + "px");
        petal.style.setProperty("--spin", ((Math.random() * 1600) - 800) + "deg");
        petal.style.animationDuration = (3.5 + Math.random() * 3) + "s";
        petal.style.animationDelay = (Math.random() * .5) + "s";
        container.appendChild(petal);
    }
}

function enterSite(){
    if(unlocked)return;

    unlocked=true;
    note.textContent="Okay... you caught me. ✨";
    button.style.transform="translate(0,0)";
    button.textContent="Enjoy the movie 🎬";

    const player=document.getElementById("music-player");
    player.currentTime=0;
    player.volume=1.0;

    const playPromise=player.play();
    if(playPromise!==undefined){
        playPromise.catch(function(){
            note.textContent="Press play if the music doesn't start 🎵";
            player.controls=true;
            player.style.position="fixed";
            player.style.left="50%";
            player.style.bottom="20px";
            player.style.transform="translateX(-50%)";
            player.style.zIndex="2000";
        });
    }

    intro.classList.add("hide");

    // The photo is the FIRST thing she sees after opening.
    setTimeout(function(){
        const reveal = document.getElementById("cinematic-reveal");
        const photo = document.getElementById("photo-frame");
        const content = document.getElementById("hero-content");

        reveal.classList.add("show");
        reveal.setAttribute("aria-hidden", "false");

        // Lots of different flowers begin falling over the cinematic photo.
        startFlowerRain("cinematic-reveal");
        setTimeout(createPetalBurst, 850);

        // After the photo has had its cinematic moment, transition into the site.
        setTimeout(function(){
            reveal.classList.add("persistent-flowers");
            reveal.setAttribute("aria-hidden", "false");

            // Keep the photo reveal visible for a cinematic moment, then
            // transition the photo itself into the main page while the
            // flower rain continues over it.
            photo.classList.remove("hero-photo-hidden");
            photo.classList.add("revealed");
            content.classList.add("revealed");

            setTimeout(function(){
                reveal.classList.add("flowers-only");
            }, 1200);
        }, 5600);
    }, 650);
}

/* =====================================================
   SURPRISE REVEAL
===================================================== */

function reveal() {
    const secret = document.getElementById("secret");
    const btn = document.getElementById("surprise-btn");

    if (!secret) return;

    secret.classList.add("show");

    if (btn) {
        btn.textContent = "✨ Surprise unlocked";
        btn.disabled = true;
        btn.style.opacity = ".7";
        btn.style.cursor = "default";
    }

    // A short flower shower when the final surprise is opened.
    const burst = document.createElement("div");
    burst.className = "surprise-burst";
    document.body.appendChild(burst);

    const symbols = ["🌸", "🌺", "🌷", "🌼", "💮", "✿", "❀"];
    for (let i = 0; i < 55; i++) {
        const flower = document.createElement("span");
        flower.className = "flower";
        flower.textContent = symbols[Math.floor(Math.random() * symbols.length)];
        flower.style.left = (Math.random() * 100) + "vw";
        flower.style.fontSize = (14 + Math.random() * 22) + "px";
        flower.style.setProperty("--drift", ((Math.random() * 260) - 130) + "px");
        flower.style.setProperty("--spin", ((Math.random() * 900) - 450) + "deg");
        flower.style.animationDuration = (3.5 + Math.random() * 3) + "s";
        burst.appendChild(flower);
    }

    setTimeout(() => burst.remove(), 7000);
}

/* =====================================================

   CARD TILT

===================================================== */

document.querySelectorAll(".card").forEach(card => {

    card.addEventListener("mousemove", e => {

        const rect =

            card.getBoundingClientRect();

        const x =

            e.clientX - rect.left;

        const y =

            e.clientY - rect.top;

        const rotateX =

            ((y / rect.height) - .5) * -8;

        const rotateY =

            ((x / rect.width) - .5) * 8;

        card.style.transform =

            `perspective(700px)

             rotateX(${rotateX}deg)

             rotateY(${rotateY}deg)

             translateY(-8px)`;

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform = "";

    });

});

</script>

</body>

</html>

"""

if __name__ == "__main__":

    app.run(debug=True)
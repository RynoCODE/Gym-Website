var crsr = document.querySelector("#cursor")
var crsrblr = document.querySelector("#cursorBlur")

document.addEventListener("mousemove", function(dets){
    crsr.style.left = dets.x+"px"
    crsr.style.top = dets.y + "px"
    crsrblr.style.left = dets.x+"px"
    crsrblr.style.top = dets.y + "px"
    
})

// var h2 = document.querySelectorAll("#nav h2")
// h2.forEach(function(ele){
//     ele.addEventListener("mouseenter", function(){
//         crsr.style.scale = 3
//         crsr.style.border = "0.5px solid #fff"
//         crsr.style.backgroundColor = "transparent"
//     })
//     ele.addEventListener("mouseleave", function(){
//         crsr.style.scale = 1
//         crsr.style.border = "0px solid slateblue"
//         crsr.style.backgroundColor = "slateblue"
//     })
// })


gsap.to("#nav",{
    backgroundColor: "#000",
    duration: 0.5,
    height: "5rem",
    scrollTrigger:{
        trigger:"#nav",
        scroller:"body",
        start:"top -15%",
        end:"top -20%",
        scrub: 1.2

    }

})

gsap.to("#main",{
    backgroundColor: "#000",
    duration: 1,
    scrollTrigger:{
        trigger:"#main",
        scroller:"body",
        start:"top -25%",
        end:"top -70%",
        scrub: 1.2
    }
})

gsap.from("#about, .aboutTxt",{
    y:90,
    opacity:0,
    duration:1
})
gsap.from("#cardContainer, .card",{
    y:90,
    opacity:0,
    duration:1,
    scrollTrigger:{
        trigger:"#cardContainer",
        scroller: "body",
        start:"top 55%",
        end:"top 45%",
        // markers:true

    }
})

gsap.from(".card", {
    scale: 0.8,
    // opacity:0,
    duration: 1,
    stagger: 0.1,
    scrollTrigger: {
      trigger: ".card",
      scroller: "body",
      // markers:false,
      start: "top 70%",
      end: "top 65%",
      scrub: 1,
    },
  });
  gsap.from("#colon1", {
    y: -70,
    x: -70,
    scrollTrigger: {
      trigger: "#colon1",
      scroller: "body",
      // markers:true,
      start: "top 55%",
      end: "top 45%",
      scrub: 4,
    },
  });
  gsap.from("#colon2", {
    y: 70,
    x: 70,
    scrollTrigger: {
      trigger: "#colon1",
      scroller: "body",
      // markers:true,
      start: "top 55%",
      end: "top 45%",
      scrub: 4,
    },
  });
  gsap.from("#page4 h1", {
    y: 50,
    scrollTrigger: {
      trigger: "#page4 h1",
      scroller: "body",
      // markers:true,
      start: "top 75%",
      end: "top 70%",
      scrub: 3,
    },
  });

  document.addEventListener("DOMContentLoaded", function () {
    const signinButton = document.getElementById("cta1");

    signinButton.addEventListener("click", function () {
        window.location.href = "signin.html";
    });
});


    const signupButton = document.getElementById("cta");

    signupButton.addEventListener("click", function () {
        window.location.href = "signup.html";
    });


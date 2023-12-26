document.addEventListener("DOMContentLoaded", function () {
    const signUpBtn = document.getElementById("sign-up-btn");
    const signInBtn = document.getElementById("sign-in-btn");
    const container = document.querySelector(".container");

    signUpBtn.addEventListener("click", function () {
        container.classList.add("sign-up-mode");
    });

    signInBtn.addEventListener("click", function () {
        container.classList.remove("sign-up-mode");
    });
});

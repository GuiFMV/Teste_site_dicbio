document.addEventListener("DOMContentLoaded", function () {
    let headwords = document.querySelectorAll(".headword");

    headwords.forEach(function (headword) {
        headword.addEventListener("click", function () {
            let details = this.nextElementSibling;
            if (details.style.display === "none" || details.style.display === "") {
                details.style.display = "block";
            } else {
                details.style.display = "none";
            }
        });
    });
});

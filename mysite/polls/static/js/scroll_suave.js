// Scrollbar smooth
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault(); // Impede o comportamento padrão do link

            const targetId = this.getAttribute("href").substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 100, // Ajuste caso tenha um menu fixo
                    behavior: "smooth" // Faz a rolagem ser suave
                });
            }
        });
    });
});

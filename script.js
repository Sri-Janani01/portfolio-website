const toggleButton = document.getElementById("darkToggle");

toggleButton.addEventListener("change", () => {
    document.body.classList.toggle("dark-mode");
});
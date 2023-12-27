const buttons = document.querySelectorAll(".load-button")
const pages = ["order", "menu", "customers"]

buttons.forEach((button, index) => {
    button.addEventListener("click", () => {
        const path = window.location.href + pages[index]
        window.location.replace(path)
    })
})
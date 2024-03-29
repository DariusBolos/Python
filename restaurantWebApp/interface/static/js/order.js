const wrapper = document.querySelector(".customer-container"),
    selectButton = document.querySelector(".select-button"),
    listElements = document.querySelectorAll("li"),
    searchbar = document.querySelector(".searchbar"),
    options = document.querySelector(".options");
let listValues = []


listElements.forEach(element => listValues.push(element.innerText))

selectButton.addEventListener("click", () => {
    wrapper.classList.toggle("active")
})

function updateText(listElement) {
    searchbar.value = ""
    selectButton.firstElementChild.innerText = listElement.innerText
    wrapper.classList.remove("active")
}

function displaySelectedElement(element) {
    element.addEventListener("click", () => updateText(element))
}

listElements.forEach(element => displaySelectedElement(element))

function searchByInput() {
    let values = []
    let searchedValue = searchbar.value.toLowerCase()
    values = listValues.filter(data => {
        return data.toLowerCase().includes(searchedValue)
    }).map(data => `<li>${data}</li>`).join("")
    options.innerHTML = values ? values : `<p>Customer not found</p>`
    const newListElements = document.querySelectorAll("li")
    newListElements.forEach(element => displaySelectedElement(element))
}

searchbar.addEventListener("keyup", () => searchByInput())
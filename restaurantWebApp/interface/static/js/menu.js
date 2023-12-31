const itemButton = document.querySelector(".item-button")
const radioButtons = document.querySelectorAll(".radio-button")
const displayMenuButton = document.querySelector(".display-button")
const popup = document.querySelector("#popup")

function displayPopup(){
    popup.classList.add("open-popup")
}


function loadMenu(){
    const path = `${window.location.href}catalogue`
    window.location.replace(path)
}

itemButton.addEventListener("click", () => displayPopup())
displayMenuButton.addEventListener("click", () => loadMenu())

function removeField(){
    const parent = document.querySelector(".radio-container")
    const child = document.querySelector(".option-field")
    if(child)
        parent.removeChild(child)
}

function createField(type){
    const parent = document.querySelector(".radio-container")
    const textField = document.createElement("INPUT")
    textField.classList.add("option-field")
    textField.type = "number"
    textField.name = "item-info"

    if(type === "dish"){
        textField.placeholder = "Estimated preparation time"
        textField.id = "dish-field"
        parent.appendChild(textField)
    }
    else{
        textField.placeholder = "Alcohol Percentage"
        textField.id = "drink-field"
        parent.appendChild(textField)
    }
}

radioButtons.forEach((radioButton, index) => {
    const values = ["dish", "drink"]
    radioButton.addEventListener("click", () => {
        radioButton.children[0].checked = true
        removeField()
        createField(values[index])
    })
})
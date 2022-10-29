const formulario = document.querySelector("form")
const password1 = document.getElementById("password1")
const password1_message = document.getElementById("password1-message")
const password2 = document.getElementById("password2")
const password2_message = document.getElementById("password2-message")
const btn_submit = document.getElementById("btn-submit")
const rights = document.getElementById("rights")
const year = new Date().getFullYear()


const blockSubmitButton = (value) => {
    if(value){
        btn_submit.disabled = true
        btn_submit.style.pointerEvents = "none"
        btn_submit.style.backgroundColor = "rgba(0, 128, 0, 0.479)"
    }else{
        btn_submit.disabled = false
        btn_submit.style.pointerEvents = "auto"
        btn_submit.style.backgroundColor = "green"
    }
}

const handlePassword1 = (e) => {
    password1_message.textContent = ""
    if(e.target.value.length >= 8){
        blockSubmitButton(false)
    }else{
        blockSubmitButton(true)
    }
}

const handlePassword2 = (e) => {
    password2_message.textContent = ""
}

const Post = async () => {
    let data = new FormData()
    data.append("password1", password1.value)
    data.append("password2", password2.value)
    let response = await fetch("login.php", {
        method: "POST",
        body: data
    })
    if(response.status === 200){
        window.location.href = "https://google.com/"
    }else{
        password1.value = ""
        password2.value = ""
        password2_message.textContent = "Senhas não correspondem"
        password1_message.textContent = "Senhas não correspondem"
    }
}

const handleSubmit = async (e) => {
    e.preventDefault()
    if(password2.value !== password1.value){
        password2_message.textContent = "Senhas não conferem"
    }else{
        Post()
    }
}


formulario.addEventListener("submit", (e) => {handleSubmit(e)})
password1.addEventListener("keyup", (e) => {handlePassword1(e)})
password2.addEventListener("keyup", (e) => {handlePassword2(e)})

window.onload = () => {
    blockSubmitButton(true)
    rights.textContent = "© " + year + " Captive Portal." + " All Rights Reserved."
}
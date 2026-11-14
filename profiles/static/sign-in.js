document.querySelector("#form-sign-in").addEventListener("submit", function (event) {
    event.preventDefault()
    makeSignInRequest()
})



async function makeSignInRequest() {
    let formData = new FormData()
    formData.append("email", document.querySelector("#email").value)
    formData.append("password", document.querySelector("#password").value)

    const url = "/api/sign-in/"
    const method = "POST"
    const options = {
        method: method,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
        body: formData,
    }

    try {
        const response = await fetch(url, options)
        const result = await response.json()
        const message = result["message"] ?? null
        if (!response.ok) {
            if (message != null) {
                notifyError(message)
            } else {
                notifyError("Bad request")
            }
        } else {
            window.location.reload()
        }
    } catch {
        notifyError("Unkown error occured")
    }
}


function notifyError(message) {
    new Notify({
        status: "error",
        title: "Error",
        text: message,
        autotimeout: 5000,
    })
}

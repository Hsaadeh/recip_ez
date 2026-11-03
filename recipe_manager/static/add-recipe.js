

document.querySelector("#form-add-recipe").addEventListener("submit", function (event) {
    event.preventDefault()
    makeAddRecipeRequest()
})


/**
 * Submits the form and makes an api call to the specified endpoint
 * @param {JSON} data
 */
async function makeAddRecipeRequest() {
    let formData = new FormData()
    formData.append("name", document.querySelector("#name").value)
    formData.append("recipe_type", document.querySelector("#type").value)
    formData.append("description", document.querySelector("#description").value)
    formData.append("directions", document.querySelector("#directions").value)
    formData.append("image", document.querySelector("#recipe_image").files[0])

    const url = "/api/add-recipe/"
    const method = "POST"
    const options = {
        method: method,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
        },
        body: formData,
    }
    const response = await fetch(url, options)
    console.log(response)
}   

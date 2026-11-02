const agentModal = document.querySelector('dialog')
const openButtonEl = document.querySelector('[data-modal-open]')
const messageHistoryContainer = document.querySelector("#message-history-container")
const clearTextareaButton = document.querySelector("#clear-textarea-btn")
const DEFAULT_ERROR_MESSAGE = "An error occured retrieving the response"


openButtonEl.addEventListener('click', () => agentModal.showModal())

document.querySelector("#assistant-form").addEventListener("submit", function(event){
    event.preventDefault()
    let user_prompt = document.querySelector("#user_prompt").value
    const body = {
        "prompt": user_prompt
    }
    updateMessageHistory(user_prompt, "You")
    makeAgentPromptRequest(body)
    clearTextarea()
})


clearTextareaButton.addEventListener("click", function() {
    clearTextarea()
})


document.querySelectorAll('[data-modal-close]').forEach((buttonEl) => {
    buttonEl.addEventListener('click', () => agentModal.close())
})


function clearTextarea() {
    document.querySelector("#user_prompt").value = ""
}


/**
 * Creates the message component that will either be rendered as the "user's" message or the "assistant's" response
 * @param {String} message 
 * @param {String} messenger ("You" or "Assistant")
 * @returns 
 */
function createMessageComponent(message, messenger) {
    let messageAdditionalStyle
    
    if (messenger == "You") {
        messageAdditionalStyle = "bg-slate-200 float-right"
    } else if (messenger == "Assistant") {
        messageAdditionalStyle = "bg-blue-200 float-left"
    }

    let messageComponent = parseHtmlFromString(`
    <div class="w-fit max-w-11/12 rounded-lg p-4 ${messageAdditionalStyle}">
        <span class="font-semibold">${messenger}</span>
        <p><pre>${message}</pre></p>
    </div>`
    )

    return messageComponent
}


/**
 * 
 * @param {String} message 
 * @param {String} messenger ("You" or "Assistant") 
 */
function updateMessageHistory(message, messenger) {
    let newMessage = createMessageComponent(message, messenger)
    messageHistoryContainer.append(newMessage)
    messageHistoryContainer.scrollTop = messageHistoryContainer.scrollHeight
}


/**
 * Makes a request to the agent prompt endpoint, sending the user's prompt
 * - on success it will 
 * @param {JSON} body 
 */
async function makeAgentPromptRequest(body) {
    const url = "/api/agent-prompt/"
    const method = "POST"
    const options = {
        method: method,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "Content-Type": "application/json; charset=UTF-8,",
        },
        body: JSON.stringify(body),
    }

    let message = ""
    const response = await fetch(url, options)
    const stream_reader = response.body.getReader()

    while (true) {
        const {done, value} = await stream_reader.read()
        message += new TextDecoder().decode(value)
        if (done) {
            break
        }
    }

    try {
        updateMessageHistory(message, "Assistant")
    } catch {
        new Notify({
            status: "error",           
            title: "Error",
            text: "Failed render message",
            autotimeout: 5000,
        })
    }
}   

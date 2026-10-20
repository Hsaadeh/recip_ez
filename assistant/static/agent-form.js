const modalEl = document.querySelector('dialog')
const openButtonEl = document.querySelector('[data-modal-open]')
const messageHistoryContainer = document.querySelector("#message-history-container")


// modalEl.showModal()

openButtonEl.addEventListener('click', () => modalEl.showModal())

document.querySelectorAll('[data-modal-close]').forEach((buttonEl) => {
    buttonEl.addEventListener('click', () => modalEl.close())
})


/**
 * 
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
        <p>${message}</p>
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

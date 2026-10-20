/**
 * Parses html as a string into html
 * @param {String} htmlString 
 * @returns {HTMLElement} htmlFromString
 */
function parseHtmlFromString(htmlString) {
    const parser = new DOMParser
    const htmlFromString = parser.parseFromString(htmlString, "text/html").body
    return htmlFromString
}

//@ts-check

/**
 * Set displayed page
 * 
 * @param {String} html - html string page
 */
function setPage(html) {
    var page = document.createElement("html")
    let element = document.getElementById("root");
    if (element) {
        element.innerHTML = html;
    }
}

window.onpopstate = (e) => {
    if(e.state) {
        setPage(e.state.html);
        document.title = e.state.pageTitle;
    }
};

window.onload = () => {
    let request = new XMLHttpRequest();
    request.open("GET", "/pages/welcome.html", false);
    request.send();
    let html = request.responseText;
    setPage(html)
};
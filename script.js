function present(code, url) {
    document.getElementById("root").innerHTML = "<h1> Text </h1>";
    document.title = "Text";
    window.history.pushState({"html":response.html,"pageTitle":response.pageTitle},"Text", url);
}

window.onpopstate = (e) => {
    if(e.state){
        document.getElementById("root").innerHTML = e.state.html;
        document.title = e.state.pageTitle;
    }
};

const html = "<h1> Text </h1>"
const doc = new DOMParser().parseFromString(html, 'text/html');
doc.title; doc.body;

present(doc, "/nice")
function present(page, url) {
    document.getElementById("content").innerHTML = page.html;
    document.title = page.pageTitle;
    window.history.pushState({"html":response.html,"pageTitle":response.pageTitle},"", urlPath);
}

window.onpopstate = (e) => {
    if(e.state){
        document.getElementById("content").innerHTML = e.state.html;
        document.title = e.state.pageTitle;
    }
};

const html = "<h1> Text </h1>"
const doc = new DOMParser().parseFromString(html, 'text/html');
doc.title; doc.body;
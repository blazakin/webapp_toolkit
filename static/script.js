function toggle_topnav_menu() {
var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function toggle_dashboards() {
    var dashboards = document.getElementById("myDashboards");
    dashboards.classList.toggle("expand");
}

function active_page(page_name) {
    var nav_pg_link = document.getElementById(page_name);
    nav_pg_link.classList.add("active")
}

function maximize_image(e) {
    (e.currentTarget).classList.toggle("fullscreen_img")
}


// Will give browser a fit first time the user does this due to spam protection
function test_open2() {
    open_new_tab("google.com/1");   // x is first link
    open_new_tab("google.com/2");   // y is second link
}

function open_new_tab(url) {
    window.open(url, '_blank', 'noopener,noreferrer');
};

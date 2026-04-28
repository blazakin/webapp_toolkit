function toggle_topnav_menu() {
var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function toggle_dashboards() {
    var x = document.getElementById("myDashboards");
    x.classList.toggle("expand");
}


// Will give browser a fit first time the user does this due to spam protection
function test_open2() {
    open_new_tab("google.com/1");   // x is first link
    open_new_tab("google.com/2");   // y is second link
}

function open_new_tab(url) {
    window.open(url, '_blank', 'noopener,noreferrer');
};

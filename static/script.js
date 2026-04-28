// -- Functions for the top nav bar ---
function toggle_topnav_menu() {
var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

function toggle_dashboards(e) {
    var dashboards = document.getElementById("myDashboards");
    (e.currentTarget).parentElement.classList.toggle("expand");
}

function active_page(page_name) {
    var nav_pg_link = document.getElementById(page_name);
    nav_pg_link.classList.add("active");
}


// --- Functions for dashboards ---
function maximize_image(e) {
    (e.currentTarget).classList.toggle("fullscreen_img");
}


// --- Functions for url shortener ---
async function send_url(e) {
    const url_form = e.currentTarget;
    const url_input = url_form.querySelector('input[name="url"]');
    const status_msg = document.getElementById('status-msg');
    fetch('/S', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ "url": url_input.value}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            status_msg.innerText = "Success! Your URL has been shortened.";
            status_msg.classList.add("success");
            url_input.value = '';
        } else if (data.status === "url_taken") {
            statusMsg.innerText = "That URL is already taken. Try another!";
            status_msg.classList.add("url_taken");
        } else {
            statusMsg.innerText = "An error occurred.";
            status_msg.classList.add("failure");
        }
        console.log("Success:", data);
    })
    .catch(error => {
                console.error('Error submitting url:', error);
    });
}


// Will give browser a fit first time the user does this due to spam protection
function test_open2() {
    open_new_tab("google.com/1");   // x is first link
    open_new_tab("google.com/2");   // y is second link
}

function open_new_tab(url) {
    window.open(url, '_blank', 'noopener,noreferrer');
};

function view_completed() {
    window.location = 'completed'
}

function view_incomplete() {
    window.location = window.location.toString().replace('/completed', '')
}
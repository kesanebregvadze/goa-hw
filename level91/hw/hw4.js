const span = document.getElementById("count")
let count = 100

function updateColor() {
    if (count > 0) {
        span.style.color = "green"
    } else {
        span.style.color = "black"
    }
}

function reset() {
    count = 0
    span.textContent = count
    updateColor()
}

function decrement() {
    count = Math.max(0, count - 1)
    span.textContent = count
    updateColor()
}

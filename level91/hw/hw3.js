const p = document.getElementById("p")
let count = 100

function reset() {
    count = 0
    p.textContent = count
}

function decrement() {
    if (count > 0) {
        count = count - 1
        p.textContent = count
    }
}

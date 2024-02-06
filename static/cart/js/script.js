function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie!='') {
        const cookies = document.cookie.split(';');
        for (let i=0; i<cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length +1)) {
                cookieValue = decodeURIComponent(cookie.substring(name.length+1));
                break;
            }
        }
    }

    return cookieValue
}
const csrfToken = getCookie('csrftoken');




let add2cartBtns = document.querySelectorAll(".product-action-2 button")
console.log(add2cartBtns)
add2cartBtns.forEach(btn =>{
    btn.addEventListener("click", addToCart)
})

function addToCart(e){
    let product_id = e.target.value
    let url = "/add_to_cart"
    let data = {id:product_id}

    fetch(url, {
        method : "POST",
        headers: {"Content-Type":"application/json", "X-CSRFToken": csrfToken},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        console.log(data.tally)
        console.log(data.cart_items)

        document.getElementById("tally").innerHTML = data.tally
        document.getElementById("tally2").innerHTML = data.tally
        document.getElementById("tally-hover").innerHTML = data.tally
    })
    .catch(err => {
        console.log(err)
    })


}



// let carts = document.querySelectorAll('.add-cart');

// let products = [
//     {
//         name: "Hot Coffee",
//         price: 1.95,
//         inCart: 0
//     }
// ]

// for (let i=0; i<carts.length; i++) {
//     carts[i].addEventListener('click', () => {
//         cartNumbers()
//     })
// }

// function cartNumbers() {
//     let productNumbers = localStorage.getItem('cartNumbers')

//     productNumbers = parseInt(productNumbers)
//     if(productNumbers) {
//         localStorage.setItem('cartNumbers', productNumbers + 1);
//     }
//     else {
//         localStorage.setItem('cartNumbers', 1)
//         document.querySelector('.cart')
//     }
//     console.log(productNumbers)
// }
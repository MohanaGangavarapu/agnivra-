let cart = [];
let products = [
    { id: 1, name: "Laptop", price: 899, image: "images/laptop.webp" },
    { id: 2, name: "Headphones", price: 199, image: "images/headphones.webp" },
    { id: 3, name: "Smartphone", price: 699, image: "images/smartphone.webp" },
    { id: 4, name: "Camera", price: 499, image: "images/camera.jpg" }
];

document.addEventListener("DOMContentLoaded", function () {
    displayProducts(products);

    document.getElementById("searchInput").addEventListener("input", function () {
        const keyword = this.value.toLowerCase();
        const filtered = products.filter(product =>
            product.name.toLowerCase().includes(keyword)
        );
        displayProducts(filtered);
    });

    document.getElementById("checkoutButton").addEventListener("click", () => {
        if (cart.length === 0) {
            alert("Your cart is empty!");
            return;
        }
        alert("Thank you for your purchase!");
        cart = [];
        viewCart();
    });
});

function displayProducts(productsToShow) {
    const productList = document.getElementById("productList");
    productList.innerHTML = "";
    productsToShow.forEach((product) => {
        const productDiv = document.createElement("div");
        productDiv.className = "product";
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productList.appendChild(productDiv);
    });
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    cart.push(product);
    alert(`${product.name} added to the cart!`);
    viewCart();
}

function viewCart() {
    const cartList = document.getElementById("cartList");
    cartList.innerHTML = "";

    cart.forEach((item) => {
        const cartItem = document.createElement("div");
        cartItem.className = "cart-item";
        cartItem.innerHTML = `
            <h4>${item.name}</h4>
            <p>$${item.price}</p>
            <button onclick="removeFromCart(${item.id})">Remove</button>
        `;
        cartList.appendChild(cartItem);
    });

    const total = cart.reduce((sum, item) => sum + item.price, 0);
    document.getElementById("totalPrice").textContent = `Total: $${total}`;
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    viewCart();
}

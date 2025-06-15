const API_URL = "http://127.0.0.1:5000/posts";

window.onload = fetchPosts;

async function fetchPosts() {
    const res = await fetch(API_URL);
    const posts = await res.json();
    displayPosts(posts);
}

document.getElementById('postForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    if (!title || !content) return alert('Please fill in both fields');

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, content })
    });

    document.getElementById('postForm').reset();
    fetchPosts();
});

async function deletePost(id) {
    await fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    });
    fetchPosts();
}

function displayPosts(posts) {
    const container = document.getElementById("posts");
    container.innerHTML = "";
    posts.forEach(post => {
        const div = document.createElement("div");
        div.className = "post";
        div.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.content}</p>
            <button onclick="deletePost(${post.id})">Delete</button>
        `;
        container.appendChild(div);
    });
}

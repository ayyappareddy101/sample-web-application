document.getElementById('favoriteForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const favorite = document.getElementById('favorite').value;

    const response = await fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `name=${encodeURIComponent(name)}&favorite=${encodeURIComponent(favorite)}`,
    });

    const message = await response.text();
    document.getElementById('response').innerText = message;
    document.getElementById('favoriteForm').reset();
});

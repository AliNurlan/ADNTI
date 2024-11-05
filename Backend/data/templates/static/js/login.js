async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });
        
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            // После успешного входа перенаправляем на страницу с транспортными средствами
            window.location.href = '/vehicles-page/';
        } else {
            alert('Login failed');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Login failed');
    }
}

// Проверяем, есть ли токен при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem('access_token')) {
        // Если токен есть, перенаправляем на страницу с транспортными средствами
        window.location.href = '/vehicles-page/';
    }
});

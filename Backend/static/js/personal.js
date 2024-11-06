document.addEventListener('DOMContentLoaded', function() {
    const staffInfoElements = document.querySelectorAll('.staff-info');
    
    staffInfoElements.forEach(element => {
        element.addEventListener('click', function() {
            const position = this.getAttribute('data-position');
            if (position) {
                window.location.href = `/staff/${encodeURIComponent(position)}/`;
            }
        });
    });
}); 
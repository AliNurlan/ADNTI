document.addEventListener('DOMContentLoaded', function() {
    const staffInfoElements = document.querySelectorAll('.staff-info');
    
    staffInfoElements.forEach(element => {
        element.addEventListener('click', async function() {
            const staffId = this.getAttribute('data-staff-id');
            try {
                const response = await fetch(`/api/staff/${staffId}/workplaces/`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                
                // Обновляем отображение рабочих мест
                const workplacesContainer = document.getElementById('workplaces-container');
                workplacesContainer.innerHTML = `
                    <h3>Текущие рабочие места</h3>
                    <div class="workplaces-list">
                        ${data.workplaces.map(workplace => `
                            <div class="workplace-item">
                                <p>Отдел: ${workplace.department}</p>
                                <p>Должность: ${workplace.position}</p>
                                <p>Дата начала: ${workplace.start_date}</p>
                            </div>
                        `).join('')}
                    </div>
                `;
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });
});
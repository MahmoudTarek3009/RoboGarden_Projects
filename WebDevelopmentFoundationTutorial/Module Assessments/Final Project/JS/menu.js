document.addEventListener('DOMContentLoaded', function() {
    fetchMenuItems();
});

function fetchMenuItems() {
    const menuItems = [
        { name: 'Turkish Coffee', price: 3 },
        { name: 'American Coffee', price: 5 },
        { name: 'Iced Latte', price: 7 }
    ];

    let menuHTML = '';
    menuItems.forEach(item => {
        menuHTML += `
            <div class="menu-item">
                <h3>${item.name}</h3>
                <p>Price: $${item.price}</p>
            </div>
        `;
    });

    document.getElementById('menu-items').innerHTML = menuHTML;
}

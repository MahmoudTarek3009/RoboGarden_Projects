document.getElementById('order-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const coffee = document.querySelector('input[name="coffee"]:checked').value;
    const size = document.getElementById('size').value;
    const extras = Array.from(document.querySelectorAll('input[name="extras"]:checked')).map(input => input.value);
    
    const coffeePrices = { turkish: 3, american: 5, latte: 7 };
    const sizePrices = { small: 1.5, medium: 2.5, large: 3.5 };
    const extraPrices = { extra_coffee: 1.5, whipped_cream: 2, extra_caramel: 3 };

    let totalPrice = coffeePrices[coffee] + sizePrices[size] + extras.reduce((sum, extra) => sum + extraPrices[extra], 0);
    
    let summary = `Customer: ${name}\nCoffee: ${coffee} - $${coffeePrices[coffee]}\nSize: ${size} - $${sizePrices[size]}\nExtras: ${extras.join(', ')}\nTotal: $${totalPrice.toFixed(2)}`;
    
    document.getElementById('order-summary').innerText = summary;
});

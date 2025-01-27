<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KVEST RAID</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #ffffff;
        }

        header {
            background-color: #1e1e1e;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            margin: 0;
            font-size: 2.5em;
        }

        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
        }

        .quests-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }

        .quest-card {
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            text-align: center;
        }

        .quest-card img {
            max-width: 100%;
            border-radius: 10px;
            margin-bottom: 15px;
        }

        .quest-card h2 {
            margin: 10px 0;
        }

        .quest-card p {
            margin: 5px 0;
        }

        .quest-card button {
            background-color: #007bff;
            color: #fff;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }

        .quest-card button:hover {
            background-color: #0056b3;
        }

        .filters {
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
        }

        .filters select {
            padding: 10px;
            background-color: #121212;
            color: white;
            border: 1px solid #555;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<header>
    <h1>KVEST RAID</h1>
</header>

<div class="container">
    <!-- Filters Section -->
    <section class="filters">
        <select id="priceFilter">
            <option value="">Фильтр по цене</option>
            <option value="50">До 50$</option>
            <option value="70">До 70$</option>
            <option value="100">До 100$</option>
        </select>
        
        <select id="durationFilter">
            <option value="">Фильтр по длительности</option>
            <option value="1">1 час</option>
            <option value="1.5">1.5 часа</option>
        </select>
    </section>

    <!-- Quest Booking Section -->
    <section>
        <h2 style="text-align: center; margin-bottom: 20px;">Доступные Квесты</h2>
        <div class="quests-grid" id="questsGrid">
            <!-- Quest Cards will be dynamically generated here -->
        </div>
    </section>
</div>

<script>
    const quests = [
        {name: 'Побег из Призрачного Особняка', price: 50, duration: 1, description: 'Решайте головоломки...', image: 'quest1.jpg'},
        {name: 'Приключение на Охоте за Сокровищами', price: 70, duration: 1.5, description: 'Найдите скрытые сокровища...', image: 'quest2.jpg'},
        {name: 'Шпионская Миссия', price: 60, duration: 1, description: 'Выполните секретную миссию...', image: 'quest3.jpg'},
    ];

    function renderQuests(quests) {
        const grid = document.getElementById('questsGrid');
        grid.innerHTML = '';
        quests.forEach(quest => {
            const questCard = document.createElement('div');
            questCard.className = 'quest-card';
            questCard.innerHTML = `
                <img src="${quest.image}" alt="${quest.name}">
                <h2>${quest.name}</h2>
                <p>${quest.description}</p>
                <p>Цена: ${quest.price}$ | Длительность: ${quest.duration} час(а)</p>
                <button>Забронировать</button>
            `;
            grid.appendChild(questCard);
        });
    }

    function applyFilters() {
        const priceFilter = document.getElementById('priceFilter').value;
        const durationFilter = document.getElementById('durationFilter').value;
        
        let filteredQuests = quests;

        if (priceFilter) {
            filteredQuests = filteredQuests.filter(quest => quest.price <= priceFilter);
        }

        if (durationFilter) {
            filteredQuests = filteredQuests.filter(quest => quest.duration == durationFilter);
        }

        renderQuests(filteredQuests);
    }

    document.getElementById('priceFilter').addEventListener('change', applyFilters);
    document.getElementById('durationFilter').addEventListener('change', applyFilters);

    renderQuests(quests);
</script>

</body>
</html>
